#!/bin/bash
# 屏幕截图脚本 - 使用 peekaboo 截取当前屏幕

# 生成带时间戳的文件名
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUTPUT_DIR="$HOME/.openclaw/workspace/产品图片"
OUTPUT_PATH="$OUTPUT_DIR/screenshot_$TIMESTAMP.png"

# 确保目录存在
mkdir -p "$OUTPUT_DIR"

# 截取主屏幕（retina 分辨率）
peekaboo image --mode screen --retina --path "$OUTPUT_PATH"

if [ $? -eq 0 ]; then
    echo "截图已保存：$OUTPUT_PATH"
    # 输出飞书可用的路径格式
    echo "MEDIA:$OUTPUT_PATH"
else
    echo "截图失败"
    exit 1
fi
