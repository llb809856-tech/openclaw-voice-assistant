#!/usr/bin/env python3
"""
AI 宠物 - 语音版接 OpenClaw
功能：语音输入 → 发送给 OpenClaw → 语音回答
"""

import pyaudio
import wave
import whisper
import os
import time
import subprocess
import json

# 配置
WHISPER_MODEL = "tiny"
AUDIO_FILE = "/tmp/voice_openclaw.wav"

class VoiceWithOpenClaw:
    def __init__(self):
        print("🎤 加载 Whisper 模型...")
        self.model = whisper.load_model(WHISPER_MODEL)
        print("✅ 模型加载完成")
        self.running = True
        
    def record_once(self, duration=3):
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
        """语音识别"""
        result = self.model.transcribe(AUDIO_FILE, language="Chinese")
        return result["text"].strip()
    
    def ask_openclaw(self, question):
        """问 OpenClaw"""
        print(f"🤖 问 OpenClaw: {question}")
        
        # 通过 curl 发送消息到 OpenClaw
        try:
            # 使用 curl 直接发到 API
            cmd = f'curl -s -X POST "http://localhost:11434/api/chat" -d \'{{"model":"llama3","messages":[{{"role":"user","content":"{question}"}}]}}\' 2>/dev/null || echo "failed"'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            # 尝试用 openclaw chat
            cmd2 = f'echo "{question}" | openclaw chat -m minimax-cn/MiniMax-M2.5 2>&1 | tail -20'
            result2 = subprocess.run(cmd2, shell=True, capture_output=True, text=True, timeout=30)
            answer = result2.stdout.strip()
            if not answer:
                answer = "我不知道怎么回答"
            return answer
        except Exception as e:
            print(f"❌ OpenClaw 错误: {e}")
            return "抱歉，我好像出了点问题"
    
    def speak(self, text):
        """语音输出"""
        print(f"🔊 回复: {text}")
        os.system(f'say "{text}"')
    
    def run(self):
        """主循环"""
        print("=" * 50)
        print("🤖 AI 宠物 - 语音版 (连接 OpenClaw)")
        print("👂 持续监听中，说任何话都会回答...")
        print("=" * 50)
        
        while self.running:
            try:
                print("🎤 监听...", end="\r", flush=True)
                self.record_once(duration=3)
                
                text = self.recognize()
                if text and len(text) > 1:
                    print(f"🗣️ 听到: {text}", flush=True)
                    
                    # 问 OpenClaw
                    answer = self.ask_openclaw(text)
                    
                    # 语音回复
                    self.speak(answer)
                
            except Exception as e:
                print(f"❌ 错误: {e}")
            
            time.sleep(0.5)
    
    def stop(self):
        self.running = False

if __name__ == "__main__":
    assistant = VoiceWithOpenClaw()
    try:
        assistant.run()
    except KeyboardInterrupt:
        print("\n👋 退出")
        assistant.stop()
