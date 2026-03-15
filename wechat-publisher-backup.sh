#!/bin/bash

# 微信公众号发布脚本（带完整排版）
# 使用方法：./publish-wechat.sh

set -e

# 配置（支持多账号）
# 默认账号：All-in-One AI
APP_ID="wx9fd7332a73e7e799"
APP_SECRET="3ed0288d0573f75c42c2a68ecffeb9db"
TITLE="早安｜新的一天，从美好开始"
AUTHOR="All-in-One AI"

# 账号 2：触心科技
# APP_ID="wxac6f4d9477e551f4"
# APP_SECRET="3a8df7e6fab8529ac90c5f59ea4aca82"
# AUTHOR="触心科技"

echo "🚀 微信公众号自动发布（带排版）"
echo "================================"

# 1. 获取 access_token
echo "📌 获取 access_token..."
TOKEN=$(curl -s "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=$APP_ID&secret=$APP_SECRET" | grep -o '"access_token":"[^"]*"' | cut -d'"' -f4)

if [ -z "$TOKEN" ]; then
  echo "❌ 获取 access_token 失败"
  exit 1
fi
echo "✓ access_token 获取成功"

# 2. 上传封面图（永久素材）
echo "📌 上传封面图..."
COVER_RESPONSE=$(curl -s -X POST "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=$TOKEN&type=image" \
  -F "media=@/Users/a01/.openclaw/workspace/cover-test.png" \
  -F "description={\"title\":\"封面图\",\"introduction\":\"AI Agent 文章封面\"}")

MEDIA_ID=$(echo "$COVER_RESPONSE" | grep -o '"media_id":"[^"]*"' | cut -d'"' -f4)

if [ -z "$MEDIA_ID" ]; then
  echo "❌ 封面图上传失败"
  echo "$COVER_RESPONSE"
  exit 1
fi
echo "✓ 封面图上传成功：$MEDIA_ID"

# 3. 生成带排版的 HTML
echo "📌 生成排版 HTML..."

# 完整的内联样式 HTML
HTML='<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body>
<section style="font-family: -apple-system, BlinkMacSystemFont, '\''PingFang SC'\'', '\''Microsoft YaHei'\'', sans-serif; font-size: 16px; line-height: 1.75; color: #333; padding: 10px 20px;">

<h1 style="font-size: 24px; font-weight: 700; color: #1a1a1a; text-align: center; margin: 30px 0 25px; padding-bottom: 15px; border-bottom: 2px solid #00b894;">2026 年，AI Agent 的爆发元年</h1>

<blockquote style="margin: 20px 0; padding: 15px 18px; background: #f0fdf7; border-left: 4px solid #00b894; border-radius: 0 6px 6px 0; color: #666;">
<p style="margin: 0;">62% 的企业正在试水 Agent 技术，一场产业重构正在发生。</p>
</blockquote>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 16px; padding-left: 12px; border-left: 4px solid #00b894;">01 爆发元年：从概念到规模化</h2>

<p style="margin: 16px 0; line-height: 1.75;">进入 2026 年，AI Agent（人工智能体）彻底火了。</p>

<p style="margin: 16px 0; line-height: 1.75;">这不是炒作，而是真金白银的投入。</p>

<p style="margin: 16px 0; line-height: 1.75;">麦肯锡最新报告显示，<strong style="color: #00b894; font-weight: 600;">62% 的企业正在试水 Agent 技术</strong>。高通 CEO 预测，AI Agent 超级浪潮将创造万亿美元价值。</p>

<p style="margin: 16px 0; line-height: 1.75;">36 氪在深度分析中指出，2026 年或成 AI 代理爆发元年。</p>

<p style="margin: 16px 0; line-height: 1.75;">曾经的 AI 助手，如今正在演变成能自主完成任务的智能体。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 16px; padding-left: 12px; border-left: 4px solid #00b894;">02 三大顶流产品</h2>

<p style="margin: 16px 0; line-height: 1.75;">从最顶级的 30 个 AI Agent 产品里，我们看到了三个关键趋势。</p>

<p style="margin: 16px 0; line-height: 1.75;"><strong style="color: #00b894; font-weight: 600;">Claude Code：代码界的自动驾驶</strong></p>

<p style="margin: 16px 0; line-height: 1.75;">Anthropic 推出的 Claude Code，正在重新定义软件开发。</p>

<p style="margin: 16px 0; line-height: 1.75;">它能自主理解需求、拆解任务、编写代码、调试修复。开发者从写代码变成审代码，效率提升 5 到 10 倍。</p>

<p style="margin: 16px 0; line-height: 1.75;"><strong style="color: #00b894; font-weight: 600;">ChatGPT Agent：OpenAI 的全能选手</strong></p>

<p style="margin: 16px 0; line-height: 1.75;">OpenAI 的 Agent 产品，正在打通工作流闭环。</p>

<p style="margin: 16px 0; line-height: 1.75;">跨应用操作邮件、日历、文档、数据，多步骤任务自主执行，企业级工作流平台集成。</p>

<p style="margin: 16px 0; line-height: 1.75;"><strong style="color: #00b894; font-weight: 600;">Manus：现象级独立 Agent</strong></p>

<p style="margin: 16px 0; line-height: 1.75;">Manus 的崛起，证明了独立 Agent 的爆发力。</p>

<p style="margin: 16px 0; line-height: 1.75;">GitHub 星标破 10 万加，无人值守全栈开发，成为开源社区现象级工具。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 16px; padding-left: 12px; border-left: 4px solid #00b894;">03 产业重构：AI 从工具变成参与者</h2>

<p style="margin: 16px 0; line-height: 1.75;">2026 年，AI 正在经历一场关键的相变。</p>

<p style="margin: 16px 0; line-height: 1.75;">过去，AI 是屏幕后的工具。现在，AI 是渗透现实的参与者。</p>

<p style="margin: 16px 0; line-height: 1.75;">过去，AI 加修修补补。现在，AI 原生重构系统底层。</p>

<p style="margin: 16px 0; line-height: 1.75;">过去，AI 局限于数字世界。现在，AI 延伸到物理世界，具身智能正在兴起。</p>

<p style="margin: 16px 0; line-height: 1.75;">这意味着什么？</p>

<p style="margin: 16px 0; line-height: 1.75;">企业运营效率将被重新定义，个人生产力边界被大幅拓展，新的职业机会和商业模式涌现。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 16px; padding-left: 12px; border-left: 4px solid #00b894;">04 普通人的机会</h2>

<p style="margin: 16px 0; line-height: 1.75;">Agent 爆发，不只是大厂的游戏。普通人也有机会。</p>

<p style="margin: 16px 0; line-height: 1.75;"><strong style="color: #00b894; font-weight: 600;">用 Agent 提升个人生产力</strong></p>

<p style="margin: 16px 0; line-height: 1.75;">内容创作，文案、脚本、设计一键生成。数据分析，自动报表、洞察提取。客户服务，7 乘 24 小时智能应答。</p>

<p style="margin: 16px 0; line-height: 1.75;"><strong style="color: #00b894; font-weight: 600;">成为 Agent 应用开发者</strong></p>

<p style="margin: 16px 0; line-height: 1.75;">低代码平台让开发门槛大幅降低。垂直场景 Agent 需求爆发，电商、教育、医疗。早入场等于早占位。</p>

<p style="margin: 16px 0; line-height: 1.75;"><strong style="color: #00b894; font-weight: 600;">提供 Agent 相关服务</strong></p>

<p style="margin: 16px 0; line-height: 1.75;">Agent 培训与咨询，工作流设计与优化，提示词工程与调优。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 16px; padding-left: 12px; border-left: 4px solid #00b894;">05 行动建议</h2>

<p style="margin: 16px 0; line-height: 1.75;">如果你想在 2026 年抓住 Agent 红利。</p>

<p style="margin: 16px 0; line-height: 1.75;">立即体验，选 1 到 2 个主流 Agent 产品深度使用。</p>

<p style="margin: 16px 0; line-height: 1.75;">找到场景，在你的工作或业务中找到可自动化的环节。</p>

<p style="margin: 16px 0; line-height: 1.75;">持续学习，关注 Agent 技术演进和最佳实践。</p>

<p style="margin: 16px 0; line-height: 1.75;">快速试错，小步快跑，验证可行后快速放大。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 16px; padding-left: 12px; border-left: 4px solid #00b894;">写在最后</h2>

<p style="margin: 16px 0; line-height: 1.75;">2026 年，AI Agent 不再是未来时，而是进行时。</p>

<p style="margin: 16px 0; line-height: 1.75;">最大的风险不是尝试后失败，而是观望中错过。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<p style="margin: 16px 0; line-height: 1.75;">本文数据来源，麦肯锡 2026 AI 应用发展核心报告、36 氪、新浪财经。</p>

</section>
</body>
</html>'

echo "✓ HTML 生成成功"

# 4. 发布到草稿箱
echo "📌 发布到草稿箱..."
RESULT=$(curl -s -X POST "https://api.weixin.qq.com/cgi-bin/draft/add?access_token=$TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"articles\": [{
      \"title\": \"$TITLE\",
      \"author\": \"$AUTHOR\",
      \"content\": $(echo "$HTML" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read(), ensure_ascii=False))'),
      \"thumb_media_id\": \"$MEDIA_ID\",
      \"show_cover_pic\": 1
    }]
  }")

echo "发布结果：$RESULT"

# 检查结果
if echo "$RESULT" | grep -q '"media_id"'; then
  echo ""
  echo "✅ 发布成功！"
  echo "👉 请登录 https://mp.weixin.qq.com 查看草稿箱"
  echo "👉 在草稿箱预览无误后，点击'群发'按钮推送给粉丝"
else
  echo ""
  echo "❌ 发布失败"
  echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'错误码：{d.get(\"errcode\")}'); print(f'错误信息：{d.get(\"errmsg\")}')"
  exit 1
fi
