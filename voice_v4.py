#!/usr/bin/env python3
"""
AI 宠物 - 语音版 v4 (检测静音)
功能：检测到声音结束后再识别
"""

import pyaudio
import wave
import whisper
import os
import time

WHISPER_MODEL = "tiny"
AUDIO_FILE = "/tmp/voice_v4.wav"

class VoiceAssistantV4:
    def __init__(self):
        print("🎤 加载 Whisper 模型...")
        self.model = whisper.load_model(WHISPER_MODEL)
        print("✅ 加载完成")
        self.running = True
        
    def record_with_silence_detection(self):
        """检测静音来结束录音"""
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        SILENCE_THRESHOLD = 500  # 静音阈值
        MAX_RECORD_TIME = 5  # 最多5秒
        
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, 
                       input=True, frames_per_buffer=CHUNK)
        
        frames = []
        silent_count = 0
        speaking = False
        
        print("🎤 说话吧...", flush=True)
        
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)
            
            # 计算音量
            import struct
            samples = struct.unpack('h' * (len(data) // 2), data)
            vol = sum(abs(s) for s in samples) / len(samples)
            
            if vol > SILENCE_THRESHOLD:
                speaking = True
                silent_count = 0
            else:
                if speaking:
                    silent_count += 1
                    if silent_count > 20:  # 静音0.5秒认为说完了
                        break
            
            # 超时保护
            if len(frames) > RATE // CHUNK * MAX_RECORD_TIME:
                break
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        # 保存
        wf = wave.open(AUDIO_FILE, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        
    def recognize(self):
        result = self.model.transcribe(AUDIO_FILE, language="zh", fp16=False)
        return result["text"].strip()
    
    def get_response(self, question):
        q = question.replace("氣", "气").replace("麼", "么")
        
        if "天" in q and "气" in q:
            return "今天天气不错！"
        elif "时" in q and "间" in q:
            return "现在是下午3点18分"
        elif "叫" in q or "名字" in q:
            return "我叫哈罗！"
        else:
            return f"我听到你说 '{question}'"
    
    def speak(self, text):
        print(f"🔊 {text}")
        os.system(f'say "{text}"')
    
    def run(self):
        print("=" * 50)
        print("🤖 AI 宠物 - 语音版 v4 (检测静音)")
        print("👂 说完后我会自动识别...")
        print("=" * 50)
        
        while self.running:
            try:
                self.record_with_silence_detection()
                
                text = self.recognize()
                if text and len(text) > 1:
                    print(f"🗣️ 听到: {text}")
                    response = self.get_response(text)
                    self.speak(response)
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"❌ {e}")

if __name__ == "__main__":
    assistant = VoiceAssistantV4()
    assistant.run()
