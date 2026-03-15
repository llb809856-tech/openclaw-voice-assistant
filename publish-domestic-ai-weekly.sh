#!/bin/bash

# 微信公众号发布脚本（国内 AI Agent 热点速递）
set -e

echo "🚀 微信公众号自动发布（国内 AI Agent 热点速递）"
echo "=============================================="

python3 << 'PYTHON_SCRIPT'
import requests
import json

# 配置
APP_ID = "wxe5c761b6af8be413"
APP_SECRET = "a21104b49ddb844188fc64fd44bb885c"
TITLE = "国内 AI Agent 热点速递 | 3 月 4 日 -6 日"
AUTHOR = "AI 助理"

# 图片路径 - 老板提供的截图
COVER_IMAGE = "/Users/a01/.openclaw/workspace/screenshot2.png"
IMG1 = "/Users/a01/.openclaw/workspace/screenshot1.png"
IMG2 = "/Users/a01/.openclaw/workspace/screenshot5.png"
IMG3 = "/Users/a01/.openclaw/workspace/screenshot3.png"
IMG4 = "/Users/a01/.openclaw/workspace/screenshot6.png"
IMG5 = "/Users/a01/.openclaw/workspace/screenshot4.png"

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
    'img4': IMG4,
    'img5': IMG5
}

urls = {}
for name, path in images.items():
    print(f"📌 上传图片：{name}...")
    try:
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
    except FileNotFoundError as e:
        print(f"⚠️ {name} 文件不存在，跳过")
        urls[name] = None

# 生成 HTML
cover_media_id = urls.get('cover', '')
img1_url = urls.get('img1', '')
img2_url = urls.get('img2', '')
img3_url = urls.get('img3', '')
img4_url = urls.get('img4', '')
img5_url = urls.get('img5', '')

html = f'''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body>
<section style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', sans-serif; font-size: 16px; line-height: 1.75; color: #333; padding: 10px 20px;">

<h1 style="font-size: 22px; font-weight: 700; color: #1a1a1a; text-align: center; margin: 30px 0 25px; padding-bottom: 15px; border-bottom: 2px solid #00b894;">国内 AI Agent 热点速递<br/>3 月 4 日 -6 日</h1>

<div style="margin: 20px 0; padding: 15px 18px; background: #f0fdf7; border-left: 4px solid #00b894; border-radius: 0 6px 6px 0;">
<p style="margin: 0; font-size: 15px; color: #2d5f4c; line-height: 1.6;">最近 3 天，国内 AI 厂商动作频频<br/>豆包大模型家族营业、阿里品牌统一<br/>MiniMax 发布 M2.5、Kimi 获 NVIDIA 推荐</p>
</div>

<!-- 封面图 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img1_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<div style="background: #f8f9fa; border-radius: 8px; padding: 20px; margin: 25px 0;">
<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 0 0 20px;">📰 热点一：字节豆包大模型家族</h2>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">时间：</strong>3 月 6 日（7 小时前）
</p>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">事件：</strong>火山引擎发布豆包"大模型家族"正式营业
</p>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">价格：</strong>0.0008 元/千 Tokens（比行业平均便宜 99%）
</p>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">Agent 能力：</strong>基于大模型推出互动娱乐应用"猫箱"、AI 创作工具"即梦"等
</p>
</div>

<!-- 图片 2 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img2_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<div style="background: #f8f9fa; border-radius: 8px; padding: 20px; margin: 25px 0;">
<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 0 0 20px;">📰 热点二：阿里通义千问品牌统一</h2>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">时间：</strong>3 月 5 日（1 天前）
</p>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">事件：</strong>阿里 AI 完成重大品牌统一，整合为"千问"
</p>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">进展：</strong>千问 APP 确立为 C 端旗舰应用，春节期间 AI 帮用户下了 2 亿个单
</p>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">人事：</strong>通义千问技术负责人林俊旸离职，Qwen 团队分拆重组
</p>
</div>

<!-- 图片 3 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img3_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<div style="background: #f8f9fa; border-radius: 8px; padding: 20px; margin: 25px 0;">
<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 0 0 20px;">📰 热点三：MiniMax M2.5 发布</h2>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">时间：</strong>3 月 6 日（1 小时前）
</p>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">发布：</strong>MiniMax 正式发布 M2.5 和 M2.5-Lightning
</p>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">性能：</strong>专为 Agent 和代码设计，价格是 Claude Sonnet 的 8%，速度是 2 倍
</p>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">活动：</strong>15 万美元全栈 AI Agent 挑战赛（3 月 5 日启动）
</p>
</div>

<!-- 图片 4 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img4_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<div style="background: #f8f9fa; border-radius: 8px; padding: 20px; margin: 25px 0;">
<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 0 0 20px;">📰 热点四：Kimi K2.5 获 NVIDIA 推荐</h2>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">时间：</strong>3 月 6 日（12 小时前）
</p>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">事件：</strong>NVIDIA 技术博客推荐 Kimi K2.5 多模态模型
</p>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">能力：</strong>Kimi K2.5 是通用多模态模型，擅长 agentic AI 任务
</p>
<p style="margin: 15px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #00b894; font-weight: 600;">商业化：</strong>通过智能体框架应用跟开源模型联合，在 AI 技术玩家中火了
</p>
</div>

<!-- 图片 5 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img5_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<div style="background: #fff9e6; border-radius: 8px; padding: 20px; margin: 25px 0; border: 1px dashed #f5a623;">
<h2 style="font-size: 18px; font-weight: 600; color: #f5a623; margin: 0 0 15px;">💡 核心趋势总结</h2>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #f5a623;">价格战：</strong>豆包 0.0008 元/千 tokens，MiniMax 是 Claude 的 8%
</p>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #f5a623;">品牌整合：</strong>阿里统一为"千问"，避免多品牌内耗
</p>
<p style="margin: 12px 0; font-size: 15px; color: #555; line-height: 1.7;">
<strong style="color: #f5a623;">Agent 落地：</strong>春节 2 亿单、15 万美元挑战赛，从概念走向实战
</p>
<p style="margin: 12px 0 0; font-size: 15px; color: #f5a623; font-weight: 500;">2026 年，AI Agent 不再是未来时，而是进行时</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<p style="text-align: center; margin: 16px 0; color: #999; font-size: 13px;">数据来源：36 氪、新浪财经、NVIDIA Developer、MiniMax 官网</p>

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
    print(f"👉 内图：5 张（老板提供的热点截图）")
    print(f"👉 内容：国内 AI Agent 3 天热点速递")
    print(f"👉 请登录 https://mp.weixin.qq.com 查看草稿箱")
else:
    print("")
    print("❌ 发布失败")
    print(f"错误码：{result.get('errcode')}")
    print(f"错误信息：{result.get('errmsg')}")
    exit(1)
PYTHON_SCRIPT
