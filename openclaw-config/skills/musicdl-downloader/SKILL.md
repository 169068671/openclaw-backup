---
name: musicdl-downloader
description: Lightweight lossless music downloader supporting 50+ platforms including NetEase Cloud Music, QQ Music, Kugou, Kuwo, Migu, Bilibili, Joox, YouTube, Spotify, etc. Use when downloading music, audiobooks, or playlists from supported Chinese and international music platforms.
---

# Musicdl Downloader

## Overview

Musicdl-downloader enables downloading music and audiobooks from 50+ platforms including NetEase Cloud Music, QQ Music, Kugou, Kuwo, Migu, Bilibili, Joox, YouTube, Spotify, Apple Music, and more. It supports single tracks, playlists, albums, and high-quality lossless formats.

## Quick Start

### Install musicdl

```bash
# Using pip
pip install musicdl

# From source
git clone https://github.com/CharlesPikachu/musicdl.git
cd musicdl
pip install .
```

### Basic Usage

```bash
# Search and download music
musicdl <song_name>

# Search and download playlist
musicdl -p <playlist_name>

# Search and download album
musicdl -a <album_name>
```

---

## Installation

### Prerequisites

- Python 3.7+
- No external dependencies required (pure Python)

### Installation Methods

**1. pip (Recommended)**
```bash
pip install musicdl
```

**2. From Source**
```bash
git clone https://github.com/CharlesPikachu/musicdl.git
cd musicdl
pip install .
```

**3. Using pip with specific version**
```bash
pip install musicdl==2.9.7
```

---

## Supported Platforms

### Chinese Music Platforms

| Platform | Support | Features |
|----------|---------|----------|
| NetEase Cloud Music | ✅ | Search, download, playlists, albums |
| QQ Music | ✅ | Search, download, playlists, albums |
| Kugou Music | ✅ | Search, download, playlists, albums |
| Kuwo Music | ✅ | Search, download, playlists, albums |
| Migu Music | ✅ | Search, download, playlists, albums |
| Bilibili | ✅ | Search, download music |
| Joox | ✅ | Search, download |
| TIDAL | ✅ | Search, download |

### International Platforms

| Platform | Support | Features |
|----------|---------|----------|
| YouTube | ✅ | Search, download |
| Spotify | ✅ | Search, download |
| Apple Music | ✅ | Search, download |
| Qobuz | ✅ | Search, download (lossless) |
| SoundCloud | ✅ | Search, download |

### Audiobook Platforms

| Platform | Support | Features |
|----------|---------|----------|
| Ximalaya | ✅ | Search, download audiobooks |
| Lazy Audio | ✅ | Search, download audiobooks |
| Litchi FM | ✅ | Search, download audiobooks |
| Qingting FM | ✅ | Search, download audiobooks |

---

## Common Tasks

### 1. Search and Download Single Track

```bash
musicdl <song_name>

# Example
musicdl 周杰伦 稻香
```

### 2. Search and Download Playlist

```bash
musicdl -p <playlist_name>

# Example
musicdl -p 流行歌曲
```

### 3. Search and Download Album

```bash
musicdl -a <album_name>

# Example
musicdl -a 情歌
```

### 4. Download Specific Platform

```bash
# Specify platform
musicdl <song_name> -p netease
musicdl <song_name> -p qq
musicdl <song_name> -p youtube
```

### 5. Download with Quality Selection

```bash
# Lossless quality
musicdl <song_name> -q lossless

# High quality
musicdl <song_name> -q 320
```

---

## Command Reference

### Main Options

| Option | Short | Description | Example |
|--------|--------|-------------|---------|
| --help | -h | Show help | -h |
| --version | -v | Show version | -v |
| --platform | -p | Specify platform | -p netease |
| --quality | -q | Audio quality | -q 320 |
| --output | -o | Output directory | -o ./downloads |
| --playlist | - | Search playlist | -p |
| --album | -a | Search album | -a |
| --limit | - | Download limit | --limit 10 |

### Platform Codes

| Platform | Code |
|----------|------|
| NetEase Cloud Music | netease |
| QQ Music | qq |
| Kugou Music | kugou |
| Kuwo Music | kuwo |
| Migu Music | migu |
| Bilibili | bilibili |
| Joox | joox |
| TIDAL | tidal |
| YouTube | youtube |
| Spotify | spotify |
| Apple Music | apple |
| Qobuz | qobuz |
| SoundCloud | soundcloud |
| Ximalaya | ximalaya |
| Lazy Audio | lazy |
| Litchi FM | litchi |
| Qingting FM | qingting |

### Quality Options

| Quality | Description |
|---------|-------------|
| lossless | Lossless quality (best) |
| 320 | 320kbps MP3 |
| 192 | 192kbps MP3 |
| 128 | 128kbps MP3 |

---

## Configuration

### Configuration File

Create `musicdl_config.json` in your home directory:

```json
{
  "platform": "netease",
  "quality": "lossless",
  "output_dir": "./downloads",
  "download_lyrics": true,
  "limit": 10
}
```

---

## Examples by Platform

### NetEase Cloud Music

```bash
# Search and download
musicdl 稻香 -p netease

# Download playlist
musicdl -p 流行歌 -p netease
```

### QQ Music

```bash
# Search and download
musicdl 光辉岁月 -p qq

# Download album
musicdl -a 情歌 -p qq
```

### Bilibili

```bash
# Search and download
musicdl 哔哩哩哩之歌 -p bilibili
```

### YouTube

```bash
# Search and download
musicdl song -p youtube
```

### Spotify

```bash
# Search and download
musicdl song -p spotify
```

---

## Troubleshooting

### Download Failed

**Problem:** Download failed

**Solutions:**
1. Check if platform is supported
2. Verify network connection
3. Try different quality setting
4. Check if song/playlist exists

### Platform Not Found

**Problem:** Platform not recognized

**Solution:**
```bash
# List supported platforms
musicdl --help
```

### Slow Download

**Problem:** Download is slow

**Solutions:**
1. Check internet speed
2. Try lower quality setting
3. Limit concurrent downloads: `--limit 5`

### Quality Not Available

**Problem:** Lossless quality not available

**Solution:**
- Not all platforms support lossless quality
- Try lower quality: `-q 320`

---

## Tips

1. **Use specific platform** for better search results
2. **Test with single track** before downloading playlists
3. **Check platform support** before downloading
4. **Use configuration file** for persistent settings
5. **Respect copyright** - for personal use only

---

## Resources

### scripts/
- [install_musicdl.sh](scripts/install_musicdl.sh) - Automated installation script

### references/
- [musicdl-platforms.md](references/musicdl-platforms.md) - Complete platform list and features
- [musicdl-official-doc.md](references/musicdl-official-doc.md) - Official documentation reference

### assets/
- [musicdl_config.json](assets/musicdl_config.json) - Configuration file template

---

## Legal Disclaimer

**This tool is for educational and research purposes only.**
- Commercial use is prohibited
- Respect copyright and terms of each platform
- For personal use only
- Do not redistribute downloaded content

---

**For more information**, see [Official Documentation](https://musicdl.readthedocs.io/) and [GitHub Repository](https://github.com/CharlesPikachu/musicdl).
