#!/usr/bin/env python3
"""
Kling AI o1 - 图生视频（多图参考）
参考图：主图 800-800 文件夹里的白底图
"""

import requests
import jwt
import time
import base64
import os

ACCESS_KEY = "AKBykrDTC3TeGQrhmKfgFFhdYdrYLdhr"
SECRET_KEY = "fQ3AY83KFJ89peMEaeH4CbHrfCBYNaE4"
BASE_URL = "https://api-beijing.klingai.com"

# 自动查找参考图
def find_images():
    base = "/Users/a01/Desktop/触心产品营销"
    paths = []
    for root, dirs, files in os.walk(base):
        for f in sorted(files):
            if f.startswith(("1", "2", "3")) and "白底" in f and f.endswith(".jpg"):
                paths.append(os.path.join(root, f))
                if len(paths) >= 3:
                    return paths
    return paths

IMAGE_PATHS = find_images()

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

def submit(img_list_b64):
    url = f"{BASE_URL}/v1/videos/omni-video"
    token = gen_jwt()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # 多图参考的 prompt 格式
    prompt = """<<<image_1>>><<<image_2>>><<<image_3>>> 专业奢侈品手套产品摄影，黑色小羊皮手套多角度展示，纯白背景，柔和侧光突出皮质纹理和缝线细节，镜头缓慢稳定环绕展示，电影级质感，高端广告风格，4K 超高清，细节清晰，轻奢品质"""
    
    # 构建 image_list
    image_list = [{"image_url": b64} for b64 in img_list_b64]
    
    payload = {
        "model_name": "kling-video-o1",
        "prompt": prompt,
        "image_list": image_list,
        "duration": "5",
        "mode": "pro",
        "aspect_ratio": "16:9",
        "camera_control": {
            "type": "simple",
            "config": {
                "pan": 0,
                "zoom": 5,  # 缓慢放大
                "tilt": 0,
                "roll": 0
            }
        },
        "negative_prompt": "deformed, blurry, low quality, distorted, watermark, 抖动，不稳定，模糊，淘宝风，廉价感"
    }
    
    print("提交任务...")
    print(f"模型：kling-video-o1")
    print(f"参考图数量：{len(img_list_b64)}")
    for i, path in enumerate(IMAGE_PATHS[:len(img_list_b64)], 1):
        print(f"  图{i}: {os.path.basename(path)}")
    print(f"Prompt: {prompt[:80]}...")
    
    resp = requests.post(url, json=payload, headers=headers, timeout=90)
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
    print("Kling AI o1 - 多图参考视频生成")
    print("=" * 60)
    
    # 1. 读取图片
    print("\n[1/5] 读取参考图...")
    img_b64_list = []
    for path in IMAGE_PATHS:
        if os.path.exists(path):
            b64 = img2base64(path)
            img_b64_list.append(b64)
            print(f"  ✅ {os.path.basename(path)} ({len(b64)} bytes)")
        else:
            print(f"  ❌ 文件不存在：{path}")
    
    if not img_b64_list:
        print("❌ 没有可用的图片")
        return
    
    # 2. 提交
    print("\n[2/5] 提交任务...")
    task_id = submit(img_b64_list)
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
    output = "/Users/a01/Desktop/触心产品营销/kling_o1_多图参考.mp4"
    download(video_url, output)
    
    # 5. 完成
    print("\n[5/5] 完成！")
    print("=" * 60)
    print(f"视频：{output}")
    print("模型：kling-video-o1")
    print("参考图：3 张白底图")
    print("运镜：缓慢放大 (zoom=5)")
    print("=" * 60)

if __name__ == "__main__":
    main()
