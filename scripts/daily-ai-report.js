#!/usr/bin/env node
// AI Model Daily Report - 每天下午6点发布全球AI公司大模型最新版本

const { execSync } = require('child_process');

// 搜索各公司最新大模型
async function searchModels() {
    const companies = [
        { name: 'OpenAI', query: 'OpenAI GPT latest model 2026' },
        { name: 'Google', query: 'Google Gemini latest model 2026' },
        { name: 'Anthropic', query: 'Anthropic Claude latest model 2026' },
        { name: 'Meta', query: 'Meta Llama latest model 2026' },
        { name: 'xAI', query: 'xAI Grok latest model 2026' },
        { name: 'Mistral', query: 'Mistral AI latest model 2026' },
        { name: '字节', query: '字节豆包 最新大模型 2026' },
        { name: '百度', query: '百度文心一言 最新模型 2026' },
        { name: '阿里', query: '阿里通义千问 Qwen 最新模型 2026' },
        { name: 'Deepseek', query: 'Deepseek 最新大模型 2026' },
        { name: 'Minimax', query: 'Minimax 最新大模型 2026' },
        { name: '智谱 AI', query: '智谱 AI GLM 最新模型 2026' },
        { name: '月之暗面', query: '月之暗面 Kimi 最新模型 2026' },
    ];

    const results = [];
    
    for (const company of companies) {
        try {
            const output = execSync(`openclaw web_search "${company.query}" --count 2`, { encoding: 'utf8' });
            results.push({ name: company.name, info: output });
        } catch (e) {
            results.push({ name: company.name, info: '暂无最新信息' });
        }
    }
    
    return results;
}

searchModels().then(results => {
    console.log(JSON.stringify(results, null, 2));
});
