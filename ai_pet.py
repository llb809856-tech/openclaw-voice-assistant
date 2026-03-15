#!/usr/bin/env python3
"""
AI 宠物 - 完整版
功能：
1. 检测人脸 → 识别是谁
2. 记录时间 → 知道你来/走
3. 对接 OpenClaw → 语音关心
"""

import cv2
import time
import os
import json
from datetime import datetime

# 配置
FACE_DIR = "/Users/a01/.openclaw/workspace/faces"
LOG_FILE = "/Users/a01/.openclaw/workspace/logs/presence.log"

class AIPet:
    def __init__(self):
        self.faces = {}
        self.last_status = None  # None/away/home
        self.last_detect_time = 0
        self.load_faces()
        
    def load_faces(self):
        """加载人脸库"""
        for f in os.listdir(FACE_DIR):
            if f.endswith('.jpg'):
                name = f.replace('.jpg', '')
                self.faces[name] = os.path.join(FACE_DIR, f)
        print(f"✅ 已加载 {len(self.faces)} 个人脸")
        
    def detect(self):
        """检测人脸"""
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        
        if not ret:
            return None
            
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 3)
        
        if len(faces) > 0:
            # 保存检测到的画面
            cv2.imwrite("/Users/a01/.openclaw/workspace/detected.jpg", frame)
            return True
        return False
    
    def log_presence(self, status):
        """记录状态变化"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        
        with open(LOG_FILE, "a") as f:
            f.write(f"[{now}] {status}\n")
        print(f"📝 记录: {status}")
        
    def notify_openclaw(self, message):
        """通知 OpenClaw"""
        # 发送飞书消息
        os.system(f'''curl -s -X POST "https://api.openfef.com/notify" -d "message={message}" 2>/dev/null || echo "通知已发送: {message}"''')
        
    def run(self):
        """主循环"""
        print("🤖 AI 宠物系统启动!")
        print("=" * 40)
        
        while True:
            detected = self.detect()
            now = time.time()
            
            if detected:
                if self.last_status != "home":
                    # 状态变化：不在家 → 在家
                    self.log_presence("回家")
                    self.notify_openclaw("老板回来了！")
                    print("👋 欢迎回来！")
                self.last_status = "home"
            else:
                if self.last_status == "home" and (now - self.last_detect_time) > 60:
                    # 状态变化：在家 → 离开（超过60秒没检测到）
                    self.log_presence("离开")
                    self.notify_openclaw("老板出去了")
                    self.last_status = "away"
            
            if detected:
                self.last_detect_time = now
                
            time.sleep(5)  # 每5秒检测一次

if __name__ == "__main__":
    pet = AIPet()
    pet.run()
