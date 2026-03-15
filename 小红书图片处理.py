#!/usr/bin/env python3
"""
小红书手套产品图批量处理脚本
功能：裁剪 3:4 比例 + 添加文字 + 统一调色
"""

from PIL import Image, ImageDraw, ImageFont
import os

# 配置
INPUT_DIR = "/Users/a01/Desktop/产品图片"
OUTPUT_DIR = "/Users/a01/Desktop/产品图片/小红书优化版"
TARGET_SIZE = (1242, 1660)  # 小红书 3:4 比例

# 创建输出目录
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 要处理的图片列表（按顺序）
images = [
    {"file": "2026-02-27 19.43.22.jpg", "text": "触屏手套天花板", "subtext": "专柜价 ¥869"},
    {"file": "img_v3_02vc_34dcbadb-4ba0-4117-b9e4-f6438fc4001g.jpg", "text": "细节展示", "subtext": "进口小山羊皮"},
    {"file": "img_v3_02vc_40085a43-f68f-4706-9521-d097b00e6fdg.jpg", "text": "通勤必备", "subtext": "丝滑触控体验"},
    {"file": "img_v3_02vc_58e1530e-c091-47d3-9b6b-c8495c76f2eg.jpg", "text": "工艺细节", "subtext": "全掌触屏技术"},
]

def process_image(img_path, output_path, title, subtitle):
    """处理单张图片"""
    img = Image.open(img_path)
    
    # 转换为 RGB（处理 PNG 透明背景）
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    # 计算裁剪区域（中心裁剪为 3:4）
    width, height = img.size
    target_ratio = TARGET_SIZE[0] / TARGET_SIZE[1]
    current_ratio = width / height
    
    if current_ratio > target_ratio:
        # 图片太宽，裁剪左右
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        img = img.crop((left, 0, left + new_width, height))
    else:
        # 图片太高，裁剪上下
        new_height = int(width / target_ratio)
        top = (height - new_height) // 2
        img = img.crop((0, top, width, top + new_height))
    
    # 缩放到目标尺寸
    img = img.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
    
    # 添加文字
    draw = ImageDraw.Draw(img)
    
    # 尝试加载字体（使用系统字体）
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 48)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 32)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # 添加标题（顶部）
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (TARGET_SIZE[0] - title_width) // 2
    draw.text((title_x, 40), title, fill="white", font=title_font, stroke_width=2, stroke_fill="black")
    
    # 添加副标题（底部）
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (TARGET_SIZE[0] - subtitle_width) // 2
    draw.text((subtitle_x, TARGET_SIZE[1] - 80), subtitle, fill="white", font=subtitle_font, stroke_width=2, stroke_fill="black")
    
    # 保存
    img.save(output_path, quality=95)
    print(f"✅ 处理完成：{output_path}")

# 批量处理
print("🎨 开始处理图片...")
for i, img_info in enumerate(images, 1):
    input_path = os.path.join(INPUT_DIR, img_info["file"])
    output_path = os.path.join(OUTPUT_DIR, f"图{i}_{img_info['text']}.jpg")
    
    if os.path.exists(input_path):
        process_image(input_path, output_path, img_info["text"], img_info["subtext"])
    else:
        print(f"❌ 文件不存在：{input_path}")

print(f"\n✨ 全部完成！输出目录：{OUTPUT_DIR}")
