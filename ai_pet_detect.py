#!/usr/bin/env python3
"""
AI 宠物 - 自动人脸识别
功能：定时检测摄像头，发现人脸后对比并识别
"""

import cv2
import time
import os

# 人脸库目录
FACE_DIR = "/Users/a01/.openclaw/workspace/faces"

def load_face_db():
    """加载人脸库"""
    faces = {}
    if os.path.exists(FACE_DIR):
        for f in os.listdir(FACE_DIR):
            if f.endswith('.jpg'):
                name = f.replace('.jpg', '')
                faces[name] = os.path.join(FACE_DIR, f)
                print(f"✅ 加载人脸: {name}")
    return faces

def detect_face(image):
    """检测人脸"""
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 尝试正面
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    if len(faces) > 0:
        return faces[0]
    
    # 尝试侧面
    profiles = profile_cascade.detectMultiScale(gray, 1.1, 3)
    if len(profiles) > 0:
        return profiles[0]
    
    return None

def run_detection():
    """运行检测"""
    print("🤖 AI 宠物 - 人脸识别系统启动")
    print("=" * 40)
    
    # 加载人脸库
    faces = load_face_db()
    if not faces:
        print("❌ 人脸库为空，请先录入人脸")
        return
    
    print(f"📁 已加载 {len(faces)} 个人脸")
    print("👀 等待检测... (按 Ctrl+C 退出)")
    
    cap = cv2.VideoCapture(0)
    last_detection_time = 0
    detection_interval = 5  # 每5秒检测一次
    
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        
        # 每5秒检测一次
        if time.time() - last_detection_time > detection_interval:
            face_rect = detect_face(frame)
            
            if face_rect is not None:
                x, y, w, h = face_rect
                print(f"✅ 检测到人脸! 位置({x},{y}) 大小({w}x{h})")
                
                # 保存检测到的图片
                cv2.imwrite("/Users/a01/.openclaw/workspace/detected.jpg", frame)
                
                # 触发后续识别（可以对接AI）
                print("👉 可以触发关心动作了！")
                print("   例如：说'欢迎回来' / 记录回家时间")
            
            last_detection_time = time.time()
        
        time.sleep(0.5)
    
    cap.release()

if __name__ == "__main__":
    run_detection()
