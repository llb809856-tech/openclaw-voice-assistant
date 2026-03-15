# Errors

Command failures, exceptions, and unexpected errors captured during development.

**Areas**: frontend | backend | infra | tests | docs | config
**Statuses**: pending | in_progress | resolved | wont_fix

---

## [ERR-20260305-001] product-info

**Logged**: 2026-03-05T12:00:00+08:00
**Priority**: high
**Status**: resolved
**Area**: content

### Summary
AI 拍摄脚本中手套颜色写成米白色，实际产品只有黑色款

### Error
- 脚本 1-8 全部使用了 "beige"、"light beige"、"米白色"
- 实际产品：触心 TOUCHING 全掌触屏手套只有黑色款

### Context
- 生成 AI 拍摄脚本时未确认产品颜色
- MEMORY.md 中未明确记录颜色信息
- 默认假设了女款常用色

### Suggested Fix
- 立即修正所有脚本中的颜色描述
- 在 MEMORY.md 中补充产品详细信息
- 生成内容前必须确认产品基础信息

### Metadata
- Reproducible: yes
- Related Files: 触心手套 AI 拍摄脚本 - Dents 风格.md, MEMORY.md

---

