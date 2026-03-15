#!/usr/bin/env python3
"""
AI 宠物 - 语音唤醒完整版
功能：监听麦克风，听到关键词后响应
"""

import pyaudio
import wave
import whisper
import os
import time

# 配置
WHISPER_MODEL = "tiny"
KEYWORDS = ["你好", "在吗", "hey", "hi", "喂"]
AUDIO_FILE = "/tmp/wakeup_audio.wav"

class VoiceWakeup:
    def __init__(self):
        print("🎤 加载 Whisper 模型...")
        self.model = whisper.load_model(WHISPER_MODEL)
        print("✅ 模型加载完成")
        
    def listen(self, duration=3):
        """录音"""
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, 
                       input=True, frames_per_buffer=CHUNK)
        
        frames = []
        for i in range(0, int(RATE / CHUNK * duration)):
            data = stream.read(CHUNK)
            frames.append(data)
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        wf = wave.open(AUDIO_FILE, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        
    def recognize(self):
        """识别语音"""
        result = self.model.transcribe(AUDIO_FILE, language="Chinese")
        text = result["text"].strip()
        return text
    
    def check_keyword(self, text):
        """检查关键词"""
        text_lower = text.lower()
        for kw in KEYWORDS:
            if kw in text_lower:
                return True, kw
        return False, None
    
    def run(self):
        """主循环"""
        print("=" * 40)
        print("🤖 AI 宠物 - 语音唤醒已启动")
        print("👂 等待听到'你好'...")
        print("=" * 40)
        
        while True:
            try:
                # 监听
                print("🎤 监听中...")
                self.listen(duration=3)
                
                # 识别
                text = self.recognize()
                if text:
                    print(f"🗣️ 听到: {text}")
                    
                    # 检查关键词
                    found, kw = self.check_keyword(text)
                    if found:
                        print(f"✅ 唤醒成功! 关键词: {kw}")
                        print("👉 触发 OpenClaw...")
                        
                        # 这里可以触发 OpenClaw
                        # 例如：发送消息到 OpenClaw
                        
                time.sleep(1)
                
            except KeyboardInterrupt:
                print("\n👋 退出")
                break
            except Exception as e:
                print(f"❌ 错误: {e}")
                time.sleep(1)

if __name__ == "__main__":
    wakeup = VoiceWakeup()
    wakeup.run()
