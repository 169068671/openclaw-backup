---
name: youtube-auth-exporter
description: Export YouTube authentication state from Chrome browser for automated access. Use when setting up YouTube on headless servers, automating YouTube downloads with yt-dlp, or migrating auth between machines.
---

# YouTube Auth Exporter

Export YouTube authentication state from Chrome browser to `storage_state.json` for automated access.

## ⚠️ Important Note

Google detects and blocks automation browsers. **DO NOT use Playwright automation to login** to Google services. Instead, export cookies from your real Chrome browser using `browser-cookies-exporter` skill.

## Why This Skill Matters

YouTube requires Google authentication for:
- **Accessing age-restricted videos**
- **Downloading private/unlisted videos**
- **YouTube Music premium content**
- **Watching videos that require login**
- **Accessing YouTube Studio features**

This skill lets you:

1. **Export auth from real Chrome** (no automation detection)
2. **Copy to headless servers** for automated downloads
3. **Use with yt-dlp** for authenticated downloads
4. **Use with Playwright** for automated browser access

## Quick Start (Recommended)

### Step 1: Export Cookies from Real Chrome

Use the `browser-cookies-exporter` skill to export Google/YouTube cookies:

```bash
# Export all Google cookies (recommended)
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# Or export YouTube-specific cookies
browser-cookies-exporter youtube.com /tmp/youtube-cookies.txt
```

### Step 2: Convert to Playwright Format

Use the conversion script included in this skill:

```bash
python3 ~/.openclaw/skills/youtube-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json
```

### Step 3: Use with yt-dlp (Most Common)

The converted storage_state.json can be used with yt-dlp:

```bash
# Convert to Netscape format for yt-dlp
python3 -c "
import http.cookiejar as cj
import json

with open('/tmp/storage_state.json', 'r') as f:
    state = json.load(f)

jar = cj.MozillaCookieJar('/tmp/youtube-cookies.txt')
for cookie in state.get('cookies', []):
    import http.cookiejar
    c = http.cookiejar.Cookie(
        version=0,
        name=cookie['name'],
        value=cookie['value'],
        port=None,
        port_specified=False,
        domain=cookie['domain'],
        domain_specified=True,
        domain_initial_dot=cookie['domain'].startswith('.'),
        path=cookie['path'],
        path_specified=True,
        secure=cookie['secure'],
        expires=cookie.get('expires', None),
        discard=False,
        comment=None,
        comment_url=None,
        rest={},
        rfc2109=False
    )
    jar.set_cookie(c)
jar.save()
"

# Download with yt-dlp using cookies
yt-dlp --cookies /tmp/youtube-cookies.txt \
  -f "bestvideo+bestaudio" \
  -o "%(title)s.%(ext)s" \
  "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Step 4: Use with Playwright

Load the storage state in your Playwright scripts:

```python
from playwright.async_api import async_playwright

async with async_playwright() as p:
    browser = await p.chromium.launch(headless=True)
    context = await browser.new_context(
        storage_state="/path/to/storage_state.json"
    )

    # Now you're already authenticated!
    page = await context.new_page()
    await page.goto("https://www.youtube.com/watch?v=VIDEO_ID")

    # Access age-restricted videos without manual login
    # ...

    await browser.close()
```

## Script Reference

### convert_cookies.py

**Location:** `scripts/convert_cookies.py`

**Usage:**
```bash
python3 convert_cookies.py <input_cookie_file> <output_json_file>
```

**Parameters:**
- `<input_cookie_file>`: Netscape cookie file (from browser-cookies-exporter)
- `<output_json_file>`: Playwright storage_state.json file

**What It Does:**
1. Reads Netscape cookie file
2. Converts to Playwright storage_state.json format
3. Saves JSON file with cookies and origins

## Example: Complete Workflow

```bash
# 1. Export cookies from Chrome
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# 2. Convert to Playwright format
python3 ~/.openclaw/skills/youtube-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  ~/.youtube/storage_state.json

# 3. Use with yt-dlp
# First convert storage_state.json to Netscape format
python3 -c "
import http.cookiejar as cj
import json

with open('/tmp/storage_state.json', 'r') as f:
    state = json.load(f)

jar = cj.MozillaCookieJar('/tmp/youtube-cookies.txt')
for cookie in state.get('cookies', []):
    import http.cookiejar
    c = http.cookiejar.Cookie(
        version=0,
        name=cookie['name'],
        value=cookie['value'],
        port=None,
        port_specified=False,
        domain=cookie['domain'],
        domain_specified=True,
        domain_initial_dot=cookie['domain'].startswith('.'),
        path=cookie['path'],
        path_specified=True,
        secure=cookie['secure'],
        expires=cookie.get('expires', None),
        discard=False,
        comment=None,
        comment_url=None,
        rest={},
        rfc2109=False
    )
    jar.set_cookie(c)
jar.save()
"

# 4. Download video with yt-dlp
yt-dlp --cookies /tmp/youtube-cookies.txt \
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
  -o "/tmp/%(title)s.%(ext)s" \
  "https://www.youtube.com/watch?v=VIDEO_ID"
```

## Common Use Cases

### Use Case 1: yt-dlp Automated Downloads (Most Common)

For downloading age-restricted, private, or unlisted videos:

```bash
# Export cookies
browser-cookies-exporter .google.com /tmp/google-cookies.txt
python3 ~/.openclaw/skills/youtube-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# Convert to Netscape format for yt-dlp
python3 -c "
import http.cookiejar as cj
import json

with open('/tmp/storage_state.json', 'r') as f:
    state = json.load(f)

jar = cj.MozillaCookieJar('/tmp/youtube-cookies.txt')
for cookie in state.get('cookies', []):
    import http.cookiejar
    c = http.cookiejar.Cookie(
        version=0,
        name=cookie['name'],
        value=cookie['value'],
        port=None,
        port_specified=False,
        domain=cookie['domain'],
        domain_specified=True,
        domain_initial_dot=cookie['domain'].startswith('.'),
        path=cookie['path'],
        path_specified=True,
        secure=cookie['secure'],
        expires=cookie.get('expires', None),
        discard=False,
        comment=None,
        comment_url=None,
        rest={},
        rfc2109=False
    )
    jar.set_cookie(c)
jar.save()
"

# Download with cookies
yt-dlp --cookies /tmp/youtube-cookies.txt "VIDEO_URL"
```

### Use Case 2: Playwright Automation

For automated browser access to YouTube:

```python
from playwright.async_api import async_playwright
import asyncio

async def automate_youtube():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            storage_state="/tmp/storage_state.json"
        )

        # Access age-restricted video
        page = await context.new_page()
        await page.goto("https://www.youtube.com/watch?v=VIDEO_ID")

        # Wait for video to load
        await page.wait_for_selector("video")

        print("✓ Successfully accessed age-restricted video")

        await browser.close()

asyncio.run(automate_youtube())
```

### Use Case 3: Headless Server Automation

1. Generate `storage_state.json` on your laptop (has Chrome)
2. Copy to server via SCP:
   ```bash
   # With sshpass (automated)
   sshpass -p 'PASSWORD' scp /tmp/storage_state.json \
     root@server:/root/.youtube/storage_state.json

   # Or manual (prompts for password)
   scp /tmp/storage_state.json user@server:/root/.youtube/storage_state.json
   ```
3. Use in yt-dlp or Playwright scripts running on server
4. Renew every 1-2 weeks as needed

### Use Case 4: Multiple YouTube Accounts

Generate different auth files for different YouTube accounts:

```bash
# Personal account (export from Chrome logged into personal account)
browser-cookies-exporter .google.com /tmp/personal-cookies.txt
python3 convert_cookies.py /tmp/personal-cookies.txt ~/.youtube/personal.json

# Work account (export from Chrome logged into work account)
browser-cookies-exporter .google.com /tmp/work-cookies.txt
python3 convert_cookies.py /tmp/work-cookies.txt ~/.youtube/work.json
```

## Best Practices

### 1. Security

- **Never commit** `storage_state.json` to version control
- Add to `.gitignore`: `*.storage_state.json`, `storage_state.json`
- Store securely with restricted permissions: `chmod 600 storage_state.json`
- Contains sensitive authentication cookies

### 2. Storage

- **Choose a permanent location** (e.g., `~/.youtube/storage_state.json`)
- Document the path in your scripts
- Create backup before renewing

### 3. Renewal

- Google sessions expire after ~14 days
- Re-export cookies from Chrome and convert
- Consider setting a calendar reminder for renewal

### 4. Cookie Domains

For YouTube, these domains are important:
- `.google.com` - Main Google cookies (recommended)
- `youtube.com` - YouTube-specific cookies
- `accounts.google.com` - Authentication cookies

## Troubleshooting

### Issue: "Sign in" page appears or "Sign in to confirm you're not a bot"

**Cause:** Cookies are missing, expired, or insufficient

**Solution:**
1. Open Chrome and login to YouTube
2. Visit the YouTube video page you want to download
3. Re-export cookies: `browser-cookies-exporter .google.com /tmp/cookies.txt`
4. Re-convert: `python3 convert_cookies.py /tmp/cookies.txt /tmp/storage_state.json`

### Issue: yt-dlp fails with "HTTP Error 403: Forbidden"

**Cause:** YouTube blocked the request (cookies expired or invalid)

**Solution:**
```bash
# 1. Re-export cookies
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# 2. Re-convert
python3 ~/.openclaw/skills/youtube-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# 3. Convert to Netscape format for yt-dlp
python3 -c "
import http.cookiejar as cj
import json

with open('/tmp/storage_state.json', 'r') as f:
    state = json.load(f)

jar = cj.MozillaCookieJar('/tmp/youtube-cookies.txt')
for cookie in state.get('cookies', []):
    import http.cookiejar
    c = http.cookiejar.Cookie(
        version=0,
        name=cookie['name'],
        value=cookie['value'],
        port=None,
        port_specified=False,
        domain=cookie['domain'],
        domain_specified=True,
        domain_initial_dot=cookie['domain'].startswith('.'),
        path=cookie['path'],
        path_specified=True,
        secure=cookie['secure'],
        expires=cookie.get('expires', None),
        discard=False,
        comment=None,
        comment_url=None,
        rest={},
        rfc2109=False
    )
    jar.set_cookie(c)
jar.save()
"

# 4. Retry download with new cookies
yt-dlp --cookies /tmp/youtube-cookies.txt "VIDEO_URL"
```

### Issue: Conversion fails

**Cause:** Invalid cookie file format

**Solution:**
```bash
# Verify cookie file
head -5 /tmp/cookies.txt

# Should look like:
# .google.com	TRUE	/	FALSE	1234567890	SID	xxx
```

### Issue: Authentication still fails after conversion

**Cause:** Missing localStorage or sessionStorage data, or insufficient cookies

**Solution:**
1. Make sure you're logged into YouTube in Chrome
2. Visit the YouTube page you want to access
3. Try exporting `.google.com` instead of just `youtube.com`
4. This is a limitation of cookie-only export

### Issue: No cookies found for domain

**Cause:** Chrome not running or no cookies exist

**Solution:**
```bash
# Make sure Chrome is running
ps aux | grep chrome

# Make sure you're logged into YouTube in Chrome
# Open Chrome, visit youtube.com, login, then re-export
```

## Example Integration

### Example 1: yt-dlp with Cookies

```bash
#!/bin/bash
# download_youtube_video.sh

VIDEO_URL="$1"
COOKIES_FILE="/tmp/youtube-cookies.txt"
OUTPUT_DIR="/tmp/youtube-downloads"

# Export cookies (do this first)
browser-cookies-exporter .google.com /tmp/google-cookies.txt
python3 ~/.openclaw/skills/youtube-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# Convert to Netscape format
python3 -c "
import http.cookiejar as cj
import json

with open('/tmp/storage_state.json', 'r') as f:
    state = json.load(f)

jar = cj.MozillaCookieJar('$COOKIES_FILE')
for cookie in state.get('cookies', []):
    import http.cookiejar
    c = http.cookiejar.Cookie(
        version=0,
        name=cookie['name'],
        value=cookie['value'],
        port=None,
        port_specified=False,
        domain=cookie['domain'],
        domain_specified=True,
        domain_initial_dot=cookie['domain'].startswith('.'),
        path=cookie['path'],
        path_specified=True,
        secure=cookie['secure'],
        expires=cookie.get('expires', None),
        discard=False,
        comment=None,
        comment_url=None,
        rest={},
        rfc2109=False
    )
    jar.set_cookie(c)
jar.save()
"

# Download video
mkdir -p "$OUTPUT_DIR"
yt-dlp --cookies "$COOKIES_FILE" \
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
  -o "$OUTPUT_DIR/%(title)s.%(ext)s" \
  "$VIDEO_URL"

echo "✅ Download complete!"
```

### Example 2: Playwright with Storage State

```python
from playwright.async_api import async_playwright
import asyncio

async def download_youtube_video(video_url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        # Load authentication state
        context = await browser.new_context(
            storage_state="/tmp/storage_state.json"
        )

        page = await context.new_page()

        # Navigate to video
        await page.goto(video_url)

        # Wait for video to load
        await page.wait_for_selector("video")

        print(f"✓ Successfully accessed: {video_url}")
        print("Note: Use yt-dlp for actual video downloading")

        await browser.close()

asyncio.run(download_youtube_video("https://www.youtube.com/watch?v=VIDEO_ID"))
```

### Example 3: Automated YouTube Downloader Script

```bash
#!/bin/bash
# automated_youtube_downloader.sh

# Configuration
YOUTUBE_URLS_FILE="/tmp/youtube_urls.txt"
STORAGE_STATE_FILE="/tmp/storage_state.json"
COOKIES_FILE="/tmp/youtube-cookies.txt"
OUTPUT_DIR="/tmp/youtube-downloads"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Export and convert cookies (run once, not in loop)
echo "🍪 Exporting cookies..."
browser-cookies-exporter .google.com /tmp/google-cookies.txt
python3 ~/.openclaw/skills/youtube-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  "$STORAGE_STATE_FILE"

# Convert to Netscape format
python3 -c "
import http.cookiejar as cj
import json

with open('$STORAGE_STATE_FILE', 'r') as f:
    state = json.load(f)

jar = cj.MozillaCookieJar('$COOKIES_FILE')
for cookie in state.get('cookies', []):
    import http.cookiejar
    c = http.cookiejar.Cookie(
        version=0,
        name=cookie['name'],
        value=cookie['value'],
        port=None,
        port_specified=False,
        domain=cookie['domain'],
        domain_specified=True,
        domain_initial_dot=cookie['domain'].startswith('.'),
        path=cookie['path'],
        path_specified=True,
        secure=cookie['secure'],
        expires=cookie.get('expires', None),
        discard=False,
        comment=None,
        comment_url=None,
        rest={},
        rfc2109=False
    )
    jar.set_cookie(c)
jar.save()
"

echo "✅ Cookies ready"

# Download videos
while IFS= read -r url; do
    if [[ -n "$url" ]]; then
        echo "📥 Downloading: $url"
        yt-dlp --cookies "$COOKIES_FILE" \
          -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
          -o "$OUTPUT_DIR/%(title)s.%(ext)s" \
          "$url"
        echo "✅ Done"
    fi
done < "$YOUTUBE_URLS_FILE"

echo "🎉 All downloads complete!"
```

## Testing Your Auth File

### Test with Playwright

```bash
python3 -c "
import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state='/tmp/storage_state.json')
        page = await context.new_page()

        await page.goto('https://www.youtube.com/', timeout=60000)
        title = await page.title()

        if 'YouTube' in title:
            print('✅ YouTube auth successful!')
        else:
            print('❌ YouTube auth failed - check cookies')

        await browser.close()

asyncio.run(test())
"
```

### Test with yt-dlp

```bash
# Convert to Netscape format first
python3 -c "
import http.cookiejar as cj
import json

with open('/tmp/storage_state.json', 'r') as f:
    state = json.load(f)

jar = cj.MozillaCookieJar('/tmp/youtube-cookies.txt')
for cookie in state.get('cookies', []):
    import http.cookiejar
    c = http.cookiejar.Cookie(
        version=0,
        name=cookie['name'],
        value=cookie['value'],
        port=None,
        port_specified=False,
        domain=cookie['domain'],
        domain_specified=True,
        domain_initial_dot=cookie['domain'].startswith('.'),
        path=cookie['path'],
        path_specified=True,
        secure=cookie['secure'],
        expires=cookie.get('expires', None),
        discard=False,
        comment=None,
        comment_url=None,
        rest={},
        rfc2109=False
    )
    jar.set_cookie(c)
jar.save()
"

# Test with a known video
yt-dlp --cookies /tmp/youtube-cookies.txt \
  --skip-download \
  "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

## Server Deployment Guide

### Deploy to Headless Server

#### 1. Prepare Server

Create the directory on the server:

```bash
# Using sshpass
sshpass -p 'PASSWORD' ssh user@server "mkdir -p /root/.youtube"

# Or manual SSH
ssh user@server "mkdir -p /root/.youtube"
```

#### 2. Copy Auth File

Upload the `storage_state.json` file:

```bash
# Using sshpass (automated)
sshpass -p 'PASSWORD' scp /tmp/storage_state.json \
  user@server:/root/.youtube/storage_state.json

# Or standard SCP (will prompt for password)
scp /tmp/storage_state.json user@server:/root/.youtube/storage_state.json
```

#### 3. Use on Server

Now you can use the auth file in yt-dlp or Playwright scripts:

```bash
# Example: Download on server with yt-dlp
yt-dlp --cookies /tmp/youtube-cookies.txt \
  -f "bestvideo+bestaudio" \
  -o "/downloads/%(title)s.%(ext)s" \
  "VIDEO_URL"
```

### Example: Hostinger VPS

For Hostinger VPS (76.13.219.143):

```bash
# Server details
SERVER="root@76.13.219.143"
PASSWORD="Whj001.Whj001"

# Deploy auth file
sshpass -p "$PASSWORD" ssh "$SERVER" "mkdir -p /root/.youtube"
sshpass -p "$PASSWORD" scp /tmp/storage_state.json "$SERVER:/root/.youtube/storage_state.json"

# Test
sshpass -p "$PASSWORD" ssh "$SERVER" "ls -lh /root/.youtube/storage_state.json"
```

## Renewal Process (Every 1-2 Weeks)

When cookies expire, repeat the process:

```bash
# 1. Export from Chrome
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# 2. Convert
python3 ~/.openclaw/skills/youtube-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# 3. Deploy to server (if needed)
sshpass -p 'PASSWORD' scp /tmp/storage_state.json \
  user@server:/root/.youtube/storage_state.json

# 4. Test
yt-dlp --cookies /tmp/youtube-cookies.txt \
  --skip-download \
  "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

## Resources

### scripts/convert_cookies.py

Convert Netscape cookie files to Playwright storage_state.json format.

**Dependencies:**
- `http.cookiejar` (standard library)
- `json` (standard library)

**No external dependencies required!**

**Python version:** 3.7+

### Related Skills

- **browser-cookies-exporter**: Export cookies from Chrome to Netscape format
- **yt-dlp-downloader**: Download videos from YouTube and 1000+ other sites

## Summary

**Quick reference:**
```bash
# Step 1: Export cookies from Chrome
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# Step 2: Convert to Playwright format
python3 ~/.openclaw/skills/youtube-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# Step 3: Use with yt-dlp
python3 -c "
import http.cookiejar as cj, json
state = json.load(open('/tmp/storage_state.json'))
jar = cj.MozillaCookieJar('/tmp/youtube-cookies.txt')
for cookie in state.get('cookies', []):
    c = cj.Cookie(version=0, name=cookie['name'], value=cookie['value'],
        port=None, port_specified=False, domain=cookie['domain'],
        domain_specified=True, domain_initial_dot=cookie['domain'].startswith('.'),
        path=cookie['path'], path_specified=True, secure=cookie['secure'],
        expires=cookie.get('expires', None), discard=False, comment=None,
        comment_url=None, rest={}, rfc2109=False)
    jar.set_cookie(c)
jar.save()
"

yt-dlp --cookies /tmp/youtube-cookies.txt "VIDEO_URL"
```

**Key points:**
- ✅ Export from real Chrome (no automation detection)
- ✅ Convert to Playwright format
- ✅ Works with yt-dlp for authenticated downloads
- ✅ Works with Playwright for browser automation
- ⚠️ Cookies expire, re-export every 1-2 weeks
- ⚠️ Cookies are sensitive, protect them

---

## 🔗 Related Skills

- **Cookie Format Converter:** Bidirectional conversion between Netscape, Playwright, and JSON formats
  - Location: `/home/admin/openclaw/workspace/Cookie Converter使用指南.md`
  - Use for: Converting cookies between different tools (yt-dlp, Playwright, curl)

- **notebooklm-auth-exporter:** Export NotebookLM authentication state
  - Location: `/home/admin/openclaw/workspace/notebooklm-auth-exporter/`
  - Use for: Setting up NotebookLM on headless servers

- **browser-cookies-exporter:** Export cookies from Chrome, Firefox, Brave, Edge
  - Location: `/home/admin/.local/bin/browser-cookies-exporter`
  - Use for: Extracting cookies from any supported browser

---

**Note:** This skill provides a cookie-only solution. For full browser state (localStorage, sessionStorage), you'll need to connect to a running Chrome instance using Chrome DevTools Protocol.
