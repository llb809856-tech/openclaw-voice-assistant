#!/usr/bin/env python3
"""使用原生 MCP SDK 调用 xiaohongshu-mcp 发布小红书"""

import httpx
import json

MCP_URL = "http://localhost:18060/mcp"

def call_mcp(messages):
    """发送 MCP 请求"""
    with httpx.Client(timeout=300.0) as client:
        response = client.post(
            MCP_URL,
            headers={"Content-Type": "application/json"},
            json=messages if isinstance(messages, list) else [messages]
        )
        result = response.json()
        # 如果是单个消息，返回列表；如果是批量消息，保持原样
        return result if isinstance(result, list) else [result]

def publish_xiaohongshu():
    """发布小红书图文"""
    
    # 1. 初始化会话
    init_result = call_mcp({
        "jsonrpc": "2.0",
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "openclaw", "version": "1.0"}
        },
        "id": 1
    })
    print("✅ MCP 初始化成功:", json.dumps(init_result[0]['result'], indent=2, ensure_ascii=False))
    
    # 2. 获取工具列表
    tools_result = call_mcp([
        {"jsonrpc": "2.0", "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "openclaw", "version": "1.0"}}, "id": 1},
        {"jsonrpc": "2.0", "method": "tools/list", "params": {}, "id": 2}
    ])
    print("\n✅ 可用工具:", len(tools_result[1]['result']['tools']), "个")
    
    # 3. 发布图文
    publish_result = call_mcp([
        {"jsonrpc": "2.0", "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "openclaw", "version": "1.0"}}, "id": 1},
        {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": "publish_content",
                "arguments": {
                    "title": "触屏手套天花板｜小山羊皮女款",
                    "content": "🧤 冬日必备！触屏手套界的天花板来了！\n\n✨ 全球专利全掌触屏技术，戴手套也能丝滑玩手机\n✨ 清水无涂工艺，不伤屏幕更耐用\n✨ 进口小山羊皮，柔软保暖有质感\n✨ 专为都市女性设计，通勤约会都百搭\n\n💰 专柜价 869 元，品质保证\n🎁 7 天无理由退换，放心入手",
                    "images": [
                        "/tmp/图1_触屏手套天花板.jpg",
                        "/tmp/图2_细节展示.jpg",
                        "/tmp/图3_通勤必备.jpg",
                        "/tmp/图4_工艺细节.jpg"
                    ],
                    "tags": ["触屏手套", "冬季必备", "女生手套", "通勤穿搭", "品质生活", "小山羊皮手套", "冬日保暖", "职场女性"],
                    "visibility": "仅自己可见"
                }
            },
            "id": 3
        }
    ])
    
    print("\n📤 发布结果:")
    print(json.dumps(publish_result[1], indent=2, ensure_ascii=False))
    
    if 'error' in publish_result[1]:
        print("\n❌ 发布失败:", publish_result[1]['error']['message'])
        return False
    else:
        print("\n🎉 发布成功！")
        return True

if __name__ == "__main__":
    publish_xiaohongshu()
