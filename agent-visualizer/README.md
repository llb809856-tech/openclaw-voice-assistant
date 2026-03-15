# 🎮 Agent Visualizer

**游戏化 AI Agent 可视化管理平台**

让每个 Agent 拥有独特的形象、状态显示和 Token 消耗可视化！

---

## ✨ 特性

- 🎮 **游戏化界面** - Agent 有形象、有表情、有状态
- 💰 **Token 可视化** - 实时显示消耗和剩余量
- 📊 **实时监控** - WebSocket 推送，数据即时更新
- 🏆 **成就系统** - 完成任务解锁徽章和皮肤
- 🔔 **预警系统** - Token 不足时声音 + 弹窗提醒

---

## 🚀 快速开始

### 后端启动

```bash
cd backend
pip install -r requirements.txt
python main.py
```

访问：http://localhost:8000

API 文档：http://localhost:8000/docs

### 前端启动

```bash
cd frontend
npm install
npm run dev
```

访问：http://localhost:5173

---

## 📁 项目结构

```
agent-visualizer/
├── frontend/           # React 前端
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── AgentCard.jsx
│   │   │   └── ActivityLog.jsx
│   │   └── App.jsx
│   └── package.json
├── backend/            # Python FastAPI 后端
│   ├── main.py
│   └── requirements.txt
├── avatars/            # Agent 形象资源
└── docs/               # 文档
    └── 产品需求文档.md
```

---

## 🎯 API 接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/agents` | GET | 获取所有 Agent |
| `/api/agents/{id}` | GET | 获取单个 Agent |
| `/api/logs` | GET | 获取活动日志 |
| `/api/stats` | GET | 获取统计数据 |
| `/api/achievements` | GET | 获取成就列表 |
| `/ws` | WebSocket | 实时数据推送 |

---

## 🎨 界面预览

```
┌─────────────────────────────────────────────────┐
│  🌌 Agent 基地                            🔔 ⚙️  │
├─────────────────────────────────────────────────┤
│  📊 今日总览                                      │
│  💰 Token: ¥1,234  ✅ 任务：23  🟢 运行：5/10    │
│                                                  │
│  🤖 Agent 团队                                    │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│  │ 🤖   │ │ 🕷️  │ │ 📊   │ │ ✍️   │ │ 💬   │  │
│  │ 思考 │ │ 工作 │ │ 空闲 │ │ 工作 │ │ 空闲 │  │
│  │ ⚡75%│ │ ⚡45%│ │ ⚡100│ │ ⚡60%│ │ ⚡100│  │
│  │ 💰234│ │ 💰567│ │ 💰89 │ │ 💰123│ │ 💰45 │  │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘  │
│                                                  │
│  📜 活动日志                                      │
│  14:32 🤖 小林 完成了 AI 日报发送任务               │
│  14:30 🕷️ 爬虫 开始抓取竞品数据                   │
└─────────────────────────────────────────────────┘
```

---

## 💰 商业模式

| 版本 | 价格 | 功能 |
|------|------|------|
| **免费版** | ¥0 | 3 个 Agent + 基础统计 |
| **专业版** | ¥99/月 | 10 个 Agent + 高级统计 |
| **企业版** | ¥999/月 | 无限 Agent + 私有部署 |

---

## 🛠️ 技术栈

**前端：**
- React 18 + TypeScript
- Three.js / React Three Fiber（3D 形象）
- TailwindCSS（样式）
- Framer Motion（动画）
- Zustand（状态管理）

**后端：**
- Python 3.11 + FastAPI
- WebSocket（实时推送）
- SQLite / PostgreSQL（数据存储）

---

## 📅 开发计划

- [x] 产品需求文档
- [x] 前端框架 + 组件
- [x] 后端 API + WebSocket
- [ ] OpenClaw 集成
- [ ] 3D Avatar 系统
- [ ] 成就系统
- [ ] 皮肤商城

---

## 📄 许可证

MIT License

---

**🌟 如果这个项目对你有帮助，请给个 Star！**
