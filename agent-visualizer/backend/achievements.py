"""
成就系统模块
管理 Agent 的成就、徽章、等级和皮肤
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
from enum import Enum

class AchievementType(Enum):
    """成就类型"""
    WORK连续 = "work_streak"  # 连续工作
    TOKEN_SAVE = "token_save"  # 节省 Token
    EFFICIENCY = "efficiency"  # 高效率
    TASK_COUNT = "task_count"  # 任务数量
    PERFECT = "perfect"  # 无错误

# 成就数据库
ACHIEVEMENTS_DB = [
    {
        "id": 1,
        "name": "勤劳小蜜蜂",
        "icon": "🏆",
        "description": "连续工作 7 天",
        "type": AchievementType.WORK连续.value,
        "condition": {"days": 7},
        "rarity": "common",  # common, rare, epic, legendary
        "reward": {"experience": 100, "badge": True}
    },
    {
        "id": 2,
        "name": "省钱能手",
        "icon": "💰",
        "description": "单日节省 10 万 Token",
        "type": AchievementType.TOKEN_SAVE.value,
        "condition": {"tokens_saved": 100000},
        "rarity": "rare",
        "reward": {"experience": 200, "badge": True, "skin_unlock": "gold"}
    },
    {
        "id": 3,
        "name": "效率之王",
        "icon": "🚀",
        "description": "任务完成速度 TOP 1",
        "type": AchievementType.EFFICIENCY.value,
        "condition": {"rank": 1},
        "rarity": "epic",
        "reward": {"experience": 500, "badge": True, "skin_unlock": "speed"}
    },
    {
        "id": 4,
        "name": "学习达人",
        "icon": "📚",
        "description": "完成 100 个任务",
        "type": AchievementType.TASK_COUNT.value,
        "condition": {"tasks": 100},
        "rarity": "rare",
        "reward": {"experience": 300, "badge": True, "accessory": "hat"}
    },
    {
        "id": 5,
        "name": "完美主义",
        "icon": "🎯",
        "description": "连续 10 次无错误",
        "type": AchievementType.PERFECT.value,
        "condition": {"streak": 10},
        "rarity": "epic",
        "reward": {"experience": 400, "badge": True, "effect": "halo"}
    },
    {
        "id": 6,
        "name": "传奇特工",
        "icon": "👑",
        "description": "完成 1000 个任务",
        "type": AchievementType.TASK_COUNT.value,
        "condition": {"tasks": 1000},
        "rarity": "legendary",
        "reward": {"experience": 2000, "badge": True, "skin_unlock": "legendary", "title": "传奇"}
    }
]

# 皮肤数据库
SKINS_DB = [
    {
        "id": "default",
        "name": "默认",
        "icon": "🤖",
        "rarity": "default",
        "price": 0,
        "description": "默认形象"
    },
    {
        "id": "gold",
        "name": "黄金",
        "icon": "🤖",
        "rarity": "rare",
        "price": 999,
        "color": "#FFD700",
        "description": "金色涂装，闪耀夺目"
    },
    {
        "id": "speed",
        "name": "极速",
        "icon": "⚡",
        "rarity": "epic",
        "price": 1999,
        "color": "#00BFFF",
        "effect": "speed_trail",
        "description": "蓝色闪电，速度加成"
    },
    {
        "id": "legendary",
        "name": "传奇",
        "icon": "👑",
        "rarity": "legendary",
        "price": 9999,
        "color": "#FF1493",
        "effect": "legendary_aura",
        "description": "传奇专属，独一无二"
    },
    {
        "id": "hacker",
        "name": "黑客",
        "icon": "💻",
        "rarity": "rare",
        "price": 1499,
        "color": "#00FF00",
        "description": "绿色代码雨效果"
    },
    {
        "id": "ninja",
        "name": "忍者",
        "icon": "🥷",
        "rarity": "epic",
        "price": 2499,
        "color": "#2C2C2C",
        "effect": "shadow_trail",
        "description": "暗影忍者，来去无踪"
    }
]

class AchievementSystem:
    """成就系统管理器"""
    
    def __init__(self):
        self.agent_stats = {}  # Agent 统计数据
    
    def init_agent_stats(self, agent_id: str):
        """初始化 Agent 统计"""
        self.agent_stats[agent_id] = {
            "level": 1,
            "experience": 0,
            "tasks_completed": 0,
            "tokens_used": 0,
            "tokens_saved": 0,
            "work_streak": 0,
            "perfect_streak": 0,
            "achievements": [],
            "unlocked_skins": ["default"],
            "current_skin": "default",
            "badges": [],
            "accessories": [],
            "effects": [],
            "title": None
        }
    
    def add_experience(self, agent_id: str, exp: int):
        """增加经验值"""
        if agent_id not in self.agent_stats:
            self.init_agent_stats(agent_id)
        
        stats = self.agent_stats[agent_id]
        stats["experience"] += exp
        
        # 升级逻辑
        level_up_threshold = stats["level"] * 100
        if stats["experience"] >= level_up_threshold:
            stats["level"] += 1
            stats["experience"] -= level_up_threshold
            return True  # 升级了
        
        return False
    
    def complete_task(self, agent_id: str, tokens_used: int, success: bool = True):
        """完成任务"""
        if agent_id not in self.agent_stats:
            self.init_agent_stats(agent_id)
        
        stats = self.agent_stats[agent_id]
        stats["tasks_completed"] += 1
        stats["tokens_used"] += tokens_used
        
        if success:
            stats["perfect_streak"] += 1
        else:
            stats["perfect_streak"] = 0
        
        # 检查成就
        new_achievements = self.check_achievements(agent_id)
        
        return new_achievements
    
    def check_achievements(self, agent_id: str) -> List[Dict]:
        """检查是否达成新成就"""
        stats = self.agent_stats[agent_id]
        new_achievements = []
        
        for achievement in ACHIEVEMENTS_DB:
            if achievement["id"] in [a["id"] for a in stats["achievements"]]:
                continue  # 已经获得
            
            condition = achievement["condition"]
            achieved = False
            
            # 检查条件
            if achievement["type"] == AchievementType.TASK_COUNT.value:
                achieved = stats["tasks_completed"] >= condition.get("tasks", 999999)
            elif achievement["type"] == AchievementType.WORK_STREAK.value:
                achieved = stats["work_streak"] >= condition.get("days", 999999)
            elif achievement["type"] == AchievementType.TOKEN_SAVE.value:
                achieved = stats["tokens_saved"] >= condition.get("tokens_saved", 999999)
            elif achievement["type"] == AchievementType.PERFECT.value:
                achieved = stats["perfect_streak"] >= condition.get("streak", 999999)
            
            if achieved:
                # 获得成就
                stats["achievements"].append({
                    "id": achievement["id"],
                    "unlocked_at": datetime.now().isoformat()
                })
                stats["badges"].append(achievement["icon"])
                
                # 发放奖励
                reward = achievement["reward"]
                self.add_experience(agent_id, reward.get("experience", 0))
                
                if reward.get("skin_unlock"):
                    if reward["skin_unlock"] not in stats["unlocked_skins"]:
                        stats["unlocked_skins"].append(reward["skin_unlock"])
                
                if reward.get("accessory"):
                    if reward["accessory"] not in stats["accessories"]:
                        stats["accessories"].append(reward["accessory"])
                
                if reward.get("effect"):
                    if reward["effect"] not in stats["effects"]:
                        stats["effects"].append(reward["effect"])
                
                if reward.get("title"):
                    stats["title"] = reward["title"]
                
                new_achievements.append(achievement)
        
        return new_achievements
    
    def get_agent_profile(self, agent_id: str) -> Dict:
        """获取 Agent 档案"""
        if agent_id not in self.agent_stats:
            self.init_agent_stats(agent_id)
        
        return self.agent_stats[agent_id]
    
    def unlock_skin(self, agent_id: str, skin_id: str) -> bool:
        """解锁皮肤"""
        if agent_id not in self.agent_stats:
            self.init_agent_stats(agent_id)
        
        stats = self.agent_stats[agent_id]
        
        # 检查是否有这个皮肤
        skin = next((s for s in SKINS_DB if s["id"] == skin_id), None)
        if not skin:
            return False
        
        # 检查是否已经解锁
        if skin_id in stats["unlocked_skins"]:
            return False
        
        # 检查是否有足够的 Token（简化处理，假设用虚拟货币）
        # 实际应该用积分或成就点数
        
        # 解锁
        stats["unlocked_skins"].append(skin_id)
        return True
    
    def set_skin(self, agent_id: str, skin_id: str) -> bool:
        """设置当前皮肤"""
        if agent_id not in self.agent_stats:
            return False
        
        stats = self.agent_stats[agent_id]
        
        if skin_id not in stats["unlocked_skins"]:
            return False
        
        stats["current_skin"] = skin_id
        return True
    
    def get_all_achievements(self) -> List[Dict]:
        """获取所有成就"""
        return ACHIEVEMENTS_DB
    
    def get_all_skins(self) -> List[Dict]:
        """获取所有皮肤"""
        return SKINS_DB


# 测试
if __name__ == "__main__":
    system = AchievementSystem()
    
    # 初始化 Agent
    system.init_agent_stats("agent_1")
    
    # 模拟完成任务
    for i in range(10):
        system.complete_task("agent_1", 1000, success=True)
    
    # 查看档案
    profile = system.get_agent_profile("agent_1")
    print(f"等级：{profile['level']}")
    print(f"经验：{profile['experience']}")
    print(f"完成任务：{profile['tasks_completed']}")
    print(f"成就：{len(profile['achievements'])}")
    print(f"徽章：{profile['badges']}")
