# YouTube 技能使用指南

## 📦 已安装的工具

| 工具 | 版本 | 用途 |
|------|------|------|
| **yt-dlp** | 2026.03.03 | 视频下载器（支持1000+网站） |
| **browser-cookies-exporter** | 自定义 | Chrome cookies 导出工具 |
| **FFmpeg** | 系统自带 | 视频处理和格式转换 |

---

## 🚀 快速开始

### 1. 下载普通 YouTube 视频

```bash
# 下载视频（最佳质量）
yt-dlp "https://www.youtube.com/watch?v=VIDEO_ID"

# 下载视频到指定目录
yt-dlp -o "/tmp/%(title)s.%(ext)s" "https://www.youtube.com/watch?v=VIDEO_ID"

# 下载视频并转换为 MP4
yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" "URL"
```

### 2. 下载需要登录的视频（年龄限制、私人视频）

**步骤1：导出 Chrome cookies**

```bash
# 确保Chrome正在运行并且你已登录 YouTube
browser-cookies-exporter .google.com /tmp/youtube-cookies.txt
```

**步骤2：使用 cookies 下载**

```bash
yt-dlp --cookies /tmp/youtube-cookies.txt "https://www.youtube.com/watch?v=VIDEO_ID"
```

### 3. 下载播放列表

```bash
# 下载整个播放列表
yt-dlp "https://www.youtube.com/playlist?list=PLAYLIST_ID"

# 下载播放列表到指定目录
yt-dlp -o "/tmp/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s" "PLAYLIST_URL"

# 下载播放列表（限制数量）
yt-dlp --playlist-end 10 "PLAYLIST_URL"  # 只下载前10个视频
```

### 4. 只下载音频

```bash
# 提取音频（最佳质量 MP3）
yt-dlp -x --audio-format mp3 "URL"

# 提取音频（最佳格式）
yt-dlp -x --audio-format best "URL"
```

---

## 🔧 高级用法

### 使用代理（访问被限制的网站）

```bash
# 使用 SOCKS5 代理（SSH 隧道）
yt-dlp --proxy socks5://127.0.0.1:1080 "URL"

# 使用 HTTP 代理
yt-dlp --proxy http://127.0.0.1:8888 "URL"
```

### 选择特定分辨率

```bash
# 只下载 1080p 视频
yt-dlp -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" "URL"

# 只下载 720p 视频
yt-dlp -f "bestvideo[height<=720]+bestaudio/best[height<=720]" "URL"
```

### 下载字幕

```bash
# 下载视频+字幕
yt-dlp --write-subs --sub-lang en,zh "URL"

# 自动生成字幕（如果可用）
yt-dlp --write-auto-subs "URL"
```

### 断点续传

```bash
# 下载中断后继续下载
yt-dlp -c "URL"

# 下载时跳过已存在的文件
yt-dlp --no-overwrites "URL"
```

---

## 📝 实用脚本

### 批量下载播放列表（带 cookies）

创建脚本 `download-playlist-with-auth.sh`：

```bash
#!/bin/bash
PLAYLIST_URL="$1"
COOKIES_FILE="/tmp/youtube-cookies.txt"
OUTPUT_DIR="/tmp/youtube-downloads"

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

# 下载播放列表
yt-dlp \
  --cookies "$COOKIES_FILE" \
  -o "$OUTPUT_DIR/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s" \
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
  --write-subs \
  --sub-lang zh,en \
  "$PLAYLIST_URL"

echo "✅ 下载完成！文件保存在: $OUTPUT_DIR"
```

使用方法：
```bash
chmod +x download-playlist-with-auth.sh
./download-playlist-with-auth.sh "PLAYLIST_URL"
```

### 导出并使用 cookies

创建脚本 `export-and-download.sh`：

```bash
#!/bin/bash
VIDEO_URL="$1"

# 导出 cookies
echo "🔑 正在导出 Chrome cookies..."
browser-cookies-exporter .google.com /tmp/youtube-cookies.txt

if [ $? -eq 0 ]; then
    echo "✅ Cookies 导出成功"
    echo "📥 开始下载视频..."
    yt-dlp \
      --cookies /tmp/youtube-cookies.txt \
      -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
      -o "/tmp/%(title)s.%(ext)s" \
      "$VIDEO_URL"
else
    echo "❌ Cookies 导出失败"
    exit 1
fi
```

使用方法：
```bash
chmod +x export-and-download.sh
./export-and-download.sh "https://www.youtube.com/watch?v=VIDEO_ID"
```

---

## ⚠️ 常见问题

### 问题1：Chrome 未运行

**错误信息：**
```
Error: No cookies found for domain '.google.com'
```

**解决方案：**
1. 打开 Chrome 浏览器
2. 登录到 YouTube（或目标网站）
3. 确保保持 Chrome 运行
4. 重新运行 cookie 导出命令

### 问题2：代理连接失败

**错误信息：**
```
Network is unreachable
```

**解决方案：**
1. 启动 SSH 隧道：
   ```bash
   sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143
   ```

2. 检查隧道状态：
   ```bash
   netstat -tlnp | grep 1080
   ```

3. 使用代理下载：
   ```bash
   yt-dlp --proxy socks5://127.0.0.1:1080 "URL"
   ```

### 问题3：视频下载速度慢

**解决方案：**
1. 选择更低的分辨率
2. 使用代理
3. 使用 `-N` 限制下载速度：
   ```bash
   yt-dlp -N 500K "URL"  # 限制500KB/s
   ```

### 问题4：FFmpeg 未找到

**错误信息：**
```
FFmpeg is not installed
```

**解决方案：**
```bash
sudo apt update
sudo apt install ffmpeg
```

---

## 📚 相关文档

- **yt-dlp-downloader 技能：** `/home/admin/openclaw/workspace/yt-dlp-downloader/yt-dlp-downloader/SKILL.md`
- **YouTube 认证导出：** `/home/admin/openclaw/workspace/youtube-auth-exporter/SKILL.md`
- **Cookie Format Converter：** `/home/admin/openclaw/workspace/Cookie Converter使用指南.md`
- **yt-dlp 官方文档：** https://github.com/yt-dlp/yt-dlp

---

## 🎯 推荐工作流

### 方案1：简单下载（无需登录）
```bash
yt-dlp "https://www.youtube.com/watch?v=VIDEO_ID"
```

### 方案2：下载需要登录的视频
```bash
# 1. 确保Chrome运行并登录
browser-cookies-exporter .google.com /tmp/youtube-cookies.txt

# 2. 使用cookies下载
yt-dlp --cookies /tmp/youtube-cookies.txt "URL"
```

### 方案3：批量下载播放列表（带字幕）
```bash
yt-dlp \
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
  --write-subs \
  --sub-lang zh,en \
  --cookies /tmp/youtube-cookies.txt \
  "PLAYLIST_URL"
```

---

## 💡 提示

1. **Cookies 有效期**：Chrome cookies 大约 14 天后过期，需要重新导出
2. **Cookie 文件安全**：cookies 文件包含你的登录信息，不要分享给他人
3. **断点续传**：使用 `-c` 参数可以在下载中断后继续下载
4. **批量下载**：先下载小部分测试，确认无误后再下载全部
5. **存储空间**：视频占用空间较大，确保有足够的磁盘空间

---

**配置完成日期：** 2026-03-12
**最后更新：** 2026-03-12
