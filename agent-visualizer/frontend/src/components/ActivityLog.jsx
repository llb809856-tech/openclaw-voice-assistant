import React from 'react';
import './ActivityLog.css';

function ActivityLog({ logs }) {
  const typeConfig = {
    success: { icon: '✅', class: 'log-success' },
    info: { icon: 'ℹ️', class: 'log-info' },
    warning: { icon: '⚠️', class: 'log-warning' },
    error: { icon: '❌', class: 'log-error' }
  };

  return (
    <div className="activity-log">
      {logs.map((log, index) => {
        const config = typeConfig[log.type] || typeConfig.info;
        return (
          <div key={index} className={`log-item ${config.class}`}>
            <span className="log-time">{log.time}</span>
            <span className="log-agent">{log.avatar} {log.agent}</span>
            <span className="log-action">{log.action}</span>
          </div>
        );
      })}
    </div>
  );
}

export default ActivityLog;
