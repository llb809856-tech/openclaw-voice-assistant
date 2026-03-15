# Seedance 视频生成脚本

**版本**：v1.0  
**创建日期**：2026-03-04  
**用途**：Seedance 网页版手动生成指南  
**适用平台**：seedance.best / seedance2.ai

---

# 一、现有素材分类清单

## 📁 素材位置
`/Users/a01/Desktop/触心产品营销/`

---

## 📋 素材分类表

| 分类 | 素材名称 | 时长 | 用途 | 可复用镜头 |
|------|---------|------|------|-----------|
| **产品视频** | `女款：产品视频.mp4` | ~30 秒 | 产品特写、质感展示 | 皮料纹理、logo 特写、手套平铺 |
| **场景模特** | `女款：场景模特.mp4` | ~40 秒 | 使用场景、佩戴效果 | 雪地触屏、模特佩戴、户外场景 |
| **男女混剪** | `男女混剪.mp4` | ~30 秒 | 人群覆盖、款式展示 | 男女佩戴对比、多场景切换 |
| **设计花絮** | `设计花絮.mp4` | ~25 秒 | 品牌故事、工艺展示 | 设计草图、工艺细节、工作室场景 |

---

## 🎬 可提取的关键帧（已生成）

**位置**：`/Users/a01/Desktop/触心产品营销/视频帧/`

| 文件名 | 来源 | 时间点 | 用途 |
|--------|------|-------|------|
| `产品视频 -03s.jpg` | 产品视频 | 0:03 | 手套平铺特写 |
| `产品视频 -05s.jpg` | 产品视频 | 0:05 | 皮质纹理微距 |
| `产品视频 -10s.jpg` | 产品视频 | 0:10 | logo 金属特写 |
| `场景模特 -03s.jpg` | 场景模特 | 0:03 | 雪地场景广角 |
| `场景模特 -08s.jpg` | 场景模特 | 0:08 | 触屏动作特写 |
| `男女混剪 -03s.jpg` | 男女混剪 | 0:03 | 男女佩戴对比 |
| `设计花絮 -03s.jpg` | 设计花絮 | 0:03 | 设计草图展示 |

---

# 二、Seedance 生成任务清单

## 🎯 需要生成的视频镜头（共 18 个）

---

## 脚本 1：技术对比视频（60 秒）

| 镜头号 | 时长 | Prompt（中文） | Prompt（英文） | 参考素材 | 优先级 |
|-------|------|--------------|---------------|---------|-------|
| **1-1** | 3 秒 | 黑色背景，白色粗体文字逐字出现，打字机效果，极简科技感 | Black background, white bold text appearing letter by letter, typewriter effect, minimalist tech vibe | 无 | ⭐⭐⭐ |
| **1-2** | 3 秒 | 俯视角度，5 双黑色手套整齐排列在深灰色桌面上，顶部柔光，轻微侧光突出皮质纹理，镜头从左到右缓慢横移 | Top down view, 5 pairs of black leather gloves arranged in a row on dark gray table, soft overhead lighting, slight side light highlighting leather texture, camera slowly pans left to right | 产品视频 -03s.jpg | ⭐⭐⭐ |
| **1-3** | 6 秒 | 分屏对比：左边是普通涂层手套显微镜视图，涂层表面有裂纹和剥落；右边是导电纤维与皮料交织的完整结构，科学可视化风格 | Split screen comparison, left: microscope view of coated leather with cracks and peeling, right: conductive fibers woven into leather matrix, intact structure, scientific visualization | 产品视频 -05s.jpg | ⭐⭐⭐ |
| **1-4** | 8 秒 | 快速剪辑序列：手套放入洗衣机→水流冲击→取出晾干→戴手套滑动手机屏幕 | Sequence: gloves being placed into washing machine, water splashing, gloves taken out drying, gloved hand swiping smartphone screen | 无 | ⭐⭐ |
| **1-5** | 10 秒 | 分屏对比：左边戴涂层手套只有指尖能触屏，手掌滑动无反应；右边戴触心手套手掌任意位置滑动都有反应，手机显示小红书 App | Split screen, left: coated glove only fingertip works on touchscreen, right: Touching glove full palm works anywhere, smartphone showing Xiaohongshu app | 场景模特 -08s.jpg | ⭐⭐⭐ |
| **1-6** | 8 秒 | 专利证书特写，镜头从顶部缓慢向下推进到专利号，暖光侧光，证书有轻微反光质感，中文文字，官方印章清晰可见 | Patent certificate close-up, camera slowly zooms from top to patent number, warm side lighting with slight glossy reflection, Chinese text, official seal visible | 设计花絮 -03s.jpg | ⭐⭐⭐ |
| **1-7** | 10 秒 | 蒙太奇序列：手套平铺微距展示皮料纹理→缝线特写针脚均匀→金属 logo 特写反光→手拿起手套展示柔软度 | Montage: gloves laid flat macro showing leather grain, stitching close-up with even needlework, metal logo close-up with reflection, hand picking up gloves showing softness | 产品视频 -05s.jpg + 产品视频 -10s.jpg | ⭐⭐⭐ |
| **1-8** | 7 秒 | 黑色背景，白色文字对比：Dents 1500 元（灰色）→触心 869 元（亮色），右侧触心手套 45 度角产品图 | Black background, white text comparison: Dents ¥1500 (gray) then Touching ¥869 (bright), product image of Touching gloves at 45-degree angle on right | 产品视频 -03s.jpg | ⭐⭐ |
| **1-9** | 5 秒 | 黑色背景，白色触心 logo（∞符号 + 中英文）淡入，下方 Slogan"触心，不脱手套的自由"逐字出现，极简结尾 | Black background, white Touching logo (infinity symbol + Chinese English) fading in, slogan appearing letter by letter below, minimalist clean ending | 无 | ⭐⭐⭐ |

---

## 脚本 2：场景共鸣视频（45 秒）

| 镜头号 | 时长 | Prompt（中文） | Prompt（英文） | 参考素材 | 优先级 |
|-------|------|--------------|---------------|---------|-------|
| **2-1** | 5 秒 | 北京地铁站台，冬天清晨，年轻女生穿羊毛大衣搓手哈气，电子屏显示 -10℃，呼出的气可见，表情皱眉缩手，中景轻微手持晃动感，冷色调蓝灰色 | Beijing subway platform, winter early morning, young woman in wool coat rubbing hands and breathing warm air, electronic display showing -10°C, visible breath, frowning and shivering, medium shot with slight handheld shake, cold blue-gray tone | 无 | ⭐⭐⭐ |
| **2-2** | 5 秒 | 手机屏幕特写，微信消息弹窗显示"老板：方案改好了吗？"，女生看手机然后看自己冻红的手，犹豫表情，浅景深，站台晨光 | Smartphone screen close-up, WeChat notification "Boss: Is the revised plan ready?", woman looking at phone then at red frozen hands, hesitation, shallow depth of field, morning platform light | 无 | ⭐⭐⭐ |
| **2-3** | 8 秒 | 快速分屏对比：左边女生在寒风中脱手套，手指冻僵打字慢，表情痛苦；右边女生戴触心手套丝滑滑动屏幕，表情轻松 | Fast cut split screen: left woman taking off gloves in cold wind, fingers frozen typing slowly, painful expression; right woman wearing Touching gloves smoothly swiping screen, relaxed | 场景模特 -08s.jpg | ⭐⭐⭐ |
| **2-4** | 7 秒 | 触心手套特写，手指滑动手机屏幕，手掌滑动、指尖点击、握拳滑动展示全掌触屏能力，站台顶灯轻微反光，微距跟随手指动作 | Touching gloves close-up, finger swiping smartphone screen, palm swipe, fingertip tap, fist swipe demonstrating full-palm touch, station ceiling light reflection, macro following finger | 场景模特 -08s.jpg | ⭐⭐⭐ |
| **2-5** | 10 秒 | 女生走进办公室脱大衣，同事问"你不冷吗？"女生微笑"手很暖"，办公室暖气充足，窗外飘雪，暖色室内光 | Woman walking into office taking off coat, colleague asking "Aren't you cold?", woman smiling "My hands are warm", office with heating, snow outside window, warm indoor lighting | 场景模特 -03s.jpg | ⭐⭐ |
| **2-6** | 5 秒 | 黑色背景，白色文字逐行出现：869 元→一个冬天 120 天→每天 7 元，极简排版，数字动画 | Black background, white text appearing line by line: ¥869 → 120 days per winter → ¥7 per day, minimalist typography, number animation | 无 | ⭐⭐ |
| **2-7** | 5 秒 | 女生戴手套走出地铁站，阳光洒在脸上微笑，底部居中文字"触心，不脱手套的自由"，右上角小 logo，暖色调结尾 | Woman wearing gloves walking out of subway station, sunlight on face smiling, text "触心，不脱手套的自由" at bottom center, small logo top right, warm color tone ending | 场景模特 -03s.jpg | ⭐⭐⭐ |

---

## 脚本 3：KOC 测评视频（60 秒）

| 镜头号 | 时长 | Prompt（中文） | Prompt（英文） | 参考素材 | 优先级 |
|-------|------|--------------|---------------|---------|-------|
| **3-1** | 5 秒 | KOC 自拍视角，室内暖光，25-30 岁职场女性自然妆容，居家背景有书架绿植，对镜头说话，Vlog 风格 | KOC selfie view, indoor warm lighting, 25-30yo professional woman natural makeup, home background with bookshelf and plants, speaking to camera, vlog style | 无 | ⭐⭐⭐ |
| **3-2** | 10 秒 | 快速剪辑开箱序列：打开快递盒→露出黑色磁吸礼盒和品牌 logo→拿出手套和防尘袋，期待惊喜表情，包装特写 | Fast cut unboxing: opening courier box, revealing black magnetic gift box with logo, taking out gloves with dust bag, anticipation and surprise expression, packaging close-ups | 设计花絮 -03s.jpg | ⭐⭐ |
| **3-3** | 10 秒 | 手套微距特写，手指抚摸皮料展示纹理，缝线细节，金属 logo 特写，揉捏手套展示柔软度，"皮质 5 星 做工 5 星"字幕 | Gloves macro close-up, finger stroking leather showing grain, stitching detail, metal logo close-up,揉捏 gloves showing softness, "Leather 5 stars Craftsmanship 5 stars" subtitle | 产品视频 -05s.jpg + 产品视频 -10s.jpg | ⭐⭐⭐ |
| **3-4** | 15 秒 | 戴手套测试触屏，多个动作：滑动小红书、点击微信、放大图片、握拳滑动，惊喜表情"哇真的可以！手掌也能用！" | Wearing gloves testing touchscreen, multiple actions: scrolling Xiaohongshu, tapping WeChat, pinch-to-zoom, fist swipe, surprised reaction "Wow it works! Palm works too!" | 场景模特 -08s.jpg | ⭐⭐⭐ |
| **3-5** | 10 秒 | 拿出旧手套（普通涂层款）对比，旧手套只有指尖能触屏，触心全掌可以，并排对比展示，"涂层 vs 无涂 代差明显"字幕 | Taking out old gloves (regular coated type) for comparison, old gloves only fingertip works, Touching full palm works, side-by-side comparison, "Coating vs No-coating" subtitle | 产品视频 -03s.jpg | ⭐⭐ |
| **3-6** | 10 秒 | 回到自拍视角，真诚推荐，"869 不便宜但值得，200 件库存卖完不知何时补"，"推荐指数 5 星"字幕，结尾挥手拜拜 | Back to selfie view, sincere recommendation, "¥869 not cheap but worth it, 200 pieces stock don't know when restock", "Recommendation 5 stars" subtitle, waving bye at end | 无 | ⭐⭐⭐ |

---

# 三、Seedance 网页版操作步骤

## 📝 步骤 1：注册登录

1. 打开 **seedance2.ai** 或 **seedance.best**
2. 点击 "Sign Up" 注册（邮箱 + 密码）
3. 验证邮箱后登录
4. 确认账户有免费额度（约 $5-10）

---

## 📝 步骤 2：创建视频

1. 点击 "Create Video" 或 "Generate"
2. 选择模型：**Seedance 2.0**
3. 选择模式：
   - **Text to Video**（纯文字生成）
   - **Image to Video**（用参考图生成）← 推荐

---

## 📝 步骤 3：填写参数

| 参数 | 推荐设置 | 说明 |
|------|---------|------|
| **Prompt** | 复制上方英文 Prompt | 英文效果更好 |
| **Negative Prompt** | `deformed hands, blurry, low quality, distorted` | 避免手部变形 |
| **Duration** | 5 秒（默认） | 最长 10 秒 |
| **Resolution** | 1080p 或 2K | 根据额度选择 |
| **Motion** | Medium | 中等运动幅度 |
| **Camera** | 根据镜头选择（pan/zoom/static） | 镜头运动方式 |
| **Seed** | 留空（随机） | 固定种子可复现 |

---

## 📝 步骤 4：上传参考图（可选但推荐）

**适用镜头**：
- 1-2、1-5、1-7、1-8（产品相关）
- 2-3、2-4、2-5、2-7（场景相关）
- 3-2、3-3、3-4、3-5（测评相关）

**参考图位置**：
`/Users/a01/Desktop/触心产品营销/视频帧/`

**操作方法**：
1. 点击 "Upload Reference Image"
2. 选择对应的 jpg 文件
3. 调整 **Image Weight**（建议 0.6-0.8）
   - 越高越像参考图
   - 越低越自由发挥

---

## 📝 步骤 5：生成与下载

1. 点击 "Generate" 开始生成
2. 等待 5-8 分钟（队列时间）
3. 预览生成结果
4. 满意则点击 "Download" 下载
5. 不满意则调整 Prompt 重新生成

---

## 📝 步骤 6：批量生成技巧

**省钱技巧**：
1. 先用 **低分辨率** 测试 Prompt（1080p）
2. 确认效果后再用 **2K** 生成最终版
3. 相似镜头可以 **固定 Seed** 保持风格一致
4. 一次提交多个镜头（队列并行）

**时间估算**：
- 每个镜头：5-8 分钟
- 18 个镜头：约 1.5-2 小时（可并行）
- 建议分批次：每天生成 6 个，3 天完成

---

# 四、生成后处理

## 🎬 视频拼接

**工具**：剪映专业版（免费）

**步骤**：
1. 导入所有生成的 mp4 文件
2. 按脚本顺序排列
3. 添加转场（建议 0.3 秒淡入淡出）
4. 添加字幕（复制脚本中的中文台词）
5. 添加 BGM（剪映音乐库）
6. 导出 1080p 或 4K

---

## 🎵 BGM 推荐

| 视频类型 | 风格 | 剪映搜索关键词 |
|---------|------|--------------|
| 技术对比 | 科技感电子乐 | "科技"、"电子"、"未来" |
| 场景共鸣 | 温暖钢琴 + 轻电子 | "温暖"、"治愈"、"钢琴" |
| KOC 测评 | 轻松 Vlog 音乐 | "Vlog"、"日常"、"轻松" |

---

## 📱 字幕规范

| 项目 | 要求 |
|------|------|
| **字体** | 思源黑体 / 苹方（无衬线） |
| **大小** | 主字幕 48-60pt，角标 24-30pt |
| **颜色** | 白色 + 黑色描边（保证可读性） |
| **位置** | 底部居中（避开平台 UI） |
| **时长** | 每句 2-4 秒，与配音同步 |

---

# 五、成本估算

| 项目 | 数量 | 单价 | 小计 |
|------|------|------|------|
| 技术对比视频 | 9 个镜头 | $0.5/个 | $4.5 |
| 场景共鸣视频 | 7 个镜头 | $0.5/个 | $3.5 |
| KOC 测评视频 | 6 个镜头 | $0.5/个 | $3.0 |
| **总计** | 22 个镜头 | - | **$11（约 80 元）** |

**备注**：
- 按 Seedance 约 $0.1/秒估算
- 免费额度约 $5-10，基本够用
- 超出部分充值约 100 元

---

# 六、常见问题

## ❓ Q1: 手部生成容易变形怎么办？

**解决**：
1. Prompt 里加 `perfect hands, detailed fingers`
2. Negative Prompt 加 `deformed hands, extra fingers`
3. 用参考图（Image to Video 模式）
4. 多生成几次选最好的

---

## ❓ Q2: 中文字幕能直接生成吗？

**解决**：
- Seedance 不支持直接生成中文字幕
- 建议后期用剪映添加
- Prompt 里也不要放中文文字（会乱码）

---

## ❓ Q3: 生成视频太短怎么办？

**解决**：
- Seedance 单次最长 10 秒
- 长镜头拆分成多个 5 秒生成
- 后期用剪映拼接

---

## ❓ Q4: 风格不一致怎么办？

**解决**：
1. 固定同一个 **Seed** 值
2. 用相同的 **Reference Image**
3. Prompt 里加统一风格词（如 `cinematic, warm lighting`）
4. 后期用剪映统一调色

---

# 七、检查清单

生成前确认：
- [ ] 已注册 Seedance 账号
- [ ] 确认有免费额度
- [ ] 参考图已整理到文件夹
- [ ] Prompt 已复制（英文版本）
- [ ]  Negative Prompt 已设置

生成后确认：
- [ ] 视频已下载
- [ ] 质量检查（手部、质感、文字）
- [ ] 按脚本顺序命名文件
- [ ] 备份到云端

---

**文档版本**：v1.0  
**最后更新**：2026-03-04  
**下次更新**：根据实际生成效果优化

---

# 附录：Prompt 快速复制区

## 技术对比视频

```
# 镜头 1-1
Black background, white bold text appearing letter by letter, typewriter effect, minimalist tech vibe

# 镜头 1-2
Top down view, 5 pairs of black leather gloves arranged in a row on dark gray table, soft overhead lighting, slight side light highlighting leather texture, camera slowly pans left to right

# 镜头 1-3
Split screen comparison, left: microscope view of coated leather with cracks and peeling, right: conductive fibers woven into leather matrix, intact structure, scientific visualization

# 镜头 1-4
Sequence: gloves being placed into washing machine, water splashing, gloves taken out drying, gloved hand swiping smartphone screen

# 镜头 1-5
Split screen, left: coated glove only fingertip works on touchscreen, right: Touching glove full palm works anywhere, smartphone showing Xiaohongshu app

# 镜头 1-6
Patent certificate close-up, camera slowly zooms from top to patent number, warm side lighting with slight glossy reflection, Chinese text, official seal visible

# 镜头 1-7
Montage: gloves laid flat macro showing leather grain, stitching close-up with even needlework, metal logo close-up with reflection, hand picking up gloves showing softness

# 镜头 1-8
Black background, white text comparison: Dents 1500 yuan (gray) then Touching 869 yuan (bright), product image of Touching gloves at 45-degree angle on right

# 镜头 1-9
Black background, white Touching logo (infinity symbol + Chinese English) fading in, slogan appearing letter by letter below, minimalist clean ending
```

## 场景共鸣视频

```
# 镜头 2-1
Beijing subway platform, winter early morning, young woman in wool coat rubbing hands and breathing warm air, electronic display showing -10C, visible breath, frowning and shivering, medium shot with slight handheld shake, cold blue-gray tone

# 镜头 2-2
Smartphone screen close-up, WeChat notification Boss: Is the revised plan ready, woman looking at phone then at red frozen hands, hesitation, shallow depth of field, morning platform light

# 镜头 2-3
Fast cut split screen: left woman taking off gloves in cold wind, fingers frozen typing slowly, painful expression; right woman wearing Touching gloves smoothly swiping screen, relaxed

# 镜头 2-4
Touching gloves close-up, finger swiping smartphone screen, palm swipe, fingertip tap, fist swipe demonstrating full-palm touch, station ceiling light reflection, macro following finger

# 镜头 2-5
Woman walking into office taking off coat, colleague asking Aren't you cold, woman smiling My hands are warm, office with heating, snow outside window, warm indoor lighting

# 镜头 2-6
Black background, white text appearing line by line: 869 yuan, 120 days per winter, 7 yuan per day, minimalist typography, number animation

# 镜头 2-7
Woman wearing gloves walking out of subway station, sunlight on face smiling, warm color tone ending, hopeful atmosphere
```

## KOC 测评视频

```
# 镜头 3-1
KOC selfie view, indoor warm lighting, 25-30yo professional woman natural makeup, home background with bookshelf and plants, speaking to camera, vlog style

# 镜头 3-2
Fast cut unboxing: opening courier box, revealing black magnetic gift box with logo, taking out gloves with dust bag, anticipation and surprise expression, packaging close-ups

# 镜头 3-3
Gloves macro close-up, finger stroking leather showing grain, stitching detail, metal logo close-up, hands showing softness, high quality product inspection

# 镜头 3-4
Wearing gloves testing touchscreen, multiple actions: scrolling Xiaohongshu, tapping WeChat, pinch-to-zoom, fist swipe, surprised reaction, genuine excitement

# 镜头 3-5
Taking out old gloves (regular coated type) for comparison, old gloves only fingertip works, Touching full palm works, side-by-side comparison, clear visual contrast

# 镜头 3-6
Back to selfie view, sincere recommendation, waving bye at end, authentic KOC review style, warm and trustworthy
```

---

**祝生成顺利！有问题随时问我！** 🚀
