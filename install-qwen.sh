#!/bin/bash

# OpenClaw 一键安装脚本（阿里云 Qwen 配置）
# 用法：curl -fsSL https://your-domain.com/install.sh | bash

set -e

echo "🦞 OpenClaw 一键安装（阿里云 Qwen 版）"
echo "========================================"
echo ""

# 1. 检查 Node.js
if ! command -v node &> /dev/null; then
  echo "❌ 未检测到 Node.js，请先安装 Node.js 22+"
  echo "   macOS: brew install node@22"
  echo "   Linux: curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -"
  exit 1
fi

NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 22 ]; then
  echo "❌ Node.js 版本过低（当前 v$NODE_VERSION），需要 v22+"
  exit 1
fi

echo "✅ Node.js 版本检查通过：$(node -v)"
echo ""

# 2. 安装 OpenClaw
echo "📦 安装 OpenClaw..."
npm install -g openclaw@latest
echo "✅ OpenClaw 安装完成"
echo ""

# 3. 配置阿里云 Qwen
echo "⚙️  配置阿里云 Qwen..."
QWEN_API_KEY="sk-sp-e3d0d03f21954521ba0fb6d6fdb7d817"

# 创建配置目录
mkdir -p ~/.openclaw

# 生成配置文件
cat > ~/.openclaw/openclaw.json << EOF
{
  "models": {
    "mode": "merge",
    "providers": {
      "bailian": {
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "apiKey": "$QWEN_API_KEY",
        "api": "openai-completions",
        "models": [
          {
            "id": "qwen3.5-plus",
            "name": "Qwen 3.5 Plus",
            "reasoning": false,
            "input": ["text", "image"],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 1000000,
            "maxTokens": 65536
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "bailian/qwen3.5-plus",
        "fallbacks": []
      },
      "workspace": "$HOME/.openclaw/workspace",
      "compaction": {
        "mode": "safeguard"
      }
    }
  },
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "loopback",
    "auth": {
      "mode": "token",
      "token": "$(openssl rand -hex 20)"
    }
  }
}
EOF

echo "✅ 配置文件已生成：~/.openclaw/openclaw.json"
echo ""

# 4. 创建工作区
echo "📁 创建工作区..."
mkdir -p ~/.openclaw/workspace
echo "✅ 工作区已创建：~/.openclaw/workspace"
echo ""

# 5. 启动 Gateway
echo "🚀 启动 OpenClaw Gateway..."
openclaw gateway --port 18789 &
sleep 3

echo ""
echo "========================================"
echo "✅ 安装完成！"
echo ""
echo "📱 访问控制 UI:"
echo "   http://127.0.0.1:18789/"
echo ""
echo "💬 使用方式:"
echo "   1. 打开浏览器访问上方地址"
echo "   2. 或使用 WhatsApp/Telegram/飞书 等聊天工具连接"
echo ""
echo "🔑 API 配置:"
echo "   - 提供商：阿里云百炼 (Qwen 3.5 Plus)"
echo "   - 上下文：1,000,000 tokens"
echo "   - 已自动配置，无需额外设置"
echo ""
echo "📝 查看日志:"
echo "   openclaw logs --follow"
echo ""
echo "🛑 停止服务:"
echo "   openclaw gateway stop"
echo ""
echo "========================================"
