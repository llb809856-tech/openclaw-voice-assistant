import React, { useState } from 'react';
import './SkinShop.css';

// 皮肤数据
const SKINS = [
  {
    id: 'default',
    name: '默认',
    icon: '🤖',
    rarity: 'default',
    price: 0,
    color: '#667eea',
    description: '默认形象'
  },
  {
    id: 'gold',
    name: '黄金',
    icon: '🤖',
    rarity: 'rare',
    price: 999,
    color: '#FFD700',
    description: '金色涂装，闪耀夺目'
  },
  {
    id: 'speed',
    name: '极速',
    icon: '⚡',
    rarity: 'epic',
    price: 1999,
    color: '#00BFFF',
    description: '蓝色闪电，速度加成'
  },
  {
    id: 'legendary',
    name: '传奇',
    icon: '👑',
    rarity: 'legendary',
    price: 9999,
    color: '#FF1493',
    description: '传奇专属，独一无二'
  },
  {
    id: 'hacker',
    name: '黑客',
    icon: '💻',
    rarity: 'rare',
    price: 1499,
    color: '#00FF00',
    description: '绿色代码雨效果'
  },
  {
    id: 'ninja',
    name: '忍者',
    icon: '🥷',
    rarity: 'epic',
    price: 2499,
    color: '#2C2C2C',
    description: '暗影忍者，来去无踪'
  }
];

const rarityColors = {
  default: '#9CA3AF',
  common: '#10B981',
  rare: '#3B82F6',
  epic: '#8B5CF6',
  legendary: '#F59E0B'
};

export default function SkinShop({ agent, onPurchase, onSelect }) {
  const [selectedSkin, setSelectedSkin] = useState(agent?.currentSkin || 'default');
  const [unlockedSkins, setUnlockedSkins] = useState(['default']);
  const [currency, setCurrency] = useState(15000); // 模拟货币
  
  const handlePurchase = (skin) => {
    if (currency >= skin.price && !unlockedSkins.includes(skin.id)) {
      setUnlockedSkins([...unlockedSkins, skin.id]);
      setCurrency(currency - skin.price);
      if (onPurchase) onPurchase(skin);
    }
  };
  
  const handleSelect = (skinId) => {
    if (unlockedSkins.includes(skinId)) {
      setSelectedSkin(skinId);
      if (onSelect) onSelect(skinId);
    }
  };
  
  return (
    <div className="skin-shop">
      {/* 顶部信息 */}
      <div className="shop-header">
        <h2>🛍️ 皮肤商城</h2>
        <div className="currency">
          <span className="currency-icon">💎</span>
          <span className="currency-amount">{currency.toLocaleString()}</span>
        </div>
      </div>
      
      {/* 当前装备 */}
      <div className="current-skin">
        <h3>当前装备</h3>
        <div className="skin-preview">
          {SKINS.find(s => s.id === selectedSkin)?.icon || '🤖'}
          <span className="skin-name">
            {SKINS.find(s => s.id === selectedSkin)?.name || '默认'}
          </span>
        </div>
      </div>
      
      {/* 皮肤列表 */}
      <div className="skins-grid">
        {SKINS.map(skin => {
          const isUnlocked = unlockedSkins.includes(skin.id);
          const isSelected = selectedSkin === skin.id;
          const canAfford = currency >= skin.price;
          
          return (
            <div
              key={skin.id}
              className={`skin-card rarity-${skin.rarity} ${isSelected ? 'selected' : ''} ${!isUnlocked ? 'locked' : ''}`}
              onClick={() => isUnlocked ? handleSelect(skin.id) : handlePurchase(skin)}
            >
              {/* 稀有度边框 */}
              <div className="rarity-border" style={{ borderColor: rarityColors[skin.rarity] }} />
              
              {/* 皮肤预览 */}
              <div className="skin-icon" style={{ color: skin.color }}>
                {skin.icon}
              </div>
              
              {/* 信息 */}
              <div className="skin-info">
                <h4 className="skin-name">{skin.name}</h4>
                <p className="skin-description">{skin.description}</p>
                
                {/* 状态 */}
                {isUnlocked ? (
                  <div className="status unlocked">
                    {isSelected ? '✓ 已装备' : '点击装备'}
                  </div>
                ) : (
                  <div className={`status locked ${canAfford ? 'can-afford' : ''}`}>
                    💎 {skin.price.toLocaleString()}
                    {!canAfford && ' (金币不足)'}
                  </div>
                )}
              </div>
              
              {/* 稀有度标签 */}
              <div className="rarity-badge" style={{ background: rarityColors[skin.rarity] }}>
                {skin.rarity.toUpperCase()}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
