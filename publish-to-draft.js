#!/usr/bin/env node

const fs = require('fs');
const https = require('https');

const CONFIG = {
  appId: 'wxe5c761b6af8be413',
  appSecret: 'a21104b49ddb844188fc64fd44bb885c',
  htmlPath: '/Users/a01/.openclaw/workspace/公众号文章 - 纯内联样式.html',
  coverPath: '/Users/a01/.openclaw/workspace/cover-test.png',
  title: '2026 年，AI Agent 的爆发元年',
  author: '智能体 LB'
};

// 获取 access_token
async function getAccessToken() {
  const url = `https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=${CONFIG.appId}&secret=${CONFIG.appSecret}`;
  
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => {
        const result = JSON.parse(data);
        if (result.access_token) {
          resolve(result.access_token);
        } else {
          reject(new Error('获取 access_token 失败：' + data));
        }
      });
    }).on('error', reject);
  });
}

// 上传封面图
async function uploadCover(token) {
  console.log(`检查封面图：${CONFIG.coverPath}`);
  if (!fs.existsSync(CONFIG.coverPath)) {
    console.log('⚠️ 封面图不存在');
    return null;
  }
  console.log('✓ 封面图文件存在');
  
  const imageBuffer = fs.readFileSync(CONFIG.coverPath);
  console.log(`✓ 封面图大小：${imageBuffer.length} bytes`);
  
  const boundary = '----WebKitFormBoundary' + Math.random().toString(36).substring(2);
  
  let postData = '';
  postData += '--' + boundary + '\r\n';
  postData += 'Content-Disposition: form-data; name="media"; filename="cover.png"\r\n';
  postData += 'Content-Type: image/png\r\n\r\n';
  
  return new Promise((resolve) => {
    const options = {
      hostname: 'api.weixin.qq.com',
      port: 443,
      path: `/cgi-bin/media/upload?access_token=${token}&type=image`,
      method: 'POST',
      headers: {
        'Content-Type': 'multipart/form-data; boundary=' + boundary,
      }
    };
    
    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => {
        console.log(`微信 API 返回：${data}`);
        try {
          const result = JSON.parse(data);
          if (result.media_id) {
            resolve(result.media_id);
          } else if (result.errcode) {
            console.log(`上传错误：${result.errmsg}`);
            resolve(null);
          } else {
            resolve(null);
          }
        } catch (e) {
          console.log(`解析错误：${e.message}`);
          resolve(null);
        }
      });
    });
    
    req.on('error', (e) => {
      console.log(`请求错误：${e.message}`);
      resolve(null);
    });
    req.write(Buffer.from(postData, 'binary'));
    req.write(imageBuffer);
    req.write(Buffer.from('\r\n--' + boundary + '--\r\n', 'binary'));
    req.end();
  });
}

// 创建草稿
async function createDraft(token, content, thumbMediaId) {
  const article = {
    title: CONFIG.title,
    author: CONFIG.author,
    content: content,
    thumb_media_id: thumbMediaId,  // 必填！
    show_cover_pic: 1
  };
  
  const postData = JSON.stringify({
    articles: [article]
  });
  
  return new Promise((resolve, reject) => {
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

// 主函数
(async () => {
  console.log('🚀 发布到公众号草稿箱...\n');
  
  try {
    // 1. 读取 HTML
    console.log('📄 读取 HTML...');
    const html = fs.readFileSync(CONFIG.htmlPath, 'utf8');
    console.log('✓ HTML 读取成功\n');
    
    // 2. 获取 Token
    console.log('🔑 获取 access_token...');
    const token = await getAccessToken();
    console.log('✓ access_token 获取成功\n');
    
    // 3. 使用已知的 media_id（curl 测试成功）
    console.log('🖼️ 使用封面图 media_id...');
    const thumbMediaId = 'u03d0_t9PQhw63k817HKDJHdOqIfKOnb8KMmwML4r0qyQFwRVeToAQuVIx2IlS16';
    console.log(`✓ 封面图 media_id: ${thumbMediaId}\n`);
    
    // 4. 发布草稿（HTML 格式）
    console.log('📤 发布到草稿箱...');
    const result = await createDraft(token, html, thumbMediaId);
    
    if (result.media_id) {
      console.log('✅ 发布成功！');
      console.log(`📋 Media ID: ${result.media_id}`);
      console.log('\n👉 请登录 https://mp.weixin.qq.com 查看草稿箱');
      console.log('👉 在草稿箱预览无误后，点击"群发"按钮推送给粉丝');
    } else {
      console.log('❌ 发布失败');
      console.log(`错误码：${result.errcode}`);
      console.log(`错误信息：${result.errmsg}`);
    }
    
  } catch (error) {
    console.error('❌ 错误:', error.message);
    process.exit(1);
  }
})();
