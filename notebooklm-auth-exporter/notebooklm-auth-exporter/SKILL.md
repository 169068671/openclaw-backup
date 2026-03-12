---
name: notebooklm-auth-exporter
description: Export NotebookLM authentication state from Chrome browser for automated access. Use when setting up NotebookLM on headless servers, automating Google authentication, or migrating auth between machines.
---

# NotebookLM Auth Exporter

Export NotebookLM authentication state from Chrome browser to `storage_state.json` for automated access.

## ⚠️ Important Note

Google detects and blocks automation browsers. **DO NOT use Playwright automation to login** to Google services. Instead, export cookies from your real Chrome browser using `browser-cookies-exporter` skill.

## Why This Skill Matters

NotebookLM requires Google authentication. This skill lets you:

1. **Export auth from real Chrome** (no automation detection)
2. **Copy to headless servers** for automated access
3. **Maintain sessions** across script runs
4. **Avoid manual login** in production environments

## Quick Start (Recommended)

### Step 1: Export Cookies from Real Chrome

Use the `browser-cookies-exporter` skill to export Google cookies:

```bash
# Export all Google cookies
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# Or export specific domains
browser-cookies-exporter accounts.google.com /tmp/google-account-cookies.txt
browser-cookies-exporter notebooklm.google.com /tmp/notebooklm-cookies.txt
```

### Step 2: Convert to Playwright Format

Use the conversion script included in this skill:

```bash
python3 ~/.openclaw/skills/notebooklm-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json
```

### Step 3: Transfer to Server

Copy the exported file to your target server.

**Using SCP (manual):**
```bash
scp /tmp/storage_state.json user@server:/root/.notebooklm/storage_state.json
```

**Using SSH password automation (with sshpass):**
```bash
# Create directory on server
sshpass -p 'PASSWORD' ssh user@server "mkdir -p /root/.notebooklm"

# Copy file
sshpass -p 'PASSWORD' scp /tmp/storage_state.json \
  user@server:/root/.notebooklm/storage_state.json
```

**Example (Hostinger VPS):**
```bash
sshpass -p 'PASSWORD' scp /tmp/storage_state.json \
  root@76.13.219.143:/root/.notebooklm/storage_state.json
```

**Automated Script:**
```bash
#!/bin/bash
# deploy_to_server.sh

SERVER="root@76.13.219.143"
PASSWORD="your_password"
LOCAL_FILE="/tmp/storage_state.json"
REMOTE_PATH="/root/.notebooklm/storage_state.json"

# Create directory and copy file
sshpass -p "$PASSWORD" ssh "$SERVER" "mkdir -p $(dirname $REMOTE_PATH)"
sshpass -p "$PASSWORD" scp "$LOCAL_FILE" "$SERVER:$REMOTE_PATH"

echo "✅ Deployed to $SERVER:$REMOTE_PATH"
```

### Step 4: Use in Playwright Scripts

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
    await page.goto("https://notebooklm.google.com/")

    # Access NotebookLM without manual login
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
python3 ~/.openclaw/skills/notebooklm-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  ~/.notebooklm/storage_state.json

# 3. Test the auth file
python3 -c "
import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            storage_state='~/.notebooklm/storage_state.json'
        )
        page = await context.new_page()
        await page.goto('https://notebooklm.google.com/')
        print('Page title:', await page.title())
        await browser.close()

asyncio.run(test())
"

# 4. Transfer to server (if needed)
# Using sshpass (password automation)
sshpass -p 'PASSWORD' scp ~/.notebooklm/storage_state.json \
  root@76.13.219.143:/root/.notebooklm/storage_state.json

# Or using standard SCP (will prompt for password)
scp ~/.notebooklm/storage_state.json user@server:/root/.notebooklm/storage_state.json
```

## Common Use Cases

### Use Case 1: Headless Server Automation

1. Generate `storage_state.json` on your laptop (has Chrome)
2. Copy to server via SCP:
   ```bash
   # With sshpass (automated)
   sshpass -p 'PASSWORD' scp ~/.notebooklm/storage_state.json \
     root@76.13.219.143:/root/.notebooklm/storage_state.json

   # Or manual (prompts for password)
   scp ~/.notebooklm/storage_state.json user@server:/root/.notebooklm/storage_state.json
   ```
3. Use in Playwright scripts running on server
4. Renew every 1-2 weeks as needed

### Use Case 2: Scheduled Jobs

For cron jobs or scheduled automation:

```python
async with async_playwright() as p:
    browser = await p.chromium.launch(headless=True)
    context = await browser.new_context(
        storage_state="/root/.notebooklm/storage_state.json"
    )
    # Run automated tasks
```

### Use Case 3: Multiple Environments

Generate different auth files for different Google accounts:

```bash
# Personal account (export from Chrome logged into personal account)
browser-cookies-exporter .google.com /tmp/personal-cookies.txt
python3 convert_cookies.py /tmp/personal-cookies.txt ~/.notebooklm/personal.json

# Work account (export from Chrome logged into work account)
browser-cookies-exporter .google.com /tmp/work-cookies.txt
python3 convert_cookies.py /tmp/work-cookies.txt ~/.notebooklm/work.json
```

## Best Practices

### 1. Security

- **Never commit** `storage_state.json` to version control
- Add to `.gitignore`: `*.storage_state.json`, `storage_state.json`
- Store securely with restricted permissions: `chmod 600 storage_state.json`
- Contains sensitive authentication cookies

### 2. Storage

- **Choose a permanent location** (e.g., `~/.notebooklm/storage_state.json`)
- Document the path in your scripts
- Create backup before renewing

### 3. Renewal

- Google sessions expire after ~14 days
- Re-export cookies from Chrome and convert
- Consider setting a calendar reminder for renewal

### 4. Cookie Domains

For NotebookLM, these domains are important:
- `.google.com` - Main Google cookies (recommended)
- `accounts.google.com` - Authentication cookies
- `notebooklm.google.com` - NotebookLM-specific cookies

## Troubleshooting

### Issue: "Sign in" page appears

**Cause:** Cookies are missing or expired

**Solution:**
1. Open Chrome and login to NotebookLM
2. Re-export cookies: `browser-cookies-exporter .google.com /tmp/cookies.txt`
3. Re-convert: `python3 convert_cookies.py /tmp/cookies.txt /tmp/storage_state.json`

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

**Cause:** Missing localStorage or sessionStorage data

**Solution:** This is a limitation of cookie-only export. If you need full browser state, consider:
- Using Chrome DevTools Protocol to connect to running Chrome
- Exporting localStorage manually from Chrome DevTools
- Using a paid service that handles auth for you

### Issue: No cookies found for domain

**Cause:** Chrome not running or no cookies exist

**Solution:**
```bash
# Make sure Chrome is running
ps aux | grep chrome

# Make sure you're logged into the domain in Chrome
# Open Chrome, visit the domain, login, then re-export
```

## Example Integration

Here's a complete example of using the exported storage state:

```python
from playwright.async_api import async_playwright
import asyncio

async def use_notebooklm():
    async with async_playwright() as p:
        # Launch headless browser on server
        browser = await p.chromium.launch(headless=True)

        # Load authentication state
        context = await browser.new_context(
            storage_state="/root/.notebooklm/storage_state.json"
        )

        # Navigate to NotebookLM (already authenticated)
        page = await context.new_page()
        await page.goto("https://notebooklm.google.com/")

        # Wait for page load
        await page.wait_for_load_state("networkidle")

        print("✓ Successfully authenticated with NotebookLM")

        # Your automation code here
        # Example: List notebooks
        notebooks = await page.locator('[data-testid="notebook-card"]').all()
        print(f"Found {len(notebooks)} notebooks")

        await browser.close()

asyncio.run(use_notebooklm())
```

## Testing Your Auth File

Before deploying to production, test the auth file:

```bash
python3 -c "
import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state='/tmp/storage_state.json')
        page = await context.new_page()

        await page.goto('https://notebooklm.google.com/', timeout=60000)
        title = await page.title()

        if 'NotebookLM' in title and 'Sign in' not in await page.content():
            print('✅ Auth successful!')
        else:
            print('❌ Auth failed - check cookies')

        await browser.close()

asyncio.run(test())
"
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
- Use this skill first to get the cookie file, then use this skill to convert

## Server Deployment Guide

### Step-by-Step Deployment to Headless Server

#### 1. Prepare Server

First, create the directory on the server:

```bash
# Using sshpass
sshpass -p 'PASSWORD' ssh user@server "mkdir -p /root/.notebooklm"

# Or manual SSH
ssh user@server "mkdir -p /root/.notebooklm"
```

#### 2. Copy Auth File

Upload the `storage_state.json` file:

```bash
# Using sshpass (automated)
sshpass -p 'PASSWORD' scp /tmp/storage_state.json \
  user@server:/root/.notebooklm/storage_state.json

# Or standard SCP (will prompt for password)
scp /tmp/storage_state.json user@server:/root/.notebooklm/storage_state.json
```

#### 3. Test on Server

Verify authentication works on the server:

```bash
# SSH into server
ssh user@server

# Run test script
python3 -c "
import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            storage_state='/root/.notebooklm/storage_state.json'
        )
        page = await context.new_page()

        await page.goto('https://notebooklm.google.com/', timeout=60000)
        title = await page.title()

        if 'NotebookLM' in title and 'Sign in' not in await page.content():
            print('✅ Auth successful on server!')
        else:
            print('❌ Auth failed on server')

        await browser.close()

asyncio.run(test())
"
```

#### 4. Use in Server Scripts

Now you can use the auth file in your server-side scripts:

```python
# server_script.py
from playwright.async_api import async_playwright
import asyncio

async def automate_notebooklm():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            storage_state="/root/.notebooklm/storage_state.json"
        )
        page = await context.new_page()

        await page.goto("https://notebooklm.google.com/")
        await page.wait_for_load_state("networkidle")

        # Your automation code here
        print("✓ Successfully authenticated on server!")

        await browser.close()

asyncio.run(automate_notebooklm())
```

### Automated Deployment Script

Create `deploy_auth.sh` for automated deployment:

```bash
#!/bin/bash
# deploy_auth.sh - Deploy storage_state.json to server

SERVER="root@76.13.219.143"
PASSWORD="your_password"
LOCAL_FILE="/tmp/storage_state.json"
REMOTE_PATH="/root/.notebooklm/storage_state.json"

echo "📤 Deploying to $SERVER..."

# Create directory
sshpass -p "$PASSWORD" ssh "$SERVER" "mkdir -p $(dirname $REMOTE_PATH)"

# Copy file
sshpass -p "$PASSWORD" scp "$LOCAL_FILE" "$SERVER:$REMOTE_PATH"

# Test connection
echo "🧪 Testing connection..."
sshpass -p "$PASSWORD" ssh "$SERVER" "test -f $REMOTE_PATH && echo '✅ File exists' || echo '❌ File not found'"

echo "✅ Deployment complete: $SERVER:$REMOTE_PATH"
```

Make it executable and run:

```bash
chmod +x deploy_auth.sh
./deploy_auth.sh
```

### Example: Hostinger VPS

For Hostinger VPS (your case):

```bash
# Server details
SERVER="root@76.13.219.143"
PASSWORD="Whj001.Whj001"

# Deploy auth file
sshpass -p "$PASSWORD" ssh "$SERVER" "mkdir -p /root/.notebooklm"
sshpass -p "$PASSWORD" scp /tmp/storage_state.json "$SERVER:/root/.notebooklm/storage_state.json"

# Test
sshpass -p "$PASSWORD" ssh "$SERVER" "ls -lh /root/.notebooklm/storage_state.json"
```

### Renewal Process (Every 1-2 Weeks)

When cookies expire, repeat the process:

```bash
# 1. Export from Chrome
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# 2. Convert
python3 ~/.openclaw/skills/notebooklm-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# 3. Deploy to server (automated)
./deploy_auth.sh

# Or manual
sshpass -p 'PASSWORD' scp /tmp/storage_state.json \
  user@server:/root/.notebooklm/storage_state.json

# 4. Test on server
ssh user@server
python3 -c "..."  # Run test script
```

### Security Considerations

- **Password storage**: Don't hardcode passwords in scripts. Use environment variables or password managers
- **SSH keys**: Consider using SSH keys instead of passwords for better security
- **File permissions**: Set restrictive permissions on the auth file: `chmod 600 /root/.notebooklm/storage_state.json`
- **Secure transfer**: Use SSH/SCP for file transfer (already secure)

## Summary

**Quick reference:**
```bash
# Step 1: Export cookies from Chrome
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# Step 2: Convert to Playwright format
python3 ~/.openclaw/skills/notebooklm-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# Step 3: Use in Playwright
# context = await browser.new_context(storage_state='/tmp/storage_state.json')
```

**Key points:**
- ✅ Export from real Chrome (no automation detection)
- ✅ Convert to Playwright format
- ✅ Works on headless servers
- ⚠️ Cookies expire, re-export every 1-2 weeks
- ⚠️ Cookies are sensitive, protect them

---

## 🔗 Related Skills

- **Cookie Format Converter:** Bidirectional conversion between Netscape, Playwright, and JSON formats
  - Location: `/home/admin/openclaw/workspace/Cookie Converter使用指南.md`
  - Use for: Converting cookies between different tools (yt-dlp, Playwright, curl)

- **youtube-auth-exporter:** Export YouTube authentication state
  - Location: `/home/admin/openclaw/workspace/youtube-auth-exporter/SKILL.md`
  - Use for: Setting up YouTube on headless servers

- **browser-cookies-exporter:** Export cookies from Chrome, Firefox, Brave, Edge
  - Location: `/home/admin/.local/bin/browser-cookies-exporter`
  - Use for: Extracting cookies from any supported browser

---

**Note:** This skill provides a cookie-only solution. For full browser state (localStorage, sessionStorage), you'll need to connect to a running Chrome instance using Chrome DevTools Protocol.
