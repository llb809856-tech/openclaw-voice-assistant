#!/usr/bin/env python3
"""
豆包语音识别 - WebSocket 流式版本
"""

import websocket
import json
import base64
import uuid
import gzip
import pyaudio
import wave
import threading
import time

# 配置
APP_KEY = "1110939398"
ACCESS_KEY = "BcwtmCmwff8rwxMUVA0QLTC3CLXWNEC"  # 注意大小写
RESOURCE_ID = "volc.seedasr.sauc.duration"  # 豆包2.0

# 全局变量
ws = None

def create_header():
    """创建鉴权Header"""
    return {
        "X-Api-App-Key": APP_KEY,
        "X-Api-Access-Key": ACCESS_KEY,
        "X-Api-Resource-Id": RESOURCE_ID,
        "X-Api-Connect-Id": str(uuid.uuid4())
    }

def build_request(audio_base64):
    """构建请求"""
    request = {
        "user": {"uid": "test_user"},
        "audio": {
            "format": "wav",
            "rate": 16000,
            "bits": 16,
            "channel": 1,
            "codec": "raw"
        },
        "request": {
            "model_name": "bigmodel",
            "enable_itn": True,
            "enable_punc": True
        }
    }
    
    # 压缩
    compressed = gzip.compress(json.dumps(request).encode())
    
    # 构建header
    header = bytearray()
    # version(4) + header_size(4) + msg_type(4) + flags(4) + serialization(4) + compression(4) + reserved(8) = 32bits = 4bytes
    header.append(0x11)  # version=1, header_size=1
    header.append(0x10)  # msg_type=1 (full request), flags=0
    header.append(0x10)  # serialization=1 (json), compression=1 (gzip)
    header.append(0x00)  # reserved
    
    # payload size
    import struct
    header.extend(struct.pack('>I', len(compressed)))
    
    return bytes(header) + compressed

def on_message(ws, message):
    """收到消息"""
    print("收到:", message[:200] if len(message) > 200 else message)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws):
    print("Closed")

def on_open(ws, audio_file):
    """连接打开"""
    print("Connected!")
    
    # 读取音频文件
    with open(audio_file, 'rb') as f:
        audio_data = f.read()
    
    # 发送请求
    request = {
        "user": {"uid": "test_user"},
        "audio": {
            "format": "wav",
            "rate": 16000,
            "bits": 16,
            "channel": 1,
            "codec": "raw"
        },
        "request": {
            "model_name": "bigmodel"
        }
    }
    
    # 压缩
    compressed = gzip.compress(json.dumps(request).encode())
    
    # Header: version=1, header_size=1, msg_type=1(full), flags=0, serialization=1(json), compression=1(gzip)
    header = bytes([0x11, 0x10, 0x10, 0x00])
    import struct
    header += struct.pack('>I', len(compressed))
    
    ws.send(header + compressed, opcode=0x1)
    print("Sent config")
    
    # 发送音频
    # 分包发送，每200ms
    chunk_size = 3200  # 16000 * 2 * 0.1 = 3200 bytes for 100ms
    for i in range(0, len(audio_data), chunk_size):
        chunk = audio_data[i:i+chunk_size]
        
        # Header: version=1, header_size=1, msg_type=2(audio), flags=0, serialization=0, compression=0
        header = bytes([0x11, 0x20, 0x00, 0x00])
        header += struct.pack('>I', len(chunk))
        
        ws.send(header + chunk, opcode=0x1)
        time.sleep(0.1)
    
    # 发送结束包
    header = bytes([0x11, 0x30, 0x00, 0x00])  # flags=2 表示最后一包
    header += struct.pack('>I', 0)
    ws.send(header, opcode=0x1)
    print("Sent end")

def test_doubao(audio_file):
    """测试豆包"""
    url = "wss://openspeech.bytedance.com/api/v3/sauc/bigmodel"
    headers = create_header()
    
    ws = websocket.WebSocket(
        header=headers,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    
    ws.connect(url)
    on_open(ws, audio_file)
    
    # 等待结果
    time.sleep(3)
    ws.close()

if __name__ == "__main__":
    # 先录个音
    print("🎤 录音3秒...")
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    frames = [stream.read(1024) for _ in range(30)]
    stream.close()
    p.terminate()
    
    wf = wave.open('/tmp/doubao_test.wav', 'wb')
    wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(16000)
    wf.writeframes(b''.join(frames)); wf.close()
    
    print("🔍 开始识别...")
    test_doubao('/tmp/doubao_test.wav')
