---
name: cookie-converter
description: Bidirectional cookie format converter supporting Netscape, Playwright, and JSON formats. Use when converting cookies between different tools (yt-dlp, Playwright, curl, browser automation).
---

# Cookie Format Converter

Bidirectional cookie format converter supporting multiple formats.

## 📦 Supported Conversions

| From | To | Command |
|------|-----|---------|
| **Netscape** | Playwright | `netscape-to-playwright` |
| **Playwright** | Netscape | `playwright-to-netscape` |
| **Netscape** | JSON | `netscape-to-json` |
| **JSON** | Netscape | `json-to-netscape` |
| **Playwright** | JSON | `playwright-to-json` |
| **JSON** | Playwright | `json-to-playwright` |

---

## 🎯 When to Use

### Use Netscape → Playwright when:
- Exporting cookies from browser with `browser-cookies-exporter`
- Using with Playwright for browser automation
- Deploying authentication to headless servers
- Configuring `notebooklm` or similar tools

### Use Playwright → Netscape when:
- Extracting cookies from Playwright storage state
- Using with `yt-dlp` for authenticated downloads
- Using with `curl` or `wget` for HTTP requests
- Sharing cookies with command-line tools

### Use JSON format when:
- Inspecting and editing cookies manually
- Integrating with custom scripts
- Storing cookies in databases or config files
- Transferring between different systems

---

## 🚀 Quick Start

### Convert Netscape to Playwright (for NotebookLM)

```bash
python3 convert_cookies.py netscape-to-playwright \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json
```

**Use case:** Export cookies from Chrome, convert for Playwright, deploy to server.

---

### Convert Playwright to Netscape (for yt-dlp)

```bash
python3 convert_cookies.py playwright-to-netscape \
  /tmp/storage_state.json \
  /tmp/youtube-cookies.txt
```

**Use case:** Extract cookies from Playwright, convert for yt-dlp, download videos.

---

### Convert to JSON (for inspection)

```bash
# Netscape → JSON
python3 convert_cookies.py netscape-to-json \
  /tmp/google-cookies.txt \
  /tmp/cookies.json

# Playwright → JSON
python3 convert_cookies.py playwright-to-json \
  /tmp/storage_state.json \
  /tmp/cookies.json
```

**Use case:** Inspect cookies manually, edit values, debug issues.

---

### Convert from JSON (for custom scripts)

```bash
# JSON → Netscape
python3 convert_cookies.py json-to-netscape \
  /tmp/cookies.json \
  /tmp/google-cookies.txt

# JSON → Playwright
python3 convert_cookies.py json-to-playwright \
  /tmp/cookies.json \
  /tmp/storage_state.json
```

**Use case:** Create cookies from scripts, test authentication, mock cookies.

---

## 📋 Format Differences

### Netscape Cookie File

**Format:** Text file with tab-separated values

```
# Netscape HTTP Cookie File
# This is a generated file! Do not edit.

.google.com	TRUE	/	FALSE	1234567890	SID	value1
.google.com	TRUE	/	FALSE	1234567890	HSID	value2
.youtube.com	TRUE	/	FALSE	1234567890	VISITOR_INFO1_LIVE	value3
```

**Fields:**
```
Domain | IncludeSubdomains | Path | Secure | Expires | Name | Value
```

**Tools using this format:**
- `browser-cookies-exporter` (output)
- `yt-dlp` (input via `--cookies`)
- `curl` (input via `--cookie`)
- `wget` (input via `--load-cookies`)

---

### Playwright storage_state.json

**Format:** JSON with cookies and origins

```json
{
  "cookies": [
    {
      "name": "SID",
      "value": "value1",
      "domain": ".google.com",
      "path": "/",
      "expires": 1234567890.0,
      "httpOnly": false,
      "secure": true,
      "sameSite": "Lax"
    },
    {
      "name": "HSID",
      "value": "value2",
      "domain": ".google.com",
      "path": "/",
      "expires": 1234567890.0,
      "httpOnly": false,
      "secure": true,
      "sameSite": "Lax"
    }
  ],
  "origins": [
    {
      "origin": "https://notebooklm.google.com",
      "localStorage": []
    }
  ]
}
```

**Tools using this format:**
- `playwright` (load/save storage state)
- `notebooklm` (authentication)
- Browser automation frameworks

---

### JSON Array (Simple)

**Format:** JSON array of cookie objects

```json
[
  {
    "name": "SID",
    "value": "value1",
    "domain": ".google.com",
    "path": "/",
    "expires": 1234567890,
    "secure": true
  },
  {
    "name": "HSID",
    "value": "value2",
    "domain": ".google.com",
    "path": "/",
    "expires": 1234567890,
    "secure": true
  }
]
```

**Tools using this format:**
- Custom scripts
- Manual inspection/editing
- Configuration files

---

## 🔧 Common Workflows

### Workflow 1: Browser → Server (Deploy authentication)

```bash
# 1. Export cookies from Chrome
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# 2. Convert to Playwright format
python3 convert_cookies.py netscape-to-playwright \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# 3. Deploy to server
scp /tmp/storage_state.json \
  user@server:/path/to/session.json
```

---

### Workflow 2: Server → Local (Extract authentication)

```bash
# 1. Download storage state from server
scp user@server:/path/to/session.json /tmp/storage_state.json

# 2. Convert to Netscape format
python3 convert_cookies.py playwright-to-netscape \
  /tmp/storage_state.json \
  /tmp/google-cookies.txt

# 3. Use with yt-dlp
yt-dlp --cookies /tmp/google-cookies.txt "URL"
```

---

### Workflow 3: Inspect and Edit

```bash
# 1. Convert to JSON for inspection
python3 convert_cookies.py playwright-to-json \
  /tmp/storage_state.json \
  /tmp/cookies.json

# 2. Edit JSON file
nano /tmp/cookies.json

# 3. Convert back to Playwright
python3 convert_cookies.py json-to-playwright \
  /tmp/cookies.json \
  /tmp/storage_state_updated.json
```

---

### Workflow 4: Create mock cookies for testing

```bash
# 1. Create JSON file with mock cookies
cat > /tmp/mock-cookies.json <<EOF
[
  {
    "name": "test_cookie",
    "value": "test_value",
    "domain": "example.com",
    "path": "/",
    "expires": 9999999999,
    "secure": false
  }
]
EOF

# 2. Convert to Playwright
python3 convert_cookies.py json-to-playwright \
  /tmp/mock-cookies.json \
  /tmp/storage_state.json

# 3. Use with Playwright
playwright codegen --load-storage=/tmp/storage_state.json https://example.com
```

---

## 📊 Conversion Examples

### Example 1: YouTube authentication

```bash
# Export cookies from Chrome
browser-cookies-exporter youtube.com /tmp/youtube-cookies.txt

# Convert to Playwright (if needed)
python3 convert_cookies.py netscape-to-playwright \
  /tmp/youtube-cookies.txt \
  /tmp/youtube_storage.json

# Use with yt-dlp (Netscape)
yt-dlp --cookies /tmp/youtube-cookies.txt "URL"

# Use with Playwright (Playwright format)
playwright codegen --load-storage=/tmp/youtube_storage.json "URL"
```

---

### Example 2: NotebookLM deployment

```bash
# Export cookies from Chrome
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# Convert to Playwright
python3 convert_cookies.py netscape-to-playwright \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# Deploy to VPS
sshpass -p 'password' scp /tmp/storage_state.json \
  root@vps:/root/.config/notebooklm/session.json

# Verify
ssh root@vps "notebooklm list"
```

---

### Example 3: Debugging authentication issues

```bash
# Convert Playwright to JSON for inspection
python3 convert_cookies.py playwright-to-json \
  /tmp/storage_state.json \
  /tmp/cookies.json

# Inspect cookies
cat /tmp/cookies.json | python3 -m json.tool | less

# Check for specific cookies
cat /tmp/cookies.json | python3 -c "
import json, sys
cookies = json.load(sys.stdin)
for c in cookies:
    if 'SID' in c.get('name', ''):
        print(f\"Found: {c['name']} = {c['value'][:20]}...\")
"
```

---

## ⚠️ Common Issues

### Issue 1: "No cookies found"

**Error:**
```
❌ Error: Input file not found: /tmp/cookies.txt
```

**Solution:**
Check if the input file exists:
```bash
ls -la /tmp/cookies.txt
```

---

### Issue 2: Invalid cookie format

**Error:**
```
❌ Error during conversion: Malformed cookie file
```

**Solution:**
Validate the input file:
```bash
# For Netscape files
head -5 /tmp/cookies.txt

# For JSON files
python3 -m json.tool /tmp/cookies.json
```

---

### Issue 3: Missing required fields

**Error:**
```
❌ Error during conversion: Missing 'name' field
```

**Solution:**
Ensure all cookies have required fields:
- Netscape: domain, path, name, value
- Playwright: name, value, domain
- JSON: name, value, domain

---

### Issue 4: Permission denied

**Error:**
```
❌ Error saving output file: Permission denied
```

**Solution:**
Check directory permissions:
```bash
# Create output directory with correct permissions
mkdir -p /tmp/output
chmod 755 /tmp/output

# Use absolute path
python3 convert_cookies.py netscape-to-playwright \
  /tmp/input.txt \
  /tmp/output/output.json
```

---

## 🔍 Advanced Usage

### Custom origins in Playwright

When converting JSON → Playwright, you can add custom origins:

```json
{
  "cookies": [...],
  "origins": [
    {
      "origin": "https://example.com",
      "localStorage": [
        {"name": "key1", "value": "value1"},
        {"name": "key2", "value": "value2"}
      ]
    }
  ]
}
```

---

### Filtering cookies by domain

Convert cookies, then filter:

```bash
# Convert to JSON
python3 convert_cookies.py playwright-to-json \
  /tmp/storage.json \
  /tmp/cookies.json

# Filter Google cookies
cat /tmp/cookies.json | python3 -c "
import json, sys
cookies = json.load(sys.stdin)
google_cookies = [c for c in cookies if 'google.com' in c.get('domain', '')]
print(json.dumps(google_cookies, indent=2))
" > /tmp/google-cookies.json
```

---

### Merging multiple cookie files

```bash
# Convert both to JSON
python3 convert_cookies.py netscape-to-json cookies1.txt cookies1.json
python3 convert_cookies.py netscape-to-json cookies2.txt cookies2.json

# Merge JSON files
python3 <<EOF
import json

with open('cookies1.json') as f1:
    cookies1 = json.load(f1)
with open('cookies2.json') as f2:
    cookies2 = json.load(f2)

# Merge and remove duplicates
merged = cookies1 + cookies2
seen = {}
unique = []
for c in merged:
    key = f"{c['name']}_{c['domain']}"
    if key not in seen:
        seen[key] = True
        unique.append(c)

with open('merged.json', 'w') as f:
    json.dump(unique, f, indent=2)
EOF

# Convert back to desired format
python3 convert_cookies.py json-to-playwright merged.json merged_storage.json
```

---

## 🔗 Related Tools

- **browser-cookies-exporter:** Export cookies from browsers
- **youtube-auth-exporter:** YouTube/Google authentication
- **notebooklm-auth-exporter:** NotebookLM authentication
- **yt-dlp:** Video downloader with cookie support
- **playwright:** Browser automation framework

---

## 📖 Reference

- **Netscape Cookie File Format:** https://curl.se/docs/http-cookies.html
- **Playwright Storage State:** https://playwright.dev/docs/emulation#reusable-authentication-state
- **HTTP Cookies:** https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies

---

## 💡 Tips

1. **Backup before conversion:** Always keep original files
2. **Validate input files:** Check format before conversion
3. **Use verbose mode:** Add `-v` to see detailed output
4. **Test small samples:** Convert a few cookies first, then all
5. **Secure sensitive data:** Cookie files contain authentication tokens

---

## 📝 Summary

This converter supports bidirectional conversion between:
- ✅ Netscape cookie files (yt-dlp, curl, wget)
- ✅ Playwright storage state (playwright, notebooklm)
- ✅ JSON arrays (custom scripts, inspection)

Use the right format for your tool and convert seamlessly!
