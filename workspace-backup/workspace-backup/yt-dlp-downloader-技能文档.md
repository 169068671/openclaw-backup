# yt-dlp Downloader 技能

> 技能创建日期：2026-03-03
> 基于 yt-dlp 开源项目：https://github.com/yt-dlp/yt-dlp

---

## 📋 技能概述

**技能名称**：yt-dlp-downloader
**技能类型**：综合视频下载工具
**开源项目**：yt-dlp - 综合视频下载器
**GitHub Stars**：100k+ ⭐⭐⭐⭐⭐
**状态**：✅ 已打包并提交

---

## 🎯 功能特性

### 核心功能
- ✅ 支持1000+网站（YouTube, Bilibili, Vimeo, Twitter等）
- ✅ 下载单个视频
- ✅ 下载播放列表/合集
- ✅ 下载音频（MP3, M4A, WAV等）
- ✅ 下载字幕（多种格式）
- ✅ 下载缩略图和元数据
- ✅ 高级格式选择
- ✅ 视频质量过滤
- ✅ 批量下载

### 支持的平台（部分）

| 平台 | URL格式 | 特性 |
|-----|---------|------|
| YouTube | youtube.com/watch?v= | 支持章节、4K、字幕 |
| Bilibili | bilibili.com/video/ | 支持大会员、弹幕 |
| Twitter/X | twitter.com/status/ | 支持视频和图片 |
| TikTok | tiktok.com/@user/video/ | 无水印下载 |
| Instagram | instagram.com/p/ | 支持Reels |
| Vimeo | vimeo.com/ | 支持高清 |
| Twitch | twitch.tv/ | 支持直播/VOD |

---

## 📦 技能结构

```
yt-dlp-downloader/
├── SKILL.md                              # 技能主文档
├── scripts/
│   └── install_yt-dlp.sh               # 自动安装脚本
├── references/
│   ├── yt-dlp-official-doc.md           # 官方文档参考
│   └── format-guide.md                   # 格式选择指南
└── assets/
    └── config                           # 配置文件模板
```

---

## 📄 文件说明

### SKILL.md

技能主文档，包含：
- 快速开始指南
- 安装方法（pip, 源码, 二进制）
- 常见任务示例
- 格式选择指南
- 平台特定选项
- 高级功能（过滤、批量、存档）
- 故障排查

### scripts/install_yt-dlp.sh

自动安装脚本，支持：
1. pip 安装
2. pip + FFmpeg 安装（推荐）
3. 预编译二进制安装
4. 源码安装

### references/yt-dlp-official-doc.md

官方文档参考，包含：
- 基本用法
- 命令行选项完整列表
- 输出模板
- 平台特定示例
- 字幕下载
- 音频提取
- 性能优化

### references/format-guide.md

格式选择详细指南，包含：
- 格式代码说明
- 格式字符串示例
- 分辨率/编码/文件格式限制
- 组合格式
- 实际应用示例
- 格式速查表

### assets/config

配置文件模板，包含：
- 输出目录和文件名设置
- 视频和音频格式
- 字幕和缩略图选项
- 播放列表选项
- 外部下载器配置
- 速度和重试设置

---

## 🚀 快速开始

### 1. 安装 yt-dlp

```bash
# 使用 pip（推荐）
pip install yt-dlp

# 或使用技能提供的安装脚本
bash /path/to/yt-dlp-downloader/scripts/install_yt-dlp.sh
```

### 2. 安装 FFmpeg（推荐）

```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg
```

### 3. 下载视频

```bash
# 下载单个视频（最佳质量）
yt-dlp https://www.youtube.com/watch?v=VIDEO_ID

# 下载音频
yt-dlp -x --audio-format mp3 URL

# 下载播放列表
yt-dlp URL/playlist
```

---

## 📚 使用示例

### YouTube

```bash
# 下载视频
yt-dlp https://www.youtube.com/watch?v=dQw4w9WgXcQ

# 下载4K视频
yt-dlp -f "bestvideo[height<=2160]+bestaudio" URL

# 下载章节和字幕
yt-dlp --write-subs --write-auto-subs URL
```

### Bilibili

```bash
# 下载视频
yt-dlp https://www.bilibili.com/video/BV1xxxxx/

# 使用 Cookie（需要大会员）
yt-dlp --cookies cookies.txt URL

# 下载弹幕
yt-dlp --write-subs URL
```

### Twitter/X

```bash
# 下载推文视频
yt-dlp "https://twitter.com/user/status/TWEET_ID"

# 下载用户所有视频
yt-dlp "https://twitter.com/user"
```

### TikTok

```bash
# 下载无水印视频
yt-dlp https://www.tiktok.com/@user/video/123456

# 下载用户视频
yt-dlp https://www.tiktok.com/@user
```

---

## 🎛️ 常用命令选项

| 选项 | 简写 | 说明 | 示例 |
|-----|------|------|------|
| --format | -f | 视频格式 | -f "bestvideo+bestaudio" |
| --extract-audio | -x | 提取音频 | -x |
| --audio-format | - | 音频格式 | --audio-format mp3 |
| --output | -o | 输出文件名 | -o "%(title)s.%(ext)s" |
| --write-subs | - | 下载字幕 | --write-subs |
| --write-thumbnail | - | 下载缩略图 | --write-thumbnail |
| --list-formats | -F | 列出可用格式 | -F |
| --cookies | - | Cookie 文件 | --cookies cookies.txt |

---

## 🔧 格式选择

### 常见格式字符串

| 格式字符串 | 说明 |
|---------|------|
| `best` | 最佳可用格式 |
| `bestvideo+bestaudio` | 最佳视频+最佳音频 |
| `bestvideo[height<=1080]+bestaudio` | 最高1080p |
| `bestvideo[height<=720]+bestaudio` | 最高720p |
| `bestvideo[ext=mp4]+bestaudio[ext=m4a]` | 仅 MP4 格式 |
| `bestvideo[vcodec^=avc]+bestaudio` | H.264 编码优先 |

---

## 💡 高级用法

### 批量下载

```bash
# 下载 URL 列表
cat urls.txt | xargs -I {} yt-dlp {}

# 下载播放列表（限制数量）
yt-dlp --playlist-end 10 URL/playlist

# 下载特定范围
yt-dlp --playlist-items 1-5 URL/playlist
```

### 过滤下载

```bash
# 只下载10分钟以上的视频
yt-dlp --match-filter "duration >= 600" URL/playlist

# 只下载2024年的视频
yt-dlp --match-filter "upload_date >= 20240101" URL/playlist

# 排除直播流
yt-dlp --match-filter "is_live != true" URL/playlist
```

### 存档下载

```bash
# 记录已下载的视频
yt-dlp --download-archive downloaded.txt URL/playlist

# 下次运行时跳过已下载的视频
```

---

## ⚙️ 配置文件

### 配置文件位置

```bash
# Linux/macOS
~/.config/yt-dlp/config

# Windows
%APPDATA%\yt-dlp\config
```

### 配置示例

```ini
[OPTIONS]
# 输出目录
output = ./downloads/%(uploader)s/%(title)s.%(ext)s

# 视频格式
format = bestvideo+bestaudio

# 提取音频
extractaudio = false
audioformat = mp3

# 字幕
writesubs = true
subtitleslangs = en,zh-CN

# 外部下载器
external_downloader = aria2c

# 下载存档
download_archive = ./downloaded.txt
```

---

## ❓ 常见问题

### Q: 如何安装 FFmpeg？

A:
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows
# 下载从 https://ffmpeg.org/
```

### Q: 如何更新 yt-dlp？

A:
```bash
pip install --upgrade yt-dlp
```

### Q: 下载速度很慢怎么办？

A:
1. 使用 aria2c: `yt-dlp --external-downloader aria2c URL`
2. 增加并发: `yt-dlp --concurrent-fragments 4 URL`
3. 使用代理: `yt-dlp --proxy socks5://127.0.0.1:1080 URL`

### Q: 如何查看支持的网站？

A:
```bash
yt-dlp --list-extractors
```

---

## 📞 参考资料

- **yt-dlp 官方文档**：https://github.com/yt-dlp/yt-dlp
- **GitHub 仓库**：https://github.com/yt-dlp/yt-dlp
- **Wiki**：https://github.com/yt-dlp/yt-dlp/wiki
- **问题反馈**：https://github.com/yt-dlp/yt-dlp/issues

---

## 📝 技能创建记录

| 日期 | 操作 | 备注 |
|------|------|------|
| 2026-03-03 16:12 | 初始化技能 | 创建技能目录结构 |
| 2026-03-03 16:12 | 编写 SKILL.md | 完整的使用指南 |
| 2026-03-03 16:12 | 创建安装脚本 | 支持 pip, 源码, 二进制安装 |
| 2026-03-03 16:12 | 创建参考文档 | 官方文档和格式指南 |
| 2026-03-03 16:12 | 创建配置模板 | yt-dlp 配置文件 |
| 2026-03-03 16:12 | 打包技能 | 生成 .skill 文件 |
| 2026-03-03 16:12 | 提交到 Git | 保存到 openclaw-backup |

---

## ✅ 验证状态

- [x] 技能结构完整
- [x] SKILL.md 文档完整
- [x] 安装脚本可执行
- [x] 参考文档齐全
- [x] 配置模板正确
- [x] 技能打包成功
- [x] 已提交到 GitHub

---

## 🎓 技能设计原则

遵循 skill-creator 规范：

1. **简洁为主**：仅包含必要信息
2. **渐进式披露**：metadata → SKILL.md → references
3. **分层组织**：scripts, references, assets 分离
4. **实用导向**：提供具体示例和常见用例
5. **资源优化**：脚本可执行，参考按需加载

---

## 🆚 与 yutto 技能对比

| 特性 | yt-dlp-downloader | yutto-downloader |
|-----|------------------|-----------------|
| 支持平台 | 1000+ | 仅 Bilibili |
| GitHub Stars | 100k+ | 1.7k |
| 视频质量 | 多种 | 多种 |
| 音频提取 | ✅ | ✅ |
| 字幕下载 | ✅ | ✅ |
| 批量下载 | ✅ | ✅ |
| GUI 支持 | 第三方 | 第三方 |
| 推荐场景 | 综合下载 | Bilibili 专用 |

**建议**：
- 综合下载：使用 yt-dlp-downloader
- Bilibili 专用：使用 yutto-downloader

---

**技能文件**：`yt-dlp-downloader.skill`
**GitHub 提交**：a667685
**仓库地址**：https://github.com/169068671/openclaw-backup

---

## 📌 安装技能

**方式1：手动安装**
```bash
# 复制技能文件到 OpenClaw skills 目录
cp yt-dlp-downloader.skill ~/.openclaw/skills/
```

**方式2：OpenClaw 自动识别**
- 将 .skill 文件放在技能目录
- OpenClaw 会自动加载

---

**技能创建完成！** ✅

现在你可以使用这个技能从1000+网站下载视频了！🎬
