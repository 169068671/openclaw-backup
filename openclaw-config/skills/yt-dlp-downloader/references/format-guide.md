# yt-dlp 格式选择指南

> 如何选择最佳的视频格式和编码

---

## 格式代码

### 格式代码结构

```
[格式代码] [扩展名] [分辨率] [帧率] [视频编码] [音频编码]

示例:
137  mp4  1920x1080  30  avc  none
248  webm  1920x1080  30  vp9  none
251  webm  1920x1080  60  vp9  none
```

### 常见格式代码

| 代码 | 扩展名 | 分辨率 | 帧率 | 视频编码 | 音频编码 | 说明 |
|-----|---------|---------|------|---------|---------|------|
| 137 | mp4 | 1920x1080 | 30 | avc | none | 1080p 30fps (MP4) |
| 138 | mp4 | 1920x1080 | 60 | avc | none | 1080p 60fps (MP4) |
| 22 | mp4 | 1280x720 | 30 | avc | none | 720p 30fps (MP4) |
| 18 | mp4 | 640x360 | 30 | avc | none | 360p 30fps (MP4) |
| 248 | webm | 1920x1080 | 30 | vp9 | none | 1080p 30fps (WebM) |
| 249 | webm | 1920x1080 | 60 | vp9 | none | 1080p 60fps (WebM) |
| 278 | webm | 1920x1080 | 30 | vp9 | opus | 1080p 30fps (WebM + Audio) |
| 313 | mp4 | 3840x2160 | 30 | avc | none | 4K 30fps (MP4) |
| 271 | webm | 3840x2160 | 30 | vp9 | none | 4K 30fps (WebM) |

---

## 格式选择字符串

### 基本格式字符串

| 格式字符串 | 说明 | 示例 |
|---------|------|------|
| `best` | 选择最佳可用格式 | 自动选择最佳质量 |
| `bestvideo+bestaudio` | 最佳视频+最佳音频 | 需要合并（FFmpeg） |
| `worst` | 选择最差可用格式 | 最小文件 |

### 分辨率限制

| 格式字符串 | 说明 | 示例 |
|---------|------|------|
| `bestvideo[height<=1080]+bestaudio` | 最高1080p | 限制在1080p以下 |
| `bestvideo[height<=720]+bestaudio` | 最高720p | 限制在720p以下 |
| `bestvideo[height<=480]+bestaudio` | 最高480p | 限制在480p以下 |
| `bestvideo[height<=360]+bestaudio` | 最高360p | 限制在360p以下 |

### 文件格式限制

| 格式字符串 | 说明 | 示例 |
|---------|------|------|
| `bestvideo[ext=mp4]+bestaudio[ext=m4a]` | 仅 MP4 | 强制 MP4 格式 |
| `bestvideo[ext=webm]+bestaudio[ext=webm]` | 仅 WebM | 强制 WebM 格式 |
| `bestvideo[ext=mp4]+bestaudio` | MP4 视频 + 任意音频 | MP4 视频，音频任意 |

### 编码限制

| 格式字符串 | 说明 | 示例 |
|---------|------|------|
| `bestvideo[vcodec^=avc]+bestaudio` | H.264 编码 | 优先 H.264 |
| `bestvideo[vcodec^=vp9]+bestaudio` | VP9 编码 | 优先 VP9 |
| `bestvideo[vcodec^=av1]+bestaudio` | AV1 编码 | 优先 AV1 |

---

## 组合格式

### 多个条件组合

```bash
# 1080p 以下，仅 MP4
bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]

# 720p 以下，H.264 编码
bestvideo[height<=720][vcodec^=avc]+bestaudio

# 仅视频，不含音频
bestvideo

# 仅音频
bestaudio
```

### 优先级格式

```bash
# 优先 MP4，其次 WebM
(bestvideo[ext=mp4]+bestaudio[ext=m4a])/(bestvideo[ext=webm]+bestaudio[ext=webm])/best

# 优先 H.264，其次 VP9，最后 AV1
(bestvideo[vcodec^=avc]+bestaudio)/(bestvideo[vcodec^=vp9]+bestaudio)/(bestvideo[vcodec^=av1]+bestaudio)
```

---

## 实际应用示例

### YouTube 下载

```bash
# 下载最佳质量
yt-dlp -f "bestvideo+bestaudio" URL

# 下载1080p
yt-dlp -f "bestvideo[height<=1080]+bestaudio" URL

# 下载仅 MP4 格式
yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" URL
```

### Bilibili 下载

```bash
# 下载最佳质量
yt-dlp -f "bestvideo+bestaudio" URL

# 下载1080p HEVC
yt-dlp -f "bestvideo[vcodec^=hevc][height<=1080]+bestaudio" URL

# 下载仅 AVC 编码
yt-dlp -f "bestvideo[vcodec^=avc]+bestaudio" URL
```

### Twitter 下载

```bash
# 下载最佳质量
yt-dlp -f "bestvideo+bestaudio" URL

# 下载仅视频（不含音频）
yt-dlp -f "bestvideo" URL
```

---

## 特殊情况处理

### 无音频格式

某些视频只有视频流，没有音频流：

```bash
# 下载视频流（无音频）
yt-dlp -f "bestvideo" URL

# 如果有音频则一起下载，否则仅视频
yt-dlp -f "(bestvideo+bestaudio)/bestvideo" URL
```

### DASH 流

现代网站使用 DASH 格式，视频和音频分开：

```bash
# 自动合并 DASH 流
yt-dlp -f "bestvideo+bestaudio" URL

# FFmpeg 会自动合并视频和音频
```

### HDR 视频

HDR 视频可能有特殊格式代码：

```bash
# 优先 SDR，其次 HDR
bestvideo[vcodec!*=hdr]+bestaudio/bestvideo+bestaudio

# 仅下载 HDR 视频
bestvideo[vcodec*=hdr]+bestaudio
```

---

## 查看可用格式

### 列出所有格式

```bash
# 列出视频的所有可用格式
yt-dlp -F URL

# 输出示例：
# 137  mp4  1920x1080  30  avc  none
# 248  webm  1920x1080  30  vp9  none
# 278  webm  1920x1080  30  vp9  opus
```

### 格式输出说明

| 列 | 说明 | 示例 |
|-----|------|------|
| ID | 格式代码 | 137 |
| EXT | 文件扩展名 | mp4 |
| RES | 分辨率 | 1920x1080 |
| FPS | 帧率 | 30 |
| VCODEC | 视频编码 | avc |
| ACODEC | 音频编码 | opus |
| MORE INFO | 其他信息 | DASH, 60fps |

---

## 最佳实践

### 1. 使用 FFmpeg

```bash
# 最佳方案：视频+音频合并
yt-dlp -f "bestvideo+bestaudio" URL

# 需要安装 FFmpeg
```

### 2. 选择合适格式

```bash
# YouTube: MP4 兼容性最好
yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" URL

# Bilibili: HEVC 质量更好
yt-dlp -f "bestvideo[vcodec^=hevc]+bestaudio" URL
```

### 3. 限制文件大小

```bash
# 限制在720p以下
yt-dlp -f "bestvideo[height<=720]+bestaudio" URL

# 限制文件大小（仅用于某些格式）
yt-dlp -f "best[filesize<100M]" URL
```

### 4. 使用输出模板

```bash
# 包含格式代码
-o "%(id)s - %(format)s - %(title)s.%(ext)s"

# 包含分辨率
-o "%(title)s (%(height)sp).%(ext)s"
```

---

## 故障排查

### Q: 视频和音频无法合并？

A: 安装 FFmpeg：
```bash
sudo apt-get install ffmpeg  # Ubuntu/Debian
brew install ffmpeg           # macOS
```

### Q: 想要特定格式但不在列表中？

A:
1. 使用 `-F` 查看所有可用格式
2. 使用精确的格式代码：`-f 137`

### Q: 下载质量很低？

A:
1. 检查是否需要登录（cookies）
2. 使用更高格式：`-f "bestvideo+bestaudio"`
3. 检查视频源是否支持高质量

---

## 格式速查表

| 需求 | 格式字符串 |
|-----|----------|
| 最佳质量 | `bestvideo+bestaudio` |
| 1080p | `bestvideo[height<=1080]+bestaudio` |
| 720p | `bestvideo[height<=720]+bestaudio` |
| 仅 MP4 | `bestvideo[ext=mp4]+bestaudio[ext=m4a]` |
| 仅音频 | `bestaudio` |
| H.264 编码 | `bestvideo[vcodec^=avc]+bestaudio` |

---

## 参考文档

- **官方文档**: https://github.com/yt-dlp/yt-dlp#format-selection
- **格式选择**: https://github.com/yt-dlp/yt-dlp#format-selection-examples
- **Wiki**: https://github.com/yt-dlp/yt-dlp/wiki
