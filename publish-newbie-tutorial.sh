#!/bin/bash

# 发布 OpenClaw 新手入门教程到公众号草稿箱

APP_ID="wxe5c761b6af8be413"
APP_SECRET="a21104b49ddb844188fc64fd44bb885c"
MARKDOWN_FILE="公众号文章-OpenClaw 新手入门教程.md"
COVER_IMAGE="ai-agent-tech.jpg"

echo "📝 开始发布：OpenClaw 新手入门教程"
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
  -F "description={'title': 'OpenClaw 新手教程', 'introduction': '零基础部署指南'}")

COVER_MEDIA_ID=$(echo "$COVER_RESPONSE" | grep -o '"media_id":"[^"]*"' | cut -d'"' -f4)

if [ -z "$COVER_MEDIA_ID" ]; then
  echo "❌ 上传封面图失败"
  echo "响应：$COVER_RESPONSE"
  exit 1
fi
echo "✓ 封面图上传成功：$COVER_MEDIA_ID"
echo ""

# 3. 准备文章内容
echo "📌 准备文章内容..."

# 提取标题
TITLE="零基础教程 | 30 分钟搭建你的第一个 AI 机器人（Mac 版）"

# 提取摘要
DIGEST="本文从零开始，手把手教你在 Mac 上部署 OpenClaw，接入大模型，创建 QQ/微信机器人。无需服务器，无需编程基础，30 分钟即可完成。"

# 简单转换 Markdown 为 HTML
CONTENT=$(cat "$MARKDOWN_FILE" | \
  sed 's/^# \(.*\)$/<h1 style="font-size: 22px; font-weight: bold; margin: 24px 0 16px; color: #1a1a1a;">\1<\/h1>/g' | \
  sed 's/^## \(.*\)$/<h2 style="font-size: 18px; font-weight: bold; margin: 20px 0 12px; color: #1a1a1a;">\1<\/h2>/g' | \
  sed 's/^### \(.*\)$/<h3 style="font-size: 16px; font-weight: bold; margin: 16px 0 10px; color: #1a1a1a;">\1<\/h3>/g' | \
  sed 's/^> \(.*\)$/<blockquote style="border-left: 4px solid #00b894; padding: 12px 16px; margin: 16px 0; background: #f8f9fa; color: #555;">\1<\/blockquote>/g' | \
  sed 's/\*\*\([^*]*\)\*\*/<strong>\1<\/strong>/g' | \
  sed 's/^[-*] \(.*\)$/<li style="margin: 8px 0; padding-left: 8px;">\1<\/li>/g' | \
  sed 's/^```\(.*\)$/<pre style="background: #2d2d2d; color: #f8f8f2; padding: 16px; border-radius: 6px; overflow-x: auto; margin: 16px 0; font-size: 14px;"><code>/g' | \
  sed 's/^```$/<\/code><\/pre>/g' | \
  sed 's/`\\([^`]*\\)`/<code style="background: #f0f0f0; padding: 2px 6px; border-radius: 3px; font-size: 14px; color: #e96900;">\1<\/code>/g' | \
  sed 's/^|.*|$/<table style="border-collapse: collapse; width: 100%; margin: 16px 0;"><tr><td>\1<\/td><\/tr><\/table>/g' | \
  sed 's/\\n\\n/<\/p><p style="margin: 16px 0; line-height: 1.8; font-size: 16px; color: #333;">/g')

# 包装成完整 HTML
CONTENT="<div style=\"font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; color: #333; max-width: 677px; margin: 0 auto; padding: 20px;\">$CONTENT</div>"

echo "✓ 文章内容准备完成"
echo "  标题：$TITLE"
echo "  摘要：$DIGEST"
echo ""

# 4. 创建草稿
echo "📌 创建草稿..."

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
