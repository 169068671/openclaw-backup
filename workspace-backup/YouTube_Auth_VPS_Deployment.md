# YouTube Auth Exporter - VPS 部署报告

**部署日期**: 2026-03-08
**部署人**: openclaw ⚡

---

## ✅ 部署状态

**状态**: 完全成功
**VPS**: root@76.13.219.143 (Hostinger)
**认证文件位置**: `/root/.youtube/`

---

## 📦 部署的文件

| 文件 | 位置 | 大小 | 用途 |
|-----|------|------|------|
| storage_state.json | /root/.youtube/storage_state.json | 18K | Playwright 认证 |
| cookies.txt | /root/.youtube/cookies.txt | 9.5K | yt-dlp 认证 |

---

## 🧪 测试结果

### 1. 认证测试
- ✅ **Playwright 认证成功**
- ✅ **页面标题**: YouTube

### 2. yt-dlp 测试
- ✅ **成功获取视频信息**
- 视频标题: Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster)
- 时长: 3:33
- 格式: 401 (2160p) + 251 (audio)

### 3. VPS 测试脚本
- 位置: `/tmp/vps_youtube_test.sh`
- 状态: ✅ 测试通过

---

## 🚀 使用方法

### 1. 本地导出认证
```bash
# 运行认证导出脚本
/tmp/youtube_auth_setup.sh
```

### 2. 部署到 VPS
```bash
# 自动部署脚本
/tmp/deploy_youtube_auth.sh
```

### 3. VPS 上使用

#### 方法 1: yt-dlp 下载视频
```bash
# SSH 到 VPS 并下载
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 \
  "yt-dlp --cookies /root/.youtube/cookies.txt \
   -f 'bestvideo+bestaudio' \
   -o '/root/youtube-downloads/%(title)s.%(ext)s' \
   'VIDEO_URL'"

# 或者先 SSH 到 VPS
ssh root@76.13.219.143

# 然后直接下载
yt-dlp --cookies /root/.youtube/cookies.txt \
  -f 'bestvideo+bestaudio' \
  -o '/root/youtube-downloads/%(title)s.%(ext)s' \
  "VIDEO_URL"
```

#### 方法 2: Playwright 自动化
```python
# VPS 上的 Python 脚本
import asyncio
from playwright.async_api import async_playwright

async def download_video():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            storage_state="/root/.youtube/storage_state.json"
        )
        page = await context.new_page()

        # 访问 YouTube
        await page.goto("https://www.youtube.com/watch?v=VIDEO_ID")
        await page.wait_for_load_state("networkidle")

        # 你的自动化代码
        print("✅ 认证成功，可以访问 YouTube")

        await browser.close()

asyncio.run(download_video())
```

---

## 📋 本地脚本

### 1. 认证导出脚本
```bash
/tmp/youtube_auth_setup.sh
```

功能：
- 导出 Chrome cookies
- 转换为 Playwright 格式
- 转换为 Netscape 格式
- 测试认证有效性

### 2. 部署脚本
```bash
/tmp/deploy_youtube_auth.sh
```

功能：
- 创建 VPS 目录
- 上传认证文件
- 验证文件完整性
- 测试 VPS 认证

### 3. 本地下载脚本
```bash
/tmp/youtube_download_with_auth.sh <URL> [输出目录]
```

功能：
- 使用认证下载视频
- 自动配置代理
- 支持自定义输出目录

### 4. VPS 测试脚本
```bash
/tmp/vps_youtube_test.sh [URL]
```

功能：
- 测试 VPS 认证
- 获取视频信息
- 显示实际下载命令

---

## 🔄 更新认证

认证文件有效期约 14 天，到期后需要重新导出：

```bash
# 步骤 1: 导出新的认证
/tmp/youtube_auth_setup.sh

# 步骤 2: 部署到 VPS
/tmp/deploy_youtube_auth.sh

# 步骤 3: 测试 VPS 认证
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 \
  "/tmp/vps_youtube_test.sh"
```

---

## ⚙️ 配置说明

### VPS 配置
- **服务器**: 76.13.219.143
- **用户**: root
- **密码**: Whj001.Whj001
- **认证目录**: /root/.youtube/
- **下载目录**: /root/youtube-downloads/

### yt-dlp 配置
- **Cookies 文件**: /root/.youtube/cookies.txt
- **推荐格式**: `bestvideo+bestaudio`
- **JavaScript 运行时**: 需要安装 Node.js（可选）

### Playwright 配置
- **存储状态文件**: /root/.youtube/storage_state.json
- **浏览器模式**: headless（无头）
- **浏览器**: Chromium

---

## 📝 故障排除

### 问题 1: "HTTP Error 403: Forbidden"
**原因**: 认证已过期
**解决**: 重新运行 `/tmp/youtube_auth_setup.sh` 和 `/tmp/deploy_youtube_auth.sh`

### 问题 2: "No supported JavaScript runtime"
**原因**: 缺少 Node.js
**解决**: 安装 Node.js（可选，不影响基本功能）
```bash
# VPS 上安装 Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt-get install -y nodejs
```

### 问题 3: VPS 认证失败
**原因**: 文件上传失败或权限问题
**解决**:
```bash
# 检查文件是否存在
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 \
  "ls -lh /root/.youtube/"

# 重新部署
/tmp/deploy_youtube_auth.sh
```

---

## 🎯 使用场景

### 1. 下载年龄限制视频
```bash
# VPS 上执行
yt-dlp --cookies /root/.youtube/cookies.txt \
  -f 'bestvideo+bestaudio' \
  "https://www.youtube.com/watch?v=AGE_RESTRICTED_VIDEO_ID"
```

### 2. 下载私人/不公开视频
```bash
# VPS 上执行
yt-dlp --cookies /root/.youtube/cookies.txt \
  -f 'bestvideo+bestaudio' \
  "https://www.youtube.com/watch?v=PRIVATE_VIDEO_ID"
```

### 3. 批量下载（创建 URL 列表文件）
```bash
# 创建视频列表文件
cat > /tmp/video_urls.txt << EOF
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
https://www.youtube.com/watch?v=VIDEO_ID_3
EOF

# VPS 上批量下载
yt-dlp --cookies /root/.youtube/cookies.txt \
  -f 'bestvideo+bestaudio' \
  -o '/root/youtube-downloads/%(title)s.%(ext)s' \
  -a /tmp/video_urls.txt
```

### 4. 下载播放列表
```bash
# VPS 上下载整个播放列表
yt-dlp --cookies /root/.youtube/cookies.txt \
  -f 'bestvideo+bestaudio' \
  -o '/root/youtube-downloads/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s' \
  "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

---

## 📚 相关技能

- **browser-cookies-exporter**: 导出 Chrome cookies（前置技能）
- **youtube-auth-exporter**: YouTube 认证导出（本技能）
- **yt-dlp-downloader**: 综合视频下载工具

---

## 🔗 技能文件位置

- **技能目录**: `~/.openclaw/skills/youtube-auth-exporter/`
- **文档**: `SKILL.md`
- **转换脚本**: `scripts/convert_cookies.py`
- **打包文件**: `youtube-auth-exporter.skill`

---

## ✅ 总结

- ✅ 认证导出成功（本地 + VPS）
- ✅ VPS 部署成功
- ✅ VPS 认证测试成功
- ✅ yt-dlp 测试成功
- ✅ 创建了完整的自动化脚本
- ✅ 文档齐全，易于维护

---

**维护人**: openclaw ⚡
**最后更新**: 2026-03-08 06:30 (GMT+8)
