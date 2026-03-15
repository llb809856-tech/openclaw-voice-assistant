#!/bin/bash
set -e

echo "🦞 OpenClaw 一键安装（阿里云 Qwen 版）"
echo "======================================"
echo ""

# 检测系统
if [[ "$OSTYPE" == "darwin"* ]]; then
  SYSTEM="macos"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  SYSTEM="linux"
else
  echo "❌ 不支持的系统：$OSTYPE"
  exit 1
fi

echo "📱 检测到系统：$SYSTEM"
echo ""

# 1. 检查并安装 Node.js
echo "🔍 检查 Node.js..."
if ! command -v node &> /dev/null; then
  echo "⚠️  未检测到 Node.js，正在安装..."
  
  if [[ "$SYSTEM" == "macos" ]]; then
    if command -v brew &> /dev/null; then
      echo "📦 使用 Homebrew 安装 Node.js 22..."
      brew install node@22
    else
      echo "❌ 未检测到 Homebrew，请先安装 Homebrew："
      echo "   /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
      exit 1
    fi
  elif [[ "$SYSTEM" == "linux" ]]; then
    echo "📦 安装 Node.js 22..."
    curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
    sudo apt-get install -y nodejs
  fi
  
  echo "✅ Node.js 安装完成"
else
  NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
  if [ "$NODE_VERSION" -lt 22 ]; then
    echo "⚠️  Node.js 版本过低 (v$NODE_VERSION)，需要 v22+"
    echo "   请手动升级：npm install -g n && n 22"
    exit 1
  fi
  echo "✅ Node.js 已安装：$(node -v)"
fi

echo ""

# 2. 检查 npm
if ! command -v npm &> /dev/null; then
  echo "❌ 未检测到 npm，请检查 Node.js 安装"
  exit 1
fi
echo "✅ npm 已安装：$(npm -v)"
echo ""

# 3. 安装 OpenClaw
echo "📦 安装 OpenClaw..."
npm install -g openclaw@latest
echo "✅ OpenClaw 安装完成"
echo ""

# 4. 配置阿里云 Qwen
echo "⚙️  配置阿里云 Qwen..."
mkdir -p ~/.openclaw

cat > ~/.openclaw/openclaw.json << 'EOF'
{
  "models": {
    "mode": "merge",
    "providers": {
      "bailian": {
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "apiKey": "sk-sp-e3d0d03f21954521ba0fb6d6fdb7d817",
        "api": "openai-completions",
        "models": [
          {
            "id": "qwen3.5-plus",
            "name": "Qwen 3.5 Plus",
            "reasoning": false,
            "input": ["text", "image"],
            "cost": {"input": 0, "output": 0},
            "contextWindow": 1000000,
            "maxTokens": 65536
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {"primary": "bailian/qwen3.5-plus"},
      "workspace": "~/.openclaw/workspace",
      "compaction": {"mode": "safeguard"}
    }
  },
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "loopback",
    "auth": {"mode": "token", "token": "openclaw-qwen-2026"}
  }
}
EOF

echo "✅ 配置文件已生成"
echo ""

# 5. 创建工作区
mkdir -p ~/.openclaw/workspace
echo "✅ 工作区已创建"
echo ""

# 6. 完成
echo "======================================"
echo "✅ 安装完成！"
echo ""
echo "🚀 启动命令："
echo "   openclaw gateway"
echo ""
echo "📱 访问地址："
echo "   http://127.0.0.1:18789/"
echo ""
echo "🔑 已配置："
echo "   - 阿里云 Qwen 3.5 Plus"
echo "   - 1,000,000 tokens 上下文"
echo "   - 无需额外配置"
echo ""
echo "======================================"
