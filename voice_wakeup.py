#!/usr/bin/env python3
"""
AI 宠物 - 语音唤醒
功能：监听麦克风，听到"你好"或其他关键词时响应
"""

import speech_recognition as sr
import threading
import time
import os

class VoiceWakeup:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        self.running = False
        self.callback = None
        
    def set_callback(self, func):
        """设置唤醒回调"""
        self.callback = func
        
    def listen(self):
        """监听"""
        with self.mic as source:
            print("👂 监听中... (说'你好'唤醒)")
            self.r.adjust_for_ambient_noise(source)
            
            while self.running:
                try:
                    audio = self.r.listen(source, timeout=1, phrase_time_limit=3)
                    text = self.r.recognize_google(audio, language='zh-CN')
                    print(f"🗣️ 听到: {text}")
                    
                    # 检查关键词
                    keywords = ['你好', 'hey', 'hi', '在吗', '唤醒']
                    if any(k in text.lower() for k in keywords):
                        print("✅ 唤醒成功!")
                        if self.callback:
                            self.callback(text)
                            
                except sr.WaitTimeoutError:
                    pass
                except sr.UnknownValueError:
                    pass
                except Exception as e:
                    print(f"❌ 错误: {e}")
                    
    def start(self):
        """开始监听"""
        self.running = True
        t = threading.Thread(target=self.listen, daemon=True)
        t.start()
        print("🎤 语音唤醒已启动")
        
    def stop(self):
        """停止监听"""
        self.running = False
        print("⏹️ 语音唤醒已停止")

if __name__ == "__main__":
    def on_wake(text):
        print(f"👉 触发响应: {text}")
        # 这里可以触发 OpenClaw
        os.system('say "你好，我是 AI 宠物"')
        
    wakeup = VoiceWakeup()
    wakeup.set_callback(on_wake)
    wakeup.start()
    
    print("按 Ctrl+C 退出")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        wakeup.stop()
