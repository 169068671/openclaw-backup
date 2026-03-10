---
name: browser-cookies-exporter
description: >
  Export browser cookies (Chrome) to Netscape format for any website.
  Supports YouTube, Bilibili, Twitter, and more.
  Use when: user needs to export cookies for yt-dlp, wget, curl, or other tools that require Netscape cookie files.
  Triggers: "导出 cookies", "export cookies", "浏览器 cookies", "保存 cookies", "cookie 文件".
---

# Browser Cookies Exporter — Usage Guide

Export Chrome browser cookies to Netscape format for any website.

## Quick Start

```bash
# 导出 YouTube cookies
browser-cookies-exporter youtube.com /home/admin/Desktop/cookies-youtube.txt

# 导出 Bilibili cookies
browser-cookies-exporter bilibili.com /home/admin/Desktop/cookies-bilibili.txt

# 导出 Twitter cookies
browser-cookies-exporter twitter.com /home/admin/Desktop/cookies-twitter.txt
```

## Installation

```bash
# 安装依赖
pip3 install --user browser-cookie3
```

## Usage

### Basic Usage

```bash
browser-cookies-exporter <domain> <output_file>
```

**Parameters**:
- `<domain>`: Website domain (e.g., `youtube.com`, `bilibili.com`, `twitter.com`)
- `<output_file>`: Output file path (e.g., `/home/admin/Desktop/cookies-youtube.txt`)

**Note**: Domain can include subdomains (e.g., `.youtube.com` to include all YouTube cookies).

### Examples

#### YouTube

```bash
# 导出 YouTube cookies
browser-cookies-exporter youtube.com /home/admin/Desktop/cookies-youtube.txt

# 使用导出的 cookies 下载 YouTube 视频
yt-dlp --proxy socks5://127.0.0.1:1080 \
  --cookies /home/admin/Desktop/cookies-youtube.txt \
  --js-runtimes node \
  --remote-components ejs:github \
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
  -o "/tmp/%(title)s.%(ext)s" \
  "https://www.youtube.com/watch?v=XXX"
```

#### Bilibili

```bash
# 导出 Bilibili cookies
browser-cookies-exporter bilibili.com /home/admin/Desktop/cookies-bilibili.txt

# 使用导出的 cookies 下载 Bilibili 视频
yt-dlp --cookies /home/admin/Desktop/cookies-bilibili.txt \
  -o "/tmp/%(title)s.%(ext)s" \
  "https://www.bilibili.com/video/BVxxx"
```

#### Twitter/X

```bash
# 导出 Twitter cookies
browser-cookies-exporter twitter.com /home/admin/Desktop/cookies-twitter.txt

# 使用导出的 cookies 访问 Twitter
curl -b /home/admin/Desktop/cookies-twitter.txt \
  https://twitter.com/user
```

#### GitHub

```bash
# 导出 GitHub cookies
browser-cookies-exporter github.com /home/admin/Desktop/cookies-github.txt
```

## Advanced Usage

### Export Multiple Domains

```bash
# 导出多个网站的 cookies
browser-cookies-exporter youtube.com /tmp/cookies/youtube.txt
browser-cookies-exporter bilibili.com /tmp/cookies/bilibili.txt
browser-cookies-exporter twitter.com /tmp/cookies/twitter.txt
```

### Wildcard Domain

```bash
# 导出所有子域名（如 .youtube.com 包括 m.youtube.com, www.youtube.com）
browser-cookies-exporter .youtube.com /home/admin/Desktop/cookies-youtube-all.txt
```

### Save to Specific Directory

```bash
# 保存到特定目录
mkdir -p /home/admin/cookies
browser-cookies-exporter youtube.com /home/admin/cookies/youtube.com.txt
```

## Output Format

The exported cookies are in **Netscape HTTP Cookie File** format:

```
# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.youtube.com	TRUE	/	FALSE	1807160053	APISID	xxx
.youtube.com	TRUE	/	FALSE	1807160053	HSID	xxx
.youtube.com	TRUE	/	FALSE	1807160053	SAPISID	xxx
.youtube.com	TRUE	/	FALSE	1807160053	SID	xxx
```

**Format Fields**:
- `domain`: Cookie domain
- `flag`: TRUE/FALSE (whether cookie can be sent over HTTPS)
- `path`: Cookie path
- `secure`: TRUE/FALSE (whether cookie is secure)
- `expiration`: Unix timestamp of expiration
- `name`: Cookie name
- `value`: Cookie value

## Cookie Lifetime

Cookies expire over time. You may need to re-export periodically:

- **YouTube**: Cookies last ~2 weeks
- **Bilibili**: Cookies last ~1 week
- **Twitter**: Cookies last ~2 weeks
- **GitHub**: Cookies last ~1 month

**When to re-export**:
- If you get authentication errors
- If you get "Sign in to confirm you're not a bot" errors
- If downloads fail with 403 Forbidden

## Security Notes

⚠️ **Important Security Notes**:

1. **Cookies contain sensitive information** - Do not share them publicly
2. **Cookies allow account access** - Protect cookie files carefully
3. **Re-export periodically** - Cookies expire and need updating
4. **Use secure storage** - Keep cookie files in secure directories

**Recommended**:
- Store cookies in `~/.cookies/` or `/home/admin/Desktop/cookies/`
- Change passwords regularly
- Limit cookie file permissions (`chmod 600 cookies-youtube.txt`)

## Troubleshooting

### No cookies exported

**Problem**: Export succeeds but file is empty or has very few cookies.

**Possible causes**:
- Chrome is not running
- No cookies exist for the domain
- Chrome profile path is incorrect

**Solutions**:
```bash
# Check if Chrome is running
ps aux | grep chrome

# Check Chrome cookies database
ls -la ~/.config/google-chrome/Default/Cookies

# Try with full domain path
browser-cookies-exporter www.youtube.com /tmp/cookies.txt
```

### Permission denied

**Problem**: Cannot read Chrome cookies file.

**Solution**:
```bash
# Stop Chrome before exporting
pkill -f chrome

# Export cookies
browser-coaches-exporter youtube.com /tmp/cookies.txt

# Restart Chrome
google-chrome &
```

### Cookies not working with yt-dlp

**Problem**: yt-dlp fails even with cookies.

**Solution**:
```bash
# Re-export cookies (may have expired)
browser-cookies-exporter youtube.com /tmp/cookies-youtube.txt

# Use --cookies-from-browser instead
yt-dlp --cookies-from-browser chrome URL

# Check cookie file format
head -5 /tmp/cookies-youtube.txt
```

## Supported Browsers

Currently only supports **Google Chrome**.

Future support:
- Firefox
- Edge
- Safari

## Manual Export (Python)

If the command fails, use Python directly:

```bash
python3 -c "
import browser_cookie3
import http.cookiejar as cj

# 导出 cookies
cookies = browser_cookie3.chrome(domain_name='youtube.com')
cookie_jar = cj.MozillaCookieJar('/home/admin/Desktop/cookies-youtube.txt')
for cookie in cookies:
    cookie_jar.set_cookie(cookie)
cookie_jar.save()

print(f'✅ 已导出 {len(cookies)} 个 cookies')
"
```

## Common Websites

| Website | Domain | Example Command |
|---------|---------|----------------|
| YouTube | `youtube.com` | `browser-cookies-exporter youtube.com /tmp/cookies-youtube.txt` |
| Bilibili | `bilibili.com` | `browser-cookies-exporter bilibili.com /tmp/cookies-bilibili.txt` |
| Twitter | `twitter.com` | `browser-cookies-exporter twitter.com /tmp/cookies-twitter.txt` |
| GitHub | `github.com` | `browser-cookies-exporter github.com /tmp/cookies-github.txt` |
| Reddit | `reddit.com` | `browser-cookies-exporter reddit.com /tmp/cookies-reddit.txt` |
| LinkedIn | `linkedin.com` | `browser-cookies-exporter linkedin.com /tmp/cookies-linkedin.txt` |
| Weibo | `weibo.com` | `browser-cookies-exporter weibo.com /tmp/cookies-weibo.txt` |
| Douyin | `douyin.com` | `browser-cookies-exporter douyin.com /tmp/cookies-douyin.txt` |

## Integration with Other Tools

### yt-dlp

```bash
# 下载 YouTube 视频
yt-dlp --cookies /home/admin/Desktop/cookies-youtube.txt "URL"

# 下载 Bilibili 视频
yt-dlp --cookies /home/admin/Desktop/cookies-bilibili.txt "URL"
```

### curl

```bash
# 使用 cookies 访问网站
curl -b /home/admin/Desktop/cookies-youtube.txt https://www.youtube.com

# 保存网页
curl -b /home/admin/Desktop/cookies-youtube.txt -o page.html https://www.youtube.com/watch?v=XXX
```

### wget

```bash
# 使用 cookies 下载文件
wget --load-cookies=/home/admin/Desktop/cookies-youtube.txt "URL"
```

### Python requests

```bash
python3 -c "
import http.cookiejar as cj
import requests

# 加载 cookies
cookie_jar = cj.MozillaCookieJar('/home/admin/Desktop/cookies-youtube.txt')
cookie_jar.load()

# 使用 cookies 发送请求
session = requests.Session()
session.cookies = cookie_jar
response = session.get('https://www.youtube.com')

print(response.text)
"
```

## Best Practices

1. **Regular re-export**: Cookies expire, re-export every 1-2 weeks
2. **Organize cookies**: Store in `~/cookies/` or `/tmp/cookies/`
3. **Label clearly**: Include domain and date in filename
4. **Secure storage**: Use `chmod 600` on cookie files
5. **Backup cookies**: Keep recent versions for easy rollback

## File Naming Convention

```
cookies-<domain>-<date>.txt

Example:
cookies-youtube-2026-03-07.txt
cookies-bilibili-2026-03-07.txt
cookies-twitter-2026-03-07.txt
```

## Summary

**Quick reference**:
```bash
# Install
pip3 install --user browser-cookie3

# Export
browser-cookies-exporter <domain> <output_file>

# Use with yt-dlp
yt-dlp --cookies <output_file> "URL"

# Re-export (when expired)
browser-cookies-exporter <domain> <output_file>
```

**Key points**:
- ✅ Supports any website domain
- ✅ Netscape format compatible with yt-dlp, curl, wget
- ✅ Export from Chrome browser
- ✅ Easy to re-export when cookies expire
- ⚠️ Cookies expire, re-export periodically
- ⚠️ Cookies are sensitive, protect them

---

**For more information**: See browser-cookie3 documentation: https://github.com/borisbabic/browser_cookie3
