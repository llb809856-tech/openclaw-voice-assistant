import React from 'react';
import AgentCard from './AgentCard';
import ActivityLog from './ActivityLog';
import './Dashboard.css';

function Dashboard({ agents, logs, stats }) {
  return (
    <div className="dashboard">
      {/* 顶部导航 */}
      <header className="dashboard-header">
        <div className="logo">
          <span className="logo-icon">🌌</span>
          <h1>Agent 基地</h1>
        </div>
        <div className="header-actions">
          <button className="icon-btn">🔔</button>
          <button className="icon-btn">⚙️</button>
        </div>
      </header>

      {/* 统计卡片 */}
      <section className="stats-section">
        <div className="stats-grid">
          <div className="stat-card">
            <div className="stat-icon">💰</div>
            <div className="stat-info">
              <div className="stat-label">Token 消耗</div>
              <div className="stat-value">¥{stats.tokenTotal.toLocaleString()}</div>
            </div>
          </div>
          <div className="stat-card">
            <div className="stat-icon">✅</div>
            <div className="stat-info">
              <div className="stat-label">任务完成</div>
              <div className="stat-value">{stats.tasksCompleted}</div>
            </div>
          </div>
          <div className="stat-card">
            <div className="stat-icon">🟢</div>
            <div className="stat-info">
              <div className="stat-label">运行中</div>
              <div className="stat-value">{stats.runningAgents}/{stats.totalAgents}</div>
            </div>
          </div>
          <div className="stat-card">
            <div className="stat-icon">⚡</div>
            <div className="stat-info">
              <div className="stat-label">效率</div>
              <div className="stat-value">98%</div>
            </div>
          </div>
        </div>
      </section>

      {/* Agent 团队 */}
      <section className="agents-section">
        <h2 className="section-title">🤖 Agent 团队</h2>
        <div className="agents-grid">
          {agents.map(agent => (
            <AgentCard key={agent.id} agent={agent} />
          ))}
        </div>
      </section>

      {/* 活动日志 */}
      <section className="logs-section">
        <h2 className="section-title">📜 活动日志</h2>
        <ActivityLog logs={logs} />
      </section>
    </div>
  );
}

export default Dashboard;
