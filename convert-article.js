const fs = require('fs');
const path = require('path');

// 读取 Markdown 文件
const markdown = fs.readFileSync('公众号文章-QQ 机器人技术教程.md', 'utf8');

// 简单的 Markdown → HTML 转换
function markdownToHtml(md) {
  let html = md;
  
  // 标题
  html = html.replace(/^# (.+)$/gm, '<h1 style="font-size: 24px; font-weight: bold; margin: 24px 0 16px; color: #1a1a1a;">$1</h1>');
  html = html.replace(/^## (.+)$/gm, '<h2 style="font-size: 20px; font-weight: bold; margin: 20px 0 12px; color: #1a1a1a;">$1</h2>');
  html = html.replace(/^### (.+)$/gm, '<h3 style="font-size: 18px; font-weight: bold; margin: 16px 0 10px; color: #1a1a1a;">$1</h3>');
  
  // 引用块
  html = html.replace(/^> (.+)$/gm, '<blockquote style="border-left: 4px solid #00b894; padding: 12px 16px; margin: 16px 0; background: #f8f9fa; color: #555; font-style: italic;">$1</blockquote>');
  
  // 粗体
  html = html.replace(/\*\*(.+?)\*\*/g, '<strong style="font-weight: bold;">$1</strong>');
  
  // 代码块
  html = html.replace(/```(\w+)?\n([\s\S]*?)```/g, '<pre style="background: #2d2d2d; color: #f8f8f2; padding: 16px; border-radius: 6px; overflow-x: auto; margin: 16px 0; font-size: 14px; line-height: 1.6;"><code>$2</code></pre>');
  
  // 行内代码
  html = html.replace(/`([^`]+)`/g, '<code style="background: #f0f0f0; padding: 2px 6px; border-radius: 3px; font-size: 14px; color: #e96900;">$1</code>');
  
  // 列表
  html = html.replace(/^\s*[-*]\s+(.+)$/gm, '<li style="margin: 8px 0; padding-left: 8px;">$1</li>');
  html = html.replace(/(<li.*<\/li>\n?)+/g, '<ul style="padding-left: 20px; margin: 12px 0;">$&</ul>');
  
  // 表格
  html = html.replace(/^\|(.+)\|$/gm, '<tr>$1</tr>');
  html = html.replace(/<tr>(.*?)<\/tr>/g, (match, content) => {
    const cells = content.split('|').map(cell => cell.trim()).filter(cell => cell);
    const isHeader = cells[0].match(/^[-:]+$/);
    if (isHeader) return '';
    const htmlCells = cells.map((cell, i) => {
      if (i === 0 && cell.match(/^[#|]/)) return `<th style="border: 1px solid #ddd; padding: 10px; background: #f5f5f5; font-weight: bold;">${cell.replace(/^#+\s*/, '')}</th>`;
      return `<td style="border: 1px solid #ddd; padding: 10px;">${cell}</td>`;
    }).join('');
    return `<tr>${htmlCells}</tr>`;
  });
  html = html.replace(/(<tr.*<\/tr>\n?)+/g, '<table style="border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 15px;">$&</table>');
  
  // 分割线
  html = html.replace(/^---+$/gm, '<hr style="border: none; border-top: 2px solid #eee; margin: 24px 0;">');
  
  // 段落
  html = html.replace(/\n\n/g, '</p><p style="margin: 16px 0; line-height: 1.8; font-size: 16px; color: #333;">');
  
  // 包装
  html = '<p style="margin: 16px 0; line-height: 1.8; font-size: 16px; color: #333;">' + html + '</p>';
  
  // 清理多余的空段落
  html = html.replace(/<p\s*style="[^"]*">\s*<\/p>/g, '');
  html = html.replace(/<p\s*style="[^"]*">\s*<\/p>/g, '');
  
  return html;
}

const htmlContent = markdownToHtml(markdown);

// 完整的 HTML 文档
const fullHtml = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>技术教程 | OpenClaw+QQ 机器人部署指南</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: #333;
      max-width: 677px;
      margin: 0 auto;
      padding: 20px;
      background: #fff;
    }
    h1, h2, h3 {
      color: #1a1a1a;
    }
    code {
      font-family: "Courier New", Courier, monospace;
    }
    pre {
      overflow-x: auto;
    }
    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 10px;
      text-align: left;
    }
    th {
      background: #f5f5f5;
      font-weight: bold;
    }
  </style>
</head>
<body>
${htmlContent}
</body>
</html>`;

// 写入文件
fs.writeFileSync('公众号文章-QQ 机器人技术教程.html', fullHtml, 'utf8');
console.log('✅ HTML 生成成功：公众号文章-QQ 机器人技术教程.html');
