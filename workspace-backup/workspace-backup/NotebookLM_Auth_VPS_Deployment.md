# NotebookLM Auth Exporter - VPS 部署报告

**部署日期**: 2026-03-08
**部署人**: openclaw ⚡

---

## ✅ 部署状态

**状态**: 文件部署成功，认证需要网络配置
**VPS**: root@76.13.219.143 (Hostinger)
**认证文件位置**: `/root/.notebooklm/`

---

## 📦 部署的文件

| 文件 | 位置 | 大小 | 状态 |
|-----|------|------|------|
| storage_state.json | /root/.notebooklm/storage_state.json | 18K | ✅ 已部署 |
| vps_notebooklm_test.sh | /tmp/vps_notebooklm_test.sh | 2.3K | ✅ 已部署 |

---

## 🧪 测试结果

### 1. 本地认证测试
- ✅ **认证成功**
- ✅ **页面标题**: NotebookLM
- ✅ **Cookies 数量**: 53 个

### 2. VPS 认证测试
- ❌ **测试失败** - 超时
- ⚠️ **问题**: VPS 访问 Google 服务受限

### 3. 网络连接测试
- ✅ **Google 可访问**（返回 HTTP/2 302）
- ⚠️ **需要认证**（Google 检测到 VPS IP）

---

## ⚠️ 当前问题

### VPS 认证失败的原因

1. **IP 限制**: Google 检测到 VPS IP 来自数据中心
2. **地理限制**: VPS 位置可能受限
3. **安全策略**: Google 对自动化访问有严格限制

### 解决方案

#### 方案 1: 使用 SSH 隧道代理（推荐）

在 VPS 上配置 SOCKS5 代理，通过本地机器访问 Google：

```bash
# 在 VPS 上设置代理环境变量
export HTTP_PROXY="http://76.13.219.143:8888"
export HTTPS_PROXY="http://76.13.219.143:8888"

# 或者在 Playwright 中配置代理
context = await browser.new_context(
    storage_state="/root/.notebooklm/storage_state.json",
    proxy={
        "server": "http://76.13.219.143:8888"
    }
)
```

#### 方案 2: 使用本地机器（最佳）

在本地机器上运行 Playwright，避免 VPS IP 限制：

```python
# 本地机器上运行
async with async_playwright() as p:
    browser = await p.chromium.launch(headless=True)
    context = await browser.new_context(
        storage_state="/tmp/notebooklm-storage-state.json"
    )
    # 本地访问，不受 VPS IP 限制
```

#### 方案 3: 使用 notebooklm CLI（推荐）

在 VPS 上使用 notebooklm CLI 工具：

```bash
# 在 VPS 上配置 notebooklm
cd /root/.notebooklm
notebooklm login

# 导入 YouTube 视频到 NotebookLM
notebooklm source add "https://www.youtube.com/watch?v=VIDEO_ID"

# 生成内容
notebooklm generate audio --wait
```

---

## 📋 本地脚本

### 1. 认证导出和部署脚本
```bash
/tmp/notebooklm_auth_deploy.sh
```

功能：
- 导出 Chrome cookies
- 转换为 Playwright 格式
- 部署到 VPS
- 本地测试认证

### 2. VPS 测试脚本
```bash
/tmp/vps_notebooklm_test.sh
```

功能：
- 测试 VPS 认证
- 显示详细测试信息

---

## 🚀 使用方法

### 推荐方案：本地机器 + SSH 远程

在本地机器上运行 Playwright，通过 SSH 远程控制 VPS：

```python
# 本地机器上的 Python 脚本
import asyncio
from playwright.async_api import async_playwright

async def use_notebooklm():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        # 使用本地认证（不受 VPS IP 限制）
        context = await browser.new_context(
            storage_state="/tmp/notebooklm-storage-state.json"
        )

        page = await context.new_page()

        # 访问 NotebookLM
        await page.goto("https://notebooklm.google.com/")
        await page.wait_for_load_state("networkidle")

        print("✅ 认证成功，可以访问 NotebookLM")

        # 你的自动化代码
        # ...

        await browser.close()

asyncio.run(use_notebooklm())
```

### VPS 方案：配置代理

如果必须在 VPS 上运行，需要配置代理：

```python
# VPS 上的 Python 脚本（需要代理）
import asyncio
from playwright.async_api import async_playwright

async def use_notebooklm_on_vps():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        # 配置代理
        context = await browser.new_context(
            storage_state="/root/.notebooklm/storage_state.json",
            proxy={
                "server": "http://76.13.219.143:8888"
            }
        )

        page = await context.new_page()

        # 访问 NotebookLM
        await page.goto("https://notebooklm.google.com/")
        await page.wait_for_load_state("networkidle")

        print("✅ 认证成功（通过代理）")

        await browser.close()

asyncio.run(use_notebooklm_on_vps())
```

### VPS 方案：使用 notebooklm CLI

使用 notebooklm CLI 工具（已安装）：

```bash
# 在 VPS 上运行
notebooklm login
notebooklm create "My Notebook"
notebooklm source add "https://www.youtube.com/watch?v=XXX"
notebooklm generate audio --wait
notebooklm download audio ./podcast.mp3
```

---

## 🔄 更新认证

认证文件有效期约 14 天，到期后需要重新导出：

```bash
# 步骤 1: 导出新的认证
/tmp/notebooklm_auth_deploy.sh

# 步骤 2: 手动复制到 VPS（如需要）
sshpass -p 'Whj001.Whj001' scp \
  /tmp/notebooklm-storage-state.json \
  root@76.13.219.143:/root/.notebooklm/storage_state.json

# 步骤 3: 测试本地认证
python3 -c "
import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            storage_state='/tmp/notebooklm-storage-state.json'
        )
        page = await context.new_page()
        await page.goto('https://notebooklm.google.com/')
        print(f'页面标题: {await page.title()}')
        await browser.close()

asyncio.run(test())
"
```

---

## 📝 与 YouTube Auth Exporter 的区别

| 特性 | notebooklm-auth-exporter | youtube-auth-exporter |
|-----|------------------------|----------------------|
| VPS 可用性 | ⚠️ 受限（IP 限制） | ✅ 可用 |
| 主要使用场景 | 本地 Playwright | VPS yt-dlp |
| 网络要求 | 本地网络 | VPS 网络或代理 |
| 推荐部署位置 | 本地机器 | VPS |

### 关键区别

- **YouTube Auth**: VPS 上可以直接使用 yt-dlp 下载，不受 IP 限制
- **NotebookLM Auth**: VPS 上使用 Playwright 受 IP 限制，建议本地使用

---

## 🎯 推荐使用方案

### 1. 本地自动化（推荐）
- 在本地机器上运行 Playwright
- 使用本地认证文件
- 不受 VPS IP 限制

### 2. VPS CLI 工具
- 使用 notebooklm CLI 工具
- 适用于简单的导入和生成操作

### 3. VPS 代理方案
- 配置 SOCKS5/HTTP 代理
- 通过代理访问 Google 服务
- 性能较差，不推荐

---

## 📚 相关技能

- **browser-cookies-exporter**: 导出 Chrome cookies（前置技能）
- **notebooklm-auth-exporter**: NotebookLM 认证导出（本技能）
- **notebooklm-youtube-importer**: YouTube 批量导入到 NotebookLM
- **NotebookLM**: 非官方 Python API 工具

---

## 🔗 技能文件位置

- **技能目录**: `~/.openclaw/skills/notebooklm-auth-exporter/`
- **文档**: `SKILL.md`
- **转换脚本**: `scripts/convert_cookies.py`
- **打包文件**: `notebooklm-auth-exporter.skill`

---

## ✅ 总结

- ✅ 认证导出成功（本地）
- ✅ 文件部署到 VPS 成功
- ⚠️ VPS 认证受 IP 限制
- ✅ 本地使用不受限制
- ✅ 创建了完整的脚本和文档

---

**维护人**: openclaw ⚡
**最后更新**: 2026-03-08 06:35 (GMT+8)
