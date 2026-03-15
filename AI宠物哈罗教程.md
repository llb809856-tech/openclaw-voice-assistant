# 如何用 OpenClaw 打造自己的 AI 宠物"哈罗"

## 成果展示

今天，我们成功实现了：
- ✅ 通过电脑麦克风实时语音对话
- ✅ AI 能听懂你的话并智能回复
- ✅ 可以语音控制打开网页
- ✅ 可以通过语音发送飞书消息

## 需要的硬件

1. **电脑** - Mac mini（或任何电脑）
2. **摄像头** - 带麦克风的 USB 摄像头（推荐海康威视 E14A，¥120）

## 需要的软件/服务

1. **OpenClaw** - AI 助手框架
2. **硅基流动** - 语音识别 API
3. **MiniMax** - AI 大脑（OpenClaw 内置）

## 步骤

### 第一步：安装依赖

```bash
# 安装 Python 依赖
pip3 install pyaudio requests websocket-client
```

### 第二步：获取 API Key

1. **硅基流动**（语音识别）
   - 注册 https://cloud.siliconflow.cn/
   - 获取 API Key

2. **MiniMax**（AI 大脑）
   - OpenClaw 已内置配置

### 第三步：创建语音脚本

创建 `voice_full.py`：

```python
#!/usr/bin/env python3
"""
AI 宠物 - 完整版
流程：麦克风 → 硅基流动(ASR) → MiniMax(LLM) → 说话
"""

import pyaudio
import wave
import requests
import os
import subprocess

# 你的硅基流动 API Key
API_KEY = "你的API Key"

# MiniMax Session ID（从 openclaw sessions 获取）
SESSION_ID = "你的Session ID"

def record(duration=3):
    """录音"""
    CHUNK = 1024
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16, 
        channels=1, 
        rate=16000, 
        input=True, 
        input_device_index=1,  # 摄像头麦克风
        frames_per_buffer=CHUNK
    )
    frames = []
    for i in range(0, int(16000 / CHUNK * duration)):
        frames.append(stream.read(CHUNK))
    stream.close()
    p.terminate()
    
    wf = wave.open("/tmp/voice.wav", 'wb')
    wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(16000)
    wf.writeframes(b''.join(frames)); wf.close()

def recognize():
    """语音识别"""
    url = "https://api.siliconflow.cn/v1/audio/transcriptions"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    with open("/tmp/voice.wav", 'rb') as f:
        files = {'file': ('test.wav', f, 'audio/wav')}
        data = {'model': 'FunAudioLLM/SenseVoiceSmall'}
        r = requests.post(url, headers=headers, files=files, data=data, timeout=60)
    
    return r.json().get("text", "").strip()

def get_reply(text):
    """获取 AI 回复"""
    cmd = ["openclaw", "agent", "--session-id", SESSION_ID, "--message", text]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    output = result.stdout + result.stderr
    # 提取回复
    lines = output.split('\n')
    for line in lines:
        if line.strip() and "Error" not in line:
            return line.strip()
    return "我在"

def speak(text):
    """语音输出"""
    os.system(f'say "{text}"')

# 主循环
while True:
    print("🎤 说话吧...")
    record(3)
    text = recognize()
    if text and len(text) > 1:
        print(f"🗣️ 你说: {text}")
        reply = get_reply(text)
        print(f"🔊 回复: {reply}")
        speak(reply)
```

### 第四步：运行

```bash
python3 voice_full.py
```

## 效果

现在你可以：
- 对着电脑说话
- AI 听懂并回复
- 语音说出来
- 还能控制打开网页、发送消息

## 视频教程

（待添加）

## 总结

今天我们证明了：
1. 不需要昂贵的设备
2. 用现有的摄像头就能实现语音对话
3. AI 伴侣不再是科幻

---

*贡献者：米米可思 + 小林（OpenClaw）*
*日期：2026年3月15日*
