# TOOLS.md - Local Notes

## 🚨 最高优先级规则

**重要**：所有操作必须遵守 `RULES.md` 中的规则：
- **第一规则：永不断开连接** - 每次更改后都要测试连接
- **第二规则：操作前备份** - 重要操作前必须创建备份

**测试连接**：
```bash
# OpenClaw 服务
systemctl status openclaw-gateway

# 网络连接
ping -c 3 8.8.8.8
curl -I https://github.com

# Git 仓库
cd /home/admin/openclaw/workspace && git status
```

详见：`RULES.md` - 这是绝对不能违反的铁律

---

## 备份信息

- **工作空间备份：** `/home/admin/backups/workspace-backup-20260302-132648.tar.gz` (49K)
- **Git 仓库：** `/home/admin/openclaw/workspace/.git` (初始提交: cfd8d95)
- **备份策略：** 重要操作前创建新备份，Git 保存历史版本

## Hostinger VPS

- **地址：** 76.13.219.143
- **主机名：** srv1437164
- **用户：** root
- **密码：** Whj001.Whj001
- **连接命令：** `sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143`
- **状态：** ✅ SSH 连接正常 (2026-03-02 22:54)
- **Guacamole：** ✅ 已部署，http://76.13.219.143:8081/guacamole
- **Docker Compose：** ✅ 已安装
- **MySQL：** ✅ 运行中（3306 端口）
- **Guacamole Daemon：** ✅ 运行中（4822 端口）
- **Guacamole Web：** ✅ 运行中（8081:8080 端口）

## HTTP 代理配置

- **推荐方案：** SSH 隧道（SOCKS5）- 更稳定 ⭐
- **替代方案：** Tinyproxy (HTTP) - 有时不稳定
- **文档：** `SSH隧道代理方案.md`
- **Tinyproxy 文档：** `HTTP代理配置方案-HostingerVPS.md`
- **状态：** Tinyproxy HTTPS 不稳定，推荐使用 SSH 隧道

### 推荐方案：直连（全局规则）⭐

**测试结果（2026-03-03 15:30）**：

| 访问类型 | 直连 | SSH隧道 | 结论 |
|---------|------|---------|------|
| GitHub HTTPS | 0.35s | 1.09s | 直连快3倍 ✅ |
| GitHub SSH | 3.09s | 4.56s | 直连快1.5倍 ✅ |
| Git Fetch | 4.00s | 5.84s | 直连快1.5倍 ✅ |

**全局规则**：
- ✅ GitHub访问（HTTP/SSH）：使用直连
- ✅ Git操作（push/pull/clone）：使用直连
- ✅ 国内网站：使用直连

**备用方案：SSH 隧道（SOCKS5）**

仅在直连失败或访问其他被限制的国外网站时使用（包括 agent-reach 需要代理时）。

**启动方法：**
```bash
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143
```

**检查隧道状态：**
```bash
netstat -tlnp | grep 1080
```

**停止隧道：**
```bash
ps aux | grep "ssh.*1080" | awk '{print $2}' | xargs kill
```

**浏览器配置：**
- Chrome/Edge → 设置 → 系统 → 代理
- SOCKS 主机：`127.0.0.1`，端口：`1080`

**详细文档：** `SSH隧道代理方案.md`

---

## GitHub CLI (gh) 配置

**认证状态**: ✅ 已认证（2026-03-07）
- 账号：169068671
- 协议：HTTPS
- Token 作用域：完整权限（admin, repo, workflow, etc.）

**GitHub Token**：
```
[REDACTED]
```

**⚠️ 安全提醒**：
- Token 已记录到此文件，请勿公开分享
- 如需重置，访问 GitHub Settings → Developer settings → Personal access tokens
- 建议定期更换 token

**使用场景**：
- agent-reach GitHub 渠道（已解锁完整功能）
- GitHub 仓库管理
- Issue/PR 操作

**认证方法**：
```bash
# 使用 token 认证
echo "<token>" | gh auth login --with-token
```

### 替代方案：Tinyproxy（HTTP）⚠️

**配置：**
- 代理服务器：76.13.219.143:8888
- 类型：HTTP 代理
- PAC 文件：`/opt/proxy.pac`

**问题：**
- ❌ HTTPS 代理连接不稳定
- ❌ 容易超时
- ⚠️ 不推荐使用

**Tinyproxy 配置（最新）：**
```conf
Port 8888
Listen 0.0.0.0
Allow 0.0.0.0/0
```

**测试结果（2026-03-02 14:25）：**
- HTTP 访问：✅ 成功
- HTTPS 访问：❌ 不稳定（经常超时）
- 国内网站：✅ 直连
- OpenClaw：✅ 直连

## 钉钉通道配置

- **插件名称：** dingtalk-connector
- **版本：** 0.6.0
- **状态：** ✅ 已安装并加载
- **配置文件：** `~/.openclaw/openclaw.json`
- **文档：** `钉钉通道配置指南.md`
- **完成报告：** `钉钉通道配置完成报告.md`
- **状态：** ✅ 双向通信测试成功

### 配置详情

1. **钉钉应用信息**
   - Client ID (AppKey): dingyscopnptfxm4hg8q
   - Client Secret: 已配置
   - Gateway Token: 已配置
   - 消息接收模式: Stream 模式
   - 应用状态: ✅ 已发布

2. **必需权限**
   - Card.Streaming.Write ✅
   - Card.Instance.Write ✅
   - qyapi_robot_sendmsg ✅

3. **功能特性**
   - AI Card 流式响应 ✅
   - 会话持久化（30分钟超时）✅
   - 双向通信 ✅
   - 图片自动上传
   - 支持会话命令：/new, /reset, /clear, 新会话, 重新开始, 清空对话

4. **测试结果**
   - 接收消息（钉钉→OpenClaw）：✅ 测试成功 (2026-03-02 14:04)
   - 主动发送（OpenClaw→钉钉）：✅ 测试成功 (2026-03-02 14:07)
   - 测试用户ID：193200103629107416

---

## 下载工具总览

| 工具 | 类型 | 功能 | 安装状态 | 位置 |
|-----|------|------|---------|------|
| **yutto** | 视频 | Bilibili 专用 | ✅ 2.1.1 | ~/.local/bin/yutto |
| **yt-dlp** | 视频 | 综合下载（1000+网站） | ✅ 2026.02.21 | ~/.local/bin/yt-dlp |
| **musicdl** | 音乐 | 音乐/有声读物（50+平台） | ✅ 2.9.7 | ~/.local/bin/musicdl |

### 推荐使用

- **Bilibili 下载**：yutto（专用，更稳定）
- **YouTube 下载**：yt-dlp（agent-reach 技能，配置完整）⭐
- **综合视频下载**：yt-dlp（支持1000+网站）
- **音乐/有声读物**：musicdl（50+音乐平台）

### YouTube 下载配置（agent-reach）⭐

**完整下载命令**：
```bash
yt-dlp --proxy socks5://127.0.0.1:1080 \
  --cookies-from-browser chrome \
  --js-runtimes node \
  --remote-components ejs:github \
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
  -o "/tmp/%(title)s.%(ext)s" \
  "https://www.youtube.com/watch?v=XXX"
```

**必需参数说明**：
- `--proxy socks5://127.0.0.1:1080`：SSH 隧道代理（必需）
- `--cookies-from-browser chrome`：使用浏览器 cookies（必需）
- `--js-runtimes node`：使用 Node.js 解析（必需）
- `--remote-components ejs:github`：使用 GitHub EJS 组件（必需）

**前置条件**：
1. 启动 SSH 隧道：`sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143`
2. 检查隧道状态：`netstat -tlnp | grep 1080`

**常见错误**：
- `Network is unreachable` → 需要代理
- `Sign in to confirm you're not a bot` → 需要 cookies
- `n challenge solving failed` → 需要 JS runtime 和 EJS 组件

**详细说明**：见 agent-reach 技能 SKILL.md

---

### YouTube Cookies 导出（Netscape 格式）📁

**Cookies 文件位置**：`/home/admin/Desktop/cookies-youtube.txt`
- 格式：Netscape HTTP Cookie File
- 大小：3.1K
- 包含：21 个 cookies

**使用导出的 cookies**：
```bash
yt-dlp --proxy socks5://127.0.0.1:1080 \
  --cookies "/home/admin/Desktop/cookies-youtube.txt" \
  --js-runtimes node \
  --remote-components ejs:github \
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
  -o "/tmp/%(title)s.%(ext)s" \
  "https://www.youtube.com/watch?v=XXX"
```

**导出 cookies 命令**：
```bash
# 安装 browser-cookie3
pip3 install --user browser-cookie3

# 导出 YouTube cookies（Netscape 格式）
python3 -c "
import browser_cookie3
import http.cookiejar as cj

cookies = browser_cookie3.chrome(domain_name='.youtube.com')
cookie_jar = cj.MozillaCookieJar('/home/admin/Desktop/cookies-youtube.txt')
for cookie in cookies:
    cookie_jar.set_cookie(cookie)
cookie_jar.save()
"
```

**Cookie 有效期**：
- Cookies 会随时间过期
- 建议定期重新导出
- 如果遇到认证错误，重新导出即可

**两种使用方式对比**：

| 方式 | 优点 | 缺点 |
|-----|------|------|
| `--cookies-from-browser chrome` | 自动获取最新 cookies | 需要浏览器运行 |
| `--cookies "/path/to/file"` | 可重复使用，方便脚本调用 | cookies 可能过期 |

**安全提醒**：
- Cookies 包含敏感信息，请勿分享
- 建议定期更换 YouTube 密码
- 注意保护 cookies 文件安全
