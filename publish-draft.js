const fs = require('fs');
const https = require('https');

const appId = 'wxe5c761b6af8be413';
const appSecret = 'a21104b49ddb844188fc64fd44bb885c';

// 1. 获取 access_token
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

// 2. 上传临时素材（封面图）
function uploadMedia(token, imagePath) {
  return new Promise((resolve, reject) => {
    const boundary = '----WebKitFormBoundary' + Math.random().toString(36).substring(2);
    const fileData = fs.readFileSync(imagePath);
    
    let postData = '';
    postData += '--' + boundary + '\r\n';
    postData += 'Content-Disposition: form-data; name="media"; filename="cover.jpg"\r\n';
    postData += 'Content-Type: image/jpeg\r\n\r\n';
    postData += fileData.toString('binary') + '\r\n';
    postData += '--' + boundary + '--\r\n';

    const options = {
      hostname: 'api.weixin.qq.com',
      port: 443,
      path: `/cgi-bin/media/upload?access_token=${token}&type=image`,
      method: 'POST',
      headers: {
        'Content-Type': 'multipart/form-data; boundary=' + boundary,
        'Content-Length': Buffer.byteLength(postData, 'binary')
      }
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => {
        const result = JSON.parse(data);
        if (result.media_id) {
          resolve(result.media_id);
        } else {
          reject(new Error('Failed to upload media: ' + data));
        }
      });
    });

    req.on('error', reject);
    req.write(postData, 'binary');
    req.end();
  });
}

// 3. 创建草稿
function createDraft(token, content, thumbMediaId) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      articles: [{
        title: '2026 年，AI Agent 的爆发元年',
        author: '智能体 LB',
        content: content,
        content_source_url: '',
        thumb_media_id: thumbMediaId,
        show_cover_pic: 1,
        need_open_comment: 0,
        only_fans_can_comment: 0
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
        if (result.media_id) {
          resolve(result);
        } else {
          reject(new Error('Failed to create draft: ' + data));
        }
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
    
    // 创建一个简单的封面图（或者用现有图片）
    // 这里先用一个占位图 URL，实际应该上传图片
    console.log('注意：需要封面图片，请提供一个图片路径或 URL');
    console.log('跳过封面上传，直接创建草稿（不带封面）...');
    
    // 读取 HTML 内容
    const htmlContent = fs.readFileSync('/Users/a01/.openclaw/workspace/公众号文章-AI Agent 爆发 - 格式化版.html', 'utf8');
    
    // 尝试不带封面创建
    const postData = JSON.stringify({
      articles: [{
        title: '2026 年，AI Agent 的爆发元年',
        author: '智能体 LB',
        content: htmlContent,
        content_source_url: '',
        thumb_media_id: '',
        show_cover_pic: 0,
        need_open_comment: 0,
        only_fans_can_comment: 0
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

    const result = await new Promise((resolve, reject) => {
      const req = https.request(options, (res) => {
        let data = '';
        res.on('data', (chunk) => data += chunk);
        res.on('end', () => {
          resolve(JSON.parse(data));
        });
      });
      req.on('error', reject);
      req.write(postData);
      req.end();
    });

    if (result.media_id) {
      console.log('✓ 草稿创建成功！');
      console.log('Media ID:', result.media_id);
    } else {
      console.log('结果:', result);
    }
  } catch (error) {
    console.error('错误:', error.message);
    process.exit(1);
  }
})();
