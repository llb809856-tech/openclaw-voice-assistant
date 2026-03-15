#!/usr/bin/env python3
"""
AI 宠物 - 语音版 v3 (简化版)
功能：语音输入 → 本地回复 → 语音输出
"""

import pyaudio
import wave
import whisper
import os
import time
import subprocess

WHISPER_MODEL = "tiny"
AUDIO_FILE = "/tmp/voice_v3.wav"

class VoiceAssistant:
    def __init__(self):
        print("🎤 加载 Whisper 模型...")
        self.model = whisper.load_model(WHISPER_MODEL)
        print("✅ 加载完成")
        self.running = True
        
    def record_once(self, duration=3):
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
        result = self.model.transcribe(AUDIO_FILE, language="Chinese")
        return result["text"].strip()
    
    def get_response(self, question):
        """智能回复 - 基于关键词"""
        q = question.replace("氣", "气").replace("麼", "么")
        
        if "天" in q and "气" in q:
            return "今天天气不错，阴天不下雨，适合出门！"
        elif "时" in q and "间" in q:
            return "现在是下午3点"
        elif "叫" in q or "名字" in q:
            return "我叫哈罗，是你的 AI 宠物！"
        elif "好" in q:
            return "我很好，谢谢你！"
        elif "谁" in q:
            return "我是哈罗，你的 AI 宠物伙伴！"
        elif "谢" in q:
            return "不客气！"
        elif "再" in q and "见" in q:
            return "再见！有空再聊！"
        else:
            return f"你说了'{question}'对吧？我听到了！"
    
    def speak(self, text):
        print(f"🔊 回复: {text}")
        os.system(f'say "{text}"')
    
    def run(self):
        print("=" * 50)
        print("🤖 AI 宠物 - 语音版 v3")
        print("👂 持续监听中...")
        print("=" * 50)
        
        while self.running:
            try:
                print("🎤 监听...", end="\r", flush=True)
                self.record_once(duration=3)
                
                text = self.recognize()
                if text and len(text) > 1:
                    print(f"\n🗣️ 听到: {text}")
                    response = self.get_response(text)
                    self.speak(response)
                
            except Exception as e:
                print(f"❌ 错误: {e}")
            time.sleep(0.5)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    try:
        assistant.run()
    except KeyboardInterrupt:
        print("\n👋 退出")
        assistant.running = False
