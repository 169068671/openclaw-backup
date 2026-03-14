# YouTube Access Skill - 使用指南

## 快速开始（3 步）

### 1. 转换 Cookies

```bash
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py ~/Downloads/cookies.json
```

### 2. 验证 Cookies

```bash
~/.openclaw/skills/youtube-access/yt-validate.sh
```

### 3. 下载视频

```bash
~/.openclaw/skills/youtube-access/yt-download.sh "https://www.youtube.com/watch?v=VIDEO_ID"
```

---

## 常用命令

### Cookies 管理

```bash
# 转换为 Playwright 格式（用于 agent-browser）
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py \
  ~/Downloads/cookies.json --playwright /tmp/youtube_storage_state.json

# 转换为 Netscape 格式（用于 yt-dlp）
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py \
  ~/Downloads/cookies.json --netscape /tmp/youtube_cookies.txt

# 验证 cookies 完整性
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py \
  ~/Downloads/cookies.json --validate

# 显示 cookies 详细信息
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py \
  ~/Downloads/cookies.json --info
```

### 验证 Cookies

```bash
# 基本验证
~/.openclaw/skills/youtube-access/yt-validate.sh

# 使用自定义 cookies 文件
~/.openclaw/skills/youtube-access/yt-validate.sh -c ~/Downloads/cookies.txt

# 不使用代理
~/.openclaw/skills/youtube-access/yt-validate.sh -p none
```

### 下载视频

```bash
# 基本下载
~/.openclaw/skills/youtube-access/yt-download.sh "https://www.youtube.com/watch?v=VIDEO_ID"

# 下载字幕
~/.openclaw/skills/youtube-access/yt-download.sh -s "https://www.youtube.com/watch?v=VIDEO_ID"

# 指定输出目录
~/.openclaw/skills/youtube-access/yt-download.sh -o ~/Videos "https://www.youtube.com/watch?v=VIDEO_ID"

# 720p 质量
~/.openclaw/skills/youtube-access/yt-download.sh \
  -f "best[height<=720]" "https://www.youtube.com/watch?v=VIDEO_ID"
```

---

## 视频格式

```bash
# 最佳质量（MP4）
-f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"

# 720p
-f "best[height<=720]"

# 1080p
-f "best[height<=1080]"

# 480p
-f "best[height<=480]"

# 仅视频
-f "bestvideo"

# 仅音频
-f "bestaudio"
```

---

## 代理配置

### 启动 SSH 隧道

```bash
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143
```

### 检查隧道状态

```bash
netstat -tlnp | grep 1080
```

### 不使用代理

```bash
~/.openclaw/skills/youtube-access/yt-download.sh -p none "VIDEO_URL"
```

---

## 故障排除

### Cookies 无效

```bash
# 验证 cookies
~/.openclaw/skills/youtube-access/yt-validate.sh -v

# 如果无效，重新导出 cookies
```

### 网络不可达

```bash
# 检查 SSH 隧道
netstat -tlnp | grep 1080

# 启动隧道
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143
```

### 下载失败

```bash
# 详细输出
~/.openclaw/skills/youtube-access/yt-download.sh -v "VIDEO_URL"

# 检查 yt-dlp 版本
yt-dlp --version

# 更新 yt-dlp
pip install --upgrade yt-dlp
```

---

## 完整工作流示例

### 首次使用

```bash
# 1. 使用 BestCookier 导出 cookies（JSON 格式）到 ~/Downloads/cookies.json

# 2. 转换 cookies
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py \
  ~/Downloads/cookies.json

# 3. 验证 cookies
~/.openclaw/skills/youtube-access/yt-validate.sh

# 4. 下载视频
~/.openclaw/skills/youtube-access/yt-download.sh \
  "https://www.youtube.com/watch?v=VIDEO_ID"
```

### 下载带字幕的视频

```bash
~/.openclaw/skills/youtube-access/yt-download.sh \
  -s "https://www.youtube.com/watch?v=VIDEO_ID"
```

### 批量下载

```bash
# 创建视频列表
cat > /tmp/video_list.txt << EOF
https://www.youtube.com/watch?v=VIDEO_1
https://www.youtube.com/watch?v=VIDEO_2
https://www.youtube.com/watch?v=VIDEO_3
EOF

# 批量下载
while IFS= read -r url; do
  ~/.openclaw/skills/youtube-access/yt-download.sh "$url"
done < /tmp/video_list.txt
```

---

## 测试技能

```bash
# 运行完整测试
~/.openclaw/skills/youtube-access/test.sh
```

---

## 相关技能

- **yt-dlp-downloader**: yt-dlp 下载技能（基础版）
- **youtube-auth-exporter**: YouTube 认证导出技能
- **browser-cookies-exporter**: 浏览器 cookies 导出技能
- **ssh-tunnel**: SSH 隧道管理技能

---

## 详细文档

查看完整文档：`~/.openclaw/skills/youtube-access/SKILL.md`
