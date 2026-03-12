# NotebookLM 技能使用指南

## 📚 已恢复的技能包

### 1. **notebooklm** (主要技能)
**位置：** `/home/admin/openclaw/workspace/skills/notebooklm/`

**功能：**
- Google NotebookLM 非官方 Python API
- 创建和管理笔记本
- 添加源文件（YouTube、网页、文本、PDF 等）
- 生成多种内容：
  - 🎙️ 音频播客（AI 生成对话）
  - 📹 视频（多种风格）
  - 📊 思维导图
  - 📄 幻灯片/讲义
  - 📝 测验/学习指南
  - 🎴 抽认卡
- 下载生成的内容

---

### 2. **notebooklm-youtube-importer** (YouTube 导入)
**位置：** `/home/admin/openclaw/workspace/skills/notebooklm-youtube-importer/`

**功能：**
- 将 YouTube 播放列表导入到 NotebookLM 笔记本
- 使用 yt-dlp 自动提取视频链接
- 批量导入、自动去重
- 后台处理、实时进度显示

**包含脚本：**
- `youtube_importer_with_ytdlp.py` - 使用 yt-dlp 提取链接
- `youtube_browser_importer.py` - 使用浏览器自动化
- `notebooklm_youtube_importer_v2.py` - 第二版导入器

---

## 🖥️ 部署位置

### VPS (Hostinger 76.13.219.143)
**已安装：** ✅ notebooklm v0.3.3
**位置：** `/usr/local/bin/notebooklm`
**认证状态：** ✅ 已登录

**VPS 使用：**
```bash
# 连接到 VPS
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143

# 使用 notebooklm
notebooklm create "My Research"
notebooklm source add "https://www.youtube.com/watch?v=XXX"
notebooklm generate audio --wait
notebooklm download audio ./podcast.mp3
```

---

### 本地机器
**安装状态：** ❌ 未安装
**原因：** 主要在 VPS 上使用（避免本地资源占用）

**如需本地安装：**
```bash
# 基本安装
pip install notebooklm-py

# 浏览器登录支持（首次设置必需）
pip install "notebooklm-py[browser]"

# 安装 Chromium（Playwright 需要）
playwright install chromium

# 首次登录
notebooklm login
```

---

## 🚀 VPS 快速开始

### 1. 创建笔记本

```bash
# 在 VPS 上
notebooklm create "FreeCAD 教程"
```

### 2. 添加 YouTube 视频作为源

```bash
# 添加单个视频
notebooklm source add "https://www.youtube.com/watch?v=VIDEO_ID"

# 添加多个视频
notebooklm source add "VIDEO_URL_1" "VIDEO_URL_2" "VIDEO_URL_3"
```

### 3. 生成音频播客

```bash
# 生成 AI 播客（需要等待）
notebooklm generate audio --wait

# 下载生成的音频
notebooklm download audio ./podcast.mp3
```

### 4. 生成其他内容

```bash
# 生成思维导图
notebooklm generate mindmap
notebooklm download mindmap ./mindmap.png

# 生成幻灯片
notebooklm generate slide-deck
notebooklm download slide-deck ./slides.pdf

# 生成测验
notebooklm generate quiz
notebooklm download quiz --format markdown ./quiz.md
```

### 5. 查看笔记本

```bash
# 列出所有笔记本
notebooklm list

# 查看当前笔记本详情
notebooklm info
```

---

## 📥 批量导入 YouTube 播放列表

### 方法1：使用 notebooklm-youtube-importer 技能

```bash
# 进入技能目录
cd /home/admin/openclaw/workspace/skills/notebooklm-youtube-importer

# 使用 yt-dlp 提取并导入
python3 youtube_importer_with_ytdlp.py "PLAYLIST_URL" "笔记本名称"

# 或者使用 v2 版本
python3 notebooklm_youtube_importer_v2.py "PLAYLIST_URL" "笔记本名称"
```

**成功案例：** FreeCAD Python 教程（38个视频）成功导入

---

## 🔧 常用命令

### 笔记本管理

```bash
# 创建笔记本
notebooklm create "笔记本名称"

# 列出所有笔记本
notebooklm list

# 切换笔记本
notebooklm use "笔记本名称"

# 删除笔记本
notebooklm delete "笔记本名称"
```

### 源文件管理

```bash
# 添加 URL 源
notebooklm source add "URL"

# 添加文本源
notebooklm source add --text "内容文本"

# 添加文件源
notebooklm source add --file /path/to/file.pdf

# 列出当前源文件
notebooklm source list

# 删除源文件
notebooklm source remove "SOURCE_ID"
```

### 内容生成

```bash
# 生成音频播客（需要等待）
notebooklm generate audio --wait

# 生成视频
notebooklm generate video --style whiteboard

# 生成思维导图
notebooklm generate mindmap

# 生成幻灯片
notebooklm generate slide-deck

# 生成测验
notebooklm generate quiz

# 生成学习指南
notebooklm generate study-guide

# 生成抽认卡
notebooklm generate flashcards
```

### 下载内容

```bash
# 下载音频
notebooklm download audio ./podcast.mp3

# 下载视频
notebooklm download video ./video.mp4

# 下载思维导图
notebooklm download mindmap ./mindmap.png

# 下载幻灯片
notebooklm download slide-deck ./slides.pdf

# 下载测验（多种格式）
notebooklm download quiz --format markdown ./quiz.md
notebooklm download quiz --format html ./quiz.html

# 下载所有内容
notebooklm download all ./output/
```

---

## 📝 实用工作流

### 工作流1：YouTube 教程 → AI 播客

```bash
# 1. 创建笔记本
notebooklm create "编程教程"

# 2. 导入 YouTube 播放列表（使用技能）
cd /home/admin/openclaw/workspace/skills/notebooklm-youtube-importer
python3 notebooklm_youtube_importer_v2.py "PLAYLIST_URL" "编程教程"

# 3. 切换回 notebooklm 目录
cd ~

# 4. 生成 AI 播客
notebooklm generate audio --wait

# 5. 下载播客
notebooklm download audio ./tutorial-podcast.mp3

# 6. 传输到本地
# 从 VPS 下载文件到本地机器
```

### 工作流2：研究资料 → 学习材料

```bash
# 1. 创建笔记本
notebooklm create "研究报告"

# 2. 添加多个来源
notebooklm source add "https://arxiv.org/abs/1234.5678"
notebooklm source add "https://example.com/research.pdf"
notebooklm source add --file ./local-notes.txt

# 3. 生成学习材料
notebooklm generate study-guide --wait
notebooklm generate quiz --wait
notebooklm generate flashcards --wait

# 4. 下载所有内容
notebooklm download all ./study-materials/
```

### 工作流3：内容创作 → 多格式输出

```bash
# 1. 创建笔记本
notebooklm create "内容创作"

# 2. 添加素材
notebooklm source add "https://example.com/blog-post"
notebooklm source add --file ./outline.txt

# 3. 生成多种格式
notebooklm generate infographic --orientation portrait
notebooklm generate video --style whiteboard
notebooklm generate slide-deck

# 4. 下载所有内容
notebooklm download all ./content-assets/
```

---

## ⚠️ 常见问题

### 问题1：认证失败

**错误信息：**
```
Authentication failed
```

**解决方案：**
```bash
# 在 VPS 上重新登录
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143

# 使用 browser-cookies-exporter 导出 Google cookies
# 详见：/home/admin/openclaw/workspace/youtube-auth-exporter/SKILL.md

# 或者使用 notebooklm login（如果浏览器可用）
notebooklm login
```

### 问题2：源文件添加失败

**错误信息：**
```
Failed to add source
```

**解决方案：**
1. 检查 URL 是否可访问
2. 检查 YouTube 视频是否公开（私人视频需要认证）
3. 检查网络连接
4. 确保使用正确的 cookies（如需要）

### 问题3：内容生成超时

**错误信息：**
```
Generation timeout
```

**解决方案：**
1. 使用 `--wait` 参数等待生成完成
2. 减少源文件数量（太多源文件可能需要更长时间）
3. 检查 NotebookLM 服务是否可用
4. 稍后重试

### 问题4：下载失败

**错误信息：**
```
Failed to download content
```

**解决方案：**
```bash
# 检查输出目录权限
chmod 755 ./output/

# 使用绝对路径
notebooklm download audio /tmp/podcast.mp3

# 检查磁盘空间
df -h
```

---

## 🔗 相关文档

- **notebooklm 主技能：** `/home/admin/openclaw/workspace/skills/notebooklm/SKILL.md`
- **notebooklm-youtube-importer：** `/home/admin/openclaw/workspace/skills/notebooklm-youtube-importer/SKILL.md`
- **Cookie Format Converter：** `/home/admin/openclaw/workspace/Cookie Converter使用指南.md`
- **NotebookLM 认证指南：** `/home/admin/openclaw/workspace/NotebookLM认证指南.md`
- **官方 GitHub：** https://github.com/joschan21/notebooklm-py
- **CLI 参考：** https://github.com/teng-lin/notebooklm-py/blob/main/docs/cli-reference.md

---

## 💡 提示

1. **非官方 API**：使用未记录的 Google API，可能随时更改
2. **最佳用途**：适合原型、研究和个人项目，不适合生产环境
3. **VPS 优势**：在 VPS 上运行可以避免本地资源占用
4. **批量操作**：使用 notebooklm-youtube-importer 技能批量导入视频
5. **内容多样性**：NotebookLM 可以生成多种格式，适合不同用途

---

**配置完成日期：** 2026-03-12
**最后更新：** 2026-03-12
