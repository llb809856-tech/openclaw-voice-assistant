import React, { useState, useEffect } from 'react';
import Dashboard from './components/Dashboard';
import './App.css';

function App() {
  const [agents, setAgents] = useState([
    {
      id: 1,
      name: '小林',
      avatar: '🤖',
      status: 'thinking',
      progress: 75,
      tokenUsed: 234,
      tokenRemaining: 80,
      task: '发送 AI 大模型日报'
    },
    {
      id: 2,
      name: '爬虫',
      avatar: '🕷️',
      status: 'working',
      progress: 45,
      tokenUsed: 567,
      tokenRemaining: 60,
      task: '抓取竞品价格数据'
    },
    {
      id: 3,
      name: '分析',
      avatar: '📊',
      status: 'idle',
      progress: 100,
      tokenUsed: 89,
      tokenRemaining: 95,
      task: '待命中'
    },
    {
      id: 4,
      name: '写作',
      avatar: '✍️',
      status: 'working',
      progress: 60,
      tokenUsed: 123,
      tokenRemaining: 85,
      task: '撰写短视频脚本'
    },
    {
      id: 5,
      name: '客服',
      avatar: '💬',
      status: 'idle',
      progress: 100,
      tokenUsed: 45,
      tokenRemaining: 90,
      task: '待命中'
    }
  ]);

  const [logs, setLogs] = useState([
    { time: '14:32', agent: '小林', avatar: '🤖', action: '完成了 AI 日报发送任务', type: 'success' },
    { time: '14:30', agent: '爬虫', avatar: '🕷️', action: '开始抓取竞品数据', type: 'info' },
    { time: '14:28', agent: '分析', avatar: '📊', action: '生成了销售报告', type: 'success' },
    { time: '14:25', agent: '写作', avatar: '✍️', action: '完成了短视频脚本', type: 'success' },
    { time: '14:20', agent: '客服', avatar: '💬', action: '回复了客户咨询', type: 'info' }
  ]);

  // 模拟实时数据更新
  useEffect(() => {
    const interval = setInterval(() => {
      setAgents(prev => prev.map(agent => {
        if (agent.status === 'working' || agent.status === 'thinking') {
          return {
            ...agent,
            progress: Math.min(100, agent.progress + Math.random() * 5),
            tokenUsed: agent.tokenUsed + Math.floor(Math.random() * 10),
            tokenRemaining: Math.max(0, agent.tokenRemaining - Math.random() * 2)
          };
        }
        return agent;
      }));
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  const stats = {
    tokenTotal: agents.reduce((sum, a) => sum + a.tokenUsed, 0),
    tasksCompleted: logs.filter(l => l.type === 'success').length,
    runningAgents: agents.filter(a => a.status === 'working' || a.status === 'thinking').length,
    totalAgents: agents.length
  };

  return (
    <div className="App">
      <Dashboard 
        agents={agents} 
        logs={logs} 
        stats={stats}
      />
    </div>
  );
}

export default App;
