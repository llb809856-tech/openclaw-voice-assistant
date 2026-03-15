#!/usr/bin/env node

/**
 * 微信公众号自动排版发布工具 v2
 * 
 * 功能：
 * 1. 读取 Markdown 文章
 * 2. 应用自定义 CSS 主题
 * 3. 转换为微信 HTML 格式
 * 4. 上传封面图
 * 5. 发布到草稿箱
 */

const fs = require('fs');
const path = require('path');
const https = require('https');
const http = require('http');
const { marked } = require('marked');

// 配置
const CONFIG = {
  // 微信配置
  appId: 'wxe5c761b6af8be413',
  appSecret: 'a21104b49ddb844188fc64fd44bb885c',
  
  // 文章配置
  markdownPath: process.argv[2] || '/Users/a01/.openclaw/workspace/公众号文章-AI Agent 爆发 - 新版.md',
  theme: process.argv[3] || '黑金商务主题',
  author: '智能体 LB',
  coverImagePath: process.argv[4] || '', // 可选封面图路径
  
  // 排版配置
  fontSize: 16,
  lineHeight: 1.8,
  letterSpacing: 0.5,
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
async function uploadCoverImage(token, imagePath) {
  if (!imagePath || !fs.existsSync(imagePath)) {
    console.log('⚠️ 未提供封面图，使用默认封面');
    return null;
  }
  
  const imageBuffer = fs.readFileSync(imagePath);
  const boundary = '----WebKitFormBoundary' + Math.random().toString(36).substring(2);
  
  let postData = '';
  postData += '--' + boundary + '\r\n';
  postData += 'Content-Disposition: form-data; name="media"; filename="cover.jpg"\r\n';
  postData += 'Content-Type: image/jpeg\r\n\r\n';
  
  return new Promise((resolve, reject) => {
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
        try {
          const result = JSON.parse(data);
          if (result.media_id) {
            resolve(result.media_id);
          } else {
            console.log('⚠️ 封面图上传失败:', data);
            resolve(null);
          }
        } catch (e) {
          console.log('⚠️ 封面图上传失败，继续使用无封面模式');
          resolve(null);
        }
      });
    });
    
    req.on('error', () => resolve(null));
    req.write(Buffer.from(postData, 'binary'));
    req.write(imageBuffer);
    req.write(Buffer.from('\r\n--' + boundary + '--\r\n', 'binary'));
    req.end();
  });
}

// 读取 CSS 主题
function loadTheme(themeName) {
  const themePath = path.join('/Users/a01/.openclaw/workspace/公众号排版主题', `${themeName}.css`);
  
  if (!fs.existsSync(themePath)) {
    throw new Error(`主题文件不存在：${themePath}`);
  }
  
  return fs.readFileSync(themePath, 'utf8');
}

// Markdown 转 HTML
function markdownToHtml(markdown, css) {
  marked.setOptions({
    gfm: true,
    breaks: true,
    headerIds: false,
    mangle: false,
  });
  
  const htmlContent = marked(markdown);
  
  const fullHtml = `
<section id="container" style="font-size: ${CONFIG.fontSize}px; line-height: ${CONFIG.lineHeight}; letter-spacing: ${CONFIG.letterSpacing}px;">
${htmlContent}
</section>

<style>
${css}
</style>
  `.trim();
  
  return fullHtml;
}

// 创建草稿（支持封面图）
async function createDraft(token, htmlContent, title, thumbMediaId) {
  const article = {
    title: title,
    author: CONFIG.author,
    content: htmlContent
  };
  
  // 如果有封面图，添加相关字段
  if (thumbMediaId) {
    article.thumb_media_id = thumbMediaId;
    article.show_cover_pic = 1;
  }
  // 没有封面图时，不添加 thumb_media_id 和 show_cover_pic 字段
  // 避免微信 API 返回 40007 错误
  
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
async function main() {
  console.log('🚀 微信公众号自动排版发布工具 v2');
  console.log('========================\n');
  
  try {
    // 1. 读取 Markdown
    console.log(`📄 读取文章：${CONFIG.markdownPath}`);
    if (!fs.existsSync(CONFIG.markdownPath)) {
      throw new Error(`文章文件不存在：${CONFIG.markdownPath}`);
    }
    const markdown = fs.readFileSync(CONFIG.markdownPath, 'utf8');
    console.log('✓ 文章读取成功\n');
    
    // 2. 加载主题
    console.log(`🎨 应用主题：${CONFIG.theme}`);
    const css = loadTheme(CONFIG.theme);
    console.log('✓ 主题加载成功\n');
    
    // 3. 提取标题
    const titleMatch = markdown.match(/^#\s+(.+)$/m);
    const title = titleMatch ? titleMatch[1] : path.basename(CONFIG.markdownPath, '.md');
    console.log(`📝 文章标题：${title}\n`);
    
    // 4. 转换 HTML
    console.log('🔄 转换 HTML...');
    const htmlContent = markdownToHtml(markdown, css);
    console.log('✓ HTML 转换成功\n');
    
    // 5. 获取 Token
    console.log('🔑 获取 access_token...');
    const token = await getAccessToken();
    console.log('✓ access_token 获取成功\n');
    
    // 6. 上传封面图（如果有）
    let thumbMediaId = null;
    if (CONFIG.coverImagePath) {
      console.log(`🖼️ 上传封面图：${CONFIG.coverImagePath}`);
      thumbMediaId = await uploadCoverImage(token, CONFIG.coverImagePath);
      if (thumbMediaId) {
        console.log('✓ 封面图上传成功\n');
      } else {
        console.log('⚠️ 封面图上传失败，将使用无封面模式\n');
      }
    }
    
    // 7. 发布草稿
    console.log('📤 发布到草稿箱...');
    const result = await createDraft(token, htmlContent, title, thumbMediaId);
    
    if (result.media_id) {
      console.log('✅ 发布成功！');
      console.log(`📋 Media ID: ${result.media_id}`);
      console.log('\n👉 请登录 https://mp.weixin.qq.com 查看草稿箱');
      console.log('👉 在草稿箱预览无误后，点击"群发"按钮推送给粉丝');
    } else {
      console.log('❌ 发布失败');
      console.log(`错误码：${result.errcode}`);
      console.log(`错误信息：${result.errmsg}`);
      
      // 错误处理建议
      if (result.errcode === 40007) {
        console.log('\n💡 解决方案：');
        console.log('1. 检查 IP 白名单：确保 50.114.55.84 在微信后台 IP 白名单中');
        console.log('2. 检查 AppID 和 AppSecret 是否正确');
        console.log('3. 尝试在微信后台重置 AppSecret');
      } else if (result.errcode === 40005) {
        console.log('\n💡 解决方案：封面图格式不支持，请使用 JPG/PNG 格式');
      }
    }
    
  } catch (error) {
    console.error('❌ 错误:', error.message);
    console.error(error.stack);
    process.exit(1);
  }
}

// 运行
main();
