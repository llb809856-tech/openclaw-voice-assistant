#!/bin/bash

# 微信公众号发布脚本（X 热门推文速递 - 精简版）
set -e

echo "🚀 微信公众号自动发布（X 热门推文速递 - 精简版）"
echo "=============================================="

python3 << 'PYTHON_SCRIPT'
import requests
import json

# 配置
APP_ID = "wxe5c761b6af8be413"
APP_SECRET = "a21104b49ddb844188fc64fd44bb885c"
TITLE = "X 爆款推文速递 | OpenClaw 火遍全球，小米发布类产品"
AUTHOR = "AI 助理"

# 图片路径 - 精简为 4 张
COVER_IMAGE = "/Users/a01/Desktop/X/jieping_1.png"  # OpenAI GPT-5.4
IMG1 = "/Users/a01/Desktop/X/jieping_1.png"  # OpenAI GPT-5.4
IMG2 = "/Users/a01/Desktop/X/jieping_2.png"  # Luma Agents
IMG3 = "/Users/a01/Desktop/X/jieping_3.png"  # OpenClaw 深圳（代表全球火爆）
IMG4 = "/Users/a01/Desktop/X/jieping_6.png"  # 小米 Miclaw

print("📌 获取 access_token...")
resp = requests.get(f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}")
token_data = resp.json()
if 'access_token' not in token_data:
    print(f"❌ 获取 access_token 失败：{token_data}")
    exit(1)
token = token_data['access_token']
print("✓ access_token 获取成功")

# 上传图片
images = {
    'cover': COVER_IMAGE,
    'img1': IMG1,
    'img2': IMG2,
    'img3': IMG3,
    'img4': IMG4
}

urls = {}
for name, path in images.items():
    print(f"📌 上传图片：{name}...")
    with open(path, 'rb') as f:
        if name == 'cover':
            files = {'media': f}
            resp = requests.post(f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=image", files=files)
            result = resp.json()
            if 'media_id' not in result:
                print(f"❌ {name} 上传失败：{result}")
                exit(1)
            urls[name] = result['media_id']
            print(f"✓ 封面 Media ID: {urls[name]}")
        else:
            files = {'media': f}
            resp = requests.post(f"https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={token}", files=files)
            result = resp.json()
            if 'url' not in result:
                print(f"❌ {name} 上传失败：{result}")
                exit(1)
            img_url = result['url'].replace('http://', 'https://')
            urls[name] = img_url
            print(f"✓ {name} URL: {img_url[:60]}...")

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
<section style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', sans-serif; font-size: 16px; line-height: 1.75; color: #333; padding: 10px 20px;">

<h1 style="font-size: 22px; font-weight: 700; color: #1a1a1a; text-align: center; margin: 30px 0 25px; padding-bottom: 15px; border-bottom: 2px solid #00b894;">X 爆款推文速递<br/>OpenClaw 火遍全球，小米发布类产品</h1>

<div style="margin: 20px 0; padding: 15px 18px; background: #f0fdf7; border-left: 4px solid #00b894; border-radius: 0 6px 6px 0;">
<p style="margin: 0; font-size: 15px; color: #2d5f4c; line-height: 1.6;">3 月 6 日，X 上 AI 圈彻底爆了<br/>OpenAI 发布 GPT-5.4、OpenClaw 线下活动座无虚席<br/>小米发布类 OpenClaw 产品 Miclaw</p>
</div>

<!-- 图 1: OpenAI GPT-5.4 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img1_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
<p style="margin: 10px 0 0; color: #999; font-size: 13px;">OpenAI 官方：GPT-5.4 Thinking 和 Pro 版本发布</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<div style="background: #f8f9fa; border-radius: 8px; padding: 20px; margin: 25px 0;">
<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 0 0 15px;">🔥 OpenAI GPT-5.4 发布</h2>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894;">时间：</strong>3 月 6 日凌晨 2:10
</p>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894;">内容：</strong>GPT-5.4 Thinking 和 GPT-5.4 Pro 在 ChatGPT 中推出，已在 API 和 Codex 中发布
</p>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894;">热度：</strong>520 万浏览量
</p>
</div>

<!-- 图 2: Luma Agents -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img2_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
<p style="margin: 10px 0 0; color: #999; font-size: 13px;">Luma：创意代理，助您高效产出</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<div style="background: #f8f9fa; border-radius: 8px; padding: 20px; margin: 25px 0;">
<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 0 0 15px;">🎬 Luma Agents 创意代理</h2>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894;">时间：</strong>3 月 6 日上午 4:00
</p>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894;">内容：</strong>创意代理，助您高效产出。您设定方向，他们与您携手共建
</p>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894;">热度：</strong>106.1 万次查看
</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #f5a623, transparent); margin: 30px 0;">

<div style="background: #fff9e6; border-radius: 8px; padding: 20px; margin: 25px 0; border: 1px dashed #f5a623;">
<h2 style="font-size: 18px; font-weight: 600; color: #f5a623; margin: 0 0 15px;">🦞 OpenClaw 火遍全球</h2>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #f5a623;">深圳站：</strong>腾讯大厦免费装龙虾活动，现场人山人海
</p>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #f5a623;">纽约站：</strong>Open Claw meetup 座无虚席
</p>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #f5a623;">热度：</strong>深圳 41.4 万浏览，纽约 sold out
</p>
</div>

<!-- 图 3: OpenClaw 深圳 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img3_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
<p style="margin: 10px 0 0; color: #999; font-size: 13px;">深圳线下 OpenClaw 装机画面，大型 AI 时代"地推"名场面</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #0066cc, transparent); margin: 30px 0;">

<div style="background: #f0f7ff; border-radius: 8px; padding: 20px; margin: 25px 0; border: 1px dashed #0066cc;">
<h2 style="font-size: 18px; font-weight: 600; color: #0066cc; margin: 0 0 15px;">📱 小米发布类 OpenClaw 产品</h2>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #0066cc;">产品名称：</strong>Miclaw（基于自家 MiMo 大模型构建）
</p>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #0066cc;">功能：</strong>以系统应用身份运行，可调用应用、生态能力
</p>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #0066cc;">场景：</strong>智能家居控制、晨新闻手机、黄金价格监控
</p>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #0066cc;">未来：</strong>可能运行在小米"人车家全生态"系统
</p>
</div>

<!-- 图 4: 小米 Miclaw -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img4_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
<p style="margin: 10px 0 0; color: #999; font-size: 13px;">小米 Miclaw 产品演示</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<div style="background: #f8f9fa; border-radius: 8px; padding: 20px; margin: 25px 0;">
<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 0 0 15px;">💡 核心观察</h2>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894;">1. 大厂跟进：</strong>OpenAI、Luma、小米纷纷发布 Agent 产品
</p>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894;">2. 线下火爆：</strong>OpenClaw 深圳、纽约活动座无虚席
</p>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894;">3. 生态整合：</strong>小米将 Agent 融入"人车家全生态"
</p>
<p style="margin: 15px 0 0; font-size: 15px; color: #00b894; font-weight: 500;">2026 年 3 月 6 日，AI Agent 正式进入主流视野</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<p style="text-align: center; margin: 16px 0; color: #999; font-size: 13px;">数据来源：X (Twitter) 热门推文</p>

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
    print(f"👉 内图：4 张（精简版）")
    print(f"👉 内容：OpenAI GPT-5.4、Luma Agents、OpenClaw 全球火爆、小米 Miclaw")
    print(f"👉 请登录 https://mp.weixin.qq.com 查看草稿箱")
else:
    print("")
    print("❌ 发布失败")
    print(f"错误码：{result.get('errcode')}")
    print(f"错误信息：{result.get('errmsg')}")
    exit(1)
PYTHON_SCRIPT
