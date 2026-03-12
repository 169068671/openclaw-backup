# Cookie 相关技能总览

**创建日期：** 2026-03-12
**更新日期：** 2026-03-12

---

## 📦 技能概览

这里有 **5 个** 与 Cookie 认证和格式转换相关的技能：

| 技能 | 功能 | 主要用途 |
|------|------|---------|
| **browser-cookies-exporter** | 从浏览器导出 cookies | 从 Chrome、Firefox 等提取认证信息 |
| **youtube-auth-exporter** | YouTube/Google 认证导出 | 专门用于 YouTube 和 Google 服务 |
| **notebooklm-auth-exporter** | NotebookLM 认证导出 | 专门用于 NotebookLM 服务 |
| **cookie-converter** | Cookie 格式双向转换 | Netscape ↔ Playwright ↔ JSON |
| **yt-dlp-downloader** | 视频下载（支持 cookies） | 使用 cookies 下载需要认证的视频 |

---

## 🔄 技能关系图

```
browser-cookies-exporter
        ↓ (导出 Netscape 格式)
    cookies.txt
        ↓ (cookie-converter)
    storage_state.json
        ↓ (部署到服务器)
    ┌───────────────┬───────────────┐
    ↓               ↓               ↓
yt-dlp-downloader  NotebookLM    Playwright
(下载视频)        (AI 学习)     (浏览器自动化)
```

---

## 🎯 常用工作流

### 工作流1：Chrome → YouTube 下载

```bash
# 1. 从 Chrome 导出 cookies
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# 2. 使用 cookies 下载视频
yt-dlp --cookies /tmp/google-cookies.txt "VIDEO_URL"
```

**相关技能：**
- browser-cookies-exporter
- yt-dlp-downloader

---

### 工作流2：Chrome → NotebookLM (VPS 部署)

```bash
# 1. 从 Chrome 导出 cookies
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# 2. 转换为 Playwright 格式
cookie-converter netscape-to-playwright \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# 3. 部署到 VPS
sshpass -p 'password' scp /tmp/storage_state.json \
  root@vps:/root/.config/notebooklm/session.json

# 4. 验证
ssh root@vps "notebooklm list"
```

**相关技能：**
- browser-cookies-exporter
- cookie-converter
- notebooklm-auth-exporter

---

### 工作流3：NotebookLM (VPS) → YouTube 下载

```bash
# 1. 从 VPS 下载 storage state
sshpass -p 'password' scp \
  root@vps:/root/.config/notebooklm/session.json \
  /tmp/storage_state.json

# 2. 转换为 Netscape 格式
cookie-converter playwright-to-netscape \
  /tmp/storage_state.json \
  /tmp/google-cookies.txt

# 3. 使用 cookies 下载视频
yt-dlp --cookies /tmp/google-cookies.txt "VIDEO_URL"
```

**相关技能：**
- cookie-converter
- yt-dlp-downloader

---

### 工作流4：检查和编辑 Cookies

```bash
# 1. 转换为 JSON（易于阅读）
cookie-converter playwright-to-json \
  /tmp/storage_state.json \
  /tmp/cookies.json

# 2. 查看内容
cat /tmp/cookies.json | python3 -m json.tool | less

# 3. 编辑 JSON
nano /tmp/cookies.json

# 4. 转换回 Playwright
cookie-converter json-to-playwright \
  /tmp/cookies.json \
  /tmp/storage_state_updated.json
```

**相关技能：**
- cookie-converter

---

## 📚 技能文档位置

### 核心 Cookie 工具

| 技能 | 文档位置 |
|------|----------|
| **browser-cookies-exporter** | `/home/admin/.local/bin/browser-cookies-exporter` |
| **cookie-converter** | `/home/admin/openclaw/workspace/Cookie Converter使用指南.md` |
|  | `/home/admin/openclaw/workspace/cookie-converter/SKILL.md` |

### 服务专用导出

| 技能 | 文档位置 |
|------|----------|
| **youtube-auth-exporter** | `/home/admin/openclaw/workspace/youtube-auth-exporter/SKILL.md` |
| **notebooklm-auth-exporter** | `/home/admin/openclaw/workspace/notebooklm-auth-exporter/notebooklm-auth-exporter/SKILL.md` |
|  | `/home/admin/openclaw/workspace/NotebookLM认证指南.md` |

### 使用技能

| 技能 | 文档位置 |
|------|----------|
| **yt-dlp-downloader** | `/home/admin/openclaw/workspace/YouTube技能使用指南.md` |
|  | `/home/admin/openclaw/workspace/yt-dlp-downloader/yt-dlp-downloader/SKILL.md` |
| **notebooklm** | `/home/admin/openclaw/workspace/NotebookLM技能使用指南.md` |
|  | `/home/admin/openclaw/workspace/skills/notebooklm/SKILL.md` |

---

## 🆚 技能对比

### 导出工具对比

| 特性 | browser-cookies-exporter | youtube-auth-exporter | notebooklm-auth-exporter |
|------|------------------------|----------------------|------------------------|
| **支持浏览器** | Chrome, Firefox, Brave, Edge | Chrome | Chrome |
| **目标服务** | 任意 | YouTube/Google | NotebookLM |
| **输出格式** | Netscape | Playwright | Playwright |
| **通用性** | ✅ 高 | ⚠️ 中 | ⚠️ 低 |
| **专用性** | ❌ 无 | ✅ 高 | ✅ 高 |

**使用建议：**
- 通用导出：使用 `browser-cookies-exporter`
- YouTube 专用：使用 `youtube-auth-exporter`
- NotebookLM 专用：使用 `notebooklm-auth-exporter`

---

### 格式对比

| 格式 | 用途 | 工具 |
|------|------|------|
| **Netscape** | yt-dlp, curl, wget | `--cookies` 参数 |
| **Playwright** | Playwright, NotebookLM | `storage_state.json` |
| **JSON** | 手动检查、编辑、脚本 | 自定义处理 |

**转换工具：** `cookie-converter`

---

## 🔧 命令速查

### Cookie 导出

```bash
# 从 Chrome 导出（通用）
browser-cookies-exporter .google.com /tmp/cookies.txt

# 从 Firefox 导出
browser-cookies-exporter --browser firefox .google.com /tmp/cookies.txt
```

### Cookie 转换

```bash
# Netscape → Playwright
cookie-converter netscape-to-playwright cookies.txt storage.json

# Playwright → Netscape
cookie-converter playwright-to-netscape storage.json cookies.txt

# Playwright → JSON
cookie-converter playwright-to-json storage.json cookies.json
```

### 使用 Cookies

```bash
# 使用 yt-dlp 下载
yt-dlp --cookies /tmp/cookies.txt "VIDEO_URL"

# 使用 curl 请求
curl --cookie /tmp/cookies.txt "URL"

# 加载到 Playwright
playwright codegen --load-storage=/tmp/storage_state.json "URL"
```

---

## 💡 使用建议

### 什么时候使用哪个技能？

**场景1：导出 Chrome cookies**
- 使用 `browser-cookies-exporter`
- 支持所有浏览器（Chrome, Firefox, Brave, Edge）
- 输出 Netscape 格式

**场景2：YouTube 视频下载**
- 使用 `yt-dlp-downloader`
- 配合 `browser-cookies-exporter` 导出 cookies
- 使用 `cookie-converter` 转换格式（如果需要）

**场景3：NotebookLM 部署**
- 使用 `notebooklm-auth-exporter`
- 配合 `browser-cookies-exporter` 导出 cookies
- 使用 `cookie-converter` 转换为 Playwright 格式

**场景4：格式转换**
- 使用 `cookie-converter`
- 支持所有格式之间的双向转换
- 可以查看、编辑、过滤 cookies

**场景5：检查和调试**
- 使用 `cookie-converter` 转换为 JSON
- 手动查看和编辑 cookies
- 转换回原始格式

---

## ⚠️ 安全提醒

1. **Cookies 包含敏感信息**：认证令牌、会话 ID、个人偏好
2. **不要分享 Cookie 文件**：特别是不要提交到 Git 或公开仓库
3. **定期更新**：Cookies 通常 14 天后过期，需要重新导出
4. **安全存储**：使用受保护的目录，设置适当权限
5. **删除旧文件**：及时清理过期的 Cookie 文件

---

## 🔗 完整工作流示例

### 示例：完整的 NotebookLM 设置流程

```bash
# 1. 在 Chrome 中登录 Google
# (手动操作）
# 访问 https://accounts.google.com 并登录
# 访问 https://notebooklm.google.com 确认可访问

# 2. 导出 cookies
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# 3. 转换为 Playwright 格式
cookie-converter netscape-to-playwright \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# 4. 部署到 VPS
sshpass -p 'Whj001.Whj001' scp /tmp/storage_state.json \
  root@76.13.219.143:/root/.config/notebooklm/session.json

# 5. 验证认证
ssh root@76.13.219.143 "notebooklm list"

# 6. 使用 NotebookLM
ssh root@76.13.219.143
notebooklm create "我的研究"
notebooklm source add "https://www.youtube.com/watch?v=VIDEO_ID"
notebooklm generate audio --wait
notebooklm download audio ./podcast.mp3
```

**涉及技能：**
- browser-cookies-exporter
- cookie-converter
- notebooklm-auth-exporter
- notebooklm

---

### 示例：从 NotebookLM 导出 cookies 下载视频

```bash
# 1. 从 VPS 下载 storage state
sshpass -p 'Whj001.Whj001' scp \
  root@76.13.219.143:/root/.config/notebooklm/session.json \
  /tmp/storage_state.json

# 2. 转换为 Netscape 格式
cookie-converter playwright-to-netscape \
  /tmp/storage_state.json \
  /tmp/google-cookies.txt

# 3. 使用 cookies 下载 YouTube 视频
yt-dlp --cookies /tmp/google-cookies.txt \
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
  -o "/tmp/%(title)s.%(ext)s" \
  "https://www.youtube.com/watch?v=VIDEO_ID"
```

**涉及技能：**
- cookie-converter
- yt-dlp-downloader

---

## 📖 推荐阅读顺序

如果你是新手，建议按以下顺序阅读：

1. **Cookie Format Converter 使用指南** - 了解格式转换
2. **browser-cookies-exporter** - 学习如何导出 cookies
3. **YouTube 技能使用指南** - 学习如何下载视频
4. **NotebookLM 技能使用指南** - 学习如何使用 NotebookLM
5. **NotebookLM 认证指南** - 学习如何在 VPS 上部署认证

---

**Cookie 相关技能已完全整合！** 🎉

所有技能之间都有交叉引用，你可以轻松找到需要的信息！🍪
