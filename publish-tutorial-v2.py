#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib.request
import re

# 配置
APP_ID = "wxe5c761b6af8be413"
APP_SECRET = "a21104b49ddb844188fc64fd44bb885c"
MARKDOWN_FILE = "公众号文章-OpenClaw 新手入门教程.md"
COVER_IMAGE = "ai-agent-tech.jpg"

# 1. 获取 access_token
print("📌 获取 access_token...")
token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}"
with urllib.request.urlopen(token_url) as response:
    token_data = json.loads(response.read().decode('utf-8'))
    TOKEN = token_data.get('access_token')

if not TOKEN:
    print("❌ 获取 access_token 失败")
    exit(1)
print(f"✓ access_token 获取成功\n")

# 2. 上传封面图
print("📌 上传封面图...")
import subprocess
cover_result = subprocess.run(
    ['curl', '-s', '-X', 'POST',
     f'https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={TOKEN}&type=image',
     '-F', f'media=@{COVER_IMAGE}'],
    capture_output=True, text=True
)
cover_data = json.loads(cover_result.stdout)
COVER_MEDIA_ID = cover_data.get('media_id')

if not COVER_MEDIA_ID:
    print(f"❌ 上传封面图失败：{cover_result.stdout}")
    exit(1)
print(f"✓ 封面图上传成功：{COVER_MEDIA_ID}\n")

# 3. 读取 Markdown 并转换
print("📌 转换文章内容...")
with open(MARKDOWN_FILE, 'r', encoding='utf-8') as f:
    markdown = f.read()

# 提取标题和摘要
TITLE = "零基础教程 | 30 分钟搭建你的第一个 AI 机器人（Mac 版）"
DIGEST = "本文从零开始，手把手教你在 Mac 上部署 OpenClaw，接入大模型，创建 QQ/微信机器人。无需服务器，无需编程基础，30 分钟即可完成。"

# Markdown → HTML 转换
def md_to_html(md):
    html = md
    
    # 移除标题行（我们用自己的）
    lines = html.split('\n')
    lines = [l for l in lines if not l.startswith('# 公众号文章')]
    html = '\n'.join(lines)
    
    # H2 标题
    html = re.sub(r'^## (.+)$', r'<section style="margin: 24px 0;"><h2 style="font-size: 18px; font-weight: bold; color: #1a1a1a; border-left: 4px solid #00b894; padding-left: 12px; margin-bottom: 16px;">\1</h2></section>', html, flags=re.MULTILINE)
    
    # H3 标题
    html = re.sub(r'^### (.+)$', r'<h3 style="font-size: 16px; font-weight: bold; color: #333; margin: 16px 0 8px;">\1</h3>', html, flags=re.MULTILINE)
    
    # 引用块
    html = re.sub(r'^> \*\*(.+?)\*\*(.+)$', r'<blockquote style="background: #f8f9fa; border-left: 4px solid #00b894; padding: 12px 16px; margin: 16px 0; color: #555;"><strong>\1</strong>\2</blockquote>', html, flags=re.MULTILINE)
    
    # 粗体
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # 代码块
    def replace_code_block(match):
        code = match.group(1)
        return f'<pre style="background: #2d2d2d; color: #f8f8f2; padding: 16px; border-radius: 6px; overflow-x: auto; margin: 16px 0; font-size: 14px; line-height: 1.6;"><code>{code}</code></pre>'
    html = re.sub(r'```(?:\w+)?\n([\s\S]*?)```', replace_code_block, html)
    
    # 行内代码
    html = re.sub(r'`([^`]+)`', r'<code style="background: #f0f0f0; padding: 2px 6px; border-radius: 3px; font-size: 14px; color: #e96900;">\1</code>', html)
    
    # 列表项
    html = re.sub(r'^[-*] (.+)$', r'<li style="margin: 8px 0; padding-left: 8px;">\1</li>', html, flags=re.MULTILINE)
    
    # 表格
    html = re.sub(r'^\|(.+)\|$', r'<tr>\1</tr>', html, flags=re.MULTILINE)
    
    # 分割线
    html = re.sub(r'^---+$', r'<hr style="border: none; border-top: 2px solid #eee; margin: 24px 0;">', html, flags=re.MULTILINE)
    
    # 段落（按空行分割）
    paragraphs = html.split('\n\n')
    html_parts = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<'):
            # 跳过纯表格行
            if not all(line.strip().startswith('|') or line.strip().startswith('<tr>') for line in p.split('\n') if line.strip()):
                html_parts.append(f'<p style="margin: 16px 0; line-height: 1.8; font-size: 16px; color: #333;">{p}</p>')
            else:
                html_parts.append(p)
        else:
            html_parts.append(p)
    
    html = '\n'.join(html_parts)
    
    # 包装列表
    html = re.sub(r'((<li.*</li>\n?)+)', r'<ul style="padding-left: 20px; margin: 12px 0;">\1</ul>', html)
    
    # 包装表格
    html = re.sub(r'((<tr.*</tr>\n?)+)', r'<table style="border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 15px;">\1</table>', html)
    
    return html

content_html = md_to_html(markdown)

# 完整 HTML 包装
full_content = f'''
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; color: #333; max-width: 677px; margin: 0 auto; padding: 20px;">
{content_html}
</div>
'''

print(f"✓ 文章内容转换完成")
print(f"  标题：{TITLE}")
print(f"  摘要：{DIGEST}")
print(f"  内容长度：{len(full_content)} 字符\n")

# 4. 创建草稿
print("📌 创建草稿...")

data = {
    "articles": [{
        "title": TITLE,
        "content": full_content,
        "thumb_media_id": COVER_MEDIA_ID,
        "author": "小林",
        "digest": DIGEST,
        "show_cover_pic": 1,
        "content_source_url": ""
    }]
}

req = urllib.request.Request(
    f'https://api.weixin.qq.com/cgi-bin/draft/add?access_token={TOKEN}',
    data=json.dumps(data, ensure_ascii=False).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)

response = urllib.request.urlopen(req)
result = json.loads(response.read().decode('utf-8'))

print(json.dumps(result, ensure_ascii=False, indent=2))

if result.get('media_id'):
    print(f"\n✅ 发布成功！")
    print(f"草稿 Media ID: {result['media_id']}")
else:
    print(f"\n❌ 发布失败：{result}")
