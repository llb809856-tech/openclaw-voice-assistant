#!/bin/bash
# AI Model Daily Report - 每天下午 6 点发布全球 AI 大模型最新版本

cd /Users/a01/.openclaw/workspace

# 生成报告内容
REPORT="🌍 全球 AI 大模型日报
========================
📅 日期：$(date '+%Y-%m-%d %H:%M')

🇺🇸 美国公司
─────────────
"

# OpenAI
INFO=$(openclaw web_search "OpenAI GPT latest model version 2026" --count 1 2>/dev/null | grep -E "^\d|title" | head -1 | sed 's/^[0-9]*\. //')
REPORT+="🔹 OpenAI：${INFO:-暂无更新}
"

# Google
INFO=$(openclaw web_search "Google Gemini latest model version 2026" --count 1 2>/dev/null | grep -E "^\d|title" | head -1 | sed 's/^[0-9]*\. //')
REPORT+="🔹 Google：${INFO:-暂无更新}
"

# Anthropic
INFO=$(openclaw web_search "Anthropic Claude latest model version 2026" --count 1 2>/dev/null | grep -E "^\d|title" | head -1 | sed 's/^[0-9]*\. //')
REPORT+="🔹 Anthropic：${INFO:-暂无更新}
"

# Meta
INFO=$(openclaw web_search "Meta Llama latest model version 2026" --count 1 2>/dev/null | grep -E "^\d|title" | head -1 | sed 's/^[0-9]*\. //')
REPORT+="🔹 Meta：${INFO:-暂无更新}
"

# xAI
INFO=$(openclaw web_search "xAI Grok latest model version 2026" --count 1 2>/dev/null | grep -E "^\d|title" | head -1 | sed 's/^[0-9]*\. //')
REPORT+="🔹 xAI：${INFO:-暂无更新}
"

# Mistral
INFO=$(openclaw web_search "Mistral AI latest model version 2026" --count 1 2>/dev/null | grep -E "^\d|title" | head -1 | sed 's/^[0-9]*\. //')
REPORT+="🔹 Mistral：${INFO:-暂无更新}
"

REPORT+="
🇨🇳 中国公司
─────────────
"

# 字节
INFO=$(openclaw web_search "字节豆包 最新大模型 2026" --count 1 2>/dev/null | grep -E "^\d|title" | head -1 | sed 's/^[0-9]*\. //')
REPORT+="🔹 字节：${INFO:-暂无更新}
"

# 百度
INFO=$(openclaw web_search "百度文心一言 最新模型 2026" --count 1 2>/dev/null | grep -E "^\d|title" | head -1 | sed 's/^[0-9]*\. //')
REPORT+="🔹 百度：${INFO:-暂无更新}
"

# 阿里
INFO=$(openclaw web_search "阿里通义千问 Qwen 最新模型 2026" --count 1 2>/dev/null | grep -E "^\d|title" | head -1 | sed 's/^[0-9]*\. //')
REPORT+="🔹 阿里：${INFO:-暂无更新}
"

# Deepseek
INFO=$(openclaw web_search "Deepseek 最新大模型 2026" --count 1 2>/dev/null | grep -E "^\d|title" | head -1 | sed 's/^[0-9]*\. //')
REPORT+="🔹 Deepseek：${INFO:-暂无更新}
"

# Minimax
INFO=$(openclaw web_search "Minimax 最新大模型 2026" --count 1 2>/dev/null | grep -E "^\d|title" | head -1 | sed 's/^[0-9]*\. //')
REPORT+="🔹 Minimax：${INFO:-暂无更新}
"

# 智谱 AI
INFO=$(openclaw web_search "智谱 AI GLM 最新模型 2026" --count 1 2>/dev/null | grep -E "^\d|title" | head -1 | sed 's/^[0-9]*\. //')
REPORT+="🔹 智谱 AI：${INFO:-暂无更新}
"

# 月之暗面
INFO=$(openclaw web_search "月之暗面 Kimi 最新模型 2026" --count 1 2>/dev/null | grep -E "^\d|title" | head -1 | sed 's/^[0-9]*\. //')
REPORT+="🔹 月之暗面：${INFO:-暂无更新}
"

REPORT+="
─────────────
✨ AI 改变世界，每天进步一点点！"

# 输出报告
echo "$REPORT"

# 发送到飞书群
openclaw message send --channel feishu -t "chat:oc_9867619abcae66edce890a4918408298" -m "$REPORT"
