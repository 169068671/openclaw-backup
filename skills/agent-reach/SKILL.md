---
name: agent-reach
description: >
  Use the internet: search, read, and interact with 13+ platforms including
  Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu (小红书), Douyin (抖音),
  WeChat Articles (微信公众号), LinkedIn, Boss直聘, RSS, Exa web search, and any web page.
  Use when: (1) user asks to search or read any of these platforms,
  (2) user shares a URL from any supported platform,
  (3) user asks to search the web, find information online, or research a topic,
  (4) user asks to post, comment, or interact on supported platforms,
  (5) user asks to configure or set up a platform channel.
  Triggers: "搜推特", "搜小红书", "看视频", "搜一下", "上网搜", "帮我查", "全网搜索",
  "search twitter", "read tweet", "youtube transcript", "search reddit",
  "read this link", "看这个链接", "B站", "bilibili", "抖音视频",
  "微信文章", "公众号", "LinkedIn", "GitHub issue", "RSS",
  "search online", "web search", "find information", "research",
  "帮我配", "configure twitter", "configure proxy", "帮我安装".
---

# Agent Reach — Usage Guide

Upstream tools for 13+ platforms. Call them directly.

Run `agent-reach doctor` to check which channels are available.

## ⚠️ Workspace Rules

**Never create files in the agent workspace.** Use `/tmp/` for temporary output and `~/.agent-reach/` for persistent data.

## Web — Any URL

```bash
curl -s "https://r.jina.ai/URL"
```

## Web Search (Exa)

```bash
mcporter call 'exa.web_search_exa(query: "query", numResults: 5)'
mcporter call 'exa.get_code_context_exa(query: "code question", tokensNum: 3000)'
```

## Twitter/X (xreach)

```bash
xreach search "query" -n 10 --json          # search
xreach tweet URL_OR_ID --json                # read tweet (supports /status/ and /article/ URLs)
xreach tweets @username -n 20 --json         # user timeline
xreach thread URL_OR_ID --json               # full thread
```

## YouTube (yt-dlp)

```bash
# 获取视频元数据
yt-dlp --dump-json "URL"

# 下载字幕
yt-dlp --write-sub --write-auto-sub --sub-lang "zh-Hans,zh,en" --skip-download -o "/tmp/%(id)s" "URL"
# 然后读取 .vtt 文件

# 搜索视频
yt-dlp --dump-json "ytsearch5:query"

# 下载视频（完整推荐配置）⭐
yt-dlp --proxy socks5://127.0.0.1:1080 \
  --cookies-from-browser chrome \
  --js-runtimes node \
  --remote-components ejs:github \
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
  -o "/tmp/%(title)s.%(ext)s" \
  "URL"
```

**🔧 必需参数说明**：

| 参数 | 作用 | 原因 |
|-----|------|------|
| `--proxy socks5://127.0.0.1:1080` | SOCKS5 代理 | YouTube 国内被封锁，需要通过 SSH 隧道访问 |
| `--cookies-from-browser chrome` | 使用浏览器 cookies | 绕过 YouTube 的机器人检测 |
| `--js-runtimes node` | 使用 Node.js 解析 | 解决 YouTube 的 JS 挑战 |
| `--remote-components ejs:github` | 使用 GitHub EJS 组件 | 解决 YouTube 的验证码挑战 |

**📋 前置条件**：

1. **启动 SSH 隧道**（使用 Hostinger VPS）：
   ```bash
   sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143
   ```

2. **检查隧道状态**：
   ```bash
   netstat -tlnp | grep 1080
   ```

3. **验证 Node.js 可用**：
   ```bash
   which node nodejs
   ```

**🎬 格式选择**：

```bash
# 最佳质量 MP4（推荐）
-f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"

# 1080p 专用
-f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]"

# 720p 专用（节省流量）
-f "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]"

# 列出所有可用格式
--list-formats
```

**🔥 常见问题**：

- **Error: Network is unreachable** → 需要使用 `--proxy`
- **Error: Sign in to confirm you're not a bot** → 需要 `--cookies-from-browser`
- **Warning: n challenge solving failed** → 需要 `--js-runtimes` 和 `--remote-components`
- **Warning: Only images are available** → 以上参数都缺失，无法获取视频流

**📝 工作流示例**：

```bash
# 1. 启动 SSH 隧道（如果未启动）
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143

# 2. 下载 YouTube 视频
yt-dlp --proxy socks5://127.0.0.1:1080 \
  --cookies-from-browser chrome \
  --js-runtimes node \
  --remote-components ejs:github \
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
  -o "/tmp/%(title)s.%(ext)s" \
  "https://www.youtube.com/watch?v=XXX"

# 3. 查看下载的文件
ls -lh /tmp/
```

## Bilibili (yt-dlp)

```bash
yt-dlp --dump-json "https://www.bilibili.com/video/BVxxx"
yt-dlp --write-sub --write-auto-sub --sub-lang "zh-Hans,zh,en" --convert-subs vtt --skip-download -o "/tmp/%(id)s" "URL"
```

> Server IPs may get 412. Use `--cookies-from-browser chrome` or configure proxy.

## Reddit

```bash
curl -s "https://www.reddit.com/r/SUBREDDIT/hot.json?limit=10" -H "User-Agent: agent-reach/1.0"
curl -s "https://www.reddit.com/search.json?q=QUERY&limit=10" -H "User-Agent: agent-reach/1.0"
```

> Server IPs may get 403. Search via Exa instead, or configure proxy.

## GitHub (gh CLI)

```bash
gh search repos "query" --sort stars --limit 10
gh repo view owner/repo
gh search code "query" --language python
gh issue list -R owner/repo --state open
gh issue view 123 -R owner/repo
```

## 小红书 / XiaoHongShu (mcporter)

```bash
mcporter call 'xiaohongshu.search_feeds(keyword: "query")'
mcporter call 'xiaohongshu.get_feed_detail(feed_id: "xxx", xsec_token: "yyy")'
mcporter call 'xiaohongshu.get_feed_detail(feed_id: "xxx", xsec_token: "yyy", load_all_comments: true)'
mcporter call 'xiaohongshu.publish_content(title: "标题", content: "正文", images: ["/path/img.jpg"], tags: ["tag"])'
```

> Requires login. Use Cookie-Editor to import cookies.

## 抖音 / Douyin (mcporter)

```bash
mcporter call 'douyin.parse_douyin_video_info(share_link: "https://v.douyin.com/xxx/")'
mcporter call 'douyin.get_douyin_download_link(share_link: "https://v.douyin.com/xxx/")'
```

> No login needed.

## 微信公众号 / WeChat Articles

**Search** (miku_ai):
```python
python3 -c "
import asyncio
from miku_ai import get_wexin_article
async def s():
    for a in await get_wexin_article('query', 5):
        print(f'{a[\"title\"]} | {a[\"url\"]}')
asyncio.run(s())
"
```

**Read** (Camoufox — bypasses WeChat anti-bot):
```bash
cd ~/.agent-reach/tools/wechat-article-for-ai && python3 main.py "https://mp.weixin.qq.com/s/ARTICLE_ID"
```

> WeChat articles cannot be read with Jina Reader or curl. Must use Camoufox.

## LinkedIn (mcporter)

```bash
mcporter call 'linkedin.get_person_profile(linkedin_url: "https://linkedin.com/in/username")'
mcporter call 'linkedin.search_people(keyword: "AI engineer", limit: 10)'
```

Fallback: `curl -s "https://r.jina.ai/https://linkedin.com/in/username"`

## Boss直聘 (mcporter)

```bash
mcporter call 'bosszhipin.get_recommend_jobs_tool(page: 1)'
mcporter call 'bosszhipin.search_jobs_tool(keyword: "Python", city: "北京")'
```

Fallback: `curl -s "https://r.jina.ai/https://www.zhipin.com/job_detail/xxx"`

## RSS

```python
python3 -c "
import feedparser
for e in feedparser.parse('FEED_URL').entries[:5]:
    print(f'{e.title} — {e.link}')
"
```

## Troubleshooting

- **Channel not working?** Run `agent-reach doctor` — shows status and fix instructions.
- **Twitter fetch failed?** Ensure `undici` is installed: `npm install -g undici`. Configure proxy: `agent-reach configure proxy URL`.

## Setting Up a Channel ("帮我配 XXX")

If a channel needs setup (cookies, Docker, etc.), fetch the install guide:
https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md

User only provides cookies. Everything else is your job.
