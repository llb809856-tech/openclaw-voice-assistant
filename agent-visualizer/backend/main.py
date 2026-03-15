"""
Agent Visualizer - Backend API
游戏化 Agent 可视化管理平台
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime
import asyncio
import json
import random
from achievements import AchievementSystem, ACHIEVEMENTS_DB, SKINS_DB

app = FastAPI(title="Agent Visualizer API", version="0.1.0")

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== 数据模型 ====================

class Agent(BaseModel):
    id: int
    name: str
    avatar: str
    status: str  # idle, thinking, working, error, offline
    progress: float
    tokenUsed: int
    tokenRemaining: float
    task: str
    level: int = 1
    experience: int = 0

class ActivityLog(BaseModel):
    time: str
    agent: str
    avatar: str
    action: str
    type: str  # success, info, warning, error

class Stats(BaseModel):
    tokenTotal: int
    tasksCompleted: int
    runningAgents: int
    totalAgents: int
    efficiency: float

# ==================== 模拟数据 ====================

# Agent 列表
agents_db: List[Agent] = [
    Agent(
        id=1,
        name="小林",
        avatar="🤖",
        status="thinking",
        progress=75,
        tokenUsed=234,
        tokenRemaining=80,
        task="发送 AI 大模型日报",
        level=3,
        experience=450
    ),
    Agent(
        id=2,
        name="爬虫",
        avatar="🕷️",
        status="working",
        progress=45,
        tokenUsed=567,
        tokenRemaining=60,
        task="抓取竞品价格数据",
        level=2,
        experience=280
    ),
    Agent(
        id=3,
        name="分析",
        avatar="📊",
        status="idle",
        progress=100,
        tokenUsed=89,
        tokenRemaining=95,
        task="待命中",
        level=4,
        experience=1200
    ),
    Agent(
        id=4,
        name="写作",
        avatar="✍️",
        status="working",
        progress=60,
        tokenUsed=123,
        tokenRemaining=85,
        task="撰写短视频脚本",
        level=2,
        experience=320
    ),
    Agent(
        id=5,
        name="客服",
        avatar="💬",
        status="idle",
        progress=100,
        tokenUsed=45,
        tokenRemaining=90,
        task="待命中",
        level=1,
        experience=80
    )
]

# 活动日志
logs_db: List[ActivityLog] = [
    ActivityLog(time="14:32", agent="小林", avatar="🤖", action="完成了 AI 日报发送任务", type="success"),
    ActivityLog(time="14:30", agent="爬虫", avatar="🕷️", action="开始抓取竞品数据", type="info"),
    ActivityLog(time="14:28", agent="分析", avatar="📊", action="生成了销售报告", type="success"),
    ActivityLog(time="14:25", agent="写作", avatar="✍️", action="完成了短视频脚本", type="success"),
    ActivityLog(time="14:20", agent="客服", avatar="💬", action="回复了客户咨询", type="info")
]

# WebSocket 连接管理
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        print(f"New WebSocket connection. Total: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        print(f"WebSocket disconnected. Total: {len(self.active_connections)}")

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception as e:
                print(f"Error sending to WebSocket: {e}")

manager = ConnectionManager()
achievement_system = AchievementSystem()

# 初始化 Agent 成就数据
for agent in agents_db:
    achievement_system.init_agent_stats(str(agent.id))

# ==================== API 路由 ====================

@app.get("/")
async def root():
    return {
        "message": "Agent Visualizer API",
        "version": "0.1.0",
        "status": "running"
    }

@app.get("/api/agents", response_model=List[Agent])
async def get_agents():
    """获取所有 Agent 列表"""
    return agents_db

@app.get("/api/agents/{agent_id}", response_model=Agent)
async def get_agent(agent_id: int):
    """获取单个 Agent 详情"""
    for agent in agents_db:
        if agent.id == agent_id:
            return agent
    return {"error": "Agent not found"}

@app.get("/api/logs", response_model=List[ActivityLog])
async def get_logs(limit: int = 20):
    """获取活动日志"""
    return logs_db[-limit:]

@app.get("/api/stats", response_model=Stats)
async def get_stats():
    """获取统计数据"""
    token_total = sum(a.tokenUsed for a in agents_db)
    tasks_completed = len([l for l in logs_db if l.type == "success"])
    running_agents = len([a for a in agents_db if a.status in ["working", "thinking"]])
    
    return Stats(
        tokenTotal=token_total,
        tasksCompleted=tasks_completed,
        runningAgents=running_agents,
        totalAgents=len(agents_db),
        efficiency=98.5
    )

@app.post("/api/agents/{agent_id}/task")
async def assign_task(agent_id: int, task: str):
    """给 Agent 分配任务"""
    for agent in agents_db:
        if agent.id == agent_id:
            agent.task = task
            agent.status = "working"
            agent.progress = 0
            
            # 添加日志
            logs_db.append(ActivityLog(
                time=datetime.now().strftime("%H:%M"),
                agent=agent.name,
                avatar=agent.avatar,
                action=f"开始执行任务：{task}",
                type="info"
            ))
            
            # 广播更新
            await manager.broadcast({
                "type": "agent_update",
                "agent": agent.dict()
            })
            
            return {"status": "success", "agent": agent.dict()}
    
    return {"error": "Agent not found"}

@app.get("/api/achievements")
async def get_achievements():
    """获取所有成就列表"""
    return ACHIEVEMENTS_DB

@app.get("/api/skins")
async def get_skins():
    """获取所有皮肤列表"""
    return SKINS_DB

@app.get("/api/agents/{agent_id}/profile")
async def get_agent_profile(agent_id: int):
    """获取 Agent 档案（包含成就、等级、皮肤等）"""
    profile = achievement_system.get_agent_profile(str(agent_id))
    return profile

@app.post("/api/agents/{agent_id}/skin")
async def set_agent_skin(agent_id: int, skin_id: str):
    """设置 Agent 皮肤"""
    success = achievement_system.set_skin(str(agent_id), skin_id)
    if success:
        return {"status": "success", "skin_id": skin_id}
    return {"status": "error", "message": "Skin not unlocked"}

@app.post("/api/agents/{agent_id}/purchase-skin")
async def purchase_skin(agent_id: int, skin_id: str):
    """购买皮肤"""
    success = achievement_system.unlock_skin(str(agent_id), skin_id)
    if success:
        return {"status": "success", "skin_id": skin_id}
    return {"status": "error", "message": "Already unlocked or insufficient funds"}

# ==================== WebSocket ====================

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket 实时推送"""
    await manager.connect(websocket)
    try:
        while True:
            # 接收客户端消息（可选）
            data = await websocket.receive_text()
            print(f"Received: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast({
            "type": "system",
            "message": f"用户断开连接"
        })

# ==================== 后台任务 ====================

async def simulate_agent_activity():
    """模拟 Agent 活动（实时更新）"""
    while True:
        for agent in agents_db:
            if agent.status in ["working", "thinking"]:
                # 更新进度
                agent.progress = min(100, agent.progress + random.uniform(1, 5))
                # 消耗 Token
                agent.tokenUsed += random.randint(5, 20)
                agent.tokenRemaining = max(0, agent.tokenRemaining - random.uniform(0.5, 2))
                
                # 完成任务
                if agent.progress >= 100 and agent.status == "working":
                    agent.status = "idle"
                    logs_db.append(ActivityLog(
                        time=datetime.now().strftime("%H:%M"),
                        agent=agent.name,
                        avatar=agent.avatar,
                        action=f"完成了任务：{agent.task}",
                        type="success"
                    ))
        
        # 广播更新
        await manager.broadcast({
            "type": "stats_update",
            "stats": {
                "tokenTotal": sum(a.tokenUsed for a in agents_db),
                "tasksCompleted": len([l for l in logs_db if l.type == "success"]),
                "runningAgents": len([a for a in agents_db if a.status in ["working", "thinking"]]),
                "totalAgents": len(agents_db)
            }
        })
        
        await asyncio.sleep(2)


async def heartbeat_checker():
    """心跳检测 - 定期检查连接状态"""
    last_check = datetime.now()
    while True:
        await asyncio.sleep(30)
        now = datetime.now()
        
        if not manager.active_connections:
            print(f"⚠️ [{now.strftime('%H:%M:%S')}] 无活跃连接，等待重连...")
        else:
            print(f"✅ [{now.strftime('%H:%M:%S')}] {len(manager.active_connections)} 个连接正常 (上次检查：{(now - last_check).seconds}s 前)")
            last_check = now

@app.on_event("startup")
async def startup_event():
    """启动后台任务"""
    asyncio.create_task(simulate_agent_activity())
    asyncio.create_task(heartbeat_checker())
    print("🚀 Agent Visualizer API started!")
    print("💓 心跳检测已启用（每 30 秒检查一次）")
    print("🔄 WebSocket 自动重连已启用（最多 5 次，指数退避）")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
