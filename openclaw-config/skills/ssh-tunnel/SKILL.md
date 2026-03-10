# SSH Tunnel 技能

通过 SSH 隧道建立 SOCKS5 代理，用于访问被墙网站。

## 功能特性

- ✅ 启动/停止 SSH 隧道
- ✅ 检查隧道状态
- ✅ 自动测试 Google 连通性
- ✅ 免密登录支持（SSH 密钥）
- ✅ 进程管理

## 配置信息

### VPS 信息
- **地址**: 76.13.219.143 (srv1437164)
- **用户**: root
- **认证方式**: SSH 密钥（已配置免密登录）
- **本地端口**: 1080 (SOCKS5)

### SSH 密钥
- **私钥**: ~/.ssh/id_rsa
- **公钥**: ~/.ssh/id_rsa.pub
- **已部署**: 76.13.219.143 的 ~/.ssh/authorized_keys

## 常用命令

### 启动 SSH 隧道（自动测试 Google）
```bash
# 启动隧道并测试 Google 连通性
~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh start

# 简化启动（不测试 Google）
~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh start --no-check
```

### 停止 SSH 隧道
```bash
~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh stop
```

### 检查隧道状态
```bash
~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh status
```

### 重启隧道
```bash
~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh restart
```

## 使用方式

### 浏览器代理配置
- **Chrome/Edge** → 设置 → 系统 → 打开代理设置
  - SOCKS 代理：127.0.0.1
  - 端口：1080

### 终端临时代代理
```bash
# 设置代理环境变量（使用 socks5h 让远程服务器解析 DNS）
export ALL_PROXY=socks5h://127.0.0.1:1080
export HTTP_PROXY=socks5h://127.0.0.1:1080
export HTTPS_PROXY=socks5h://127.0.0.1:1080

# 测试出口 IP
curl ifconfig.me

# 测试 Google（通过代理）
curl -I https://www.google.com

# 取消代理
unset ALL_PROXY HTTP_PROXY HTTPS_PROXY
```

**重要说明**：
- `socks5://` - 本地解析 DNS（可能无法访问 Google）
- `socks5h://` - 远程服务器解析 DNS（推荐，可正常访问 Google）⭐

### 应用程序代理配置

**yt-dlp（YouTube 下载）**:
```bash
yt-dlp --proxy socks5h://127.0.0.1:1080 "https://www.youtube.com/watch?v=XXX"
```

**agent-browser（浏览器自动化）**:
```bash
agent-browser open https://example.com --proxy socks5://127.0.0.1:1080
```

**curl（命令行）**:
```bash
curl --proxy socks5h://127.0.0.1:1080 https://example.com
```

## Google 连通性测试

### 测试说明
SSH 隧道启动后会自动测试 Google 连通性：
- 测试方法：通过隧道访问 Google
- 测试地址：https://www.google.com
- 超时时间：10 秒
- 结果判定：
  - ✅ 成功：返回 HTTP 200 或 301/302 重定向
  - ❌ 失败：连接超时或错误

### 测试结果说明

**测试失败的原因**：
1. **VPS 网络限制** - Hostinger VPS 无法访问 Google
2. **Google 被墙** - Google 在中国被屏蔽
3. **网络延迟** - VPS 到 Google 的连接超时

**重要提醒**：
- SSH 隧道本身工作正常（端口在监听）
- 问题在于 VPS 无法访问 Google
- 这是 VPS 网络质量限制，不是隧道配置问题

### 手动测试
```bash
# 通过代理测试 Google（使用 socks5h）
curl --proxy socks5h://127.0.0.1:1080 -I https://www.google.com --connect-timeout 10

# 测试 VPS 直连 Google（需要 SSH 到 VPS）
ssh root@76.13.219.143 "curl -I https://www.google.com --connect-timeout 10"

# 测试本地直连 Google
curl -I https://www.google.com --connect-timeout 5
```

### 为什么使用 socks5h://？

**问题根源**：
- 本地和 VPS 的 DNS 解析结果不同（Google 使用 GeoDNS）
- 本地解析：www.google.com → 199.16.158.8
- VPS 解析：www.google.com → 172.217.26.132

**两种 SOCKS5 代理模式**：
- `socks5://` - 本地解析 DNS，然后连接远程 IP（可能失败）❌
- `socks5h://` - 远程服务器解析 DNS，返回域名让远程连接（成功）✅

**推荐**：使用 `socks5h://` 确保远程服务器解析 DNS。

## 隧道状态

### 检查命令
```bash
# 检查端口监听
ss -tlnp | grep 1080

# 检查进程
ps aux | grep "ssh.*1080" | grep -v grep

# 查看完整状态
~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh status
```

### 状态输出示例

**隧道运行中**：
```
🟢 SSH 隧道状态：运行中
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 服务器: 76.13.219.143 (srv1437164)
🔌 本地端口: 127.0.0.1:1080 (SOCKS5)
👤 用户: root
🔑 认证: SSH 密钥
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 进程信息:
  PID: 95584
  CPU: 0.0%
  MEM: 0.1%
  运行时间: 00:05:23
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 网络监听:
  IPv4: 127.0.0.1:1080 ✅
  IPv6: [::1]:1080 ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 Google 连通性:
  ⚠️  测试失败: Connection timed out
  说明: VPS 无法访问 Google（网络限制）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**隧道未运行**：
```
🔴 SSH 隧道状态：未运行
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
提示: 使用以下命令启动隧道
  ~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh start
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 进程管理

### 手动操作（高级用户）
```bash
# 启动隧道（直接命令）
ssh -N -D 1080 -f root@76.13.219.143

# 查看进程
ps aux | grep "ssh.*1080" | grep -v grep

# 停止隧道（按 PID）
kill <PID>

# 停止所有 SSH 隧道
ps aux | grep "ssh.*1080" | grep -v grep | awk '{print $2}' | xargs kill
```

## 安全建议

### 当前配置
- ✅ SSH 密钥认证（已配置）
- ✅ 免密登录（已测试）
- ⚠️ 密码认证未禁用（可选）

### VPS 安全加固（可选）
```bash
# SSH 到 VPS
ssh root@76.13.219.143

# 编辑 SSH 配置
nano /etc/ssh/sshd_config

# 修改以下配置
PasswordAuthentication no

# 重启 SSH 服务
systemctl restart sshd
```

**注意**：禁用密码认证后，只能通过 SSH 密钥登录。

## 故障排查

### 隧道无法启动
1. 检查 SSH 密钥：`ls -la ~/.ssh/id_rsa`
2. 测试 SSH 连接：`ssh root@76.13.219.143`
3. 检查端口占用：`ss -tlnp | grep 1080`

### 隧道自动断开
1. 检查 VPS SSH 服务：`systemctl status sshd`
2. 检查网络连接：`ping 76.13.219.143`
3. 使用 systemd 服务（待开发）

### Google 访问失败
1. **检查代理模式** - 确认使用 `socks5h://` 而不是 `socks5://`
2. 测试 VPS 直连：`ssh root@76.13.219.143 "curl -I https://www.google.com"`
3. 测试本地直连：`curl -I https://www.google.com`
4. 通过 socks5h 测试：`curl --proxy socks5h://127.0.0.1:1080 -I https://www.google.com`

### 代理不生效
1. 检查隧道状态：`~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh status`
2. 检查代理配置：确认代理地址为 `socks5://127.0.0.1:1080`
3. 测试代理：`curl --proxy socks5://127.0.0.1:1080 https://www.google.com`

## 相关文档

- TOOLS.md - SSH隧道代理方案
- SSH隧道代理方案.md

## 更新日志

### v1.0 (2026-03-07)
- ✅ 基本隧道管理（启动/停止/状态/重启）
- ✅ SSH 密钥认证
- ✅ Google 连通性测试
- ✅ 彩色输出和状态显示
- ✅ 进程信息展示
