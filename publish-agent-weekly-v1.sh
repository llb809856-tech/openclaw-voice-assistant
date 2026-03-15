#!/bin/bash

# 微信公众号发布脚本（AI Agent X 热门总结）
set -e

echo "🚀 微信公众号自动发布（AI Agent 周榜）"
echo "======================================"

python3 << 'PYTHON_SCRIPT'
import requests
import json

# 配置
APP_ID = "wxe5c761b6af8be413"
APP_SECRET = "a21104b49ddb844188fc64fd44bb885c"
TITLE = "一周观察：AI Agent 在 X 上爆了，这 5 个趋势值得注意"
AUTHOR = "AI 助理"

# 图片路径
COVER_IMAGE = "/Users/a01/Desktop/公众号图片/2026-03-06 17.47.21.jpg"
IMG1 = "/Users/a01/Desktop/公众号图片/2026-03-06 17.47.21.jpg"  # 封面龙虾图
IMG2 = "/Users/a01/Desktop/公众号图片/2026-03-06 17.47.48.jpg"  # OpenClaw 实战
IMG3 = "/Users/a01/Desktop/公众号图片/2026-03-06 17.47.52.jpg"  # 结尾 logo

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

# 生成 HTML
cover_media_id = urls['cover']
img1_url = urls['img1']
img2_url = urls['img2']
img3_url = urls['img3']

html = f'''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body>
<section style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', sans-serif; font-size: 15px; line-height: 1.5; color: #333; padding: 10px 20px;">

<h1 style="font-size: 24px; font-weight: 700; color: #1a1a1a; text-align: center; margin: 30px 0 25px; padding-bottom: 15px; border-bottom: 2px solid #00b894;">一周观察：AI Agent 在 X 上爆了，这 5 个趋势值得注意</h1>

<blockquote style="margin: 20px 0; padding: 15px 18px; background: #f0fdf7; border-left: 4px solid #00b894; border-radius: 0 6px 6px 0; color: #666;">
<p style="margin: 0;">2024 年是 prompt 的年份，2025 年是视频的年份，2026 年 3 月，是 AI Agent 的月份。</p>
</blockquote>

<!-- 开头配图 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img1_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
<p style="margin: 10px 0 0; color: #999; font-size: 13px;">TechCrunch 报道：Luma 发布创意 AI Agents</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 4px; padding-left: 12px; border-left: 4px solid #00b894;">01 过去 7 天，AI Agent 在 X 上刷屏了</h2>

<p style="margin: 4px 0 16px; line-height: 1.5;">过去一周，X（前 Twitter）上最火的话题不是 GPT-5.4，而是<strong style="color: #00b894; font-weight: 600;">AI Agent</strong>。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;">OpenAI 官方发推"5.4 sooner than you think"，300 万播放，2.5 万点赞。但这只是序幕，真正的爆款是 AI Agent 的集中爆发。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;"><strong style="color: #00b894; font-weight: 600;">Luma Agents</strong> 发布，协调多个 AI 系统生成文本、图片、视频、音频，TechCrunch 头条报道。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;"><strong style="color: #00b894; font-weight: 600;">OpenClaw</strong> 几周 GitHub 星标破 22.8 万，创下最快增长纪录，被称为"有很多手的大龙虾"。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;"><strong style="color: #00b894; font-weight: 600;">Claude Code</strong> 成为开发者首选 AI 编程工具，MCP 协议成主流。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 4px; padding-left: 12px; border-left: 4px solid #00b894;">02 5 个关键趋势</h2>

<p style="margin: 4px 0 16px; line-height: 1.5;">从 X 上的热门讨论和科技媒体头条中，我们总结出 5 个关键趋势。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;"><strong style="color: #00b894; font-weight: 600;">趋势 1：从聊天到执行</strong></p>

<p style="margin: 4px 0 16px; line-height: 1.5;">Agent 不再是对话框里的聊天机器人，而是独立的工作环境。能同时调用邮件、文档、社交平台，7×24 小时自主执行任务。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;"><strong style="color: #00b894; font-weight: 600;">趋势 2：B 端变现加速</strong></p>

<p style="margin: 4px 0 16px; line-height: 1.5;">真正的 AI 收入故事不是 C 端订阅，而是企业自动化。自动化对账流程、潜在客户筛选、生成合规文档、减少客服开销——这些不性感但赚钱的场景正在爆发。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;"><strong style="color: #00b894; font-weight: 600;">趋势 3：工具链成熟</strong></p>

<p style="margin: 4px 0 16px; line-height: 1.5;">MCP 协议、Claude Code、OpenClaw 等基础设施完善，开发者可以像搭积木一样构建 Agent 应用。</p>

<!-- 02 节后配图 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img2_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
<p style="margin: 10px 0 0; color: #999; font-size: 13px;">36 氪：2026 年 AI Agent 全面爆发</p>
</div>

<p style="margin: 4px 0 16px; line-height: 1.5;"><strong style="color: #00b894; font-weight: 600;">趋势 4：推理 > 训练</strong></p>

<p style="margin: 4px 0 16px; line-height: 1.5;">2026 年焦点从训练大模型转向毫秒级推理响应。NVIDIA GTC 即将发布的 Feynman 架构，就是专为 Agent AI 设计的推理芯片。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;"><strong style="color: #00b894; font-weight: 600;">趋势 5：多 Agent 协作</strong></p>

<p style="margin: 4px 0 16px; line-height: 1.5;">单一 Agent 退化为孤岛，编排（Orchestration）才是核心价值。协调多个专业 Agent 完成复杂任务，才是企业真正需要的。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 4px; padding-left: 12px; border-left: 4px solid #00b894;">03 国内外的差距在缩小</h2>

<p style="margin: 4px 0 16px; line-height: 1.5;">有意思的是，国内 AI Agent 的发展速度超乎想象。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;">OpenClaw 开源框架几周 GitHub 星标破 10 万 +，用户可通过它实现无人值守的全栈开发。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;">Kimi K2.5 通过智能体框架 + 开源模型联合，在 AI 技术玩家中火了。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;">MiniMax 海外市场收入占比超 70%，C 端用户主要是技术用户。</p>

<!-- 03 节后配图 -->
<div style="margin: 25px 0; text-align: center;">
<img src="{img3_url}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
<p style="margin: 10px 0 0; color: #999; font-size: 13px;">OpenClaw 实战：用 AI Agent 提升效率</p>
</div>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 4px; padding-left: 12px; border-left: 4px solid #00b894;">04 普通人的机会</h2>

<p style="margin: 4px 0 16px; line-height: 1.5;">Agent 爆发，不只是大厂的游戏。普通人也有机会。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;">在 Coze 上打造一个爆款智能体，用户量破万。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;">在 GitHub 上开源一个 AI 项目，拿到几百个 Star。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;">在 ProductHunt 上发布一个 AI 小工具，被社区推荐到首页。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;">这些事情，每一件都比任何证书有说服力。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<h2 style="font-size: 18px; font-weight: 600; color: #00b894; margin: 28px 0 4px; padding-left: 12px; border-left: 4px solid #00b894;">写在最后</h2>

<p style="margin: 4px 0; line-height: 1.5;">2023-2024 年是 LLM 影响 10% 任务的年份。</p>

<p style="margin: 4px 0; line-height: 1.5;">2026 年，Agent 影响 44% 的任务。</p>

<p style="margin: 4px 0; line-height: 1.5;">CEO 的 AI 暴露度从 25% 飙升至 60%+。</p>

<p style="margin: 4px 0; line-height: 1.5;">管理层不再安全，Agent 能自主安排日程、分配预算、追踪进度。</p>

<p style="margin: 4px 0; line-height: 1.5;">聊天机器人已成过去，自主执行才是未来。</p>

<p style="margin: 4px 0 16px; line-height: 1.5;">选择权在你。</p>

<hr style="height: 1px; border: none; background: linear-gradient(90deg, transparent, #00b894, transparent); margin: 30px 0;">

<p style="margin: 16px 0; line-height: 1.5; color: #999; font-size: 14px;">数据来源：X (Twitter)、TechCrunch、36 氪、虎嗅、DEV Community</p>

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
    print(f"👉 内图数量：3 张（TechCrunch 截图 +36 氪截图+OpenClaw 图）")
    print(f"👉 请登录 https://mp.weixin.qq.com 查看草稿箱")
else:
    print("")
    print("❌ 发布失败")
    print(f"错误码：{result.get('errcode')}")
    print(f"错误信息：{result.get('errmsg')}")
    exit(1)
PYTHON_SCRIPT
