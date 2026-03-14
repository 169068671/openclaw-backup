# Chrome Proxy Linux Skill - 创建完成报告

**创建时间：** 2026-03-14 15:49
**技能名称：** chrome-proxy-linux
**版本：** 1.0.0
**作者：** openclaw

---

## 📦 技能概述

基于 Windows 版本的 Chrome Proxy Skill，创建了适用于 Linux 环境的代理上网技能。

### 核心功能

1. **SSH SOCKS5 隧道管理**
   - 连接到 VPS (76.13.219.143)
   - 创建本地 SOCKS5 代理 (端口 1080)
   - 自动检测和停止旧连接

2. **Chrome 浏览器代理启动**
   - 使用独立用户数据目录
   - 配置 SOCKS5 代理参数
   - 支持 `google-chrome` 和 `google-chrome-stable`

3. **代理测试**
   - 测试 SSH 隧道状态
   - 检测出口 IP
   - 测试网站访问能力

4. **状态管理**
   - 查看代理运行状态
   - 停止 Chrome 和 SSH 隧道

---

## 📁 文件结构

```
~/.openclaw/skills/chrome-proxy-linux/
├── SKILL.md                      # 技能文档 (4705 bytes)
├── skill.json                    # 技能配置 (1641 bytes)
├── start-chrome.sh               # Chrome 启动脚本 (3556 bytes) ✅ 可执行
├── stop-chrome.sh                # Chrome 停止脚本 (987 bytes) ✅ 可执行
└── scripts/
    ├── start-ssh.sh              # SSH 隧道脚本 (1287 bytes) ✅ 可执行
    └── test-proxy.sh             # 代理测试脚本 (1493 bytes) ✅ 可执行
```

**总计：** 6 个文件，13,669 bytes

---

## 🔧 技术实现

### 与 Windows 版本的对比

| 特性 | Windows 版本 | Linux 版本 |
|------|-------------|-----------|
| **脚本语言** | PowerShell | Bash |
| **SSH 命令** | `ssh -D 1080` | `ssh -D 1080` |
| **Chrome 路径** | `C:\Program Files\Google\Chrome\Application\chrome.exe` | `google-chrome` (命令) |
| **用户数据目录** | `C:\Users\admin\AppData\Local\Google\Chrome\ProxyProfile` | `/tmp/chrome-proxy-profile` |
| **SSH 密钥** | 默认密钥 | `~/.ssh/id_rsa` |
| **进程管理** | `Get-Process`, `Stop-Process` | `pgrep`, `pkill` |
| **端口检查** | `Get-NetTCPConnection` | `netstat` |
| **彩色输出** | `Write-Host -ForegroundColor` | ANSI 转义序列 |

### 核心差异

1. **路径处理**
   - Windows: `C:\Users\admin\AppData\Local\Google\Chrome\ProxyProfile`
   - Linux: `/tmp/chrome-proxy-profile` (更简洁)

2. **SSH 密钥**
   - Windows: 使用默认密钥配置
   - Linux: 明确指定 `~/.ssh/id_rsa`

3. **浏览器检测**
   - Windows: 检测文件是否存在
   - Linux: 使用 `command -v` 检测命令是否可用

4. **进程管理**
   - Windows: PowerShell 原生命令
   - Linux: 标准的 `pgrep`/`pkill` 工具

5. **彩色输出**
   - Windows: PowerShell 原生支持
   - Linux: ANSI 转义序列 (`\033[0;32m`)

---

## 🚀 使用方法

### 基本命令

```bash
# 启动 Chrome with SOCKS5 代理
~/.openclaw/skills/chrome-proxy-linux/start-chrome.sh

# 停止 Chrome 和 SSH 隧道
~/.openclaw/skills/chrome-proxy-linux/stop-chrome.sh

# 测试代理连接
~/.openclaw/skills/chrome-proxy-linux/scripts/test-proxy.sh

# 仅启动 SSH 隧道
~/.openclaw/skills/chrome-proxy-linux/scripts/start-ssh.sh
```

### 集成到 OpenClaw

激活技能后，可以使用：
```
/chrome-proxy-linux start
/chrome-proxy-linux stop
/chrome-proxy-linux status
/chrome-proxy-linux test
```

---

## 🎯 测试结果

### SSH 隧道
- ✅ 连接到 VPS (76.13.219.143)
- ✅ SOCKS5 代理 (127.0.0.1:1080)
- ✅ SSH 密钥认证

### Chrome 启动
- ✅ 检测 `google-chrome` 命令
- ✅ 独立用户数据目录
- ✅ SOCKS5 代理配置

### 代理测试
- ✅ 出口 IP: 76.13.219.143
- ✅ GitHub 可访问
- ✅ StackOverflow 可访问
- ✅ NPM 可访问
- ⚠️ Google/YouTube 受限 (VPS 网络限制)

---

## 📊 性能优化

### 相比 Windows 版本的改进

1. **更简洁的路径**
   - Linux 使用 `/tmp` 目录，更符合系统规范
   - 避免了复杂的 Windows 路径

2. **更可靠的进程管理**
   - 使用 `pgrep -f` 精确匹配进程
   - 避免误杀其他 Chrome 进程

3. **更完善的错误处理**
   - SSH 密钥存在性检查
   - 浏览器命令可用性检查
   - 清晰的错误提示

4. **更友好的输出**
   - ANSI 彩色输出（与终端兼容）
   - 进度指示器 `[1/4]`, `[2/4]` 等
   - 清晰的成功/失败状态

---

## 🔐 安全特性

1. **SSH 密钥认证**
   - 使用 `~/.ssh/id_rsa` 密钥
   - 避免密码明文传输

2. **独立用户数据目录**
   - 不影响主 Chrome 配置
   - 代理配置隔离

3. **进程隔离**
   - 精确匹配代理 Chrome 进程
   - 避免影响其他 Chrome 实例

---

## 📝 注意事项

### 前置条件

1. **SSH 密钥**
   ```bash
   # 生成 SSH 密钥（如果没有）
   ssh-keygen -t ed25519

   # 复制公钥到 VPS
   ssh-copy-id root@76.13.219.143
   ```

2. **Chrome 安装**
   ```bash
   # 安装 Chrome（如果没有）
   sudo apt install google-chrome-stable
   ```

3. **VPS 连接**
   - 确保 VPS 可访问
   - 确保 SSH 密钥已配置

### 已知限制

1. **Google/YouTube 限制**
   - Hostinger VPS 网络策略限制
   - 可通过更换 VPS 解决

2. **SSH 隧道稳定性**
   - 已配置保活参数 (`ServerAliveInterval=60`)
   - 网络波动可能导致断开

---

## 🔄 后续改进建议

### 短期改进

1. **添加配置文件**
   - 支持自定义 VPS 配置
   - 支持自定义端口和路径

2. **添加日志功能**
   - 记录启动/停止日志
   - 记录代理测试结果

3. **添加自动重连**
   - SSH 隧道断开自动重连
   - Chrome 崩溃自动重启

### 长期改进

1. **系统服务化**
   - 创建 systemd 服务
   - 开机自启动

2. **GUI 界面**
   - 桌面托盘图标
   - 一键启动/停止

3. **多 VPS 支持**
   - 支持多个 VPS 配置
   - 自动选择最快的 VPS

---

## 📚 相关文档

- **Windows 原版**: `/home/admin/Downloads/Chrome Proxy Skill.zip`
- **Linux 版本**: `~/.openclaw/skills/chrome-proxy-linux/`
- **SSH 隧道配置**: `/home/admin/openclaw/workspace/SSH隧道代理方案.md`
- **VPS 信息**: `/home/admin/openclaw/workspace/MEMORY.md` (Hostinger VPS)

---

## ✅ 验证清单

- [x] 所有脚本文件已创建
- [x] 所有脚本已添加执行权限
- [x] SKILL.md 文档完整
- [x] skill.json 配置正确
- [x] 与 Windows 版本功能对等
- [x] Linux 特性优化（路径、进程管理、彩色输出）
- [x] SSH 密钥认证
- [x] 错误处理完善

---

## 🎉 总结

成功创建了适用于 Linux 环境的 Chrome Proxy Skill！

**关键成就：**
- ✅ 完整功能移植（SSH 隧道 + Chrome 代理）
- ✅ Linux 特性优化（路径、进程管理、彩色输出）
- ✅ 安全特性增强（SSH 密钥认证、进程隔离）
- ✅ 完善的文档和错误处理

**相比 Windows 版本的优势：**
- 更简洁的路径和配置
- 更可靠的进程管理
- 更友好的终端输出
- 更好的系统集成

---

**创建人：** openclaw ⚡
**完成时间：** 2026-03-14 15:49 GMT+8
**技能版本：** 1.0.0
