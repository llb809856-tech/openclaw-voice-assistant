#!/usr/bin/env python3
"""Kling AI o1 - 手套正确展示"""
import requests, jwt, time, base64, os

AK = "AKBykrDTC3TeGQrhmKfgFFhdYdrYLdhr"
SK = "fQ3AY83KFJ89peMEaeH4CbHrfCBYNaE4"
URL = "https://api-beijing.klingai.com/v1/videos/omni-video"

def jwt_token():
    t = int(time.time())
    return jwt.encode({"iss": AK, "exp": t+1800, "nbf": t-5}, SK, algorithm="HS256", headers={"alg": "HS256", "typ": "JWT"})

def find_imgs():
    base = "/Users/a01/Desktop/触心产品营销"
    paths = []
    for root, dirs, files in os.walk(base):
        for f in sorted(files):
            if f.startswith(("1", "2", "3")) and "白底" in f and f.endswith(".jpg"):
                paths.append(os.path.join(root, f))
                if len(paths) >= 3: return paths
    return paths

def img2b64(p):
    with open(p, "rb") as f: return base64.b64encode(f.read()).decode("utf-8")

def submit(b64_list):
    token = jwt_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    # 修正后的 prompt - 强调手套正确结构
    prompt = """<<<image_1>>><<<image_2>>><<<image_3>>> 专业奢侈品手套产品摄影，黑色小羊皮手套平铺展示，手背朝上（手背平整没有大拇指套，logo 金属标志在手腕处），纯白背景，柔和侧光突出皮质纹理和精细缝线，镜头缓慢从上方俯视平移，高端广告质感，4K 超高清，细节清晰，轻奢品质，不是悬浮，平铺在展示台上"""
    
    payload = {
        "model_name": "kling-video-o1",
        "prompt": prompt,
        "image_list": [{"image_url": b} for b in b64_list],
        "duration": "5", "mode": "pro", "aspect_ratio": "16:9",
        "camera_control": {"type": "simple", "config": {"pan": -5, "tilt": 0, "zoom": 0}},
        "negative_prompt": "deformed, blurry, low quality, distorted, watermark, 悬浮，站立，抖动，淘宝风，手掌朝上，大拇指套明显"
    }
    print(f"提交任务，{len(b64_list)}张参考图...")
    r = requests.post(URL, json=payload, headers=headers, timeout=90)
    print(f"状态：{r.status_code}, 响应：{r.text[:200]}")
    if r.status_code == 200:
        tid = r.json().get("data", {}).get("task_id")
        print(f"Task ID: {tid}")
        return tid
    return None

def check(tid):
    r = requests.get(f"{URL}/{tid}", headers={"Authorization": f"Bearer {jwt_token()}"}, timeout=30)
    return r.json() if r.status_code == 200 else None

def main():
    print("="*50)
    print("Kling AI o1 - 手套正确展示（手背朝上）")
    
    paths = find_imgs()
    print(f"\n找到 {len(paths)} 张图:")
    for p in paths: print(f"  {os.path.basename(p)}")
    
    b64s = [img2b64(p) for p in paths]
    print(f"\nbase64 总长度：{sum(len(b) for b in b64s)}")
    
    tid = submit(b64s)
    if not tid: return
    
    print("\n等待生成...")
    vurl = None
    for i in range(30):
        time.sleep(10)
        s = check(tid)
        if not s: continue
        if s.get("code") == 0:
            st = s.get("data", {}).get("task_status", "")
            print(f"  {i+1}: {st}")
            if st == "succeed":
                vurl = s.get("data", {}).get("task_result", {}).get("videos", [{}])[0].get("url")
                break
            elif st == "failed":
                print(f"失败：{s}")
                return
    
    if not vurl:
        print("超时")
        return
    
    print("\n下载视频...")
    out = "/Users/a01/Desktop/触心产品营销/kling_o1_手背朝上.mp4"
    with open(out, "wb") as f: f.write(requests.get(vurl).content)
    print(f"✅ 完成：{out}")

if __name__ == "__main__": main()
