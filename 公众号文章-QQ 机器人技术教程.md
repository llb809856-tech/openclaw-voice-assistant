# 公众号文章：QQ 机器人技术教程

## 标题备选
1. 技术教程 | 30 分钟部署 OpenClaw+QQ 机器人，手把手教你配置
2. 保姆级教程 | OpenClaw 接入 QQ 机器人完整指南（含配置文件）
3. 不写代码！OpenClaw+QQ 机器人一键部署教程（2026 最新版）
4. 实战教程 | 从零搭建你的第一个 QQ AI 机器人（附完整配置）

## 摘要
本文详细介绍如何在 30 分钟内部署 OpenClaw 并接入 QQ 机器人，包含 QQ 开放平台配置、OpenClaw 安装、插件配置、常见问题解决等完整流程。提供配置文件模板和避坑指南。

---

## 正文

> **前置要求：** 有 QQ 账号、能访问外网、基础命令行操作能力
> 
> **预计耗时：** 30-60 分钟
> 
> **成本：** 0 元（QQ 机器人免费 + OpenClaw 开源）

---

## 01 环境准备

### 系统要求

| 系统 | 版本 | 备注 |
|------|------|------|
| macOS | 12.0+ | 推荐 M 系列芯片 |
| Windows | 10/11 | 需要 WSL2 |
| Linux | Ubuntu 20.04+ | 推荐服务器部署 |
| Docker | 20.0+ | 最简部署方式 |

### 必要工具

```bash
# 检查 Node.js（v18+）
node -v

# 检查 npm
npm -v

# 检查 Docker（可选）
docker -v
```

**如果没有安装：**
- Node.js: https://nodejs.org/
- Docker: https://www.docker.com/

---

## 02 创建 QQ 机器人

### Step 1: 访问 QQ 开放平台

打开浏览器，访问：
```
https://q.qq.com/
```

### Step 2: 登录账号

使用手机 QQ 扫描二维码登录。

**注意：**
- ✅ 个人账号即可创建
- ✅ 不需要企业资质
- ⚠️ 建议使用常用账号（需要接收通知）

### Step 3: 创建机器人

1. 点击「创建机器人」按钮
2. 填写基本信息：
   ```
   机器人名称：你的 AI 助手（可自定义）
   机器人头像：上传一张图片（建议 200x200）
   机器人简介：一个智能 AI 助手
   ```
3. 选择应用场景：
   - ✅ 单聊
   - ✅ 群聊
   - ✅ 频道（可选）

### Step 4: 获取凭证

创建成功后，在「应用信息」页面保存以下信息：

```
AppID: 1234567890（示例）
AppSecret: abcdefghijklmnopqrstuvwxyz（示例）
Token: 可选，用于回调验证
```

**⚠️ 重要：**
- AppSecret 只显示一次，务必复制保存
- 如果忘记，需要重新生成

### Step 5: 配置回调地址（可选）

如果需要接收事件通知，配置回调地址：

```
回调地址：http://你的服务器 IP:5800/qq/callback
IP 白名单：添加你的服务器 IP
```

**本地测试可跳过此步骤。**

---

## 03 部署 OpenClaw

### 方案 A：Docker 部署（推荐）

**适合：** 服务器部署、生产环境

```bash
# 1. 拉取镜像
docker pull openclaw/openclaw:latest

# 2. 创建配置目录
mkdir -p ~/openclaw/config
mkdir -p ~/openclaw/data

# 3. 启动容器
docker run -d \
  --name openclaw \
  -p 5800:5800 \
  -v ~/openclaw/config:/root/.openclaw/config \
  -v ~/openclaw/data:/root/.openclaw/data \
  -e OPENCLAW_MODEL=bailian/qwen3.5-plus \
  openclaw/openclaw:latest

# 4. 查看日志
docker logs -f openclaw
```

**验证：** 访问 `http://localhost:5800` 看到 Web 界面即成功。

---

### 方案 B：npm 安装（本地开发）

**适合：** 本地测试、技能开发

```bash
# 1. 全局安装
npm install -g openclaw

# 2. 初始化配置
openclaw init

# 3. 配置模型
openclaw config set model bailian/qwen3.5-plus

# 4. 启动服务
openclaw gateway start

# 5. 查看状态
openclaw gateway status
```

---

### 方案 C：阿里云一键部署

**适合：** 新手、不想配置环境

1. 访问阿里云轻量应用服务器
2. 选择 OpenClaw 应用镜像
3. 点击「立即开通」
4. 等待 3-5 分钟自动部署完成
5. 获取公网 IP 和管理后台地址

**成本：** 约 24 元/月（基础配置）

---

## 04 配置 QQ 插件

### Step 1: 安装 QQ 插件

```bash
# Docker 环境
docker exec -it openclaw openclaw plugins install @sliverp/qqbot@latest

# npm 环境
openclaw plugins install @sliverp/qqbot@latest
```

**如果安装失败（网络问题）：**

```bash
# 使用国内镜像
npm config set registry https://registry.npmmirror.com

# 或源码安装
git clone https://github.com/sliverp/qqbot.git
cd qqbot
openclaw plugins install .
```

### Step 2: 配置 QQ 凭证

```bash
# 设置 AppID
openclaw config set channels.qq-official.appId "你的 AppID"

# 设置 AppSecret
openclaw config set channels.qq-official.appSecret "你的 AppSecret"

# 设置 Token（如果配置了回调）
openclaw config set channels.qq-official.token "你的 Token"

# 配置交互权限
openclaw config set channels.qq-official.allowPrivateChat true
openclaw config set channels.qq-official.allowChannelAt true
openclaw config set channels.qq-official.allowGroupChat true
```

### Step 3: 配置文件方式（可选）

编辑配置文件：

```bash
# 找到配置目录
openclaw config path

# 编辑 config.json
nano ~/.openclaw/config/config.json
```

配置文件模板：

```json
{
  "model": "bailian/qwen3.5-plus",
  "channels": {
    "qq-official": {
      "appId": "你的 AppID",
      "appSecret": "你的 AppSecret",
      "token": "",
      "allowPrivateChat": true,
      "allowChannelAt": true,
      "allowGroupChat": true,
      "sandbox": false
    }
  },
  "skills": {
    "enabled": ["web-search", "browser", "exec"]
  }
}
```

### Step 4: 重启服务

```bash
# Docker 环境
docker restart openclaw

# npm 环境
openclaw gateway restart

# 或使用服务管理
openclaw service restart
```

---

## 05 测试验证

### 测试 1：单聊测试

1. 打开手机 QQ
2. 搜索你的机器人名称
3. 发送消息：`你好`
4. 等待响应（通常 3-10 秒）

**预期响应：**
```
你好！我是你的 AI 助手，有什么可以帮你的吗？
```

### 测试 2：功能测试

发送以下测试命令：

```
# 测试搜索
今天北京天气怎么样？

# 测试计算
123 * 456 等于多少？

# 测试创作
写一首关于春天的诗

# 测试代码
用 Python 写一个快速排序
```

### 测试 3：日志检查

```bash
# 查看实时日志
docker logs -f openclaw

# 或
openclaw gateway logs
```

**正常日志示例：**
```
[INFO] QQ message received: {"user_id": 123456, "message": "你好"}
[INFO] Processing with model: bailian/qwen3.5-plus
[INFO] Response sent: 你好！我是你的 AI 助手...
```

---

## 06 常见问题解决

### Q1: 插件安装失败

**错误信息：**
```
npm ERR! network request failed
```

**解决方案：**
```bash
# 切换 npm 镜像
npm config set registry https://registry.npmmirror.com

# 或使用源码安装
git clone https://github.com/sliverp/qqbot.git
cd qqbot
openclaw plugins install .
```

---

### Q2: 机器人无响应

**排查步骤：**

1. 检查服务状态
```bash
openclaw gateway status
# 或
docker ps | grep openclaw
```

2. 检查 QQ 插件配置
```bash
openclaw config get channels.qq-official
```

3. 检查日志
```bash
docker logs openclaw | tail -50
```

4. 确认 QQ 机器人状态
- 登录 q.qq.com
- 检查机器人是否「启用」状态
- 检查 IP 白名单（如果配置了回调）

---

### Q3: 响应速度慢

**可能原因：**
- 模型响应慢（网络问题）
- 服务器性能不足
- 技能调用耗时

**优化方案：**

1. 切换更快的模型
```bash
openclaw config set model bailian/qwen3.5-plus
```

2. 禁用不需要的技能
```json
{
  "skills": {
    "enabled": ["web-search"]
  }
}
```

3. 升级服务器配置
- CPU: 2 核 → 4 核
- 内存：4GB → 8GB

---

### Q4: 中文乱码

**解决方案：**

1. 检查系统编码
```bash
locale
# 应该是 zh_CN.UTF-8 或 en_US.UTF-8
```

2. 设置环境变量
```bash
export LANG=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8
```

3. Docker 容器内设置
```bash
docker exec -it openclaw bash
echo "export LANG=zh_CN.UTF-8" >> ~/.bashrc
source ~/.bashrc
```

---

## 07 进阶配置

### 配置多个模型

```bash
# 主模型（默认）
openclaw config set model bailian/qwen3.5-plus

# 备用模型
openclaw config set models.fallback bailian/glm-5

# 特定任务使用特定模型
openclaw config set models.code bailian/qwen3.5-plus
openclaw config set models.creative minimax-cn/MiniMax-M2.5
```

### 配置技能白名单

```json
{
  "skills": {
    "enabled": [
      "web-search",
      "browser",
      "exec",
      "message",
      "feishu_doc"
    ],
    "disabled": [
      "tts",
      "canvas"
    ]
  }
}
```

### 配置速率限制

```json
{
  "rateLimit": {
    "messagesPerMinute": 10,
    "tokensPerHour": 100000,
    "concurrentRequests": 5
  }
}
```

### 配置持久化存储

```bash
# 数据目录
openclaw config set dataPath /root/.openclaw/data

# 记忆文件
openclaw config set memory.enabled true
openclaw config set memory.path /root/.openclaw/memory
```

---

## 08 安全建议

### 1. 保护 AppSecret

```bash
# 不要提交到 git
echo "config.json" >> .gitignore

# 使用环境变量
export QQ_APP_SECRET="你的密钥"
```

### 2. 配置 IP 白名单

在 QQ 开放平台设置：
```
IP 白名单：你的服务器 IP
```

### 3. 启用沙箱模式（测试环境）

```bash
openclaw config set channels.qq-official.sandbox true
```

### 4. 定期更新

```bash
# 更新 OpenClaw
npm update -g openclaw

# 或 Docker
docker pull openclaw/openclaw:latest
docker restart openclaw

# 更新插件
openclaw plugins update
```

---

## 09 资源下载

**配置文件模板：**
```
https://github.com/openclaw/openclaw/blob/main/config.example.json
```

**QQ 机器人插件：**
```
https://github.com/sliverp/qqbot
```

**OpenClaw 官方文档：**
```
https://docs.openclaw.ai
```

**社区论坛：**
```
https://discord.com/invite/clawd
```

---

## 10 下一步

机器人已经跑起来了，接下来可以：

### ✅ 方向 1：定制技能

学习开发自定义 Skills，让机器人更懂你的需求。

### ✅ 方向 2：接入更多平台

- 飞书机器人
- 钉钉机器人
- 企业微信
- Telegram

### ✅ 方向 3：搭建多机器人矩阵

利用 5 个机器人名额，创建不同用途的 AI 助手。

### ✅ 方向 4：商业化运营

- AI 代运营服务
- 垂直领域问答
- 机器人定制开发

---

**🎁 福利：**

关注公众号，回复"QQ 机器人"获取：
1. 完整配置文件模板（JSON）
2. 常见问题排查手册（PDF）
3. 技能开发教程
4. 技术交流群入口

---

*本文测试环境：OpenClaw v2.6.0 / QQ 开放平台 2026.03*

*遇到问题？在评论区留言，我会逐一回复*

*如果觉得有用，请点赞 + 在看 + 分享*
