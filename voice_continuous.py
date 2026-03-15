#!/usr/bin/env python3
"""
AI 宠物 - 语音唤醒持续监听版 v2
功能：持续监听麦克风，听到任何话都响应
"""

import pyaudio
import wave
import whisper
import os
import time

# 配置
WHISPER_MODEL = "tiny"
AUDIO_FILE = "/tmp/continuous.wav"

class ContinuousWakeup:
    def __init__(self):
        print("🎤 加载 Whisper 模型...")
        self.model = whisper.load_model(WHISPER_MODEL)
        print("✅ 模型加载完成")
        self.running = True
        
    def record_once(self, duration=2):
        """录制一次"""
        CHUNK = 1024
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, 
                       input=True, frames_per_buffer=CHUNK)
        
        frames = []
        for i in range(0, int(16000 / CHUNK * duration)):
            frames.append(stream.read(CHUNK))
        
        stream.close()
        p.terminate()
        
        wf = wave.open(AUDIO_FILE, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        wf.writeframes(b''.join(frames))
        wf.close()
        
    def recognize(self):
        """识别"""
        result = self.model.transcribe(AUDIO_FILE, language="Chinese")
        return result["text"].strip()
    
    def respond(self, text):
        """响应 - 现在会对任何识别到的话回应"""
        print(f"🎉 收到: {text}")
        
        # 简繁体转换
        text_conv = text.replace("氣", "气").replace("麼", "么").replace("怎麼", "怎么")
        
        # 根据内容回应
        if "天气" in text_conv:
            response = "今天天气不错，阴天不下雨！"
        elif "时间" in text_conv or "几点" in text_conv:
            response = f"现在的时间是下午3点"
        elif "名字" in text_conv or "叫" in text_conv:
            response = "我叫哈罗，是你的 AI 宠物"
        elif "好" in text_conv:
            response = "我很好，谢谢关心！"
        else:
            response = "我听到了，你想说什么？"
        
        os.system(f'say "{response}"')
        print(f"👉 回复: {response}")
    
    def run(self):
        """主循环"""
        print("=" * 50)
        print("🤖 AI 宠物 - 语音持续监听 v2")
        print("👂 持续监听中，说任何话都会回应...")
        print("=" * 50)
        
        while self.running:
            try:
                print("🎤 监听...", end="\r", flush=True)
                self.record_once(duration=2)
                
                text = self.recognize()
                if text and len(text) > 1:  # 有实际内容
                    print(f"🗣️ 听到: {text}", flush=True)
                    self.respond(text)
                
            except Exception as e:
                print(f"❌ 错误: {e}")
            
            time.sleep(0.5)
    
    def stop(self):
        self.running = False

if __name__ == "__main__":
    wakeup = ContinuousWakeup()
    try:
        wakeup.run()
    except KeyboardInterrupt:
        print("\n👋 退出")
        wakeup.stop()
