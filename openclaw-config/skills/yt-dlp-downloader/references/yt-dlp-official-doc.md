# yt-dlp 官方文档参考

> 基于 https://github.com/yt-dlp/yt-dlp

---

## 基本用法

### 下载单个视频

```bash
yt-dlp URL
```

### 下载音频

```bash
# 提取音频
yt-dlp -x URL

# 提取并转换为 MP3
yt-dlp -x --audio-format mp3 URL
```

### 下载播放列表

```bash
yt-dlp URL/playlist
```

---

## 命令行选项

### 主要选项

| 选项 | 简写 | 说明 | 示例 |
|-----|------|------|------|
| --format | -f | 视频格式 | -f "bestvideo+bestaudio" |
| --extract-audio | -x | 提取音频 | -x |
| --audio-format | - | 音频格式 | --audio-format mp3 |
| --output | -o | 输出文件名 | -o "%(title)s.%(ext)s" |
| --write-subs | - | 下载字幕 | --write-subs |
| --write-thumbnail | - | 下载缩略图 | --write-thumbnail |
| --list-formats | -F | 列出可用格式 | -F |
| --update | -U | 更新 yt-dlp | -U |
| --verbose | -v | 详细输出 | -v |

### 格式选择

| 格式字符串 | 说明 |
|---------|------|
| `best` | 最佳可用格式 |
| `bestvideo+bestaudio` | 最佳视频+最佳音频 |
| `bestvideo[height<=1080]+bestaudio` | 1080p 最高 |
| `bestvideo[ext=mp4]+bestaudio[ext=m4a]` | 仅 MP4 |

### 输出模板

```bash
# 基本模板
-o "%(title)s.%(ext)s"

# 包含上传者
-o "%(uploader)s - %(title)s.%(ext)s"

# 创建子目录
-o "downloads/%(uploader)s/%(title)s.%(ext)s"

# 包含日期
-o "%(upload_date)s - %(title)s.%(ext)s"

# 完整元数据
-o "%(id)s - %(title)s.%(ext)s"
```

---

## 支持的元数据字段

### 通用字段

| 字段 | 说明 | 示例 |
|-----|------|------|
| id | 视频 ID | dQw4w9WgXcQ |
| title | 标题 | Rick Astley |
| uploader | 上传者 | Rick Astley |
| upload_date | 上传日期 | 20241231 |
| duration | 时长（秒） | 212 |
| view_count | 观看次数 | 1000000 |
| like_count | 点赞次数 | 50000 |
| description | 描述 | 视频描述 |

### 格式字段

| 字段 | 说明 |
|-----|------|
| format | 格式代码 |
| ext | 文件扩展名 |
| height | 视频高度 |
| width | 视频宽度 |
| fps | 帧率 |
| vcodec | 视频编码 |
| acodec | 音频编码 |

---

## 平台特定选项

### YouTube

```bash
# 下载章节
yt-dlp --write-subs --write-auto-subs URL

# 下载4K视频
yt-dlp -f "bestvideo[height<=2160]+bestaudio" URL

# 下载特定日期范围
yt-dlp --datebefore 20240101 --dateafter 20230101 URL/channel

# 仅下载非直播内容
yt-dlp --match-filter "is_live != true" URL/channel
```

### Bilibili

```bash
# 使用 Cookie（需要大会员）
yt-dlp --cookies cookies.txt URL

# 下载弹幕
yt-dlp --write-subs URL

# 下载系列
yt-dlp --download-archive downloaded.txt URL/series
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
yt-dlp URL

# 下载用户视频
yt-dlp URL/user
```

---

## 高级功能

### 过滤器

```bash
# 只下载10分钟以上的视频
yt-dlp --match-filter "duration >= 600" URL/playlist

# 只下载2024年的视频
yt-dlp --match-filter "upload_date >= 20240101" URL/playlist

# 排除直播流
yt-dlp --match-filter "is_live != true" URL/playlist

# 组合过滤器
yt-dlp --match-filter "duration >= 600 & upload_date >= 20240101" URL/playlist
```

### 批量下载

```bash
# 下载URL列表
cat urls.txt | xargs -I {} yt-dlp {}

# 下载播放列表（限制数量）
yt-dlp --playlist-end 10 URL/playlist

# 下载特定范围
yt-dlp --playlist-items 1-5 URL/playlist
```

### 存档下载

```bash
# 记录已下载的视频
yt-dlp --download-archive downloaded.txt URL/playlist

# 下次运行时跳过已下载的视频
yt-dlp --download-archive downloaded.txt URL/playlist
```

---

## 字幕下载

### 下载字幕

```bash
# 下载所有字幕
yt-dlp --write-subs URL

# 下载特定语言
yt-dlp --write-subs --sub-lang en,zh-CN URL

# 下载自动生成的字幕
yt-dlp --write-auto-subs URL

# 下载所有字幕和自动字幕
yt-dlp --write-subs --write-auto-subs URL
```

### 字幕格式

yt-dlp 支持多种字幕格式：
- VTT (默认）
- SRT
- ASS

---

## 音频提取

### 提取音频

```bash
# 提取音频（最佳质量）
yt-dlp -x URL

# 提取并转换为 MP3
yt-dlp -x --audio-format mp3 URL

# 提取并转换为 M4A
yt-dlp -x --audio-format m4a URL

# 提取并转换为 WAV
yt-dlp -x --audio-format wav URL
```

---

## 性能优化

### 并发下载

```bash
# 使用更多并发片段
yt-dlp --concurrent-fragments 4 URL

# 使用外部下载器
yt-dlp --external-downloader aria2c URL
```

### 限制速度

```bash
# 限制下载速度（字节/秒）
yt-dlp --limit-rate 1M URL

# 限制下载速度（1MB/s）
yt-dlp --limit-rate 1024K URL
```

---

## 常见问题

### Q: 如何更新 yt-dlp？

A:
```bash
pip install --upgrade yt-dlp
```

### Q: FFmpeg 是必须的吗？

A: 不必须，但强烈推荐。FFmpeg 用于合并视频和音频流。

### Q: 如何下载受年龄限制的视频？

A:
1. 使用 cookies.txt: `yt-dlp --cookies cookies.txt URL`
2. cookies.txt 包含你的登录信息

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

## 更多信息

- **GitHub 仓库**: https://github.com/yt-dlp/yt-dlp
- **官方文档**: https://github.com/yt-dlp/yt-dlp#readme
- **问题反馈**: https://github.com/yt-dlp/yt-dlp/issues
- **Wiki**: https://github.com/yt-dlp/yt-dlp/wiki
