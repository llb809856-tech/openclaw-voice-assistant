#!/bin/bash
set -e
echo "🦞 OpenClaw 一键安装（阿里云 Qwen）"
node -v 2>/dev/null || { echo "❌ 请先安装 Node.js 22+"; exit 1; }
npm install -g openclaw@latest
mkdir -p ~/.openclaw
cat > ~/.openclaw/openclaw.json << 'EOF'
{"models":{"mode":"merge","providers":{"bailian":{"baseUrl":"https://coding.dashscope.aliyuncs.com/v1","apiKey":"sk-sp-e3d0d03f21954521ba0fb6d6fdb7d817","api":"openai-completions","models":[{"id":"qwen3.5-plus","name":"Qwen 3.5 Plus","reasoning":false,"input":["text","image"],"cost":{"input":0,"output":0},"contextWindow":1000000,"maxTokens":65536}]}}},"agents":{"defaults":{"model":{"primary":"bailian/qwen3.5-plus"},"workspace":"~/.openclaw/workspace","compaction":{"mode":"safeguard"}}},"gateway":{"port":18789,"mode":"local","bind":"loopback","auth":{"mode":"token","token":"openclaw-qwen-2026"}}}
EOF
mkdir -p ~/.openclaw/workspace
echo "✅ 安装完成！运行：openclaw gateway"
