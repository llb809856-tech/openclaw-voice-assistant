# Learnings

Corrections, insights, and knowledge gaps captured during development.

**Categories**: correction | insight | knowledge_gap | best_practice
**Areas**: frontend | backend | infra | tests | docs | config
**Statuses**: pending | in_progress | resolved | wont_fix | promoted | promoted_to_skill

## Status Definitions

| Status | Meaning |
|--------|---------|
| `pending` | Not yet addressed |
| `in_progress` | Actively being worked on |
| `resolved` | Issue fixed or knowledge integrated |
| `wont_fix` | Decided not to address (reason in Resolution) |
| `promoted` | Elevated to CLAUDE.md, AGENTS.md, or copilot-instructions.md |
| `promoted_to_skill` | Extracted as a reusable skill |

## Skill Extraction Fields

When a learning is promoted to a skill, add these fields:

```markdown
**Status**: promoted_to_skill
**Skill-Path**: skills/skill-name
```

Example:
```markdown
## [LRN-20250115-001] best_practice

**Logged**: 2025-01-15T10:00:00Z
**Priority**: high
**Status**: promoted_to_skill
**Skill-Path**: skills/docker-m1-fixes
**Area**: infra

### Summary
Docker build fails on Apple Silicon due to platform mismatch
...
```

---

## [LRN-20260305-001] correction

**Logged**: 2026-03-05T11:29:00+08:00
**Priority**: high
**Status**: pending
**Category**: correction
**Area**: content

### Summary
用户反馈广告内容审美不够、缺乏创新

### Details
- 用户原话："我想让你做广告的审美有点提升该怎么搞，我觉得你现在拍的广告太没创新了"
- 问题：内容创作过于模板化，缺少视觉冲击力和创意
- 影响：可能导致视频完播率低、转化率差

### Suggested Action
1. 研究竞品爆款视频的视觉风格、节奏、转场
2. 引入更多创意元素（故事线、反差、情绪共鸣）
3. 提升画面质感（灯光、构图、配色）
4. 参考小红书/抖音高赞内容的审美趋势
5. **保留专业术语和品牌调性** — 不要为了"去 AI 味"牺牲格调

### Metadata
- Source: user_feedback
- Related Files: 电商内容包 - 家居日用.md, 触心 TOUCHING 手套_多平台营销内容.md
- Tags: 内容创作，审美，创新，视频质量

### Resolution
- **Resolved**: 2026-03-05T11:35:00+08:00
- **Output**: `2026 短视频审美调研报告 - 触心手套.md`
- **Notes**: 完成审美调研，输出完整报告包含：莫兰迪配色方案、灯光构图指南、4 种爆款脚本结构、创意 Checklist、竞品参考

---

## [LRN-20260305-002] insight

**Logged**: 2026-03-05T11:48:00+08:00
**Priority**: medium
**Status**: resolved
**Category**: insight
**Area**: content

### Summary
humanizer skill 需要保留专业术语，不能为了"去 AI 味"牺牲格调

### Details
- 用户反馈：专业术语其实有格调，不想要全部白话
- 问题：humanizer 可能过度修改，删掉提升高级感的技术词
- 解决：修改 skill 规则，明确保留专利、材质、工艺等专业术语

### Suggested Action
- 生成内容后选择性使用 humanizer
- 产品详情页保留专业术语
- 客服话术/小红书笔记可以用 humanizer 优化

### Metadata
- Source: user_feedback
- Related Files: humanizer/SKILL.md
- Tags: humanizer, 专业术语，品牌调性，内容质量

### Resolution
- **Resolved**: 2026-03-05T11:48:00+08:00
- **Notes**: humanizer 已安装并修改规则，添加「保留专业术语」章节，明确什么该留什么该删

---

## [LRN-20260305-003] insight

**Logged**: 2026-03-05T12:49:00+08:00
**Priority**: high
**Status**: resolved
**Category**: insight
**Area**: content

### Summary
拍摄场景需要符合真实使用习惯 — 手套主要在室外戴，室内场景不合理

### Details
- 用户指出：正常人不会在室内戴手套（咖啡厅、会议室场景不真实）
- 问题：AI 拍摄脚本中设计了咖啡厅、会议室等室内场景
- 洞察：手套是室外用品，室内戴手套不符合生活习惯

### Suggested Action
修正拍摄场景：
- ❌ 避免：咖啡厅内、会议室内、办公室内
- ✅ 推荐：街道、地铁口、停车场、进出门口、车内、室外步行街

### Metadata
- Source: user_feedback
- Related Files: 触心手套 AI 拍摄脚本 - Dents 风格.md
- Tags: 场景设计，用户习惯，真实性，拍摄脚本

### Resolution
- **Resolved**: 2026-03-05T12:50:00+08:00
- **Notes**: 已修正脚本 2 和脚本 8，改为室外/过渡场景

---

