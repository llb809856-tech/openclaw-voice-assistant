# 📝 微信公众号发布工具

**位置**: `~/.openclaw/skills/wechat-publisher/`

**创建时间**: 2026-03-06  
**更新时间**: 2026-03-09  

---

## 🚀 快速使用

### 方法 1：Shell 脚本（推荐）⭐⭐⭐

```bash
cd ~/.openclaw/skills/wechat-publisher
./publish.sh
```

**功能**：
- ✅ 自动获取 Token
- ✅ 上传封面图（永久素材）
- ✅ 生成带排版的 HTML
- ✅ 发布到草稿箱

**配置**：
编辑 `publish.sh` 修改：
```bash
APP_ID="你的 AppID"
APP_SECRET="你的 AppSecret"
TITLE="文章标题"
AUTHOR="作者名"
```

---

### 方法 2：Node.js 脚本（免费版）⭐⭐

```bash
cd ~/.openclaw/skills/wechat-publisher
node publish-free.js /path/to/article.md green /path/to/cover.jpg
```

**参数**：
1. Markdown 文件路径
2. 主题颜色（red/green/blue）
3. 封面图路径（可选）

**配置**：
编辑 `publish-free.js` 修改：
```javascript
const CONFIG = {
  appId: '你的 AppID',
  appSecret: '你的 AppSecret',
  markdownPath: '/path/to/article.md',
  theme: 'green',
  author: '作者名',
  coverImagePath: '/path/to/cover.jpg'
};
```

---

## 📁 文件说明

| 文件 | 说明 |
|------|------|
| `publish.sh` | Shell 脚本（完整排版） |
| `publish-free.js` | Node.js 脚本（免费版） |
| `cover.jpg` | 默认封面图 |

---

## ⚠️ 关键注意事项

### 1. IP 白名单

确保你的服务器 IP 在微信后台白名单中：

```
登录 https://mp.weixin.qq.com/
设置与开发 → 基本配置 → IP 白名单
添加你的服务器 IP
```

### 2. 永久素材 vs 临时素材

**草稿箱 API 要求**：
- ✅ 必须用 **永久素材** API 上传封面图
- ❌ 不能用 **临时素材** API

**正确 API**：
```bash
# ✅ 永久素材
https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=xxx&type=image

# ❌ 临时素材（会报 40007 错误）
https://api.weixin.qq.com/cgi-bin/media/upload?access_token=xxx&type=image
```

### 3. 公众号类型

- **订阅号**：需要认证才有草稿箱 API 权限
- **服务号**：默认有草稿箱 API 权限

---

## 🐛 故障排查

### 错误码 40007

**原因**：
1. IP 不在白名单
2. 用了临时素材 API（不是永久素材）
3. 公众号无草稿箱权限

**解决**：
1. 检查 IP 白名单
2. 确保用 `add_material` API（不是 `upload`）
3. 公众号认证

### 错误码 48001

**原因**：API 未授权

**解决**：公众号认证

### 错误码 45106

**原因**：API 已废弃

**解决**：用草稿箱 API（不是素材管理 API）

---

## 📖 使用流程

```
1. 准备 Markdown 文章
   ↓
2. 准备封面图（可选）
   ↓
3. 运行发布脚本
   ↓
4. 检查草稿箱
   ↓
5. 预览无误后群发
```

---

## 📝 更新日志

### v1.1 (2026-03-09)
- ✅ 修复：使用永久素材 API（之前用临时素材报 40007）
- ✅ 整理：工具统一放到 `~/.openclaw/skills/wechat-publisher/`

### v1.0 (2026-03-06)
- ✅ 初始版本

---

**最后更新**: 2026-03-09 23:56
