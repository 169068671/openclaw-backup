# NotebookLM YouTube 播放列表导入器

## 简介

这个技能帮助您将 YouTube 播放列表中的所有视频导入到 NotebookLM 笔记本，支持多种导入方式。

---

## 功能

1. **自动提取播放列表** - 使用 yt-dlp 提取所有视频链接
2. **创建笔记本** - 为播放列表创建新笔记本
3. **批量导入** - 批量导入所有视频到笔记本
4. **去重处理** - 自动跳过已存在的视频，只添加新的
5. **后台处理** - 不等待每个视频完成，提高速度
6. **进度显示** - 实时显示导入进度

---

## 使用方法

### ⭐ 方式一：使用 yt-dlp 自动提取（推荐）

```bash
# 进入 skill 目录
cd ~/.openclaw/skills/notebooklm-youtube-importer

# 使用 yt-dlp 提取并导入
./youtube_importer_with_ytdlp.py ytdlp \
  "https://www.youtube.com/playlist?list=PLAYLIST_ID" \
  "我的笔记本"

# 从视频链接提取
./youtube_importer_with_ytdlp.py ytdlp \
  "https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID" \
  "教程"
```

**功能特点：**
- ✅ **自动提取** - 使用 yt-dlp 自动提取播放列表中的所有视频
- ✅ **快速可靠** - yt-dlp 比浏览器提取更快更稳定
- ✅ **自动去重** - 自动去除重复的视频链接
- ✅ **批量导入** - 批量导入所有视频到笔记本
- ✅ **后台处理** - 不等待每个视频完成
- ✅ **进度显示** - 实时显示导入进度

---

## 使用示例

### 示例 1：使用 yt-dlp 导入（推荐）⭐

```bash
cd ~/.openclaw/skills/notebooklm-youtube-importer

# 导入 FreeCAD 教程
./youtube_importer_with_ytdlp.py ytdlp \
  "https://www.youtube.com/watch?v=KujiAIHNRKQ&list=PLWuyJLVUNtc15o92Bo6SgtYzXt7zlSIsh" \
  "FreeCAD Python 教程"

# 导入 Django 教程
./youtube_importer_with_ytdlp.py ytdlp \
  "https://www.youtube.com/watch?v=IhiR9osXhYs&list=PLpzgvcyYOSTDGU5tYikH14x5JUoFFB0o7" \
  "Python Django 教程"
```

### 示例 2：从播放列表 URL 导入

```bash
cd ~/.openclaw/skills/notebooklm-youtube-importer

# 直接从播放列表 URL 导入
./youtube_importer_with_ytdlp.py ytdlp \
  "https://www.youtube.com/playlist?list=PLAYLIST_ID" \
  "我的笔记本"
```

### 示例 3：快速导入（不指定笔记本名称）

```bash
cd ~/.openclaw/skills/notebooklm-youtube-importer

# 使用默认笔记本名称 "YouTube 播放列表"
./youtube_importer_with_ytdlp.py ytdlp \
  "https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID"
```

---

## 代理配置

### 如果需要代理访问 YouTube

```bash
# 启动 SSH 隧道
sshpass -p 'password' ssh -N -D 1080 -f user@host

# 设置代理环境变量
export HTTP_PROXY="socks5://127.0.0.1:1080"
export HTTPS_PROXY="socks5://127.0.0.1:1080"
export ALL_PROXY="socks5://127.0.0.1:1080"
```

**注意：** 脚本已内置代理配置，无需手动设置。

---

## 脚本说明

### 1. youtube_importer_with_ytdlp.py（推荐）⭐

**功能：** 使用 yt-dlp 提取播放列表并导入

**使用：**
```bash
./youtube_importer_with_ytdlp.py ytdlp <YouTube_URL> [笔记本名称]
```

**特点：**
- ✅ 自动提取所有视频链接
- ✅ 批量导入到笔记本
- ✅ 自动去重
- ✅ 后台处理（不等待）

---

## 常见问题

### Q: 如何获取 YouTube 播放列表 ID？

**A:** 播放列表 URL 格式：
```
https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID
```
其中 `PLAYLIST_ID` 就是播放列表 ID（以 `PL` 开头的字符串）。

### Q: yt-dlp 提取失败怎么办？

**A:**
1. 检查代理配置：`netstat -tlnp | grep 1080`
2. 检查 yt-dlp 版本：`yt-dlp --version`
3. 手动测试：`yt-dlp --flat-playlist --get-url "URL" --proxy "socks5://127.0.0.1:1080"`

### Q: 导入速度很慢怎么办？

**A:**
- NotebookLM 处理需要时间，请耐心等待
- 脚本使用后台处理模式，不等待每个视频
- 可以稍后检查笔记本状态

### Q: 如何查看已添加的视频？

**A:**
```bash
notebooklm use <notebook_id>
notebooklm source list
```

### Q: 如何删除笔记本？

**A:**
```bash
notebooklm delete -n <notebook_id> -y
```

---

## 依赖

- **Python 3.7+**
- **notebooklm-py**: `pip install notebooklm-py`
- **yt-dlp**: `pip install --upgrade yt-dlp`
- **代理**（可选）：访问 YouTube 需要代理

---

## 技能文件

- **SKILL.md**: `~/.openclaw/skills/notebooklm-youtube-importer/SKILL.md`（本文件）
- **yt-dlp 导入器**: `~/.openclaw/skills/notebooklm-youtube-importer/youtube_importer_with_ytdlp.py`
- **FreeCAD 导入器**: `~/.openclaw/skills/notebooklm-youtube-importer/notebooklm_youtube_importer.py`
- **YouTube 导入器**: `~/.openclaw/skills/notebooklm-youtube-importer/youtube_to_notebooklm.py`
- **去重脚本**: `/tmp/delete_duplicates.py`

---

## 工作流程

### 使用 yt-dlp 导入的完整流程：

1. **提取视频链接**
   ```bash
   yt-dlp --flat-playlist --get-url "URL" --proxy "socks5://127.0.0.1:1080"
   ```

2. **创建笔记本**
   ```bash
   notebooklm create "笔记本名称"
   ```

3. **批量导入视频**
   ```bash
   for url in $(cat /tmp/videos.txt); do
       notebooklm use <notebook_id>
       notebooklm source add "$url"
   done
   ```

4. **后台处理**
   - NotebookLM 在后台处理所有视频
   - 可以稍后检查状态

---

## 许可证

MIT License

---

**版本**: 2.0.0
**创建日期**: 2026-03-07
**更新日期**: 2026-03-07
