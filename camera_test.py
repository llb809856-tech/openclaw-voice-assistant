#!/usr/bin/env python3
"""
AI 宠物 - 摄像头测试脚本
功能：检测画面是否有变化（有人/无人）
"""

import cv2
import time
import os

def test_camera():
    print("📷 摄像头测试")
    print("=" * 40)
    
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ 无法打开摄像头")
        return
    
    print("✅ 摄像头已打开")
    
    # 拍一张照片
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("/Users/a01/workspace/camera_test.jpg", frame)
        print("📸 已保存测试照片: camera_test.jpg")
    else:
        print("❌ 无法读取画面")
    
    cap.release()
    print("✅ 测试完成")

if __name__ == "__main__":
    test_camera()
