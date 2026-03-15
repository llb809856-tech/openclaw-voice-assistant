#!/usr/bin/env python3
"""
Kling AI 2.6 - 图生视频（base64）
参考图：2 白底反 2.jpg
"""

import requests
import jwt
import time
import base64

ACCESS_KEY = "AKBykrDTC3TeGQrhmKfgFFhdYdrYLdhr"
SECRET_KEY = "fQ3AY83KFJ89peMEaeH4CbHrfCBYNaE4"
BASE_URL = "https://api-beijing.klingai.com"
# 自动找 2 白底反 2.jpg
import os
base = "/Users/a01/Desktop/触心产品营销"
IMAGE_PATH = None
for root, dirs, files in os.walk(base):
    for f in files:
        if f.startswith("2") and "白底反" in f and f.endswith(".jpg"):
            IMAGE_PATH = os.path.join(root, f)
            break
    if IMAGE_PATH:
        break

def gen_jwt():
    t = int(time.time())
    return jwt.encode(
        {"iss": ACCESS_KEY, "exp": t+1800, "nbf": t-5},
        SECRET_KEY,
        algorithm="HS256",
        headers={"alg": "HS256", "typ": "JWT"}
    )

def img2base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def submit(img_b64):
    url = f"{BASE_URL}/v1/videos/omni-video"
    token = gen_jwt()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Kling 2.6 模型 + camera_control
    payload = {
        "model_name": "kling-video-2.6",  # 2.6 专业版
        "prompt": "<<<image_1>>> 专业奢侈品产品摄影，黑色小羊皮手套平铺，纯白色背景，柔和侧光突出皮质纹理，镜头缓慢稳定从左向右横移，电影级质感，高端广告风格，4K 超高清，细节清晰",
        "image_list": [{"image_url": img_b64}],
        "duration": "5",
        "mode": "pro",
        "aspect_ratio": "16:9",
        "camera_control": {
            "type": "simple",
            "config": {
                "pan": -10,  # 从右到左平移
                "zoom": 0,
                "tilt": 0,
                "roll": 0
            }
        },
        "negative_prompt": "deformed, blurry, low quality, distorted, watermark,抖动，不稳定，模糊"
    }
    
    print("提交任务...")
    print(f"模型：kling-video@2.6-pro")
    print(f"图片：{IMAGE_PATH}")
    print(f"base64 长度：{len(img_b64)}")
    
    resp = requests.post(url, json=payload, headers=headers, timeout=60)
    print(f"状态码：{resp.status_code}")
    print(f"响应：{resp.text[:300]}")
    
    if resp.status_code == 200:
        task_id = resp.json().get("data", {}).get("task_id")
        print(f"✅ Task ID: {task_id}")
        return task_id
    return None

def check(task_id):
    url = f"{BASE_URL}/v1/videos/omni-video/{task_id}"
    token = gen_jwt()
    resp = requests.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=30)
    if resp.status_code == 200:
        return resp.json()
    return None

def download(url, path):
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(path, "wb") as f:
            f.write(resp.content)
        print(f"✅ 已下载：{path}")
        return True
    return False

def main():
    print("=" * 60)
    print("Kling AI 2.6 - 图生视频")
    print("参考图：2 白底反 2.jpg")
    print("=" * 60)
    
    # 1. 读图
    print("\n[1/5] 读取图片...")
    img_b64 = img2base64(IMAGE_PATH)
    
    # 2. 提交
    print("\n[2/5] 提交任务...")
    task_id = submit(img_b64)
    if not task_id:
        print("❌ 提交失败")
        return
    
    # 3. 等待
    print("\n[3/5] 等待生成（最多 5 分钟）...")
    video_url = None
    for i in range(30):
        time.sleep(10)
        status = check(task_id)
        if not status:
            continue
        code = status.get("code", -1)
        if code == 0:
            data = status.get("data", {})
            s = data.get("task_status", "")
            print(f"  第{i+1}次：{s}")
            if s == "succeed":
                video_url = data.get("task_result", {}).get("videos", [{}])[0].get("url")
                break
            elif s == "failed":
                print(f"❌ 失败：{data}")
                return
    
    if not video_url:
        print("❌ 超时")
        return
    
    # 4. 下载
    print("\n[4/5] 下载视频...")
    output = "/Users/a01/Desktop/触心产品营销/kling26_镜头 1-2.mp4"
    download(video_url, output)
    
    # 5. 完成
    print("\n[5/5] 完成！")
    print("=" * 60)
    print(f"视频：{output}")
    print("模型：kling-video@2.6-pro")
    print("运镜：camera_control pan=-10（稳定横移）")
    print("=" * 60)

if __name__ == "__main__":
    main()
