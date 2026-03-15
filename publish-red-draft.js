const fs = require('fs');
const https = require('https');

const appId = 'wxe5c761b6af8be413';
const appSecret = 'a21104b49ddb844188fc64fd44bb885c';

// 获取 access_token
function getAccessToken() {
  return new Promise((resolve, reject) => {
    const url = `https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=${appId}&secret=${appSecret}`;
    https.get(url, (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => {
        const result = JSON.parse(data);
        if (result.access_token) {
          resolve(result.access_token);
        } else {
          reject(new Error('Failed to get access_token: ' + data));
        }
      });
    }).on('error', reject);
  });
}

// 创建草稿（不带封面字段）
function createDraftMinimal(token, htmlContent) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      articles: [{
        title: '2026 年，AI Agent 的爆发元年',
        author: '智能体 LB',
        content: htmlContent
      }]
    });

    const options = {
      hostname: 'api.weixin.qq.com',
      port: 443,
      path: `/cgi-bin/draft/add?access_token=${token}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData)
      }
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => {
        const result = JSON.parse(data);
        resolve(result);
      });
    });

    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

// 执行
(async () => {
  try {
    console.log('正在获取 access_token...');
    const token = await getAccessToken();
    console.log('✓ access_token 获取成功');
    
    console.log('正在读取 HTML 内容...');
    const htmlContent = fs.readFileSync('/Users/a01/.openclaw/workspace/公众号文章-AI Agent 爆发 - 黑红主题.html', 'utf8');
    
    console.log('正在创建草稿（最小化参数）...');
    const result = await createDraftMinimal(token, htmlContent);
    
    if (result.media_id) {
      console.log('✅ 草稿创建成功！');
      console.log('Media ID:', result.media_id);
      console.log('请登录 https://mp.weixin.qq.com 查看草稿箱');
    } else {
      console.log('结果:', result);
      if (result.errcode) {
        console.log('错误码:', result.errcode);
        console.log('错误信息:', result.errmsg);
      }
    }
  } catch (error) {
    console.error('错误:', error.message);
    process.exit(1);
  }
})();
