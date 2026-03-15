# 公众号文章：OpenClaw 新手入门教程

## 标题备选
1. 零基础教程 | 30 分钟搭建你的第一个 AI 机器人（Mac 版）
2. 手把手教学 | OpenClaw 本地部署 + 接入 QQ/微信，看完就会
3. 不用服务器！在 Mac 上部署 OpenClaw，接入 QQ/微信机器人
4. 新手必看 | OpenClaw 从安装到使用完整指南（2026 最新版）

## 摘要
本文从零开始，手把手教你在 Mac 上部署 OpenClaw，接入大模型，创建 QQ/微信机器人。无需服务器，无需编程基础，30 分钟即可完成。

---

## 正文

> **适合人群：** 完全零基础的小白
> 
> **所需设备：** 一台 Mac 电脑（Intel 或 M 系列芯片）
> 
> **预计耗时：** 30-60 分钟
> 
> **成本：** 0 元（本地部署免费）

---

## 01 第一步：安装 OpenClaw

### Step 1: 打开终端

在 Mac 上，按 `Command + 空格`，搜索「终端」，打开它。

你会看到一个黑色的窗口，这就是终端。

![终端界面](https://example.com/terminal.png)

### Step 2: 安装 Node.js

OpenClaw 需要 Node.js 环境。在终端输入：

```bash
node -v
```

**如果显示版本号**（如 v20.0.0），说明已安装，跳过这步。

**如果显示「command not found」**，需要安装：

1. 访问：https://nodejs.org/
2. 下载「LTS 版本」（长期支持版）
3. 双击安装包，一路「下一步」

### Step 3: 安装 OpenClaw

在终端输入以下命令（复制粘贴，然后按回车）：

```bash
npm install -g openclaw
```

**等待安装完成**（约 1-3 分钟），看到类似提示即成功：

```
added 150 packages in 2m
```

### Step 4: 验证安装

输入：

```bash
openclaw --version
```

如果显示版本号，说明安装成功！✅

---

## 02 第二步：配置大模型

OpenClaw 本身是个「空壳」，需要接入大模型才能对话。

### Step 1: 选择模型

推荐模型（性价比高）：

| 模型 | 提供商 | 特点 | 价格 |
|------|--------|------|------|
| qwen3.5-plus | 阿里云 | 综合能力强 | 便宜 |
| glm-5 | 智谱 AI | 响应快 | 便宜 |
| MiniMax-M2.5 | MiniMax | 创意好 | 中等 |

**新手推荐：qwen3.5-plus**（综合最好）

### Step 2: 获取 API Key

以阿里云为例：

1. 访问：https://dashscope.console.aliyun.com/
2. 登录/注册阿里云账号
3. 进入「API-KEY 管理」
4. 点击「创建新的 API-KEY」
5. 复制生成的 Key（类似 `sk-xxxxxxxxxxxxxxxx`）

**⚠️ 注意：** API Key 只显示一次，务必复制保存！

### Step 3: 配置 OpenClaw

在终端输入：

```bash
openclaw config set model bailian/qwen3.5-plus
openclaw config set bailian.api_key 你的 API_KEY
```

把 `你的 API_KEY` 替换成刚才复制的 Key。

**验证配置：**

```bash
openclaw config list
```

应该能看到你配置的模型和 API Key。

---

## 03 第三步：启动 OpenClaw

### Step 1: 启动服务

在终端输入：

```bash
openclaw gateway start
```

看到以下提示即成功：

```
✓ Gateway started on port 5800
```

### Step 2: 测试对话

在终端输入：

```bash
openclaw chat 你好
```

如果看到 AI 回复，说明一切正常！✅

**示例：**
```
你：你好
AI: 你好！我是你的 AI 助手，有什么可以帮你的吗？
```

### Step 3: 查看状态

随时可以查看运行状态：

```bash
openclaw gateway status
```

**停止服务：**
```bash
openclaw gateway stop
```

---

## 04 第四步：创建 QQ 机器人

### Step 1: 访问 QQ 开放平台

浏览器打开：
```
https://q.qq.com/
```

### Step 2: 登录账号

用手机 QQ 扫描二维码登录。

**注意：**
- ✅ 个人账号即可
- ✅ 不需要企业资质

### Step 3: 创建机器人

1. 点击「创建机器人」
2. 填写信息：
   ```
   名称：你的 AI 助手
   头像：随便选一张
   简介：一个智能 AI 助手
   ```
3. 点击「确定」

### Step 4: 获取凭证

创建成功后，在「应用信息」页面保存：

```
AppID: 1234567890（示例）
AppSecret: abcdefghijklmnopqrstuvwxyz（示例）
```

**⚠️ 重要：** AppSecret 只显示一次，务必复制保存！

---

## 05 第五步：接入 QQ 机器人

### Step 1: 安装 QQ 插件

在终端输入：

```bash
openclaw plugins install @sliverp/qqbot@latest
```

**如果安装慢**（网络问题），用国内镜像：

```bash
npm config set registry https://registry.npmmirror.com
openclaw plugins install @sliverp/qqbot@latest
```

### Step 2: 配置 QQ 凭证

在终端输入（替换成你的）：

```bash
openclaw config set channels.qq-official.appId 你的 AppID
openclaw config set channels.qq-official.appSecret 你的 AppSecret
openclaw config set channels.qq-official.allowPrivateChat true
```

### Step 3: 重启服务

```bash
openclaw gateway restart
```

### Step 4: 测试对话

1. 打开手机 QQ
2. 搜索你的机器人名称
3. 发送：`你好`
4. 等待回复（3-10 秒）

**如果收到回复，恭喜成功！** 🎉

---

## 06 第六步：创建微信机器人（可选）

微信机器人需要企业资质，个人用户可跳过。

### Step 1: 访问微信开放平台

```
https://developers.weixin.qq.com/
```

### Step 2: 创建企业微信应用

1. 登录/注册
2. 进入「企业微信」
3. 创建应用
4. 获取 CorpID 和 Secret

### Step 3: 安装微信插件

```bash
openclaw plugins install @openclaw/wechat-bot
```

### Step 4: 配置

```bash
openclaw config set channels.wechat.corpId 你的 CorpID
openclaw config set channels.wechat.secret 你的 Secret
openclaw gateway restart
```

---

## 07 常见问题

### Q1: 安装时提示「权限不足」

**错误：**
```
npm ERR! Error: EACCES: permission denied
```

**解决：**
```bash
sudo npm install -g openclaw
```

输入密码（不会显示），按回车。

---

### Q2: 找不到命令

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

### Q3: QQ 机器人无响应

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

### Q4: API Key 无效

**错误：**
```
Invalid API Key
```

**解决：**
1. 确认复制完整（没有多余空格）
2. 在阿里云后台确认 Key 状态正常
3. 重新配置：
```bash
openclaw config set bailian.api_key 新的 API_KEY
openclaw gateway restart
```

---

## 08 下一步

机器人已经跑起来了，可以：

### ✅ 试试这些命令

在 QQ 里发送：

```
今天天气怎么样？
写一首关于春天的诗
123 * 456 等于多少？
用 Python 写一个快速排序
```

### ✅ 探索更多功能

- 网页搜索：`openclaw plugins install web-search`
- 浏览器自动化：`openclaw plugins install browser`
- 文件处理：`openclaw plugins install file-tools`

### ✅ 加入社区

- 官方文档：https://docs.openclaw.ai
- Discord 社区：https://discord.com/invite/clawd
- GitHub: https://github.com/openclaw/openclaw

---

## 09 资源汇总

**必备链接：**

| 资源 | 地址 |
|------|------|
| OpenClaw 官网 | https://openclaw.ai |
| 阿里云 DashScope | https://dashscope.console.aliyun.com/ |
| QQ 开放平台 | https://q.qq.com/ |
| 官方文档 | https://docs.openclaw.ai |

**配置文件位置：**
```
~/.openclaw/config/config.json
```

**日志文件位置：**
```
~/.openclaw/logs/gateway.log
```

---

## 10 写在最后

恭喜你完成了从零到一的部署！

**最大的障碍不是技术，而是开始。**

现在你已经拥有了一个 7×24 小时在线的 AI 助手，可以：
- 回答各种问题
- 帮你写代码、写文章
- 自动处理任务
- 7×24 小时在线

**接下来，发挥你的想象力，让它为你创造价值！**

---

**🎁 福利：**

关注公众号，回复「新手教程」获取：
1. 本文 PDF 版本（可打印）
2. 常见问题排查手册
3. 技术交流群入口
4. 1 对 1 配置指导（限前 50 名）

---

*本文测试环境：macOS 14.0 / OpenClaw v2.6.0 / Node.js v20*

*遇到问题？在评论区留言，我会逐一回复*

*如果觉得有用，请点赞 + 在看 + 分享*
