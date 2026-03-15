#!/usr/bin/env python3
"""
小红书 MCP 测试脚本
测试完整的 MCP 会话流程
"""

import requests
import json

BASE_URL = "http://localhost:18060/mcp"

def test_mcp():
    session = requests.Session()
    
    # Step 1: Initialize
    print("Step 1: Initialize...")
    resp = session.post(BASE_URL, json={
        "jsonrpc": "2.0",
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {}},
            "clientInfo": {"name": "test", "version": "1.0"}
        },
        "id": 1
    })
    print(f"Initialize: {resp.status_code}")
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))
    
    # Step 2: List Tools
    print("\nStep 2: List Tools...")
    resp = session.post(BASE_URL, json={
        "jsonrpc": "2.0",
        "method": "tools/list",
        "params": {},
        "id": 2
    })
    print(f"List Tools: {resp.status_code}")
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))
    
    # Step 3: Call Tool (publish_content)
    print("\nStep 3: Call publish_content...")
    resp = session.post(BASE_URL, json={
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {
            "name": "publish_content",
            "arguments": {
                "title": "晚安🦋",
                "content": "塞浦路斯闪蝶，来自哥伦比亚的国蝶✨",
                "images": ["/Users/a01/Desktop/塞浦路斯闪蝶.jpg"]
            }
        },
        "id": 3
    })
    print(f"Call Tool: {resp.status_code}")
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    test_mcp()
