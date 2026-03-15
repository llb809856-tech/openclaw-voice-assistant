# 🎮 Agent Visualizer

> **游戏化 AI Agent 可视化管理平台** - 让每个 Agent 都有独特的形象和生命！

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/yourusername/agent-visualizer)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-beta-yellow.svg)](https://github.com/yourusername/agent-visualizer)

---

## ✨ 特性预览

![Agent Visualizer Demo](https://via.placeholder.com/800x450.png?text=Agent+Visualizer+Demo)

- 🎮 **游戏化界面** - 每个 Agent 都是独特的角色
- 📊 **实时监控** - Token 消耗、任务进度一目了然
- 🏆 **成就系统** - 完成任务解锁徽章和皮肤
- 🔔 **智能预警** - Token 不足时声音 + 弹窗提醒
- 🎨 **3D Avatar** - Three.js 渲染的可交互形象

---

## 🚀 快速开始

### 后端启动

```bash
cd backend
pip install -r requirements.txt
python main.py
```

访问 API 文档：http://localhost:8000/docs

### 前端启动

```bash
cd frontend
npm install
npm run dev
```

访问演示页面：http://localhost:5173

### 快速演示

直接打开演示页面（无需安装）：

```bash
open demo.html
```

---

## 📸 界面预览

### 主界面

![Dashboard](https://via.placeholder.com/800x450.png?text=Dashboard+Preview)

### Agent 卡片

每个 Agent 显示：
- Avatar 形象 + 状态表情
- 实时任务进度条
- Token 消耗和剩余量
- 状态颜色边框

### 3D Avatar

![3D Avatar](https://via.placeholder.com/400x400.png?text=3D+Avatar+Preview)

---

## 🎯 核心功能

### Agent 状态系统

| 状态 | 颜色 | 表情 | 说明 |
|------|------|------|------|
| 空闲 | 🟢 绿色 | 😴 | 等待任务 |
| 思考 | 🔵 蓝色 | 🤔 | 正在处理 |
| 工作 | 🟡 黄色 | 💪 | 执行任务 |
| 错误 | 🔴 红色 | 😵 | 出现错误 |
| 离线 | ⚫ 灰色 | 💤 | 离线状态 |

### Token 可视化

- 💰 **已用 Token** - 实时累计
- ❤️ **剩余配额** - 百分比显示
- 🎨 **颜色预警** - 绿/黄/红三色
- 🔔 **声音提醒** - 低于 20% 时播放

### 成就系统

| 徽章 | 名称 | 解锁条件 |
|------|------|---------|
| 🏆 | 勤劳小蜜蜂 | 连续工作 7 天 |
| 💰 | 省钱能手 | 单日节省 10 万 Token |
| 🚀 | 效率之王 | 任务完成速度 TOP1 |
| 📚 | 学习达人 | 完成 100 个任务 |
| 🎯 | 完美主义 | 连续 10 次无错误 |

---

## 🛠️ 技术栈

### 前端

- **React 18** - UI 框架
- **Three.js** - 3D 渲染
- **TailwindCSS** - 样式
- **Framer Motion** - 动画
- **Zustand** - 状态管理

### 后端

- **Python 3.11** - 运行环境
- **FastAPI** - Web 框架
- **WebSocket** - 实时推送
- **SQLite** - 数据存储

---

## 📦 项目结构

```
agent-visualizer/
├── frontend/              # React 前端
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── AgentCard.jsx
│   │   │   ├── ActivityLog.jsx
│   │   │   └── Avatar3D.jsx
│   │   └── App.jsx
│   ├── package.json
│   └── vite.config.js
├── backend/               # Python 后端
│   ├── main.py
│   ├── openclaw_integration.py
│   └── requirements.txt
├── avatars/               # 形象资源
│   ├── default/
│   └── premium/
├── docs/                  # 文档
│   ├── 产品需求文档.md
│   ├── 项目演示.md
│   └── GitHub 发布页.md
├── demo.html              # 演示页面
├── README.md
└── LICENSE
```

---

## 🔌 API 接口

### RESTful API

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/agents` | GET | 获取所有 Agent |
| `/api/agents/{id}` | GET | 获取单个 Agent |
| `/api/logs` | GET | 获取活动日志 |
| `/api/stats` | GET | 获取统计数据 |
| `/api/achievements` | GET | 获取成就列表 |

### WebSocket

连接：`ws://localhost:8000/ws`

推送数据类型：
- `agent_update` - Agent 状态更新
- `stats_update` - 统计数据更新
- `system` - 系统消息

---

## 💡 使用场景

### 个人开发者

管理多个 AI Agent，一目了然：
- 哪个 Agent 在工作
- Token 消耗情况
- 任务完成进度

### 小团队

团队协作监控：
- 实时查看团队成员状态
- Token 消耗统计
- 工作效率分析

### 企业用户

私有化部署：
- 自定义 Agent 形象
- 对接内部系统
- 数据本地存储

---

## 🗺️ 开发路线图

### Phase 1: MVP ✅ (2026-03-08)
- [x] 产品需求文档
- [x] 前端框架
- [x] 后端 API
- [x] WebSocket 推送
- [x] 演示页面

### Phase 2: 增强 (2 周)
- [ ] OpenClaw 集成
- [ ] 3D Avatar 系统
- [ ] 成就系统
- [ ] 提示音
- [ ] 移动端适配

### Phase 3: 商业化 (4 周)
- [ ] 付费系统
- [ ] 皮肤商城
- [ ] 企业版
- [ ] 文档完善
- [ ] 官网

### Phase 4: 发布 (6 周)
- [ ] GitHub 开源
- [ ] Product Hunt
- [ ] 社交媒体
- [ ] 用户反馈
- [ ] 持续迭代

---

## 🤝 贡献指南

欢迎贡献代码！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

- [OpenClaw](https://openclaw.ai) - AI Agent 框架
- [Three.js](https://threejs.org) - 3D 渲染库
- [FastAPI](https://fastapi.tiangolo.com) - Python Web 框架

---

## 📞 联系方式

- **作者**: [你的名字]
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Email**: your.email@example.com

---

<div align="center">

**🌟 如果这个项目对你有帮助，请给个 Star！**

Made with ❤️ by [Your Name]

</div>
