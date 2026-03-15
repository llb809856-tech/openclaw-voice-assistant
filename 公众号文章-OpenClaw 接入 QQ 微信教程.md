# 公众号文章：OpenClaw 接入 QQ/微信教程

## 标题备选
1. 手把手教学 | OpenClaw 接入微信、QQ 机器人，看完就会
2. 建议收藏 | OpenClaw 接入微信 QQ 详细教程（2026 最新版）
3. 30 分钟搞定 | OpenClaw 接入微信、QQ 机器人完整指南
4. 零基础也能懂 | OpenClaw 接入微信 QQ，打造你的 AI 助手

## 摘要
本文详细介绍如何将 OpenClaw 接入微信和 QQ 机器人，从安装配置到接入 IM 平台，手把手教学，看完就能上手。无需服务器，本地即可运行。

---

## 正文

> **前置要求：** 已安装 OpenClaw
> 
> **适合人群：** 想接入微信/QQ 机器人的新手
> 
> **预计耗时：** 30-60 分钟
> 
> **成本：** 免费（本地部署）

---

## 01 前置准备

### 检查 OpenClaw 状态

打开终端，输入：

```bash
openclaw gateway status
```

**如果未安装**，先执行安装：

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

### 配置大模型

OpenClaw 需要接入大模型才能对话。

**获取 API Key：**

1. 访问：https://dashscope.console.aliyun.com/
2. 登录/注册账号
3. 进入「API-KEY 管理」
4. 复制生成的 Key

**配置命令：**

```bash
openclaw config set models.bailian.apiKey 你的 API_KEY
openclaw config set agents.defaults.model.primary bailian/qwen3.5-plus
openclaw gateway restart
```

---

## 02 接入 QQ 机器人

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

![创建 QQ 机器人](https://example.com/qq-create.png)

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

**预期回复：**
```
你好！我是你的 AI 助手，有什么可以帮你的吗？
```

**如果收到回复，恭喜成功！** 🎉

---

## 03 接入微信机器人

微信机器人有 3 种方案，根据你的情况选择：

### 方案 A：微信公众号（推荐个人）

适合个人用户，通过公众号菜单与 AI 对话。

**步骤：**

#### 1. 注册公众号

1. 访问：https://mp.weixin.qq.com/
2. 点击「立即注册」
3. 选择「订阅号」（个人即可）
4. 填写信息并完成验证

#### 2. 配置服务器

1. 登录公众号后台
2. 进入「设置与开发」→「基本配置」
3. 填写服务器配置：
   ```
   URL: http://你的服务器 IP:5800/wechat/callback
   Token: 自定义一个字符串（如：mytoken123）
   EncodingAESKey: 随机生成
   ```
4. 点击「提交」

#### 3. 安装微信插件

```bash
openclaw plugins install @openclaw/wechat-mp
```

#### 4. 配置微信凭证

```bash
openclaw config set channels.wechat-mp.token 你的 Token
openclaw config set channels.wechat-mp.aesKey 你的 AES Key
openclaw config set channels.wechat-mp.appId 你的 AppID
openclaw config set channels.wechat-mp.appSecret 你的 AppSecret
openclaw gateway restart
```

#### 5. 验证配置

在公众号后台点击「启用服务器」，看到成功提示即可。

---

### 方案 B：企业微信（有企业可用）

适合有企业资质的用户，可在企业微信群中使用。

**步骤：**

#### 1. 创建企业

1. 访问：https://work.weixin.qq.com/
2. 点击「立即注册」
3. 创建企业（个人可创建测试企业）

#### 2. 创建应用

1. 进入「应用管理」
2. 点击「创建应用」
3. 填写应用信息
4. 获取 CorpID 和 Secret

#### 3. 安装插件

```bash
openclaw plugins install @openclaw/wecom
```

#### 4. 配置凭证

```bash
openclaw config set channels.wecom.corpId 你的 CorpID
openclaw config set channels.wecom.secret 你的 Secret
openclaw config set channels.wecom.agentId 你的 AgentId
openclaw gateway restart
```

---

### 方案 C：个人微信（需要第三方工具）

**注意：** 个人微信没有官方 API，需要使用第三方工具。

**推荐工具：**
- Wechaty（开源框架）
- 微秘书（付费服务）
- 其他第三方平台

**风险提示：** 使用第三方工具存在封号风险，请谨慎选择。

---

## 04 常见问题

### Q1: QQ 机器人无响应

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

### Q2: 微信公众号验证失败

**可能原因：**
1. URL 无法访问（服务器未启动）
2. Token 不匹配
3. 网络问题

**解决方案：**

1. 确认 OpenClaw 已启动
2. 检查 Token 是否一致
3. 确保服务器可公网访问

---

### Q3: 插件安装失败

**错误：**
```
npm ERR! network request failed
```

**解决：**
```bash
npm config set registry https://registry.npmmirror.com
openclaw plugins install 插件名
```

---

### Q4: 提示 "channel not found"

**原因：** 插件未正确安装或配置

**解决：**
```bash
# 重新安装插件
openclaw plugins uninstall @sliverp/qqbot
openclaw plugins install @sliverp/qqbot@latest

# 重新配置
openclaw config set channels.qq-official.appId 你的 AppID
openclaw config set channels.qq-official.appSecret 你的 AppSecret
openclaw gateway restart
```

---

## 05 进阶配置

### 配置多个机器人

可以创建多个机器人，用于不同场景：

```bash
# 机器人 1：客服助手
openclaw config set channels.qq-official.appId xxx1
openclaw config set channels.qq-official.appSecret xxx1

# 机器人 2：技术助手
# 需要配置多个 channel，参考官方文档
```

### 配置技能

让机器人具备更多能力：

```bash
# 网页搜索
openclaw plugins install web-search

# 浏览器自动化
openclaw plugins install browser

# 文件处理
openclaw plugins install file-tools
```

### 配置模型

不同场景使用不同模型：

```bash
# 日常对话用 qwen3.5-plus
openclaw config set agents.defaults.model.primary bailian/qwen3.5-plus

# 代码任务用 qwen3-coder-next
# 在对话中输入 /model qwen3-coder-next
```

---

## 06 测试清单

接入完成后，建议测试以下功能：

### QQ 机器人测试

- [ ] 发送「你好」，检查是否回复
- [ ] 发送「今天天气怎么样」，检查联网搜索
- [ ] 发送「写一首诗」，检查创意能力
- [ ] 发送「1+1 等于几」，检查基本计算
- [ ] 在群聊中@机器人，检查群聊功能

### 微信机器人测试

- [ ] 公众号菜单可正常点击
- [ ] 发送消息后 AI 正常回复
- [ ] 图片消息可正常处理
- [ ] 长文本消息可正常处理

---

## 07 资源汇总

**官方链接：**

| 资源 | 地址 |
|------|------|
| OpenClaw 官网 | https://openclaw.ai |
| 官方文档 | https://docs.openclaw.ai |
| GitHub | https://github.com/openclaw/openclaw |
| Discord 社区 | https://discord.com/invite/clawd |

**平台链接：**

| 平台 | 地址 |
|------|------|
| QQ 开放平台 | https://q.qq.com/ |
| 微信公众号 | https://mp.weixin.qq.com/ |
| 企业微信 | https://work.weixin.qq.com/ |

**配置文件位置：**
```
~/.openclaw/config/config.json
```

---

## 08 写在最后

恭喜你完成了 OpenClaw 与微信、QQ 的接入！

**现在你拥有了：**
- ✅ 一个 7×24 小时在线的 AI 助手
- ✅ QQ 机器人（个人可用）
- ✅ 微信机器人（公众号/企业微信）
- ✅ 可扩展的插件系统

**接下来：**
- 让 AI 帮你处理日常问题
- 接入更多技能（搜索、浏览器、文件）
- 探索商业化可能（客服、问答、内容创作）

**最大的价值不是拥有，而是使用。**

---

**🎁 福利：**

关注公众号，回复「QQ 机器人」获取：
1. 本文 PDF 版本（可打印）
2. QQ 机器人配置视频教程
3. 常见问题排查手册
4. 技术交流群入口

---

*本文基于 OpenClaw v2.6.0 编写*

*遇到问题？在评论区留言，我会逐一回复*

*如果觉得有用，请点赞 + 在看 + 分享*
