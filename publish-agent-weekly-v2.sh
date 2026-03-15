#!/bin/bash

# 微信公众号发布脚本（AI Agent 周榜 - 清爽版）
set -e

echo "🚀 微信公众号自动发布（AI Agent 周榜 - 清爽版）"
echo "=============================================="

python3 << 'PYTHON_SCRIPT'
import requests
import json

# 配置
APP_ID = "wxe5c761b6af8be413"
APP_SECRET = "a21104b49ddb844188fc64fd44bb885c"
TITLE = "一周观察：AI Agent 在 X 上爆了，这 5 个趋势值得注意"
AUTHOR = "AI 助理"

# 图片路径 - 只用清晰的配图，不用截图
COVER_IMAGE = "/Users/a01/Desktop/公众号图片/2026-03-06 17.47.21.jpg"  # 封面龙虾图
IMG1 = "/Users/a01/.openclaw/workspace/x-gpt54-tweet1.jpg"  # X 帖子 1
IMG2 = "/Users/a01/.openclaw/workspace/x-gpt54-tweet2.jpg"  # X 帖子 2
IMG3 = "/Users/a01/.openclaw/workspace/x-gpt54-tweet3.jpg"  # X 帖子 3

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
    'img3': IMG3
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
            print(f"✓ {name} URL: {img_url}")

# 生成 HTML - 不用截图，用大字号引用框
cover_media_id = urls['cover']
img1_url = urls['img1']
img2_url = urls['img2']
img3_url = urls['img3']

html = f'''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body>
<section style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', sans-serif; font-size: 17px; line-height: 1.75; color: #333; padding: 10px 20px;">

<h1 style="font-size: 22px; font-weight: 700; color: #1a1a1a; text-align: center; margin: 30px 0 25px; padding-bottom: 15px; border-bottom: 2px solid #00b894;">一周观察：AI Agent 在 X 上爆了<br/>这 5 个趋势值得注意</h1>

<div style="margin: 25px 0; text-align: center;">
<p style="font-size: 14px; color: #888; margin-bottom: 10px;">热门帖子 1</p>
<img src="{img1_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
</div>

<div style="margin: 20px 0; padding: 18px 20px; background: linear-gradient(135deg, #f0fdf7 0%, #e6f7ef 100%); border-left: 4px solid #00b894; border-radius: 8px;">
<p style="margin: 0; font-size: 16px; color: #2d5f4c; font-weight: 500; line-height: 1.6;">2024 年是 prompt 的年份<br/>2025 年是视频的年份<br/>2026 年 3 月，是 AI Agent 的月份</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<div style="background: #f8f9fa; border-radius: 8px; padding: 20px; margin: 25px 0;">
<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 0 0 15px;">📈 过去 7 天热门事件</h2>

<div style="margin: 15px 0; padding: 12px 15px; background: white; border-radius: 6px; border-left: 3px solid #00b894;">
<p style="margin: 0 0 8px; font-weight: 600; color: #1a1a1a;">OpenAI 官方推文</p>
<p style="margin: 0; font-size: 15px; color: #555;">"5.4 sooner than you think"</p>
<p style="margin: 8px 0 0; font-size: 14px; color: #888;">300 万播放 · 2.5 万点赞</p>
</div>

<div style="margin: 15px 0; padding: 12px 15px; background: white; border-radius: 6px; border-left: 3px solid #00b894;">
<p style="margin: 0 0 8px; font-weight: 600; color: #1a1a1a;">Luma Agents 发布</p>
<p style="margin: 0; font-size: 15px; color: #555;">协调多 AI 系统生成文本/图片/视频/音频</p>
<p style="margin: 8px 0 0; font-size: 14px; color: #888;">TechCrunch 头条报道</p>
</div>

<div style="margin: 15px 0; padding: 12px 15px; background: white; border-radius: 6px; border-left: 3px solid #00b894;">
<p style="margin: 0 0 8px; font-weight: 600; color: #1a1a1a;">OpenClaw 爆火</p>
<p style="margin: 0; font-size: 15px; color: #555;">GitHub 星标破 22.8 万</p>
<p style="margin: 8px 0 0; font-size: 14px; color: #888;">最快增长纪录</p>
</div>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<div style="background: #f8f9fa; border-radius: 8px; padding: 20px; margin: 25px 0;">
<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 0 0 20px;">🔥 5 个关键趋势</h2>

<div style="margin: 15px 0;">
<p style="margin: 0 0 8px; font-weight: 600; color: #00b894; font-size: 16px;">01 从聊天到执行</p>
<p style="margin: 0; font-size: 15px; color: #555; line-height: 1.6;">Agent 不再是对话框，是独立工作环境</p>
</div>

<div style="margin: 15px 0;">
<p style="margin: 0 0 8px; font-weight: 600; color: #00b894; font-size: 16px;">02 B 端变现加速</p>
<p style="margin: 0; font-size: 15px; color: #555; line-height: 1.6;">真正的收入在企业自动化，不是 C 端订阅</p>
</div>

<div style="margin: 15px 0;">
<p style="margin: 0 0 8px; font-weight: 600; color: #00b894; font-size: 16px;">03 工具链成熟</p>
<p style="margin: 0; font-size: 15px; color: #555; line-height: 1.6;">MCP 协议、Claude Code、OpenClaw 完善</p>
</div>

<div style="margin: 15px 0;">
<p style="margin: 0 0 8px; font-weight: 600; color: #00b894; font-size: 16px;">04 推理 > 训练</p>
<p style="margin: 0; font-size: 15px; color: #555; line-height: 1.6;">2026 焦点转向毫秒级推理响应</p>
</div>

<div style="margin: 15px 0;">
<p style="margin: 0 0 8px; font-weight: 600; color: #00b894; font-size: 16px;">05 多 Agent 协作</p>
<p style="margin: 0; font-size: 15px; color: #555; line-height: 1.6;">编排才是核心价值</p>
</div>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<div style="background: #fff9e6; border-radius: 8px; padding: 20px; margin: 25px 0; border: 1px dashed #f5a623;">
<h2 style="font-size: 18px; font-weight: 600; color: #f5a623; margin: 0 0 15px;">💡 普通人的机会</h2>
<p style="margin: 10px 0; font-size: 15px; color: #555; line-height: 1.6;">✅ 在 Coze 上打造爆款智能体，用户量破万</p>
<p style="margin: 10px 0; font-size: 15px; color: #555; line-height: 1.6;">✅ 在 GitHub 上开源 AI 项目，拿几百个 Star</p>
<p style="margin: 10px 0; font-size: 15px; color: #555; line-height: 1.6;">✅ 在 ProductHunt 发布 AI 小工具，被推荐到首页</p>
<p style="margin: 15px 0 0; font-size: 15px; color: #f5a623; font-weight: 500;">这些事情，每一件都比任何证书有说服力</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<div style="margin: 25px 0; text-align: center;">
<p style="font-size: 14px; color: #888; margin-bottom: 10px;">热门帖子 2</p>
<img src="{img2_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
</div>

<div style="margin: 25px 0; text-align: center;">
<p style="font-size: 14px; color: #888; margin-bottom: 10px;">热门帖子 3</p>
<img src="{img3_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
</div>

<div style="text-align: center; margin: 30px 0;">
<p style="font-size: 18px; font-weight: 600; color: #00b894; margin: 15px 0;">写在最后</p>
<p style="font-size: 16px; color: #555; margin: 10px 0;">2023-2024 年<br/>LLM 影响 10% 的任务</p>
<p style="font-size: 16px; color: #555; margin: 10px 0;">2026 年<br/>Agent 影响 44% 的任务</p>
<p style="font-size: 16px; color: #555; margin: 10px 0;">CEO 的 AI 暴露度<br/>从 25% 飙升至 60%+</p>
</div>

<div style="text-align: center; margin: 25px 0; padding: 20px; background: #f8f9fa; border-radius: 8px;">
<p style="font-size: 17px; font-weight: 600; color: #1a1a1a; margin: 15px 0;">聊天机器人已成过去<br/>自主执行才是未来</p>
<p style="font-size: 16px; color: #00b894; margin: 15px 0; font-weight: 500;">选择权在你</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<p style="text-align: center; margin: 16px 0; color: #999; font-size: 13px;">数据来源：X (Twitter)、TechCrunch、36 氪、虎嗅、DEV Community</p>

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
    print(f"👉 内图：3 张（X 热门帖子截图，每张 3-4 行）")
    print(f"👉 排版：大字号 + 卡片式布局，无截图")
    print(f"👉 请登录 https://mp.weixin.qq.com 查看草稿箱")
else:
    print("")
    print("❌ 发布失败")
    print(f"错误码：{result.get('errcode')}")
    print(f"错误信息：{result.get('errmsg')}")
    exit(1)
PYTHON_SCRIPT
