#!/usr/bin/env python3
"""
Kling AI API - 图生视频（base64 格式）
镜头 1-2: 产品平铺特写
"""

import requests
import jwt
import time
import base64

ACCESS_KEY = "AKBykrDTC3TeGQrhmKfgFFhdYdrYLdhr"
SECRET_KEY = "fQ3AY83KFJ89peMEaeH4CbHrfCBYNaE4"
BASE_URL = "https://api-beijing.klingai.com"
IMAGE_PATH = "/Users/a01/Desktop/触心产品营销/视频帧/产品视频-03s.jpg"

def generate_jwt_token():
    current_time = int(time.time())
    payload = {"iss": ACCESS_KEY, "exp": current_time + 1800, "nbf": current_time - 5}
    headers = {"alg": "HS256", "typ": "JWT"}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256", headers=headers)

def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def submit_task(img_base64):
    url = f"{BASE_URL}/v1/videos/omni-video"
    token = generate_jwt_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # 纯 base64 字符串，不加前缀
    payload = {
        "model_name": "kling-video-o1",
        "prompt": "<<<image_1>>> 俯视角度，5 双黑色皮手套整齐排列在深灰色桌面上，暖光侧光突出皮质纹理，镜头从左到右缓慢横移，奢侈品产品摄影风格，高画质，4k",
        "image_list": [{"image_url": img_base64}],
        "duration": "5",
        "mode": "pro",
        "aspect_ratio": "16:9"
    }
    
    print("提交任务...")
    print(f"图片 base64 长度：{len(img_base64)}")
    print(f"Prompt: {payload['prompt'][:80]}...")
    
    # 增加超时到 60 秒
    response = requests.post(url, json=payload, headers=headers, timeout=60)
    print(f"状态码：{response.status_code}")
    print(f"响应：{response.text[:300]}")
    
    if response.status_code == 200:
        result = response.json()
        task_id = result.get("data", {}).get("task_id")
        print(f"✅ Task ID: {task_id}")
        return task_id
    else:
        print(f"❌ 失败：{response.status_code}")
        return None

def check_status(task_id):
    url = f"{BASE_URL}/v1/videos/omni-video/{task_id}"
    token = generate_jwt_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, timeout=30)
    if response.status_code == 200:
        return response.json()
    return None

def download(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, "wb") as f:
            f.write(response.content)
        print(f"✅ 已下载：{path}")
        return True
    return False

def main():
    print("=" * 60)
    print("Kling AI - base64 图生视频")
    print("=" * 60)
    
    # 1. 读取图片
    print("\n[1/5] 读取图片...")
    img_base64 = image_to_base64(IMAGE_PATH)
    
    # 2. 提交
    print("\n[2/5] 提交任务...")
    task_id = submit_task(img_base64)
    if not task_id:
        return
    
    # 3. 等待
    print("\n[3/5] 等待生成（最多 5 分钟）...")
    for i in range(30):
        time.sleep(10)
        status = check_status(task_id)
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
    output = "/Users/a01/Desktop/触心产品营销/kling_test_镜头 1-2.mp4"
    download(video_url, output)
    
    # 5. 完成
    print("\n[5/5] 完成！")
    print("=" * 60)
    print(f"视频：{output}")
    print("=" * 60)

if __name__ == "__main__":
    main()
