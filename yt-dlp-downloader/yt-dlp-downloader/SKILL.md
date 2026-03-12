---
name: yt-dlp-downloader
description: Comprehensive video downloader supporting 1000+ websites including YouTube, Bilibili, Vimeo, Twitter, etc. Use when downloading videos, audio, or extracting media from any supported platform.
---

# yt-dlp Downloader

## Overview

yt-dlp-downloader enables downloading videos and audio from 1000+ websites including YouTube, Bilibili, Vimeo, Twitter, Instagram, TikTok, and many more. It supports multiple formats, quality selection, subtitles, and advanced filtering.

## Quick Start

### Install yt-dlp

```bash
# Using pip
pip install yt-dlp

# Using pip with FFmpeg (recommended)
pip install yt-dlp
sudo apt-get install ffmpeg
```

### Basic Usage

```bash
# Download video (best quality)
yt-dlp URL

# Download audio only
yt-dlp -x --audio-format mp3 URL

# Download playlist
yt-dlp URL/playlist
```

---

## Installation

### Prerequisites

- Python 3.8+
- FFmpeg (recommended for merging video/audio)

### Installation Methods

**1. pip (Recommended)**
```bash
pip install yt-dlp
```

**2. pip with FFmpeg**
```bash
pip install yt-dlp
# Ubuntu/Debian
sudo apt-get install ffmpeg
# macOS
brew install ffmpeg
```

**3. From Source**
```bash
git clone https://github.com/yt-dlp/yt-dlp.git
cd yt-dlp
pip install .
```

**4. Pre-built Binary**
```bash
# Linux
sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp

# macOS
brew install yt-dlp
```

---

## Common Tasks

### 1. Download Single Video

```bash
yt-dlp https://www.youtube.com/watch?v=VIDEO_ID
```

### 2. Download Best Quality

```bash
yt-dlp -f "bestvideo+bestaudio" URL
```

### 3. Download Audio Only

```bash
# Extract audio (best quality)
yt-dlp -x URL

# Extract and convert to MP3
yt-dlp -x --audio-format mp3 URL
```

### 4. Download Playlist

```bash
# Download entire playlist
yt-dlp URL/playlist

# Download specific range
yt-dlp --playlist-items 1-5 URL/playlist

# Download playlist with limit
yt-dlp --playlist-end 10 URL/playlist
```

### 5. Download Subtitles

```bash
# Download all subtitles
yt-dlp --write-subs URL

# Download specific language
yt-dlp --write-subs --sub-lang en,zh-CN URL
```

### 6. Download Bilibili Video

```bash
# Download with cookies (for membership)
yt-dlp --cookies cookies.txt URL

# Download specific quality
yt-dlp -f "bestvideo[height<=1080]+bestaudio" URL
```

---

## Format Selection

### Format Codes

yt-dlp uses format codes to select video/audio quality:

```
Format syntax: [format_code] [ext] [height] [fps] [vcodec] [acodec]

Examples:
137  mp4  1920x1080  30  avc  none
248  webm  1920x1080  30  vp9  none
251  webm  1920x1080  60  vp9  none
```

### Common Format Strings

```bash
# Best quality (auto-selects best format)
-f best

# Best video + best audio (merges with FFmpeg)
-f "bestvideo+bestaudio"

# 1080p max
-f "bestvideo[height<=1080]+bestaudio"

# MP4 only
-f "bestvideo[ext=mp4]+bestaudio[ext=m4a]"

# 720p max
-f "bestvideo[height<=720]+bestaudio"
```

---

## Advanced Options

### Output Templates

Customize output filenames:

```bash
# Video title only
-o "%(title)s.%(ext)s"

# Video title + upload date
-o "%(upload_date)s - %(title)s.%(ext)s"

# Create subdirectories
-o "downloads/%(uploader)s/%(title)s.%(ext)s"

# All metadata
-o "%(id)s - %(title)s.%(ext)s"
```

### Thumbnail and Metadata

```bash
# Download thumbnail
yt-dlp --write-thumbnail URL

# Download metadata
yt-dlp --write-description URL
yt-dlp --write-info-json URL

# All together
yt-dlp --write-thumbnail --write-description --write-info-json URL
```

### Filtering

```bash
# Download only videos longer than 10 minutes
yt-dlp --match-filter "duration >= 600" URL/playlist

# Download only videos from 2024
yt-dlp --match-filter "upload_date >= 20240101" URL/playlist

# Exclude live streams
yt-dlp --match-filter "is_live != true" URL/playlist
```

---

## Platform-Specific Examples

### YouTube

```bash
# Download with chapters
yt-dlp --write-subs --write-auto-subs URL

# Download 4K video
yt-dlp -f "bestvideo[height<=2160]+bestaudio" URL

# Download from specific date range
yt-dlp --datebefore 20240101 --dateafter 20230101 URL/channel
```

### Bilibili

```bash
# Download with cookies (for membership)
yt-dlp --cookies cookies.txt URL

# Download danmaku
yt-dlp --write-subs URL

# Download series
yt-dlp --download-archive downloaded.txt URL/series
```

### Twitter/X

```bash
# Download tweet with video
yt-dlp "https://twitter.com/user/status/TWEET_ID"

# Download all videos from user
yt-dlp "https://twitter.com/user"
```

### TikTok

```bash
# Download video (no watermark)
yt-dlp URL

# Download all videos from user
yt-dlp URL/user
```

---

## Configuration

### Configuration File

Create `~/.config/yt-dlp/config`:

```ini
[OPTIONS]
# Output directory
output = ./downloads/%(uploader)s/%(title)s.%(ext)s

# Video format
format = bestvideo+bestaudio

# Subtitles
writesubs = true
subtitleslangs = en,zh-CN

# Audio extraction
extractaudio = true
audioformat = mp3

# FFmpeg location
ffmpeglocation = /usr/bin/ffmpeg
```

---

## Troubleshooting

### FFmpeg Not Found

**Problem:** FFmpeg is required for merging video/audio

**Solution:**
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/
```

### 403 Forbidden Error

**Problem:** Access denied

**Solutions:**
1. Update yt-dlp: `pip install --upgrade yt-dlp`
2. Use cookies: `yt-dlp --cookies cookies.txt URL`
3. Use user agent: `yt-dlp --user-agent "Mozilla/5.0..." URL`

### Slow Download Speed

**Problem:** Download is very slow

**Solutions:**
1. Use aria2c: `yt-dlp --external-downloader aria2c URL`
2. Increase concurrent downloads: `yt-dlp --concurrent-fragments 4 URL`
3. Use different format: `yt-dlp -f bestvideo+bestaudio URL`

### Age-Restricted Content

**Problem:** Cannot download age-restricted video

**Solutions:**
1. Use cookies: `yt-dlp --cookies cookies.txt URL`
2. Pass cookies.txt with your login
3. Use account authentication (advanced)

---

## Tips

1. **Use FFmpeg** for best results (merges video/audio)
2. **Update regularly**: `pip install --upgrade yt-dlp`
3. **Test with single video** before downloading playlists
4. **Use format strings** for consistent quality
5. **Check supported sites**: `yt-dlp --list-extractors`
6. **Use filters** to avoid unwanted content
7. **Download archives** to track downloaded videos

---

## Resources

### scripts/
- [install_yt-dlp.sh](scripts/install_yt-dlp.sh) - Automated installation script

### references/
- [yt-dlp-official-doc.md](references/yt-dlp-official-doc.md) - Official documentation reference
- [format-guide.md](references/format-guide.md) - Format selection guide

### assets/
- [config](assets/config) - Configuration file template

---

**For more information**, see [Official Documentation](https://github.com/yt-dlp/yt-dlp#readme) and [YouTube-DL Wiki](https://github.com/ytdl-org/youtube-dl/wiki).
