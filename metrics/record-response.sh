#!/bin/bash
# 📊 AI 响应时间监控 - 自动记录脚本

LOG_FILE="/Users/a01/.openclaw/workspace/metrics/response-time-log.md"
DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M:%S)

# 参数
QUESTION_TYPE="$1"  # 简单/中等/复杂
THINKING_TIME="$2"  # 思考时间（秒）
TOOL_CALLS="$3"     # 工具调用次数
TOTAL_TIME="$4"     # 总耗时（秒）
RESPONSE_LENGTH="$5" # 回复长度
SUMMARY="$6"        # 问题摘要

# 添加到日志
echo "" >> "$LOG_FILE"
echo "[$DATE $TIME] $SUMMARY" >> "$LOG_FILE"
echo "- 思考时间：${THINKING_TIME}秒" >> "$LOG_FILE"
echo "- 工具调用：${TOOL_CALLS}次" >> "$LOG_FILE"
echo "- 总耗时：${TOTAL_TIME}秒" >> "$LOG_FILE"
echo "- 回复长度：~${RESPONSE_LENGTH}字符" >> "$LOG_FILE"

echo "✅ 已记录：$SUMMARY"
