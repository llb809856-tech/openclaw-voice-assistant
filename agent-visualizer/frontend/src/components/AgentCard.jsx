import React from 'react';
import './AgentCard.css';

function AgentCard({ agent }) {
  const statusConfig = {
    idle: { label: '空闲', color: 'green', emoji: '😴' },
    thinking: { label: '思考中', color: 'blue', emoji: '🤔' },
    working: { label: '工作中', color: 'yellow', emoji: '💪' },
    error: { label: '错误', color: 'red', emoji: '😵' },
    offline: { label: '离线', color: 'gray', emoji: '💤' }
  };

  const status = statusConfig[agent.status] || statusConfig.idle;
  
  const getTokenColor = (remaining) => {
    if (remaining >= 50) return 'green';
    if (remaining >= 20) return 'yellow';
    return 'red';
  };

  const tokenColor = getTokenColor(agent.tokenRemaining);

  return (
    <div className={`agent-card status-${status.color}`}>
      {/* Avatar 区域 */}
      <div className="agent-avatar">
        <div className="avatar-emoji">{agent.avatar}</div>
        <div className="status-indicator">
          {status.emoji}
        </div>
      </div>

      {/* 基本信息 */}
      <div className="agent-info">
        <h3 className="agent-name">{agent.name}</h3>
        <p className="agent-status">{status.label}</p>
        <p className="agent-task">{agent.task}</p>
      </div>

      {/* 进度条 */}
      <div className="agent-progress">
        <div className="progress-label">
          <span>⚡ 进度</span>
          <span>{Math.round(agent.progress)}%</span>
        </div>
        <div className="progress-bar">
          <div 
            className="progress-fill" 
            style={{ width: `${agent.progress}%` }}
          />
        </div>
      </div>

      {/* Token 信息 */}
      <div className="agent-tokens">
        <div className="token-item">
          <span className="token-icon">💰</span>
          <span className="token-value">{agent.tokenUsed}</span>
        </div>
        <div className="token-item">
          <span className={`token-icon token-${tokenColor}`}>❤️</span>
          <span className="token-value">{Math.round(agent.tokenRemaining)}%</span>
        </div>
      </div>
    </div>
  );
}

export default AgentCard;
