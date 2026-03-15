#!/bin/bash

# 发布 QQ 机器人技术教程到公众号草稿箱

APP_ID="wxe5c761b6af8be413"
APP_SECRET="a21104b49ddb844188fc64fd44bb885c"
MARKDOWN_FILE="公众号文章-QQ 机器人技术教程.md"
COVER_IMAGE="ai-agent-tech.jpg"

echo "📝 开始发布：QQ 机器人技术教程"
echo ""

# 1. 获取 access_token
echo "📌 获取 access_token..."
TOKEN=$(curl -s "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=$APP_ID&secret=$APP_SECRET" | grep -o '"access_token":"[^"]*"' | cut -d'"' -f4)

if [ -z "$TOKEN" ]; then
  echo "❌ 获取 access_token 失败"
  exit 1
fi
echo "✓ access_token 获取成功"
echo ""

# 2. 上传封面图（永久素材）
echo "📌 上传封面图..."
COVER_RESPONSE=$(curl -s -X POST "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=$TOKEN&type=image" \
  -F "media=@$COVER_IMAGE" \
  -F "description={'title': 'QQ 机器人技术教程', 'introduction': 'OpenClaw 接入教程'}")

COVER_MEDIA_ID=$(echo "$COVER_RESPONSE" | grep -o '"media_id":"[^"]*"' | cut -d'"' -f4)

if [ -z "$COVER_MEDIA_ID" ]; then
  echo "❌ 上传封面图失败"
  echo "响应：$COVER_RESPONSE"
  exit 1
fi
echo "✓ 封面图上传成功：$COVER_MEDIA_ID"
echo ""

# 3. 准备文章内容（读取 Markdown 并简单转换）
echo "📌 准备文章内容..."

# 提取标题
TITLE=$(grep "^# " "$MARKDOWN_FILE" | head -1 | sed 's/^# //')
if [ -z "$TITLE" ]; then
  TITLE="技术教程 | OpenClaw+QQ 机器人部署指南"
fi

# 提取摘要
DIGEST="本文详细介绍如何在 30 分钟内部署 OpenClaw 并接入 QQ 机器人，包含 QQ 开放平台配置、OpenClaw 安装、插件配置、常见问题解决等完整流程。"

# 读取 HTML 内容（已生成的）
HTML_FILE="公众号文章-QQ 机器人技术教程.html"
if [ -f "$HTML_FILE" ]; then
  # 提取 body 内容
  CONTENT=$(cat "$HTML_FILE" | sed -n '/<body>/,/<\/body>/p' | sed '1d;$d')
else
  # 简单转换 Markdown
  CONTENT=$(cat "$MARKDOWN_FILE" | sed 's/^\(.*\)$/<p>\1<\/p>/g' | tr '\n' ' ')
fi

echo "✓ 文章内容准备完成"
echo "  标题：$TITLE"
echo "  摘要：$DIGEST"
echo ""

# 4. 创建草稿
echo "📌 创建草稿..."

# 构建 JSON（使用 Python 处理中文）
python3 << PYTHON_EOF
import json
import urllib.request

content = '''$CONTENT'''

data = {
    "articles": [{
        "title": "$TITLE",
        "content": content,
        "thumb_media_id": "$COVER_MEDIA_ID",
        "author": "小林",
        "digest": "$DIGEST",
        "show_cover_pic": 1,
        "content_source_url": ""
    }]
}

req = urllib.request.Request(
    'https://api.weixin.qq.com/cgi-bin/draft/add?access_token=$TOKEN',
    data=json.dumps(data, ensure_ascii=False).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)

response = urllib.request.urlopen(req)
result = json.loads(response.read().decode('utf-8'))
print(json.dumps(result, ensure_ascii=False, indent=2))
PYTHON_EOF

echo ""
echo "✅ 发布完成！"
