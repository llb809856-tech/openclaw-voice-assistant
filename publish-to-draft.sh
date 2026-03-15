#!/bin/bash

# 获取 access_token
TOKEN=$(curl -s "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxe5c761b6af8be413&secret=a21104b49ddb844188fc64fd44bb885c" | grep -o '"access_token":"[^"]*"' | cut -d'"' -f4)

echo "Access Token: ${TOKEN:0:20}..."

# 读取 HTML 文件
HTML_CONTENT=$(cat "/Users/a01/.openclaw/workspace/公众号文章-AI Agent 爆发 - 排版完成版.html" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read()))')

# 上传封面图（用之前的）
echo "上传封面图..."
MEDIA_ID=$(curl -s -F "media=@/Users/a01/.openclaw/workspace/cover-test.png" "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=$TOKEN&type=image" | grep -o '"media_id":"[^"]*"' | cut -d'"' -f4)

if [ -z "$MEDIA_ID" ]; then
  echo "⚠️ 封面图上传失败，使用无封面模式"
  # 无封面发布
  RESULT=$(curl -s -X POST "https://api.weixin.qq.com/cgi-bin/draft/add?access_token=$TOKEN" \
    -H "Content-Type: application/json" \
    -d "{
      \"articles\": [{
        \"title\": \"2026 年，AI Agent 的爆发元年\",
        \"author\": \"智能体 LB\",
        \"content\": \"$HTML_CONTENT\"
      }]
    }")
else
  echo "✓ 封面图上传成功，Media ID: $MEDIA_ID"
  # 有封面发布
  RESULT=$(curl -s -X POST "https://api.weixin.qq.com/cgi-bin/draft/add?access_token=$TOKEN" \
    -H "Content-Type: application/json" \
    -d "{
      \"articles\": [{
        \"title\": \"2026 年，AI Agent 的爆发元年\",
        \"author\": \"智能体 LB\",
        \"content\": \"$HTML_CONTENT\",
        \"thumb_media_id\": \"$MEDIA_ID\",
        \"show_cover_pic\": 1
      }]
    }")
fi

echo "发布结果：$RESULT"

# 检查结果
if echo "$RESULT" | grep -q '"media_id"'; then
  echo "✅ 发布成功！"
  echo "👉 请登录 https://mp.weixin.qq.com 查看草稿箱"
else
  echo "❌ 发布失败"
  echo "$RESULT" | grep -o '"errmsg":"[^"]*"'
fi
