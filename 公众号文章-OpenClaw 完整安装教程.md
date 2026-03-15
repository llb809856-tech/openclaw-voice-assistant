# 公众号文章：OpenClaw 完整安装教程

## 标题备选
1. 建议收藏 | OpenClaw 安装配置完整教程（2026 最新版）
2. 零基础也能懂 | OpenClaw 安装 + 配置 + 使用一篇搞定
3. 从安装到接入 QQ/微信 | OpenClaw 完整使用指南
4. 新手必看 | OpenClaw 本地部署 + 接入机器人全流程

## 摘要
详细介绍 OpenClaw 的安装、配置、使用全流程。包含 Node.js 安装、大模型配置、QQ/微信机器人接入、常见问题解决等内容。

---

## 正文

> **前置要求：** Node.js v22.0 或更高版本
> 
> **适合人群：** 零基础新手、命令行不熟悉者
> 
> **预计耗时：** 30-60 分钟
> 
> **成本：** 免费（本地部署）

---

## 01 安装前准备

### 检查 Node.js 版本

打开终端，输入：

```bash
node -v
```

**要求：** v22.0 或更高版本

**如果版本过低或未安装：**

1. 访问：https://nodejs.org/
2. 下载「LTS 版本」
3. 安装后重新打开终端

---

## 02 安装 OpenClaw

### Mac / Linux 用户

在终端执行以下命令：

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

### Windows 用户

1. 下载安装包
2. 双击运行安装程序
3. 按提示完成安装

---

## 03 初始配置

安装结束后会自动出现配置界面，共 **9 个步骤**。

**操作说明：**
- ⬆️⬇️ 方向键：上下选择
- ↩️ 回车键：确认
- ␣ 空格键：勾选/取消勾选

---

### Step 1：风险确认

```
I understand this is powerful and inherently risky. Continue?
```

**选择：** `Yes`

**说明：** 确认你了解 OpenClaw 能力强大，但也有潜在风险。

---

### Step 2：选择模式

```
Onboarding mode
```

**选择：** `QuickStart`（快速启动）

**说明：** 新手推荐，简化配置流程。

---

### Step 3：选择模型提供商

```
Model/auth provider
```

**选择：** `Skip for now`（稍后配置）

**说明：** 先跳过，后面会单独配置大模型。

---

### Step 4：过滤模型

```
Filter models by provider
```

**选择：** `All providers`（所有提供商）

**说明：** 显示所有可用模型。

---

### Step 5：默认模型

```
Default model
```

**选择：** 使用默认配置（直接回车）

---

### Step 6：选择渠道

```
Select channel (QuickStart)
```

**选择：** `Skip for now`（稍后配置）

**说明：** 先跳过，后面可以配置 QQ/微信/飞书等。

---

### Step 7：配置技能

```
Configure skills now? (recommended)
```

**选择：** `No`

**说明：** 先不配置技能，后续按需安装。

---

### Step 8：启用钩子

```
Enable hooks?
```

**操作：**
1. 按 ␣ 空格键勾选
2. 选择 `Skip for now`
3. 按 ↩️ 回车继续

---

### Step 9：启动方式

```
How do you want to hatch your bot?
```

**选择：** `Hatch in TUI`（终端界面）

**说明：** 在终端中启动对话界面。

---

### ✅ 配置完成

看到以下提示即成功：

```
✓ Configuration complete
✓ Gateway started on port 5800
```

**下一步：** 打开浏览器访问 `http://localhost:5800` 查看 Web 界面。

---

## 04 配置大模型

OpenClaw 本身是个「空壳」，需要接入大模型才能对话。

### 可选模型

| 模型 | 提供商 | 特点 |
|------|--------|------|
| qwen3.5-plus | 通义千问 | 综合能力强，性价比高 ⭐ |
| qwen3-max | 通义千问 | 最强版本 |
| glm-5 | 智谱 AI | 响应快 |
| kimi-k2.5 | 月之暗面 | 长文本处理 |
| MiniMax-M2.5 | MiniMax | 创意好 |

### 获取 API Key

以通义千问为例：

1. 访问：https://dashscope.console.aliyun.com/
2. 登录/注册账号
3. 进入「API-KEY 管理」
4. 点击「创建新的 API-KEY」
5. 复制生成的 Key（类似 `sk-xxxxxxxxxxxxxxxx`）

**⚠️ 注意：** API Key 只显示一次，务必复制保存！

### 配置 API Key

在终端执行：

```bash
openclaw config set models.bailian.apiKey 你的 API_KEY
openclaw config set agents.defaults.model.primary bailian/qwen3.5-plus
```

把 `你的 API_KEY` 替换成刚才复制的 Key。

### 验证配置

```bash
openclaw config list
```

应该能看到你配置的模型和 API Key。

---

## 05 测试对话

### 方式一：TUI（终端界面）

在终端输入：

```bash
openclaw tui
```

进入对话界面后，输入：

```
你好
```

如果看到 AI 回复，说明配置成功！

### 方式二：Web UI

在终端输入：

```bash
openclaw dashboard
```

在浏览器打开的界面中进行对话。

### 方式三：命令行

```bash
openclaw chat 今天天气怎么样
```

---

## 06 接入 QQ 机器人

### Step 1: 创建 QQ 机器人

1. 访问 QQ 开放平台：https://q.qq.com/
2. 用手机 QQ 扫码登录
3. 点击「创建机器人」
4. 填写信息：
   ```
   名称：你的 AI 助手
   头像：随便选一张
   简介：一个智能 AI 助手
   ```
5. 点击「确定」

### Step 2: 获取凭证

创建成功后，在「应用信息」页面保存：

```
AppID: 1234567890（示例）
AppSecret: abcdefghijklmnopqrstuvwxyz（示例）
```

**⚠️ 重要：** AppSecret 只显示一次，务必复制保存！

### Step 3: 安装 QQ 插件

在终端输入：

```bash
openclaw plugins install @sliverp/qqbot@latest
```

**如果安装慢**（网络问题），用国内镜像：

```bash
npm config set registry https://registry.npmmirror.com
openclaw plugins install @sliverp/qqbot@latest
```

### Step 4: 配置 QQ 凭证

在终端输入（替换成你的）：

```bash
openclaw config set channels.qq-official.appId 你的 AppID
openclaw config set channels.qq-official.appSecret 你的 AppSecret
openclaw config set channels.qq-official.allowPrivateChat true
openclaw config set channels.qq-official.allowGroupChat true
```

### Step 5: 重启服务

```bash
openclaw gateway restart
```

### Step 6: 测试对话

1. 打开手机 QQ
2. 搜索你的机器人名称
3. 发送：`你好`
4. 等待回复（3-10 秒）

**如果收到回复，恭喜成功！** 🎉

---

## 07 接入微信机器人

### 方案 A：个人微信（需要企业资质）

**注意：** 个人微信接入需要企业微信资质，个人用户建议使用 QQ 机器人。

### 方案 B：微信公众号（推荐个人）

可以创建公众号机器人，用户通过公众号菜单与 AI 对话。

**步骤：**

1. 注册微信公众号：https://mp.weixin.qq.com/
2. 创建公众号（订阅号即可）
3. 在公众号后台配置服务器
4. 使用 OpenClaw 处理消息

**配置命令：**

```bash
openclaw plugins install @openclaw/wechat-mp
openclaw config set channels.wechat-mp.token 你的 Token
openclaw config set channels.wechat-mp.aesKey 你的 AES Key
openclaw gateway restart
```

### 方案 C：企业微信（有企业可用）

1. 访问：https://work.weixin.qq.com/
2. 创建企业（个人可创建测试企业）
3. 创建应用
4. 获取 CorpID 和 Secret

**配置命令：**

```bash
openclaw plugins install @openclaw/wecom
openclaw config set channels.wecom.corpId 你的 CorpID
openclaw config set channels.wecom.secret 你的 Secret
openclaw gateway restart
```

---

## 08 切换模型

### 临时切换（当前会话有效）

在 TUI 界面输入：

```
/model qwen3-coder-next
```

界面返回 `model set to qwen3-coder-next` 即表示生效。

### 永久切换（所有新会话生效）

修改配置文件：

```bash
openclaw config set agents.defaults.model.primary bailian/glm-5
openclaw gateway restart
```

### 查看可用模型

```bash
openclaw tui
/model
```

---

## 09 常见问题

### Q1: 报错 "HTTP 401: Incorrect API key provided."

**可能原因：**
1. API Key 无效、过期、为空
2. API Key 复制不完整（有空格）
3. 订阅状态异常

**解决方案：**

1. 重新获取 API Key
2. 重新配置：
```bash
openclaw config set models.bailian.apiKey 新的 API_KEY
openclaw gateway restart
```

---

### Q2: QQ 机器人无响应

**排查步骤：**

1. 检查服务状态
```bash
openclaw gateway status
```

2. 检查配置
```bash
openclaw config get channels.qq-official
```

3. 查看日志
```bash
openclaw gateway logs
```

4. 确认 QQ 机器人是「启用」状态

---

### Q3: 安装时提示权限不足

**错误：**
```
EACCES: permission denied
```

**解决：**
```bash
sudo curl -fsSL https://openclaw.ai/install.sh | bash
```

---

### Q4: 命令找不到

**错误：**
```
command not found: openclaw
```

**解决：**
```bash
export PATH=$PATH:$(npm config get prefix)/bin
```

然后重新打开终端。

---

## 10 模型说明

| 模型 | 特点 | 适用场景 |
|------|------|---------|
| **qwen3.5-plus** | 综合能力强，性价比高 | 日常对话、写作、分析 ⭐ |
| qwen3-max | 最强版本 | 复杂任务、深度分析 |
| qwen3-coder-next | 代码专用 | 编程、代码审查 |
| glm-5 | 响应快 | 快速问答 |
| kimi-k2.5 | 长文本 | 文档分析、长文阅读 |
| MiniMax-M2.5 | 创意好 | 创意写作、头脑风暴 |

**新手推荐：qwen3.5-plus**（默认已配置）

---

## 11 下一步

安装配置完成后，可以：

### ✅ 试试这些命令

```bash
# 对话
openclaw chat 你好

# 查看状态
openclaw gateway status

# 查看日志
openclaw gateway logs

# 安装技能
openclaw plugins install web-search
openclaw plugins install browser
```

### ✅ 探索更多功能

- **网页搜索**：让 AI 联网查资料
- **浏览器自动化**：让 AI 操作网页
- **文件处理**：让 AI 读写文件
- **定时任务**：让 AI 定时执行任务

### ✅ 接入更多平台

- **飞书机器人**：配置飞书开放平台
- **钉钉机器人**：配置钉钉开放平台
- **Telegram 机器人**：配置 Telegram Bot

---

## 12 资源汇总

**官方链接：**

| 资源 | 地址 |
|------|------|
| OpenClaw 官网 | https://openclaw.ai |
| 官方文档 | https://docs.openclaw.ai |
| GitHub | https://github.com/openclaw/openclaw |
| Discord 社区 | https://discord.com/invite/clawd |

**QQ 开放平台：**
- 地址：https://q.qq.com/

**模型平台：**
- 通义千问：https://dashscope.console.aliyun.com/
- 智谱 AI：https://open.bigmodel.cn/
- 月之暗面：https://platform.moonshot.cn/

**配置文件位置：**
```
~/.openclaw/config/config.json
```

**日志文件位置：**
```
~/.openclaw/logs/gateway.log
```

---

## 13 写在最后

恭喜你完成了 OpenClaw 的安装配置！

**现在你拥有了：**
- ✅ 一个本地运行的 AI 助手
- ✅ 多个主流大模型随意切换
- ✅ QQ/微信机器人接入能力
- ✅ 可扩展的插件系统

**接下来：**
- 用它帮你写代码、写文章、查资料
- 接入 QQ/微信，让 AI 随时待命
- 探索各种 Skills，解锁更多能力

**最大的价值不是拥有，而是使用。**

---

**🎁 福利：**

关注公众号，回复「OpenClaw」获取：
1. 本文 PDF 版本（可打印）
2. 配置文件模板（JSON）
3. QQ 机器人接入视频教程
4. 技术交流群入口

---

*本文基于 OpenClaw v2.6.0 编写*

*遇到问题？在评论区留言，我会逐一回复*

*如果觉得有用，请点赞 + 在看 + 分享*
