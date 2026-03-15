"""
OpenClaw 集成模块
获取真实的 Agent 状态和数据
"""

import asyncio
import aiohttp
from datetime import datetime
from typing import List, Dict, Optional

class OpenClawIntegration:
    """OpenClaw API 集成"""
    
    def __init__(self, gateway_url: str = "http://localhost:9876"):
        self.gateway_url = gateway_url
        self.session: Optional[aiohttp.ClientSession] = None
    
    async def connect(self):
        """建立连接"""
        if not self.session:
            self.session = aiohttp.ClientSession()
    
    async def disconnect(self):
        """断开连接"""
        if self.session:
            await self.session.close()
            self.session = None
    
    async def get_session_status(self) -> Dict:
        """获取当前会话状态"""
        try:
            # 这里调用 OpenClaw 的 session_status API
            # 由于 OpenClaw 没有直接暴露 API，我们用模拟数据
            # 实际使用时需要调用 openclaw CLI 或读取状态文件
            
            return {
                "model": "bailian/qwen3.5-plus",
                "tokens_in": 79000,
                "tokens_out": 212,
                "cost": 0.0,
                "context_usage": 8,
                "updated_at": datetime.now().isoformat()
            }
        except Exception as e:
            print(f"Error getting session status: {e}")
            return {}
    
    async def get_active_agents(self) -> List[Dict]:
        """获取活跃的 Agent 列表"""
        try:
            # 从 OpenClaw 获取当前运行的 Agent
            # 这里用模拟数据，实际需要从 OpenClaw 会话中获取
            
            return [
                {
                    "id": "main",
                    "name": "小林",
                    "avatar": "🤖",
                    "status": "working",
                    "model": "qwen3.5-plus",
                    "task": "开发 Agent Visualizer",
                    "tokens_used": 15000,
                    "started_at": datetime.now().isoformat()
                },
                {
                    "id": "scraper",
                    "name": "爬虫",
                    "avatar": "🕷️",
                    "status": "idle",
                    "model": "qwen3.5-plus",
                    "task": "待命中",
                    "tokens_used": 0,
                    "started_at": None
                }
            ]
        except Exception as e:
            print(f"Error getting agents: {e}")
            return []
    
    async def get_token_usage(self) -> Dict:
        """获取 Token 使用情况"""
        try:
            status = await self.get_session_status()
            return {
                "total_in": status.get("tokens_in", 0),
                "total_out": status.get("tokens_out", 0),
                "total": status.get("tokens_in", 0) + status.get("tokens_out", 0),
                "cost": status.get("cost", 0.0),
                "context_usage": status.get("context_usage", 0)
            }
        except Exception as e:
            print(f"Error getting token usage: {e}")
            return {}
    
    async def get_recent_activities(self, limit: int = 20) -> List[Dict]:
        """获取最近的活动记录"""
        try:
            # 从 OpenClaw 会话历史中获取活动
            # 这里用模拟数据
            
            activities = [
                {
                    "time": datetime.now().strftime("%H:%M"),
                    "agent": "小林",
                    "avatar": "🤖",
                    "action": "完成了 demo.html 页面开发",
                    "type": "success"
                },
                {
                    "time": datetime.now().strftime("%H:%M"),
                    "agent": "小林",
                    "avatar": "🤖",
                    "action": "启动了后端 API 服务",
                    "type": "success"
                },
                {
                    "time": datetime.now().strftime("%H:%M"),
                    "agent": "小林",
                    "avatar": "🤖",
                    "action": "创建了 React 组件框架",
                    "type": "success"
                },
                {
                    "time": datetime.now().strftime("%H:%M"),
                    "agent": "小林",
                    "avatar": "🤖",
                    "action": "开始开发 Agent Visualizer 项目",
                    "type": "info"
                }
            ]
            
            return activities[:limit]
        except Exception as e:
            print(f"Error getting activities: {e}")
            return []


# 测试函数
async def test_integration():
    """测试 OpenClaw 集成"""
    integration = OpenClawIntegration()
    await integration.connect()
    
    print("📊 Session Status:")
    status = await integration.get_session_status()
    print(status)
    
    print("\n🤖 Active Agents:")
    agents = await integration.get_active_agents()
    for agent in agents:
        print(f"  - {agent['name']} ({agent['status']}): {agent['task']}")
    
    print("\n💰 Token Usage:")
    usage = await integration.get_token_usage()
    print(usage)
    
    print("\n📜 Recent Activities:")
    activities = await integration.get_recent_activities()
    for activity in activities:
        print(f"  {activity['time']} {activity['agent']}: {activity['action']}")
    
    await integration.disconnect()


if __name__ == "__main__":
    asyncio.run(test_integration())
