# SSH Tunnel 技能

SSH 隧道管理技能，自动启动/停止隧道并测试 Google 连通性。

## 快速开始

```bash
# 启动隧道（自动测试 Google）
~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh start

# 启动隧道（不测试 Google）
~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh start --no-check

# 停止隧道
~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh stop

# 查看状态
~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh status

# 重启隧道
~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh restart
```

## 功能特性

- ✅ **一键启动/停止** - 简单命令管理隧道
- ✅ **自动检测 Google** - 启动时自动测试连通性
- ✅ **详细状态显示** - 进程信息、网络监听、连通性
- ✅ **彩色输出** - 清晰的视觉反馈
- ✅ **SSH 密钥认证** - 免密登录

## 配置

| 配置项 | 值 |
|-------|-----|
| 服务器 | 76.13.219.143 (srv1437164) |
| 用户 | root |
| 本地端口 | 1080 (SOCKS5) |
| SSH 密钥 | ~/.ssh/id_rsa |

## 使用代理

### 浏览器
- Chrome/Edge → 设置 → 系统 → 代理
- SOCKS 主机：127.0.0.1，端口：1080

### 终端
```bash
export ALL_PROXY=socks5h://127.0.0.1:1080
curl https://example.com
```

**重要**：
- `socks5://` - 本地解析 DNS（可能无法访问 Google）❌
- `socks5h://` - 远程服务器解析 DNS（推荐）✅

### 应用程序
```bash
# yt-dlp
yt-dlp --proxy socks5h://127.0.0.1:1080 "URL"

# agent-browser
agent-browser open URL --proxy socks5://127.0.0.1:1080

# curl
curl --proxy socks5h://127.0.0.1:1080 URL
```

## Google 测试说明

### 测试结果

**测试失败 ❌**：
```
❌ 测试失败: Connection timed out
说明: VPS 无法访问 Google（网络限制）
提示: 这是 VPS 网络质量问题，不是隧道配置问题
```

**原因**：
- Hostinger VPS 无法访问 Google（被墙或网络限制）
- 这是 VPS 网络质量问题，不是隧道配置问题
- SSH 隧道本身工作正常（端口在监听）

**解决方法**：
1. 更换 VPS 到可访问 Google 的节点
2. 使用国内替代服务（百度、必应）
3. YouTube 下载已有 cookies 方案，不依赖浏览器访问

### 手动测试

```bash
# 通过代理测试 Google（使用 socks5h）
curl --proxy socks5h://127.0.0.1:1080 -I https://www.google.com

# 测试 VPS 直连
ssh root@76.13.219.143 "curl -I https://www.google.com"

# 测试本地直连
curl -I https://www.google.com
```

### 为什么测试失败了？（之前）

**问题**：使用 `socks5://` 时，Google 测试失败

**原因**：
- 本地和 VPS 的 DNS 解析结果不同（GeoDNS）
- `socks5://` 在本地解析 DNS，返回的 IP 可能无法从 VPS 访问
- `socks5h://` 在远程服务器解析 DNS，可以正常访问

**解决方案**：使用 `socks5h://` 而不是 `socks5://`

## 状态示例

### 运行中
```
🟢 SSH 隧道状态：运行中
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 服务器: 76.13.219.143 (srv1437164)
🔌 本地端口: 127.0.0.1:1080 (SOCKS5)
👤 用户: root
🔑 认证: SSH 密钥
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 进程信息:
  PID: 97158
  CPU: 0.0%
  MEM: 0.0%
  运行时间: 00:16
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 网络监听:
  IPv4: 127.0.0.1:1080 ✅
  IPv6: [::1]:1080 ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 Google 连通性:
  ❌ 测试失败: Connection timed out
  说明: VPS 无法访问 Google（网络限制）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 未运行
```
🔴 SSH 隧道状态：未运行
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
提示: 使用以下命令启动隧道
  ~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh start
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 相关文档

- SKILL.md - 完整技能文档
- TOOLS.md - SSH隧道代理方案

## 更新日志

### v1.0 (2026-03-07)
- ✅ 隧道管理（启动/停止/状态/重启）
- ✅ Google 连通性测试
- ✅ 彩色输出和状态显示
- ✅ 进程信息展示
- ✅ SSH 密钥认证
