#!/usr/bin/env python3
"""
Kling AI API - 图生视频（Image-to-Video）
镜头 1-2: 产品平铺特写
参考图：产品视频 -03s.jpg（手套平铺）
"""

import requests
import jwt
import time
import base64
import json

ACCESS_KEY = "AKBykrDTC3TeGQrhmKfgFFhdYdrYLdhr"
SECRET_KEY = "fQ3AY83KFJ89peMEaeH4CbHrfCBYNaE4"
BASE_URL = "https://api-beijing.klingai.com"

# 参考图路径
IMAGE_PATH = "/Users/a01/Desktop/触心产品营销/视频帧/产品视频-03s.jpg"

def generate_jwt_token():
    current_time = int(time.time())
    payload = {
        "iss": ACCESS_KEY,
        "exp": current_time + 1800,
        "nbf": current_time - 5
    }
    headers = {"alg": "HS256", "typ": "JWT"}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256", headers=headers)

def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def submit_video_task(image_path):
    url = f"{BASE_URL}/v1/videos/omni-video"
    token = generate_jwt_token()
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # 先用图片 URL 方式（更稳定）
    # 注意：需要图片有公开可访问的 URL
    # 这里我们用本地路径，Kling 可能不支持，先测试
    payload = {
        "model_name": "kling-video-o1",
        "prompt": "<<<image_1>>> 俯视角度，5 双黑色皮手套整齐排列在深灰色桌面上，暖光侧光突出皮质纹理，镜头从左到右缓慢横移，奢侈品产品摄影风格，高画质，4k",
        "image_list": [
            {
                "image_url": image_path
            }
        ],
        "duration": "5",
        "mode": "pro",
        "aspect_ratio": "16:9"
    }
    
    print("提交图生视频任务...")
    print(f"参考图：{image_path}")
    print(f"Prompt: {payload['prompt'][:100]}...")
    print("-" * 60)
    
    response = requests.post(url, json=payload, headers=headers, timeout=30)
    print(f"状态码：{response.status_code}")
    print(f"响应：{response.text[:500]}")
    
    if response.status_code == 200:
        result = response.json()
        task_id = result.get("data", {}).get("task_id")
        print(f"✅ Task ID: {task_id}")
        return task_id
    else:
        print(f"❌ 提交失败：{response.status_code}")
        return None

def check_status(task_id):
    url = f"{BASE_URL}/v1/videos/omni-video/{task_id}"
    token = generate_jwt_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers, timeout=30)
    if response.status_code == 200:
        return response.json()
    return None

def download_video(video_url, output_path):
    print(f"下载视频中...")
    response = requests.get(video_url)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ 视频已下载：{output_path}")
        return True
    return False

def main():
    print("=" * 60)
    print("Kling AI - 图生视频测试")
    print("镜头 1-2: 产品平铺特写")
    print("=" * 60)
    
    # 步骤 1: 准备参考图
    print("\n[1/5] 准备参考图...")
    print(f"参考图：{IMAGE_PATH}")
    
    # 步骤 2: 提交任务
    print("\n[2/5] 提交视频生成任务...")
    task_id = submit_video_task(IMAGE_PATH)
    if not task_id:
        print("\n❌ 提交失败")
        return
    
    # 步骤 3: 等待生成
    print("\n[3/5] 等待视频生成（约 3-5 分钟）...")
    max_attempts = 30
    video_url = None
    
    for i in range(max_attempts):
        time.sleep(10)
        status = check_status(task_id)
        
        if not status:
            continue
        
        code = status.get("code", -1)
        if code == 0:
            data = status.get("data", {})
            task_status = data.get("task_status", "")
            print(f"  第 {i+1} 次查询：状态 = {task_status}")
            
            if task_status == "succeed":
                video_url = data.get("task_result", {}).get("videos", [{}])[0].get("url")
                break
            elif task_status == "failed":
                print(f"❌ 任务失败：{data}")
                return
        else:
            print(f"  第 {i+1} 次查询：错误码 = {code}")
    
    if not video_url:
        print("❌ 超时，视频未生成完成")
        return
    
    print("✅ 视频生成成功")
    
    # 步骤 4: 下载视频
    print("\n[4/5] 下载视频...")
    output_path = "/Users/a01/Desktop/触心产品营销/kling_test_镜头 1-2.mp4"
    download_video(video_url, output_path)
    
    # 步骤 5: 完成
    print("\n[5/5] 完成！")
    print("=" * 60)
    print(f"视频位置：{output_path}")
    print("请老板检查效果！")
    print("=" * 60)

if __name__ == "__main__":
    main()
