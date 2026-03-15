# 📕 小红书发布指南

**创建时间**: 2026-03-03  
**最后更新**: 2026-03-03

---

## 🚀 发布流程

### 1. 检查登录状态
```bash
npx mcporter call xiaohongshu-mcp.check_login_status
```
✅ 返回 "已登录" 即可继续

### 2. 发布图文笔记
```bash
npx mcporter call xiaohongshu-mcp.publish_content 'title:"标题"' 'content:"正文内容"' 'images:["/图片/绝对路径.jpg"]'
```

### 3. 参数说明
| 参数 | 说明 | 要求 |
|------|------|------|
| title | 笔记标题 | 最多 20 个中文字或英文单词 |
| content | 正文内容 | 不包含#标签，标签用 tags 参数 |
| images | 图片路径列表 | 至少 1 张，必须本地绝对路径 |
| tags | 话题标签 | 可选，如 `tags:["美食","旅行"]` |
| visibility | 可见范围 | 可选：公开可见 (默认)/仅自己可见/仅互关好友可见 |
| schedule_at | 定时发布 | 可选，ISO8601 格式，支持 1 小时至 14 天内 |
| is_original | 声明原创 | 可选，true/false |

---

## ⚠️ 关键注意事项

1. **图片必须是本地文件** - 不能用网络链接
2. **图片路径必须用绝对路径** - 如 `/Users/a01/Desktop/photo.jpg`
3. **参数格式** - 使用 `'key:"value"'` 格式
4. **cookies.json 位置** - `/Users/a01/.openclaw/workspace/cookies.json`
5. **MCP 服务地址** - `http://localhost:18060/mcp`

---

## 📋 可用工具列表

| 工具 | 说明 |
|------|------|
| check_login_status | 检查登录状态 |
| delete_cookies | 删除 cookies，重置登录 |
| list_feeds | 获取首页 Feeds 列表 |
| get_feed_detail | 获取笔记详情 |
| publish_content | 发布图文内容 |
| publish_with_video | 发布视频内容 |
| like_feed | 点赞/取消点赞 |
| favorite_feed | 收藏/取消收藏 |
| post_comment_to_feed | 发表评论 |
| reply_comment_in_feed | 回复评论 |
| search_feeds | 搜索内容 |
| user_profile | 获取用户主页 |

---

## 🔧 部署配置

### MCP 配置位置
```
/Users/a01/.openclaw/workspace/config/mcporter.json
```

### 配置命令
```bash
# 安装 mcporter
npm i -g mcporter

# 添加小红书 MCP
npx mcporter config add xiaohongshu-mcp http://localhost:18060/mcp

# 查看配置
npx mcporter list xiaohongshu-mcp
```

---

## 📝 内容模板

### 触心 TOUCHING 手套 - 5 篇笔记已准备
1. 开箱体验向 - "869 的手套到底值不值？"
2. 穿搭种草向 - "被问了 800 遍的手套链接！"
3. 送礼指南向 - "送女友/送妈妈不出错礼物"
4. 材质科普向 - "小山羊皮凭什么卖 869？"
5. 细节控向 - "869 的手套细节有多绝？"

内容文件：`/Users/a01/.openclaw/workspace/触心 TOUCHING 手套_多平台营销内容.md`

---

## 💡 发布技巧

- **最佳时间**: 早 8-10 点、午 12-14 点、晚 19-22 点
- **图片数量**: 3-6 张效果最佳，至少 1 张
- **标签数量**: 5-10 个相关标签
- **互动维护**: 发布后 1 小时内积极回复评论

---

**备注**: 此文件为永久记忆，小红书发布相关操作以此为准。

---

## 🔍 图片搜索方式

**不需要 API key**，直接用 curl 搜索和下载：

```bash
# 搜索图片并下载
curl -L -A "Mozilla/5.0" -o /路径/图片.jpg "图片 URL"

# 验证图片
file /路径/图片.jpg
ls -lh /路径/图片.jpg
```

**推荐图片源**：
- Unsplash (unsplash.com)
- Pexels (pexels.com)
- Pixabay (pixabay.com)
- 谷歌图片搜索

---

## 📅 发布频率

**每天 3 篇**：
- 早 10:00
- 午 14:00
- 晚 20:00
