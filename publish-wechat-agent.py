#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

# 配置
APP_ID = "wxe5c761b6af8be413"
APP_SECRET = "a21104b49ddb844188fc64fd44bb885c"
TITLE = "AI Agent 来了"  # 缩短标题
AUTHOR = "AI 助手"
COVER_IMAGE = "/Users/a01/.openclaw/workspace/ai-agent-tech.jpg"
INLINE_IMAGE = "/Users/a01/.openclaw/workspace/ai-agent-cover.jpg"

print("🚀 微信公众号自动发布（Agent 文章 - Python 版）")
print("=" * 50)

# 1. 获取 access_token
print("📌 获取 access_token...")
token_resp = requests.get(
    f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}"
)
token_data = token_resp.json()
TOKEN = token_data.get("access_token")

if not TOKEN:
    print(f"❌ 获取 access_token 失败：{token_data}")
    exit(1)
print(f"✓ access_token 获取成功")

# 2. 上传封面图（永久素材）
print("📌 上传封面图...")
with open(COVER_IMAGE, 'rb') as f:
    cover_resp = requests.post(
        f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={TOKEN}&type=image",
        files={'media': f},
        data={'description': json.dumps({"title": "AI Agent 封面", "introduction": "AI 改变工作"})}
    )
cover_data = cover_resp.json()
COVER_MEDIA_ID = cover_data.get("media_id")

if not COVER_MEDIA_ID:
    print(f"❌ 封面图上传失败：{cover_data}")
    exit(1)
print(f"✓ 封面图上传成功：{COVER_MEDIA_ID}")

# 3. 上传文章内配图
print("📌 上传文章内配图...")
with open(INLINE_IMAGE, 'rb') as f:
    img_resp = requests.post(
        f"https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={TOKEN}",
        files={'media': f}
    )
img_data = img_resp.json()
print(f"图片上传返回：{img_data}")

if 'url' not in img_data:
    print(f"❌ 文章内配图上传失败：{img_data}")
    exit(1)

# 转换为 HTTPS
IMG_URL = img_data['url'].replace('http://', 'https://')
print(f"✓ 文章内配图上传成功，URL: {IMG_URL}")

# 4. 生成 HTML
print("📌 生成排版 HTML...")

html = f'''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body>
<section style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', sans-serif; font-size: 16px; line-height: 1.75; color: #333; padding: 10px 20px;">

<h1 style="font-size: 24px; font-weight: 700; color: #1a1a1a; text-align: center; margin: 30px 0 25px; padding-bottom: 15px; border-bottom: 2px solid #00b894;">AI Agent 来了</h1>

<blockquote style="margin: 20px 0; padding: 15px 18px; background: #f0fdf7; border-left: 4px solid #00b894; border-radius: 0 6px 6px 0; color: #666;">
<p style="margin: 0;">别慌，被取代的不是人，而是那些不会用 AI 的人。</p>
</blockquote>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 16px; padding-left: 12px; border-left: 4px solid #00b894;">01 什么是 AI Agent？</h2>

<p style="margin: 16px 0; line-height: 1.75;">简单说，AI Agent 就是能<strong style="color: #00b894; font-weight: 600;">自主完成任务</strong>的 AI。</p>

<p style="margin: 16px 0; line-height: 1.75;">以前的 AI，你问它答。现在的 Agent，你给目标，它自己拆解、执行、交付。</p>

<p style="margin: 16px 0; line-height: 1.75;">比如你说"帮我策划一次周末旅行"，Agent 会：</p>

<ul style="margin: 16px 0; padding-left: 20px; line-height: 1.75;">
<li style="margin: 8px 0;">查天气、看攻略、比价格</li>
<li style="margin: 8px 0;">订机票酒店、排行程</li>
<li style="margin: 8px 0;">甚至帮你写请假邮件</li>
</ul>

<p style="margin: 16px 0; line-height: 1.75;">一气呵成，不用你来回切换 App。</p>

<div style="margin: 25px 0; text-align: center;">
<img src="{IMG_URL}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" alt="AI Agent 工作流程"/>
<p style="margin: 10px 0 0; color: #999; font-size: 13px;">AI Agent 自主完成多步骤任务</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 16px; padding-left: 12px; border-left: 4px solid #00b894;">02 哪些工作最危险？</h2>

<p style="margin: 16px 0; line-height: 1.75;">麦肯锡报告说得很直白：</p>

<p style="margin: 16px 0; line-height: 1.75;"><strong style="color: #00b894; font-weight: 600;">重复性、规则明确的工作</strong>，最容易被 Agent 接管。</p>

<p style="margin: 16px 0; line-height: 1.75;">比如：</p>

<ul style="margin: 16px 0; padding-left: 20px; line-height: 1.75;">
<li style="margin: 8px 0;">数据录入、报表生成</li>
<li style="margin: 8px 0;">基础客服问答</li>
<li style="margin: 8px 0;">简单代码编写</li>
<li style="margin: 8px 0;">内容初稿撰写</li>
</ul>

<p style="margin: 16px 0; line-height: 1.75;">但别慌——<strong style="color: #00b894; font-weight: 600;">被取代的不是人，是任务</strong>。</p>

<p style="margin: 16px 0; line-height: 1.75;">你的工作里，可能 80% 是重复劳动，20% 是创造性决策。Agent 拿走那 80%，你专注剩下的 20%。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 16px; padding-left: 12px; border-left: 4px solid #00b894;">03 普通人怎么用 Agent？</h2>

<p style="margin: 16px 0; line-height: 1.75;">三个场景，立刻能用：</p>

<p style="margin: 16px 0; line-height: 1.75;"><strong style="color: #00b894; font-weight: 600;">📝 内容创作</strong></p>

<p style="margin: 16px 0; line-height: 1.75;">写公众号、拍短视频、做海报。给 Agent 一个主题，它出大纲、写初稿、改语气，甚至帮你找配图。</p>

<p style="margin: 16px 0; line-height: 1.75;">我有个朋友，用 Agent 写电商文案，效率翻了 3 倍，转化率还提高了。</p>

<p style="margin: 16px 0; line-height: 1.75;"><strong style="color: #00b894; font-weight: 600;">📊 数据分析</strong></p>

<p style="margin: 16px 0; line-height: 1.75;">丢给它一个 Excel，它自动清洗、分析、画图表、写结论。不用学 Python，不用记函数。</p>

<p style="margin: 16px 0; line-height: 1.75;"><strong style="color: #00b894; font-weight: 600;">💬 客户服务</strong></p>

<p style="margin: 16px 0; line-height: 1.75;">7×24 小时在线，常见问题自动回复，复杂问题转人工。客户不用等，你不用熬夜。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 16px; padding-left: 12px; border-left: 4px solid #00b894;">04 如何不被淘汰？</h2>

<p style="margin: 16px 0; line-height: 1.75;">记住一句话：<strong style="color: #00b894; font-weight: 600;">AI 不会取代你，但会用 AI 的人会</strong>。</p>

<p style="margin: 16px 0; line-height: 1.75;">三个建议：</p>

<p style="margin: 16px 0; line-height: 1.75;"><strong style="color: #00b894; font-weight: 600;">1. 立刻开始用</strong></p>

<p style="margin: 16px 0; line-height: 1.75;">选一个主流 Agent 产品（Claude、ChatGPT、Kimi 都行），每天用它处理一件实际工作。</p>

<p style="margin: 16px 0; line-height: 1.75;"><strong style="color: #00b894; font-weight: 600;">2. 找到你的"杠杆点"</strong></p>

<p style="margin: 16px 0; line-height: 1.75;">哪个环节最耗时？哪个任务最重复？从那里入手。</p>

<p style="margin: 16px 0; line-height: 1.75;"><strong style="color: #00b894; font-weight: 600;">3. 培养"AI 协作力"</strong></p>

<p style="margin: 16px 0; line-height: 1.75;">学会给 AI 下指令、判断输出质量、做最终决策。这是未来最核心的能力。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 16px; padding-left: 12px; border-left: 4px solid #00b894;">写在最后</h2>

<p style="margin: 16px 0; line-height: 1.75;">技术变革从来不是"会不会来"，而是"什么时候来"。</p>

<p style="margin: 16px 0; line-height: 1.75;">AI Agent 的浪潮已经拍上岸了。</p>

<p style="margin: 16px 0; line-height: 1.75;">你可以选择观望，等别人用熟了再学。</p>

<p style="margin: 16px 0; line-height: 1.75;">也可以选择现在就开始，成为那批<strong style="color: #00b894; font-weight: 600;">会用 AI 的人</strong>。</p>

<p style="margin: 16px 0; line-height: 1.75;">选择权在你。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<p style="margin: 16px 0; line-height: 1.75; color: #999; font-size: 14px;">本文参考资料：麦肯锡《2026 AI 应用发展报告》、36 氪《AI Agent 爆发元年》</p>

</section>
</body>
</html>'''

print("✓ HTML 生成成功")

# 保存 HTML 文件
with open('/Users/a01/.openclaw/workspace/article-content-final.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("✓ HTML 已保存到：/Users/a01/.openclaw/workspace/article-content-final.html")

# 5. 发布到草稿箱
print("📌 发布到草稿箱...")
payload = {
    "articles": [{
        "title": TITLE,
        "author": AUTHOR,
        "content": html,
        "thumb_media_id": COVER_MEDIA_ID,
        "show_cover_pic": 1
    }]
}

draft_resp = requests.post(
    f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={TOKEN}",
    json=payload
)
draft_data = draft_resp.json()
print(f"发布结果：{draft_data}")

if 'media_id' in draft_data:
    print("")
    print("✅ 发布成功！")
    print(f"👉 标题：{TITLE}")
    print(f"👉 封面 Media ID: {COVER_MEDIA_ID}")
    print(f"👉 内图 URL: {IMG_URL}")
    print(f"👉 草稿 Media ID: {draft_data['media_id']}")
    print("👉 请登录 https://mp.weixin.qq.com 查看草稿箱")
else:
    print("")
    print("❌ 发布失败")
    print(f"错误码：{draft_data.get('errcode')}")
    print(f"错误信息：{draft_data.get('errmsg')}")
    exit(1)
