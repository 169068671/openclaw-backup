---
name: yutto-downloader
description: Bilibili video downloader using yutto. Use when user needs to download videos, anime, courses, or collections from Bilibili. Supports single video download, batch download, multiple resolutions (360P-1080P), and codecs (HEVC, AVC, AV1).
---

# Yutto Downloader

## Overview

Yutto-downloader enables downloading Bilibili videos, anime series, courses, and collections using the open-source yutto CLI tool. It supports downloading with membership authentication, multiple video qualities, and subtitle/danmaku extraction.

## Quick Start

### Install yutto

```bash
# Using pip
pip install yutto

# Using Homebrew (macOS)
brew tap siguremo/tap
brew install yutto
```

### Basic Usage

```bash
# Download a single video
yutto https://www.bilibili.com/video/BV1xxxxx/

# Download with membership
yutto --sessdata YOUR_SESSDATA https://www.bilibili.com/video/BV1xxxxx/
```

---

## Installation

### Prerequisites

- Python 3.8+ or Homebrew
- Bilibili account (optional, for membership content)

### Installation Methods

**1. pip (Recommended)**
```bash
pip install yutto
```

**2. Homebrew (macOS)**
```bash
brew tap siguremo/tap
brew install yutto
```

**3. From Source**
```bash
git clone https://github.com/yutto-dev/yutto.git
cd yutto
pip install -e .
```

---

## Configuration

### Configuration File (yutto.toml)

Create `yutto.toml` in your home directory:

```toml
[bilibili]
sessdata = "YOUR_SESSDATA"  # Optional: for membership content
download_dir = "./downloads"
```

### Get SESSDATA

1. Login to Bilibili in browser
2. Open Developer Tools (F12)
3. Go to Application → Cookies
4. Find `SESSDATA` value
5. Copy and paste to config file

---

## Common Tasks

### 1. Download Single Video

```bash
yutto https://www.bilibili.com/video/BV1xxxxx/
```

**Options:**
- Select quality: `--quality 1080` (720, 480, 360)
- Select codec: `--codec hevc` (avc, av1)

### 2. Download Anime/TV Series

```bash
yutto https://www.bilibili.com/bangumi/play/ep123456
```

### 3. Download Collection/Folder

```bash
yutto https://space.bilibili.com/channel/collectiondetail?sid=xxxxx
```

### 4. Download with Danmaku

```bash
yutto https://www.bilibili.com/video/BV1xxxxx/ --with-danmaku
```

### 5. Download Only Audio

```bash
yutto https://www.bilibili.com/video/BV1xxxxx/ --download-only-audio
```

---

## Video Quality Selection

yutto automatically lists available qualities. Common options:

| Quality | Resolution | Codec |
|---------|------------|--------|
| 1080P | 1920x1080 | HEVC/AVC/AV1 |
| 720P | 1280x720 | HEVC/AVC/AV1 |
| 480P | 852x480 | HEVC/AVC/AV1 |
| 360P | 640x360 | HEVC/AVC/AV1 |

**Note:** HEVC and AV1 require membership for high-quality content.

---

## Command Reference

### Main Options

```
--quality, -q       Video quality (auto, 1080, 720, 480, 360)
--codec, -c         Video codec (auto, hevc, avc, av1)
--sessdata          Bilibili SESSDATA for membership content
--download-dir       Download directory (default: ./downloads)
--with-danmaku     Download danmaku as ASS subtitle
--download-only-audio Download audio only
--overwrite          Overwrite existing files
```

### Examples

```bash
# Download 1080P HEVC video
yutto --quality 1080 --codec hevc https://www.bilibili.com/video/BV1xxxxx/

# Download with custom directory
yutto --download-dir ./my_videos https://www.bilibili.com/video/BV1xxxxx/

# Batch download with danmaku
yutto --with-danmaku https://space.bilibili.com/channel/collectiondetail?sid=xxxxx/
```

---

## Troubleshooting

### Video Not Downloading

**Problem:** Video fails to download

**Solutions:**
1. Check if URL is valid
2. Verify internet connection
3. Try with membership credentials (add SESSDATA)
4. Check if video is available in your region

### Low Quality Only

**Problem:** Can only download low quality (480P/360P)

**Solution:**
- Login with SESSDATA to access higher quality
- Verify membership status for premium content

### Network Error

**Problem:** Network timeout or connection error

**Solutions:**
1. Check internet connection
2. Try again (temporary network issue)
3. Use VPN if outside China
4. Set timeout: `--timeout 300`

---

## Resources

### scripts/
Installation and helper scripts for yutto setup.

- See [scripts/install_yutto.sh](scripts/install_yutto.sh) for automated installation

### references/
- [yutto-official-doc.md](references/yutto-official-doc.md) - Official documentation reference
- [bilibili-url-guide.md](references/bilibili-url-guide.md) - Guide to Bilibili URL formats

### assets/
- [yutto.toml](assets/yutto.toml) - Configuration file template

---

## Advanced Usage

### Batch Download from URL List

```bash
# Create urls.txt with one URL per line
cat urls.txt | xargs -I {} yutto {}
```

### Resume Download

yutto supports resume. If download is interrupted:
```bash
# Re-run the same command
yutto https://www.bilibili.com/video/BV1xxxxx/
```

### Download Multiple Videos with Config

```bash
# Set default config in yutto.toml
# Download multiple videos using same config
yutto URL1
yutto URL2
yutto URL3
```

---

## Tips

1. **Use yutto.toml** for persistent configuration
2. **Test with single video** before batch downloading
3. **Check available qualities** first - yutto lists them automatically
4. **Use HEVC or AV1** for better quality (may be slower)
5. **Enable danmaku** if you want subtitles/comments

---

**For more information**, see [Official Documentation](https://yutto.nyakku.moe/) and [GitHub Repository](https://github.com/yutto-dev/yutto).
