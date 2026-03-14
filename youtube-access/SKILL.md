# YouTube Access Skill

## 功能说明

YouTube 访问技能 - 管理 YouTube cookies 和下载 YouTube 视频

### 主要功能

1. **Cookies 管理**
   - 从 BestCookier 导出的 JSON 文件转换为 Playwright/Netscape 格式
   - 验证 cookies 的完整性和有效性
   - 显示 cookies 的详细信息

2. **视频下载**
   - 使用 cookies 下载 YouTube 视频
   - 支持代理（SSH 隧道）
   - 支持字幕下载
   - 支持自定义视频格式

3. **Cookies 验证**
   - 测试 cookies 是否有效
   - 检查登录状态

---

## 安装位置

- **技能目录**: `~/.openclaw/skills/youtube-access/`
- **Python 管理器**: `yt-cookies-manager.py`
- **下载脚本**: `yt-download.sh`
- **验证脚本**: `yt-validate.sh`

---

## 快速开始

### 1. 从 BestCookier 导出 cookies

使用 BestCookier 浏览器插件导出 YouTube cookies（JSON 格式）

### 2. 转换 cookies

```bash
# 转换为 Playwright 和 Netscape 两种格式（默认）
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py ~/Downloads/cookies.json

# 仅转换为 Playwright 格式
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py \
  ~/Downloads/cookies.json --playwright /tmp/youtube_storage_state.json

# 仅转换为 Netscape 格式
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py \
  ~/Downloads/cookies.json --netscape /tmp/youtube_cookies.txt

# 验证 cookies 的完整性
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py \
  ~/Downloads/cookies.json --validate

# 显示 cookies 的详细信息
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py \
  ~/Downloads/cookies.json --info
```

### 3. 验证 cookies 是否有效

```bash
# 基本验证（使用默认的 cookies 文件和代理）
~/.openclaw/skills/youtube-access/yt-validate.sh

# 使用自定义 cookies 文件
~/.openclaw/skills/youtube-access/yt-validate.sh -c ~/Downloads/cookies.txt

# 不使用代理
~/.openclaw/skills/youtube-access/yt-validate.sh -p none

# 详细输出
~/.openclaw/skills/youtube-access/yt-validate.sh -v
```

### 4. 下载 YouTube 视频

```bash
# 基本下载
~/.openclaw/skills/youtube-access/yt-download.sh "https://www.youtube.com/watch?v=VIDEO_ID"

# 使用自定义 cookies 文件
~/.openclaw/skills/youtube-access/yt-download.sh \
  -c ~/Downloads/cookies.txt "https://www.youtube.com/watch?v=VIDEO_ID"

# 不使用代理
~/.openclaw/skills/youtube-access/yt-download.sh \
  -p none "https://www.youtube.com/watch?v=VIDEO_ID"

# 下载字幕
~/.openclaw/skills/youtube-access/yt-download.sh \
  -s "https://www.youtube.com/watch?v=VIDEO_ID"

# 指定输出目录
~/.openclaw/skills/youtube-access/yt-download.sh \
  -o ~/Videos "https://www.youtube.com/watch?v=VIDEO_ID"

# 自定义视频格式
~/.openclaw/skills/youtube-access/yt-download.sh \
  -f "best[height<=720]" "https://www.youtube.com/watch?v=VIDEO_ID"
```

---

## Cookies 转换格式说明

### Playwright storage_state.json

用于 agent-browser 或其他 Playwright 自动化工具

```json
{
  "cookies": [
    {
      "name": "SID",
      "value": "...",
      "domain": ".youtube.com",
      "path": "/",
      "expires": 1808041341.297748,
      "httpOnly": false,
      "secure": false,
      "sameSite": "Lax"
    }
  ],
  "origins": []
}
```

### Netscape cookies.txt

用于 yt-dlp、curl、wget 等命令行工具

```
# Netscape HTTP Cookie File
.youtube.com	TRUE	/	FALSE	1808041341	SID	...
.youtube.com	TRUE	/	TRUE	1808041341	APISID	...
```

---

## 代理配置

### SSH 隧道代理（推荐）

```bash
# 启动 SSH 隧道
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143

# 检查隧道状态
netstat -tlnp | grep 1080

# 使用代理（默认）
~/.openclaw/skills/youtube-access/yt-download.sh "https://www.youtube.com/watch?v=VIDEO_ID"
```

### 不使用代理

```bash
# 使用直连（需要网络支持）
~/.openclaw/skills/youtube-access/yt-download.sh \
  -p none "https://www.youtube.com/watch?v=VIDEO_ID"
```

---

## 视频格式说明

### 常用格式

```bash
# 最佳质量（MP4）
-f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"

# 720p
-f "best[height<=720]"

# 1080p
-f "best[height<=1080]"

# 仅视频
-f "bestvideo"

# 仅音频
-f "bestaudio"
```

### 字幕选项

```bash
# 下载字幕（中文简体、中文繁体、英文）
-s

# 所有字幕
--write-subs --sub-langs all
```

---

## 常见问题

### 1. Cookies 过期

Cookies 有效期通常为 14 天，过期后需要重新导出

**解决方法**：
- 使用 BestCookier 重新导出 cookies
- 再次运行转换脚本

### 2. 网络不可达

访问 YouTube 需要使用代理

**解决方法**：
```bash
# 检查 SSH 隧道状态
netstat -tlnp | grep 1080

# 如果未启动，启动 SSH 隧道
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143
```

### 3. n challenge solving failed

需要安装 JS runtime 和 EJS 组件

**解决方法**：
- 脚本已自动添加 `--js-runtimes node --remote-components ejs:github` 参数
- 确保已安装 Node.js

### 4. 登录状态检测失败

cookies 可能无效或已过期

**解决方法**：
```bash
# 验证 cookies
~/.openclaw/skills/youtube-access/yt-validate.sh -c /tmp/youtube_cookies.txt
```

---

## 技能依赖

### 必需工具

- **Python 3**: 运行 cookies 管理器
- **yt-dlp**: 下载 YouTube 视频
- **curl**: 测试网络连接
- **bash**: 运行 Shell 脚本

### 安装命令

```bash
# 安装 yt-dlp
pip install --upgrade yt-dlp

# 安装 Python 依赖
pip install --upgrade requests
```

---

## 安全提醒

- Cookies 包含敏感信息，请勿分享
- 定期更换 YouTube 密码
- 注意保护 cookies 文件安全
- 建议 cookies 文件保存在本地，不要上传到云端

---

## 相关技能

- **yt-dlp-downloader**: yt-dlp 下载技能（基础版）
- **youtube-auth-exporter**: YouTube 认证导出技能
- **browser-cookies-exporter**: 浏览器 cookies 导出技能
- **ssh-tunnel**: SSH 隧道管理技能

---

## 更新日志

### 2026-03-14

- ✅ 创建 YouTube Access 技能
- ✅ 支持从 BestCookier JSON 导入 cookies
- ✅ 支持转换为 Playwright/Netscape 格式
- ✅ 支持验证 cookies 的有效性
- ✅ 支持使用 cookies 下载 YouTube 视频
- ✅ 支持代理和字幕下载
