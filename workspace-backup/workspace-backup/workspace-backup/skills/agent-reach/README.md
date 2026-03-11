# Agent Reach - OpenClaw Skill

## 概述

Agent Reach 为 OpenClaw 提供互联网访问能力，支持 13+ 平台：
- 🌐 网页阅读（任意 URL）
- 📺 YouTube（字幕提取 + 搜索）
- 📡 RSS 订阅
- 🔍 全网搜索（Exa AI）
- 📦 GitHub（公开仓库 + 搜索）
- 🐦 Twitter/X（读取 + 搜索）
- 📺 B站（字幕提取 + 搜索）
- 📖 Reddit（搜索）
- 📕 小红书（读取 + 搜索 + 发帖）
- 🎵 抖音（视频解析 + 下载）
- 💼 LinkedIn
- 🏢 Boss直聘
- 💬 微信公众号（搜索 + 阅读）

## 快速开始

### 1. 安装

运行安装脚本：

```bash
~/.openclaw/skills/agent-reach/scripts/install.sh
```

或者手动安装：

```bash
# 安装 agent-reach
pip install agent-reach

# 安装 Node.js（如果还没有）
# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# 安装 xreach CLI（Twitter/X）
npm install -g xreach-cli undici

# 安装 FFmpeg（视频处理）
sudo apt-get update
sudo apt-get install -y ffmpeg

# 安装 gh CLI（GitHub）
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt-get update
sudo apt-get install -y gh

# 安装其他依赖
pip install feedparser
npm install -g @mcporter/mcporter
```

### 2. 检查状态

```bash
agent-reach doctor
```

这会显示每个平台的状态以及配置说明。

### 3. 配置需要认证的平台

某些平台需要配置才能使用：

**Twitter/X：**
```bash
# 使用 Cookie-Editor 导出 Cookie，然后配置
agent-reach configure twitter-cookies "YOUR_COOKIES"
```

**GitHub（私有仓库）：**
```bash
# 告诉 OpenClaw "帮我登录 GitHub"，它会引导你完成认证
gh auth login
```

**小红书：**
```bash
# 需要运行 Docker 服务
# 告诉 OpenClaw "帮我配小红书"
```

**代理（服务器 IP 被封锁时）：**
```bash
# 配置住宅代理（Reddit、B站 等需要）
agent-reach configure proxy http://user:pass@ip:port
```

## 使用示例

### 网页阅读
```bash
# 读取任意网页
curl -s "https://r.jina.ai/URL"
```

### 网络搜索
```bash
# 全网搜索
mcporter call 'exa.web_search_exa(query: "query", numResults: 5)'
```

### Twitter/X
```bash
# 搜索推文
xreach search "query" -n 10 --json

# 读取单条推文
xreach tweet URL_OR_ID --json

# 用户时间线
xreach tweets @username -n 20 --json
```

### YouTube
```bash
# 获取视频信息
yt-dlp --dump-json "URL"

# 下载字幕
yt-dlp --write-sub --write-auto-sub --sub-lang "zh-Hans,zh,en" --skip-download -o "/tmp/%(id)s" "URL"

# 搜索视频
yt-dlp --dump-json "ytsearch5:query"
```

### B站
```bash
# 获取视频信息
yt-dlp --dump-json "https://www.bilibili.com/video/BVxxx"

# 下载字幕
yt-dlp --write-sub --write-auto-sub --sub-lang "zh-Hans,zh,en" --convert-subs vtt --skip-download -o "/tmp/%(id)s" "URL"
```

### GitHub
```bash
# 搜索仓库
gh search repos "query" --sort stars --limit 10

# 查看仓库
gh repo view owner/repo

# 搜索代码
gh search code "query" --language python

# 查看 Issue
gh issue list -R owner/repo --state open
gh issue view 123 -R owner/repo
```

### 小红书
```bash
# 搜索笔记
mcporter call 'xiaohongshu.search_feeds(keyword: "query")'

# 读取笔记详情
mcporter call 'xiaohongshu.get_feed_detail(feed_id: "xxx", xsec_token: "yyy")'
```

### 抖音
```bash
# 解析视频信息
mcporter call 'douyin.parse_douyin_video_info(share_link: "https://v.douyin.com/xxx/")'

# 获取下载链接
mcporter call 'douyin.get_douyin_download_link(share_link: "https://v.douyin.com/xxx/")'
```

### RSS
```python
python3 -c "
import feedparser
for e in feedparser.parse('FEED_URL').entries[:5]:
    print(f'{e.title} — {e.link}')
"
```

## 常见问题

### 1. Twitter 读取失败？
确保安装了 undici：
```bash
npm install -g undici
```

### 2. Reddit 返回 403？
配置住宅代理：
```bash
agent-reach configure proxy http://user:pass@ip:port
```

### 3. 某个平台用不了？
运行诊断命令：
```bash
agent-reach doctor
```

这会显示每个平台的状态和修复说明。

## 隐私与安全

- ✅ 所有 Cookie 和 Token 只存储在本地 `~/.agent-reach/config.yaml`
- ✅ 文件权限 600（仅所有者可读写）
- ✅ 不上传、不外传任何凭据
- ✅ 代码完全开源，可随时审查

## 注意事项

⚠️ **使用专用小号**：Twitter、小红书等需要 Cookie 的平台，存在被平台检测并封号的风险。请使用专用小号，不要用主账号。

## 更多信息

- **GitHub**: https://github.com/Panniantong/agent-reach
- **文档**: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
- **Issues**: https://github.com/Panniantong/agent-reach/issues

## 技术栈

- **网页**: Jina Reader
- **Twitter**: xreach CLI
- **视频**: yt-dlp
- **搜索**: Exa AI
- **GitHub**: gh CLI
- **RSS**: feedparser
- **小红书**: xiaohongshu-mcp
- **抖音**: douyin-mcp-server
- **LinkedIn**: linkedin-scraper-mcp
- **Boss直聘**: mcp-bosszp
- **微信公众号**: camoufox + miku_ai
