#!/usr/bin/env python3
"""
豆包语音识别测试
"""

import requests
import json
import base64
import wave

# 配置
APP_ID = "1110939398"
ACCESS_TOKEN = "BcwtmCmwff8rwxMUva0QLtc3CLXwnIec"
SECRET_KEY = "RBgsqBrKTRGej8t_cU4ZGO10KwIHRKl2"

def get_token():
    """获取 access token"""
    url = "https://open.volcengineapi.com/oauth/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": APP_ID,
        "client_secret": SECRET_KEY
    }
    r = requests.post(url, data=data)
    print("Token response:", r.text)
    return r.json().get("access_token")

def asr(audio_file):
    """语音识别"""
    # 读取音频文件
    with open(audio_file, 'rb') as f:
        audio_data = f.read()
    
    # 转 base64
    audio_base64 = base64.b64encode(audio_data).decode()
    
    # 调用 ASR API
    url = "https://open.volcengineapi.com/v1/asr"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "app": {
            "appid": APP_ID,
            "token": ACCESS_TOKEN
        },
        "audio": {
            "format": "wav",
            "rate": 16000,
            "bits": 16,
            "channel": 1,
            "codec": "raw",
            "base64": audio_base64
        },
        "request": {
            "reqid": "test123",
            "sequence": 1
        }
    }
    
    r = requests.post(url, headers=headers, json=data)
    print("ASR response:", r.text)
    return r.json()

# 测试
if __name__ == "__main__":
    print("🔊 豆包语音识别测试")
    result = asr("/tmp/mic_test.wav")
    print("结果:", result)
