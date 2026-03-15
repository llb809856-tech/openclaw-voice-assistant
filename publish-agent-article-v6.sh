#!/bin/bash

# 微信公众号发布脚本（Agent 文章 - 多张配图 v6）
set -e

echo "🚀 微信公众号自动发布（Agent 文章 - 多张配图 v6）"
echo "=================================================="

# 全部用 Python 处理
python3 << 'PYTHON_SCRIPT'
import requests
import json

# 配置
APP_ID = "wxe5c761b6af8be413"
APP_SECRET = "a21104b49ddb844188fc64fd44bb885c"
TITLE = "AI Agent 来了"
AUTHOR = "AI 助理"

# 图片路径
COVER_IMAGE = "/Users/a01/Desktop/公众号图片/2026-03-06 17.47.21.jpg"
IMG1 = "/Users/a01/Desktop/公众号图片/2026-03-06 17.47.34.jpg"  # 开头
IMG2 = "/Users/a01/Desktop/公众号图片/2026-03-06 17.47.39.jpg"  # 01 节后
IMG3 = "/Users/a01/Desktop/公众号图片/2026-03-06 17.47.48.jpg"  # 03 节后
IMG4 = "/Users/a01/Desktop/公众号图片/2026-03-06 17.47.52.jpg"  # 结尾

print("📌 获取 access_token...")
resp = requests.get(f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}")
token_data = resp.json()
if 'access_token' not in token_data:
    print(f"❌ 获取 access_token 失败：{token_data}")
    exit(1)
token = token_data['access_token']
print("✓ access_token 获取成功")

# 图片列表
images = {
    'cover': COVER_IMAGE,
    'img1': IMG1,
    'img2': IMG2,
    'img3': IMG3,
    'img4': IMG4
}

# 上传所有图片
urls = {}
for name, path in images.items():
    print(f"📌 上传图片：{name}...")
    with open(path, 'rb') as f:
        if name == 'cover':
            # 封面用永久素材接口
            files = {'media': f}
            resp = requests.post(f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=image", files=files)
            result = resp.json()
            if 'media_id' not in result:
                print(f"❌ {name} 上传失败：{result}")
                exit(1)
            urls[name] = result['media_id']
            print(f"✓ 封面 Media ID: {urls[name]}")
        else:
            # 文章内图用 uploadimg 接口
            files = {'media': f}
            resp = requests.post(f"https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={token}", files=files)
            result = resp.json()
            if 'url' not in result:
                print(f"❌ {name} 上传失败：{result}")
                exit(1)
            img_url = result['url'].replace('http://', 'https://')
            urls[name] = img_url
            print(f"✓ {name} URL: {img_url}")

# 生成 HTML
cover_media_id = urls['cover']
img1_url = urls['img1']
img2_url = urls['img2']
img3_url = urls['img3']
img4_url = urls['img4']

html = f'''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body>
<section style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', sans-serif; font-size: 15px; line-height: 1.5; color: #333; padding: 10px 20px;">

<h1 style="font-size: 24px; font-weight: 700; color: #1a1a1a; text-align: center; margin: 30px 0 25px; padding-bottom: 15px; border-bottom: 2px solid #00b894;">AI Agent 来了，你的工作会被取代吗？</h1>

<blockquote style="margin: 20px 0; padding: 15px 18px; background: #f0fdf7; border-left: 4px solid #00b894; border-radius: 0 6px 6px 0; color: #666;">
<p style="margin: 0;">别慌，被取代的不是人，而是那些不会用 AI 的人。</p>
</blockquote>

<!-- 开头配图 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img1_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 4px; padding-left: 12px; border-left: 4px solid #00b894;">01 什么是 AI Agent？</h2>

<p style="margin: 4px 0 16px; line-height: 1.6;">简单说，AI Agent 就是能<strong style="color: #00b894; font-weight: 600;">自主完成任务</strong>的 AI。</p>

<p style="margin: 16px 0; line-height: 1.6;">以前的 AI，你问它答。现在的 Agent，你给目标，它自己拆解、执行、交付。</p>

<p style="margin: 16px 0; line-height: 1.6;">比如你说"帮我策划一次周末旅行"，Agent 会：</p>

<ul style="margin: 16px 0; padding-left: 0; list-style: none; line-height: 1.6;">
<li style="margin: 8px 0; padding-left: 16px; position: relative;">查天气、看攻略、比价格</li>
<li style="margin: 8px 0; padding-left: 16px; position: relative;">订机票酒店、排行程</li>
<li style="margin: 8px 0; padding-left: 16px; position: relative;">甚至帮你写请假邮件</li>
</ul>

<p style="margin: 16px 0; line-height: 1.6;">一气呵成，不用你来回切换 App。</p>

<!-- 01 节后配图 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img2_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
<p style="margin: 10px 0 0; color: #999; font-size: 13px;">AI Agent 自主完成多步骤任务</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 4px; padding-left: 12px; border-left: 4px solid #00b894;">02 哪些工作最危险？</h2>

<p style="margin: 4px 0 16px; line-height: 1.6;">麦肯锡报告说得很直白：</p>

<p style="margin: 16px 0; line-height: 1.6;"><strong style="color: #00b894; font-weight: 600;">重复性、规则明确的工作</strong>，最容易被 Agent 接管。</p>

<p style="margin: 16px 0; line-height: 1.6;">比如：</p>

<ul style="margin: 16px 0; padding-left: 0; list-style: none; line-height: 1.6;">
<li style="margin: 8px 0; padding-left: 16px; position: relative;">数据录入、报表生成</li>
<li style="margin: 8px 0; padding-left: 16px; position: relative;">基础客服问答</li>
<li style="margin: 8px 0; padding-left: 16px; position: relative;">简单代码编写</li>
<li style="margin: 8px 0; padding-left: 16px; position: relative;">内容初稿撰写</li>
</ul>

<p style="margin: 16px 0; line-height: 1.6;">但别慌——<strong style="color: #00b894; font-weight: 600;">被取代的不是人，是任务</strong>。</p>

<p style="margin: 16px 0; line-height: 1.6;">你的工作里，可能 80% 是重复劳动，20% 是创造性决策。Agent 拿走那 80%，你专注剩下的 20%。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 4px; padding-left: 12px; border-left: 4px solid #00b894;">03 普通人怎么用 Agent？</h2>

<p style="margin: 4px 0 16px; line-height: 1.6;">三个场景，立刻能用：</p>

<p style="margin: 16px 0; line-height: 1.6;"><strong style="color: #00b894; font-weight: 600;">📝 内容创作</strong></p>

<p style="margin: 16px 0; line-height: 1.6;">写公众号、拍短视频、做海报。给 Agent 一个主题，它出大纲、写初稿、改语气，甚至帮你找配图。</p>

<p style="margin: 16px 0; line-height: 1.6;">我有个朋友，用 Agent 写电商文案，效率翻了 3 倍，转化率还提高了。</p>

<p style="margin: 16px 0; line-height: 1.6;"><strong style="color: #00b894; font-weight: 600;">📊 数据分析</strong></p>

<p style="margin: 16px 0; line-height: 1.6;">丢给它一个 Excel，它自动清洗、分析、画图表、写结论。不用学 Python，不用记函数。</p>

<p style="margin: 16px 0; line-height: 1.6;"><strong style="color: #00b894; font-weight: 600;">💬 客户服务</strong></p>

<p style="margin: 16px 0; line-height: 1.6;">7×24 小时在线，常见问题自动回复，复杂问题转人工。客户不用等，你不用熬夜。</p>

<!-- 03 节后配图 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img3_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
<p style="margin: 10px 0 0; color: #999; font-size: 13px;">OpenClaw 实战：用 AI Agent 提升效率</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 4px; padding-left: 12px; border-left: 4px solid #00b894;">04 如何不被淘汰？</h2>

<p style="margin: 4px 0 16px; line-height: 1.6;">记住一句话：<strong style="color: #00b894; font-weight: 600;">AI 不会取代你，但会用 AI 的人会</strong>。</p>

<p style="margin: 16px 0; line-height: 1.6;">三个建议：</p>

<p style="margin: 16px 0; line-height: 1.6;"><strong style="color: #00b894; font-weight: 600;">1. 立刻开始用</strong></p>

<p style="margin: 16px 0; line-height: 1.6;">选一个主流 Agent 产品（Claude、ChatGPT、Kimi 都行），每天用它处理一件实际工作。</p>

<p style="margin: 16px 0; line-height: 1.6;"><strong style="color: #00b894; font-weight: 600;">2. 找到你的"杠杆点"</strong></p>

<p style="margin: 16px 0; line-height: 1.6;">哪个环节最耗时？哪个任务最重复？从那里入手。</p>

<p style="margin: 16px 0; line-height: 1.6;"><strong style="color: #00b894; font-weight: 600;">3. 培养"AI 协作力"</strong></p>

<p style="margin: 16px 0; line-height: 1.6;">学会给 AI 下指令、判断输出质量、做最终决策。这是未来最核心的能力。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 4px; padding-left: 12px; border-left: 4px solid #00b894;">写在最后</h2>

<p style="margin: 4px 0; line-height: 1.6;">技术变革从来不是"会不会来"，而是"什么时候来"。</p>

<p style="margin: 4px 0; line-height: 1.6;">AI Agent 的浪潮已经拍上岸了。</p>

<p style="margin: 4px 0; line-height: 1.6;">你可以选择观望，等别人用熟了再学。</p>

<p style="margin: 4px 0; line-height: 1.6;">也可以选择现在就开始，成为那批<strong style="color: #00b894; font-weight: 600;">会用 AI 的人</strong>。</p>

<p style="margin: 4px 0 16px; line-height: 1.6;">选择权在你。</p>

<!-- 结尾配图 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img4_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<p style="margin: 16px 0; line-height: 1.6; color: #999; font-size: 14px;">本文参考资料：麦肯锡《2026 AI 应用发展报告》、36 氪《AI Agent 爆发元年》</p>

</section>
</body>
</html>'''

print("✓ HTML 生成成功")

# 发布到草稿箱
print("📌 发布到草稿箱...")
draft_data = {
    "articles": [{
        "title": TITLE,
        "author": AUTHOR,
        "content": html,
        "thumb_media_id": cover_media_id,
        "show_cover_pic": 1
    }]
}

# 手动序列化 JSON，确保中文不被转义
json_data = json.dumps(draft_data, ensure_ascii=False).encode('utf-8')
resp = requests.post(
    f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}",
    data=json_data,
    headers={'Content-Type': 'application/json; charset=utf-8'}
)
result = resp.json()
print(f"发布结果：{result}")

if 'media_id' in result:
    print("")
    print("✅ 发布成功！")
    print(f"👉 标题：{TITLE}")
    print(f"👉 封面 Media ID: {cover_media_id}")
    print(f"👉 内图数量：4 张")
    print(f"👉 请登录 https://mp.weixin.qq.com 查看草稿箱")
else:
    print("")
    print("❌ 发布失败")
    print(f"错误码：{result.get('errcode')}")
    print(f"错误信息：{result.get('errmsg')}")
    exit(1)
PYTHON_SCRIPT
