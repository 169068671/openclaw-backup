# NotebookLM - Google NotebookLM 非官方 Python API

## 简介

**NotebookLM** 是 Google 的研究助手工具，可以创建笔记本、添加源文件、生成各种内容（音频、视频、测验、思维导图等）。

**notebooklm-py** 是一个非官方的 Python API，提供完整的程序化访问 NotebookLM 的功能。

---

## ⚠️ 重要提醒

**非官方库**：
- ✅ 完全免费、开源（MIT License）
- ⚠️ 使用未记录的 Google API（可能随时更改）
- ⚠️ 不受 Google 官方支持
- ✅ 最适合原型、研究和个人项目

**最佳用途**：
- 📚 研究自动化
- 🤖 AI Agent 集成
- 📥 批量下载和导出
- 🎙️ 内容生成（音频、视频、测验等）

---

## 安装

### 基本安装

```bash
pip install notebooklm-py
```

### 浏览器登录支持（首次设置必需）⭐

```bash
# 安装浏览器支持
pip install "notebooklm-py[browser]"

# 安装 Playwright Chromium
playwright install chromium
```

### 安装验证

```bash
notebooklm --version
# 输出：NotebookLM CLI, version 0.3.3
```

---

## 🌐 代理配置

notebooklm-py 使用 httpx 库，支持通过环境变量配置代理。

### SOCKS5 代理（SSH 隧道）⭐

```bash
# 1. 启动 SSH 隧道
sshpass -p 'password' ssh -N -D 1080 -f user@host

# 2. 设置代理环境变量
export HTTP_PROXY="socks5://127.0.0.1:1080"
export HTTPS_PROXY="socks5://127.0.0.1:1080"
export ALL_PROXY="socks5://127.0.0.1:1080"

# 3. 使用 notebooklm
notebooklm login
```

### HTTP 代理

```bash
# 设置 HTTP 代理
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"

# 使用 notebooklm
notebooklm create "My Research"
```

### 代理绕过（某些主机不使用代理）

```bash
# 设置代理
export HTTP_PROXY="socks5://127.0.0.1:1080"
export HTTPS_PROXY="socks5://127.0.0.1:1080"

# 设置绕过（某些主机直接连接）
export NO_PROXY="localhost,*.internal.com,127.0.0.1"

# 使用 notebooklm
notebooklm list
```

### 推荐配置（本地）⭐

**~/.bashrc 或 ~/.zshrc**：

```bash
# NotebookLM 代理配置
export HTTP_PROXY="socks5://127.0.0.1:1080"
export HTTPS_PROXY="socks5://127.0.0.1:1080"
export ALL_PROXY="socks5://127.0.0.1:1080"
export NO_PROXY="localhost,*.internal.com,127.0.0.1"

# SSH 隧道启动函数
function start-ssh-tunnel() {
    sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143
    echo "✅ SSH 隧道已启动（SOCKS5: 127.0.0.1:1080）"
}

# 停止隧道
function stop-ssh-tunnel() {
    ps aux | grep "ssh.*1080" | awk '{print $2}' | xargs kill
    echo "✅ SSH 隧道已停止"
}
```

### 使用示例

```bash
# 1. 启动 SSH 隧道
start-ssh-tunnel

# 2. 设置代理（如果已在 ~/.bashrc 中配置，可跳过）
export HTTP_PROXY="socks5://127.0.0.1:1080"
export HTTPS_PROXY="socks5://127.0.0.1:1080"

# 3. 使用 notebooklm
notebooklm login
notebooklm create "My Research"
notebooklm source add "https://www.youtube.com/watch?v=XXX"

# 4. 停止隧道（可选）
stop-ssh-tunnel
```

### 验证代理

```bash
# 检查环境变量
echo $HTTP_PROXY
echo $HTTPS_PROXY

# 测试代理连接
curl --socks5 127.0.0.1:1080 https://www.google.com
```

---

## 📋 功能总览

| 类别 | 功能 | 说明 |
|------|------|------|
| **笔记本** | 创建、列出、重命名、删除 | 管理研究项目 |
| **源文件** | URL, YouTube, PDF, 文本, Google Drive | 添加各种类型的源文件 |
| **聊天** | 提问、对话历史、自定义角色 | 与源文件对话 |
| **研究** | Web/Drive 研究代理 | 自动化研究任务 |
| **生成内容** | 音频、视频、幻灯片、测验、思维导图 | 生成多种格式的内容 |
| **下载/导出** | MP3, MP4, PDF, PNG, CSV, JSON, Markdown | 批量下载所有生成的内容 |

---

## 🔧 CLI 使用

### 1. 认证（首次使用）⭐

```bash
# 打开浏览器进行登录
notebooklm login
```

**说明**：
- 首次使用需要在浏览器中登录 Google
- 会自动打开 Chromium 浏览器
- 登录后凭据会保存到本地

---

### 2. 创建笔记本并添加源文件

```bash
# 创建新笔记本
notebooklm create "My Research"

# 使用特定笔记本
notebooklm use <notebook_id>

# 添加源文件（URL）
notebooklm source add "https://en.wikipedia.org/wiki/Artificial_Intelligence"

# 添加源文件（PDF）
notebooklm source add "./paper.pdf"

# 添加源文件（YouTube）
notebooklm source add "https://www.youtube.com/watch?v=XXX"
```

---

### 3. 与源文件聊天

```bash
# 提问
notebooklm ask "What are the key themes?"

# 使用自定义角色
notebooklm ask "Summarize this for a 10-year-old" --persona child
```

---

### 4. 生成内容

#### 音频概述（播客）

```bash
# 生成音频（默认设置）
notebooklm generate audio

# 自定义说明
notebooklm generate audio "make it engaging"

# 等待完成
notebooklm generate audio --wait
```

**音频选项**：
- 4 种格式（deep-dive, brief, critique, debate）
- 3 种长度
- 50+ 种语言

---

#### 视频概述

```bash
# 生成视频（默认样式）
notebooklm generate video

# 自定义样式
notebooklm generate video --style whiteboard

# 等待完成
notebooklm generate video --wait
```

**视频样式**：
- 9 种视觉样式（classic, whiteboard, kawaii, anime 等）

---

#### 测验

```bash
# 生成测验（默认难度）
notebooklm generate quiz

# 自定义难度
notebooklm generate quiz --difficulty hard

# 自定义数量
notebooklm generate quiz --quantity more
```

---

#### 闪示卡

```bash
# 生成闪示卡（默认数量）
notebooklm generate flashcards

# 自定义数量
notebooklm generate flashcards --quantity more

# 自定义难度
notebooklm generate flashcards --difficulty hard
```

---

#### 幻灯片

```bash
# 生成幻灯片（详细格式）
notebooklm generate slide-deck

# 讲者格式
notebooklm generate slide-deck --format presenter
```

---

#### 信息图

```bash
# 生成信息图（默认）
notebooklm generate infographic

# 自定义方向
notebooklm generate infographic --orientation portrait
```

**信息图选项**：
- 3 种方向（portrait, landscape, square）
- 3 种细节级别

---

#### 思维导图

```bash
# 生成思维导图
notebooklm generate mind-map
```

---

#### 数据表

```bash
# 生成数据表（自定义结构）
notebooklm generate data-table "compare key concepts"
```

---

### 5. 下载生成的内容

```bash
# 下载音频（MP3）
notebooklm download audio ./podcast.mp3

# 下载视频（MP4）
notebooklm download video ./overview.mp4

# 下载测验（Markdown）
notebooklm download quiz --format markdown ./quiz.md

# 下载测验（JSON）
notebooklm download quiz --format json ./quiz.json

# 下载闪示卡（JSON）
notebooklm download flashcards --format json ./cards.json

# 下载幻灯片（PDF）
notebooklm download slide-deck ./slides.pdf

# 下载思维导图（JSON）
notebooklm download mind-map ./mindmap.json

# 下载数据表（CSV）
notebooklm download data-table ./data.csv
```

---

## 🐍 Python API

### 基本使用

```python
import asyncio
from notebooklm import NotebookLMClient

async def main():
    # 从存储加载客户端
    async with await NotebookLMClient.from_storage() as client:
        # 创建笔记本
        nb = await client.notebooks.create("Research")

        # 添加源文件（URL）
        await client.sources.add_url(nb.id, "https://example.com", wait=True)

        # 聊天
        result = await client.chat.ask(nb.id, "Summarize this")
        print(result.answer)

        # 生成音频
        status = await client.artifacts.generate_audio(nb.id, instructions="make it fun")
        await client.artifacts.wait_for_completion(nb.id, status.task_id)
        await client.artifacts.download_audio(nb.id, "podcast.mp3")

asyncio.run(main())
```

---

### 高级功能

#### 生成测验并下载

```python
# 生成测验
status = await client.artifacts.generate_quiz(nb.id)

# 等待完成
await client.artifacts.wait_for_completion(nb.id, status.task_id)

# 下载为 JSON
await client.artifacts.download_quiz(nb.id, "quiz.json", output_format="json")
```

---

#### 生成思维导图并导出

```python
# 生成思维导图
result = await client.artifacts.generate_mind_map(nb.id)

# 下载为 JSON
await client.artifacts.download_mind_map(nb.id, "mindmap.json")
```

---

## 📚 NotebookLM vs Web UI

### API 提供的功能（Web UI 没有）

| 功能 | 说明 |
|------|------|
| **批量下载** | 一次性下载所有同类型的生成内容 |
| **测验/闪示卡导出** | 获取结构化的 JSON、Markdown 或 HTML |
| **思维导图数据提取** | 导出分层 JSON 供可视化工具使用 |
| **数据表 CSV 导出** | 下载结构化表格为电子表格 |
| **幻灯片 PPTX** | 下载可编辑的 PowerPoint 文件（Web UI 仅 PDF）|
| **幻灯片修订** | 用自然语言提示修改单个幻灯片 |
| **报告模板自定义** | 在内置格式模板中附加额外说明 |
| **保存聊天到笔记** | 将 Q&A 答案或对话历史保存为笔记本笔记 |
| **源文件全文访问** | 检索任何源文件的索引文本内容 |
| **程序化共享** | 无需 UI 管理权限 |

---

## 🌟 典型使用场景

### 1. 研究自动化

```bash
# 创建研究笔记本
notebooklm create "AI Research"

# 添加多个源文件
notebooklm source add "https://en.wikipedia.org/wiki/Artificial_Intelligence"
notebooklm source add "https://arxiv.org/pdf/2301.07041.pdf"
notebooklm source add "https://www.youtube.com/watch?v=XXX"

# 生成音频概述
notebooklm generate audio "Create an engaging podcast" --wait

# 下载所有生成的内容
notebooklm download audio ./ai-podcast.mp3
notebooklm download quiz ./ai-quiz.md
notebooklm download mind-map ./ai-mindmap.json
```

---

### 2. 教学内容生成

```bash
# 创建教学笔记本
notebooklm create "Lesson Plan"

# 添加课程材料
notebooklm source add "./lesson-text.pdf"

# 生成测验
notebooklm generate quiz --difficulty hard --quantity more

# 生成闪示卡
notebooklm generate flashcards --quantity many

# 下载所有内容
notebooklm download quiz --format markdown ./lesson-quiz.md
notebooklm download flashcards --format html ./lesson-cards.html
```

---

### 3. 内容营销

```bash
# 创建内容笔记本
notebooklm create "Content Marketing"

# 添加源材料
notebooklm source add "https://example.com/blog-post"

# 生成多种格式
notebooklm generate infographic --orientation portrait
notebooklm generate video --style whiteboard
notebooklm generate slide-deck

# 下载所有内容
notebooklm download infographic ./content-infographic.png
notebooklm download video ./content-video.mp4
notebooklm download slide-deck ./content-slides.pdf
```

---

## 🔧 配置

### 存储位置

**凭据存储**：`~/.config/notebooklm/`

**会话存储**：`~/.config/notebooklm/session.json`

---

## ⚠️ 故障排除

### 常见问题

**1. 登录失败**
```bash
# 确保已安装浏览器支持
pip install "notebooklm-py[browser]"
playwright install chromium

# 重新登录
notebooklm login
```

**2. 源文件添加失败**
- 检查 URL 是否可访问
- 检查文件路径是否正确
- 检查网络连接

**3. 生成内容失败**
- 检查源文件是否已添加
- 检查 NotebookLM 服务是否可用
- 尝试使用 `--wait` 参数

---

## 📖 参考文档

- [CLI 参考](https://github.com/teng-lin/notebooklm-py/blob/main/docs/cli-reference.md) - 完整命令文档
- [Python API](https://github.com/teng-lin/notebooklm-py/blob/main/docs/python-api.md) - 完整 API 参考
- [配置](https://github.com/teng-lin/notebooklm-py/blob/main/docs/configuration.md) - 存储和设置
- [故障排除](https://github.com/teng-lin/notebooklm-py/blob/main/docs/troubleshooting.md) - 常见问题和解决方案
- [API 稳定性](https://github.com/teng-lin/notebooklm-py/blob/main/docs/stability.md) - 版本策略和稳定性保证

---

## 📄 许可证

MIT License

---

## 🔗 相关链接

- GitHub: https://github.com/teng-lin/notebooklm-py
- PyPI: https://pypi.org/project/notebooklm-py/
- Google NotebookLM: https://notebooklm.google.com/

---

## 💡 最佳实践

1. **首次使用**：务必运行 `notebooklm login` 进行首次登录
2. **批量操作**：使用 `--wait` 参数等待生成完成
3. **源文件**：添加多个源文件以获得更好的结果
4. **自定义角色**：使用 `--persona` 参数定制聊天风格
5. **定期更新**：保持库更新以获得最新功能和修复

---

**版本**：0.3.3
**安装日期**：2026-03-07
