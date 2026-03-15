#!/usr/bin/env python3
"""
AI 宠物 - 完整版
流程：硅基流动(ASR) → OpenClaw(LLM) → 硅基流动(TTS) → 说话
"""

import pyaudio
import wave
import requests
import os
import time
import subprocess

API_KEY = "sk-nykzvzhagekipeurfkbdswrxfjwzkvkazufshcofurgenavv"
AUDIO_FILE = "/tmp/voice_full.wav"

class VoicePet:
    def __init__(self):
        self.running = True
        
    def record(self, duration=3):
        CHUNK = 1024
        p = pyaudio.PyAudio()
        # 使用摄像头作为输入设备 (device_index=1)
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, input_device_index=1, frames_per_buffer=CHUNK)
        
        frames = []
        for i in range(0, int(16000 / CHUNK * duration)):
            frames.append(stream.read(CHUNK))
        
        stream.close()
        p.terminate()
        
        wf = wave.open(AUDIO_FILE, 'wb')
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(16000)
        wf.writeframes(b''.join(frames)); wf.close()
        
    def asr_recognize(self):
        """硅基流动 ASR"""
        url = "https://api.siliconflow.cn/v1/audio/transcriptions"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        
        with open(AUDIO_FILE, 'rb') as f:
            files = {'file': ('test.wav', f, 'audio/wav')}
            data = {'model': 'FunAudioLLM/SenseVoiceSmall'}
            r = requests.post(url, headers=headers, files=files, data=data, timeout=60)
        
        result = r.json()
        return result.get("text", "").strip()
    
    def get_openclaw_reply(self, text):
        """发给 OpenClaw 获取回复"""
        # 用 session ID
        session_id = "e3f510da-9606-4d9e-b77a-2402b1b87e7c"
        cmd = ["openclaw", "agent", "--session-id", session_id, "--message", text]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            output = result.stdout + result.stderr
            # 提取回复
            lines = output.split('\n')
            reply = None
            for line in lines:
                if line.strip() and not any(x in line for x in ['plugins', 'Warning', 'lcm', 'feishu', 'Error:', 'error:']):
                    reply = line.strip()
            return reply or "我在"
        except:
            pass
        
        # 备用：用硅基流动
        url = "https://api.siliconflow.cn/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "Qwen/Qwen2.5-7B-Instruct",
            "messages": [
                {"role": "system", "content": "你是哈罗，一个智能的AI宠物。用自然、简洁的中文回复。"},
                {"role": "user", "content": text}
            ]
        }
        r = requests.post(url, headers=headers, json=data, timeout=20)
        result = r.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", "我没听清")
    
    def speak(self, text):
        """语音合成并播放"""
        print(f"🔊 回复: {text}")
        os.system(f'say "{text}"')
    
    def run(self):
        print("="*50)
        print("🤖 AI 宠物 - 完整版 (OpenClaw + 硅基流动)")
        print("👂 说话，我会用 AI 回复你！")
        print("="*50)
        
        while self.running:
            try:
                print("\n🎤 说话吧...", flush=True)
                self.record(duration=3)
                
                # 1. 识别
                text = self.asr_recognize()
                if text and len(text) > 1:
                    print(f"\n🗣️ 你说: {text}")
                    
                    # 2. 发给 OpenClaw
                    print("🧠 思考中...")
                    reply = self.get_openclaw_reply(text)
                    
                    # 3. 说出来
                    self.speak(reply)
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"❌ {e}")
                time.sleep(1)

if __name__ == "__main__":
    pet = VoicePet()
    pet.run()
