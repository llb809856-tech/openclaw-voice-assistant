#!/usr/bin/env python3
"""
AI 宠物 - 硅基流动语音版
功能：听到 → 识别 → 回复 → 说话
"""

import pyaudio
import wave
import requests
import os
import time

API_KEY = "sk-nykzvzhagekipeurfkbdswrxfjwzkvkazufshcofurgenavv"
AUDIO_FILE = "/tmp/voice_sf.wav"

class VoicePet:
    def __init__(self):
        self.running = True
        
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
        url = "https://api.siliconflow.cn/v1/audio/transcriptions"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        
        with open(AUDIO_FILE, 'rb') as f:
            files = {'file': ('test.wav', f, 'audio/wav')}
            data = {'model': 'FunAudioLLM/SenseVoiceSmall'}
            r = requests.post(url, headers=headers, files=files, data=data, timeout=60)
        
        result = r.json()
        return result.get("text", "").strip()
    
    def speak(self, text):
        print(f"🔊 {text}")
        os.system(f'say "{text}"')
    
    def run(self):
        print("="*50)
        print("🤖 AI 宠物 - 硅基流动语音版")
        print("👂 说话，我会听到并回复你！")
        print("="*50)
        
        while self.running:
            try:
                print("\n🎤 说话吧...", flush=True)
                self.record(duration=3)
                
                text = self.recognize()
                if text and len(text) > 1:
                    print(f"\n🗣️ 你说: {text}")
                    
                    # 回复
                    response = f"我听到你说 {text}"
                    self.speak(response)
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"❌ {e}")
                time.sleep(1)

if __name__ == "__main__":
    pet = VoicePet()
    pet.run()
