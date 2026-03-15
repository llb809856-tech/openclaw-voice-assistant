#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrapling 测试脚本
用于测试爬虫功能是否正常工作
"""

from scrapling.fetchers import AsyncFetcher

async def test_scrapling():
    print("🕷️  Scrapling 测试开始...")
    
    # 使用 AsyncFetcher 进行异步爬取
    fetcher = AsyncFetcher()
    
    # 测试抓取一个简单的页面
    response = await fetcher.get("https://httpbin.org/html")
    
    result = {
        "status": response.status,
        "url": response.url,
        "title": response.css("title::text").get(),
        "body_length": len(response.text),
        "success": True
    }
    
    print("✅ 测试结果:", result)
    return result

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_scrapling())
