#!/usr/bin/env python3
"""
AI 宠物 - 语音版 v5
功能：听到 → 打印出来 → 等回复
"""

import pyaudio
import wave
import whisper
import os
import time
import threading

WHISPER_MODEL = "tiny"
AUDIO_FILE = "/tmp/voice_v5.wav"

class VoiceToMe:
    def __init__(self):
        print("🎤 加载 Whisper...")
        self.model = whisper.load_model(WHISPER_MODEL)
        print("✅ 加载完成")
        
    def record(self, duration=3):
        CHUNK = 1024
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=CHUNK)
        
        frames = []
        for i in range(0, int(16000 / CHUNK * duration)):
            frames.append(stream.read(CHUNK))
        
        stream.close()
        p.terminate()
        
        wf = wave.open(AUDIO_FILE, 'wb')
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(16000)
        wf.writeframes(b''.join(frames)); wf.close()
        
    def recognize(self):
        result = self.model.transcribe(AUDIO_FILE, language="zh", fp16=False)
        return result["text"].strip()
    
    def speak(self, text):
        print(f"🔊 回复: {text}")
        os.system(f'say "{text}"')

# 启动
print("="*50)
print("🤖 说话，我会听到并回复你！")
print("="*50)

assistant = VoiceToMe()

while True:
    try:
        print("\n🎤 说话吧...", flush=True)
        assistant.record(duration=3)
        
        text = assistant.recognize()
        if text and len(text) > 1:
            print(f"\n🗣️ 你说: {text}")
            
            # 这里我会自动回复你！
            # 不用等，我直接说
            assistant.speak(f"我听到了！你说{text}")
            
    except KeyboardInterrupt:
        print("\n👋 退出")
        break
    except Exception as e:
        print(f"❌ {e}")
