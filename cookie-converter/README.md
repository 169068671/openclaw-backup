# Cookie Format Converter

Bidirectional cookie format converter supporting Netscape, Playwright, and JSON formats.

## 🚀 Quick Start

```bash
# Netscape → Playwright
python3 scripts/convert_cookies.py netscape-to-playwright \
  cookies.txt storage.json

# Playwright → Netscape
python3 scripts/convert_cookies.py playwright-to-netscape \
  storage.json cookies.txt

# With verbose output
python3 scripts/convert_cookies.py netscape-to-playwright \
  cookies.txt storage.json -v
```

## 📦 Supported Conversions

| From | To |
|------|-----|
| Netscape | Playwright |
| Playwright | Netscape |
| Netscape | JSON |
| JSON | Netscape |
| Playwright | JSON |
| JSON | Playwright |

## 📖 Full Documentation

See [SKILL.md](./SKILL.md) for complete documentation.

## 🔧 Installation

No installation required. Just ensure Python 3.6+ is installed:

```bash
python3 --version  # Should be 3.6 or higher
```

## 🎯 Use Cases

- **Browser → Server:** Export cookies from Chrome, deploy to headless servers
- **Server → Local:** Extract authentication from server, use with local tools
- **Format Conversion:** Convert between formats for different tools
- **Inspection:** Convert to JSON for manual inspection/editing

## ⚠️ Important Notes

- Cookie files contain sensitive authentication tokens
- Never share cookie files publicly
- Cookies have expiration dates (usually 14 days for Google)
- Backup original files before conversion

## 🔗 Related Skills

- **browser-cookies-exporter:** Export cookies from browsers
- **youtube-auth-exporter:** YouTube/Google authentication
- **notebooklm-auth-exporter:** NotebookLM authentication
