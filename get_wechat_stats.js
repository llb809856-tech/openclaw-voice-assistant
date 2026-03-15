const https = require('https');

const APP_ID = 'wxe5c761b6af8be413';
const APP_SECRET = 'a21104b49ddb844188fc64fd44bb885c';

// 获取 access_token
async function getToken() {
  const url = `https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=${APP_ID}&secret=${APP_SECRET}`;
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        const result = JSON.parse(data);
        resolve(result.access_token);
      });
    }).on('error', reject);
  });
}

// 获取文章数据
async function getArticleStats(token) {
  const postData = JSON.stringify({
    begin: 0,
    count: 10,
    type: 'comm'
  });
  
  return new Promise((resolve, reject) => {
    const options = {
      hostname: 'api.weixin.qq.com',
      port: 443,
      path: `/cgi-bin/appmsg/get?access_token=${token}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData)
      }
    };
    
    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
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

// 获取用户分析（7 天）
async function getUserAnalysis(token) {
  const today = new Date();
  const endDate = today.toISOString().split('T')[0].replace(/-/g, '');
  const startDate = new Date(today - 7*24*60*60*1000).toISOString().split('T')[0].replace(/-/g, '');
  
  return new Promise((resolve, reject) => {
    https.get(`https://api.weixin.qq.com/datacube/getusersummary?access_token=${token}&begin_date=${startDate}&end_date=${endDate}`, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        resolve(JSON.parse(data));
      });
    }).on('error', reject);
  });
}

(async () => {
  try {
    console.log('📊 获取 access_token...\n');
    const token = await getToken();
    console.log('✓ Token 获取成功\n');
    
    console.log('📰 获取文章数据...');
    const articles = await getArticleStats(token);
    console.log(JSON.stringify(articles, null, 2));
    
    console.log('\n👥 获取用户分析...');
    const users = await getUserAnalysis(token);
    console.log(JSON.stringify(users, null, 2));
  } catch (error) {
    console.error('❌ 错误:', error.message);
  }
})();
