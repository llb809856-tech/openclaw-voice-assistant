# 公众号文章：OpenClaw 官方安装教程

## 标题备选
1. 官方教程 | OpenClaw 完整安装配置指南（2026 最新版）
2. 阿里云官方出品 | OpenClaw 从安装到使用全流程
3. 建议收藏 | OpenClaw 安装配置完整教程（含 Coding Plan 配置）
4. 零基础也能懂 | OpenClaw 安装 + 配置 + 使用一篇搞定

## 摘要
本文根据阿里云官方教程整理，详细介绍 OpenClaw 的安装、配置、使用全流程。包含 Node.js 安装、Coding Plan 配置、模型切换、常见问题解决等内容。

---

## 正文

> **前置要求：** Node.js v22.0 或更高版本
> 
> **适合人群：** 零基础新手、命令行不熟悉者
> 
> **预计耗时：** 20-40 分钟
> 
> **成本：** 免费（Coding Plan 套餐）

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

**说明：** 先跳过，后面会单独配置 Coding Plan。

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

## 04 配置 Coding Plan

### 方式一：通过 Web UI 配置（推荐）

#### Step 1: 打开 Web UI

在终端执行：

```bash
openclaw dashboard
```

会自动在浏览器中打开配置界面。

#### Step 2: 进入配置页面

在 Web UI 左侧菜单栏选择：
```
配置 > All Settings > RAW
```

#### Step 3: 复制配置内容

复制以下内容到「Raw JSON」输入框，替换已有内容：

```json
{
  "models": {
    "mode": "merge",
    "providers": {
      "bailian": {
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "apiKey": "YOUR_API_KEY",
        "api": "openai-completions",
        "models": [
          {
            "id": "qwen3.5-plus",
            "name": "qwen3.5-plus",
            "reasoning": false,
            "input": ["text", "image"],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 1000000,
            "maxTokens": 65536
          },
          {
            "id": "qwen3-max-2026-01-23",
            "name": "qwen3-max-2026-01-23",
            "reasoning": false,
            "input": ["text"],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 262144,
            "maxTokens": 65536
          },
          {
            "id": "qwen3-coder-next",
            "name": "qwen3-coder-next",
            "reasoning": false,
            "input": ["text"],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 262144,
            "maxTokens": 65536
          },
          {
            "id": "qwen3-coder-plus",
            "name": "qwen3-coder-plus",
            "reasoning": false,
            "input": ["text"],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 1000000,
            "maxTokens": 65536
          },
          {
            "id": "MiniMax-M2.5",
            "name": "MiniMax-M2.5",
            "reasoning": false,
            "input": ["text"],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 204800,
            "maxTokens": 131072
          },
          {
            "id": "glm-5",
            "name": "glm-5",
            "reasoning": false,
            "input": ["text"],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 202752,
            "maxTokens": 16384
          },
          {
            "id": "glm-4.7",
            "name": "glm-4.7",
            "reasoning": false,
            "input": ["text"],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 202752,
            "maxTokens": 16384
          },
          {
            "id": "kimi-k2.5",
            "name": "kimi-k2.5",
            "reasoning": false,
            "input": ["text", "image"],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 262144,
            "maxTokens": 32768
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "bailian/qwen3.5-plus"
      },
      "models": {
        "bailian/qwen3.5-plus": {},
        "bailian/qwen3-max-2026-01-23": {},
        "bailian/qwen3-coder-next": {},
        "bailian/qwen3-coder-plus": {},
        "bailian/MiniMax-M2.5": {},
        "bailian/glm-5": {},
        "bailian/glm-4.7": {},
        "bailian/kimi-k2.5": {}
      }
    }
  },
  "gateway": {
    "mode": "local"
  }
}
```

#### Step 4: 替换 API Key

**重要：** 将 `YOUR_API_KEY` 替换为你的 Coding Plan 专属 API Key。

**获取 API Key：**
1. 访问：https://coding.dashscope.aliyuncs.com/
2. 登录阿里云账号
3. 进入「API Key 管理」
4. 复制你的 Key

#### Step 5: 保存配置

1. 单击右上角 **Save** 保存
2. 单击 **Update** 使配置生效

**保存成功后**，apiKey 将显示为 `__OPENCLAW_REDACTED__`（脱敏保护，不影响实际调用）。

---

### 方式二：通过终端配置

在终端执行：

```bash
openclaw config set models.bailian.apiKey 你的 API_KEY
openclaw config set agents.defaults.model.primary bailian/qwen3.5-plus
```

---

## 05 使用 OpenClaw

### Web UI 方式

新开一个终端，运行：

```bash
openclaw dashboard
```

在浏览器打开的 Web UI 中进行对话。

### TUI 方式（终端界面）

在终端运行：

```bash
openclaw tui
```

进入终端对话界面。

---

## 06 切换模型

### 临时切换（当前会话有效）

在 TUI 界面输入：

```
/model qwen3-coder-next
```

界面返回 `model set to qwen3-coder-next` 即表示生效。

**可用模型：**
- qwen3.5-plus（推荐，综合能力最强）
- qwen3-max-2026-01-23
- qwen3-coder-next（代码专用）
- qwen3-coder-plus
- MiniMax-M2.5
- glm-5
- glm-4.7
- kimi-k2.5

### 永久切换（所有新会话生效）

修改配置文件中的 `agents.defaults.model.primary` 字段：

```json
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "bailian/qwen3.5-plus"
      }
    }
  }
}
```

---

## 07 查看已配置模型

在终端输入：

```bash
openclaw tui
```

进入 TUI 界面后，输入：

```
/model
```

即可查看模型列表。

**操作：**
- 回车键：选中模型
- Esc 键：退出模型列表

---

## 08 常见问题

### Q1: 报错 "HTTP 401: Incorrect API key provided."

**可能原因：**

1. API Key 无效、过期、为空、格式错误
2. API Key 与端点环境不匹配
3. OpenClaw 历史配置缓存导致错误

**解决方案：**

**方案 1：检查 API Key**
- 确认是 Coding Plan 套餐专属 Key
- 复制完整且无空格
- 确认订阅状态有效

**方案 2：清除缓存**

删除配置文件中的 bailian 配置项：

```bash
# Mac / Linux
rm ~/.openclaw/agents/main/agent/models.json

# 或直接编辑文件，删除 providers.bailian 部分
```

然后重启 OpenClaw：

```bash
openclaw gateway restart
```

---

### Q2: 安装时提示权限不足

**错误：**
```
EACCES: permission denied
```

**解决：**
```bash
sudo curl -fsSL https://openclaw.ai/install.sh | bash
```

---

### Q3: 命令找不到

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

### Q4: 配置不生效

**解决步骤：**

1. 检查配置文件语法（JSON 格式）
2. 确认已点击「Update」使配置生效
3. 重启 OpenClaw：
```bash
openclaw gateway restart
```

---

## 09 模型说明

| 模型 | 特点 | 适用场景 |
|------|------|---------|
| **qwen3.5-plus** | 综合能力强，性价比高 | 日常对话、写作、分析 ⭐ |
| qwen3-max-2026-01-23 | 最强版本 | 复杂任务、深度分析 |
| qwen3-coder-next | 代码专用 | 编程、代码审查 |
| qwen3-coder-plus | 代码增强版 | 复杂项目开发 |
| MiniMax-M2.5 | 创意好 | 创意写作、头脑风暴 |
| glm-5 | 响应快 | 快速问答 |
| glm-4.7 | 轻量级 | 简单任务 |
| kimi-k2.5 | 长文本 | 文档分析、长文阅读 |

**新手推荐：qwen3.5-plus**（默认已配置）

---

## 10 下一步

安装配置完成后，可以：

### ✅ 试试这些命令

```bash
# 对话
openclaw chat 你好

# 查看状态
openclaw gateway status

# 查看日志
openclaw gateway logs
```

### ✅ 探索更多功能

- 网页搜索：`openclaw plugins install web-search`
- 浏览器自动化：`openclaw plugins install browser`
- 文件处理：`openclaw plugins install file-tools`

### ✅ 接入 IM 平台

- QQ 机器人：配置 QQ 开放平台
- 飞书机器人：配置飞书开放平台
- 钉钉机器人：配置钉钉开放平台

---

## 11 资源汇总

**官方链接：**

| 资源 | 地址 |
|------|------|
| OpenClaw 官网 | https://openclaw.ai |
| 官方文档 | https://docs.openclaw.ai |
| Coding Plan | https://coding.dashscope.aliyuncs.com/ |
| GitHub | https://github.com/openclaw/openclaw |
| Discord 社区 | https://discord.com/invite/clawd |

**配置文件位置：**
```
~/.openclaw/config/config.json
```

**日志文件位置：**
```
~/.openclaw/logs/gateway.log
```

---

## 12 写在最后

恭喜你完成了 OpenClaw 的安装配置！

**现在你拥有了：**
- ✅ 一个本地运行的 AI 助手
- ✅ 8 个主流大模型随意切换
- ✅ Coding Plan 免费额度
- ✅ 可扩展的插件系统

**接下来：**
- 用它帮你写代码、写文章
- 接入 QQ/微信/飞书，让 AI 随时待命
- 探索各种 Skills，解锁更多能力

**最大的价值不是拥有，而是使用。**

---

**🎁 福利：**

关注公众号，回复「OpenClaw」获取：
1. 本文 PDF 版本（可打印）
2. 配置文件模板（JSON）
3. 常见问题排查手册
4. 技术交流群入口

---

*本文根据阿里云官方教程整理 / OpenClaw v2.6.0*

*遇到问题？在评论区留言，我会逐一回复*

*如果觉得有用，请点赞 + 在看 + 分享*
