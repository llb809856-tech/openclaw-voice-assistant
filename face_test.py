#!/usr/bin/env python3
"""
AI 宠物 - 人脸识别（使用 macOS Vision 框架）
"""

import cv2
import os
from Foundation import NSUUID
import Vision

def capture_and_detect():
    print("📷 拍照并检测人脸...")
    
    # 打开摄像头
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ 无法打开摄像头")
        return
    
    # 拍照
    ret, frame = cap.read()
    if not ret:
        print("❌ 无法读取画面")
        cap.release()
        return
    
    # 保存图片
    image_path = "/Users/a01/workspace/face_capture.jpg"
    cv2.imwrite(image_path, frame)
    cap.release()
    
    print(f"📸 已保存: {image_path}")
    
    # 使用 Vision 框架检测人脸
    from Cocoa import NSImage, NSRect
    from Vision import VNDetectFaceRectanglesRequest, VNImageRequestHandler
    
    # 加载图片
    img = NSImage.alloc().initWithContentsOfFile_(image_path)
    
    # 创建人脸检测请求
    request = VNDetectFaceRectanglesRequest.alloc().init()
    
    # 执行检测
    handler = VNImageRequestHandler.alloc().initWithData_(img.tiffRepresentation(), {})
    results = handler.performRequests_error_([request], None)
    
    if results and len(results) > 0:
        face_count = len(results)
        print(f"✅ 检测到 {face_count} 张人脸")
        
        # 获取第一张人脸的位置
        first_face = results[0]
        bbox = first_face.boundingBox()
        print(f"📍 人脸位置: x={bbox.origin.x:.2f}, y={bbox.origin.y:.2f}, w={bbox.size.width:.2f}, h={bbox.size.height:.2f}")
    else:
        print("❌ 未检测到人脸")
    
    print("\n👀 请在摄像头前摆好姿势，我来录入你的脸...")
    print("（这个版本先检测人脸，录入功能后续添加）")

if __name__ == "__main__":
    capture_and_detect()
