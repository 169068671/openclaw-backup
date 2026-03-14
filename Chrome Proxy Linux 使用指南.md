# Chrome Proxy Linux - 使用指南

**状态：** ✅ 已验证，可以使用  
**测试时间：** 2026-03-14 16:21 GMT+8

---

## 🎯 快速开始

### 前置条件检查

```bash
# 检查 Chrome 是否已安装
command -v google-chrome && echo "✅ Chrome 已安装"

# 检查 sshpass 是否已安装
command -v sshpass && echo "✅ sshpass 已安装"

# 检查 VPS 连接
sshpass -p 'Whj001.Whj001' ssh -o ConnectTimeout=5 root@76.13.219.143 "echo '✅ VPS 连接正常'"
```

---

## 🚀 使用方法

### 方式 1：直接使用脚本

#### 启动 Chrome 代理

```bash
# 启动 Chrome with SOCKS5 代理
~/.openclaw/skills/chrome-proxy-linux/start-chrome.sh
```

**预期输出：**
```
========================================
   Chrome Proxy Starter (Linux)
========================================

[1/4] Checking existing SSH tunnel...
[2/4] Starting SSH SOCKS5 tunnel...
  SUCCESS: SSH tunnel established (port 1080)
[3/4] Checking Chrome...
  Chrome found
[4/4] Starting browser with SOCKS5 proxy...
  SUCCESS: Chrome started (PID: 12345)

========================================
   Chrome Proxy Started
========================================

  Proxy: SOCKS5 127.0.0.1:1080
  VPS:   76.13.219.143

  Browser will open automatically.
  Close browser and run stop script when done.
```

#### 停止 Chrome 代理

```bash
# 停止 Chrome 和 SSH 隧道
~/.openclaw/skills/chrome-proxy-linux/stop-chrome.sh
```

**预期输出：**
```
========================================
   Stopping Chrome Proxy
========================================

[1/2] Stopping Chrome...
  SUCCESS: Chrome stopped
[2/2] Stopping SSH tunnel...
  SUCCESS: SSH tunnel stopped

Done!
```

#### 测试代理

```bash
# 测试代理连接
~/.openclaw/skills/chrome-proxy-linux/scripts/test-proxy.sh
```

**预期输出：**
```
========================================
   Proxy Test
========================================

[1/3] Checking SSH tunnel...
  SUCCESS: SSH tunnel running (port 1080)
[2/3] Testing exit IP...
  Exit IP: 76.13.219.143
[3/3] Testing websites...
  GitHub: SUCCESS
  StackOverflow: SUCCESS
  NPM: SUCCESS

Test complete!
```

---

### 方式 2：集成到 OpenClaw

激活技能后，可以使用以下命令：

```
/chrome-proxy-linux start    # 启动 Chrome with SOCKS5 代理
/chrome-proxy-linux stop     # 停止 Chrome 和 SSH 隧道
/chrome-proxy-linux status   # 查看状态
/chrome-proxy-linux test     # 测试代理连接
```

---

## 📊 验证代理是否工作

### 测试出口 IP

```bash
# 使用代理访问 API 检查出口 IP
curl --socks5 127.0.0.1:1080 -s https://api.ip.sb/ip

# 预期输出：76.13.219.143
```

### 测试网站访问

```bash
# 测试 GitHub
curl --socks5 127.0.0.1:1080 -s -o /dev/null -w "GitHub: %{http_code}\n" https://github.com

# 预期输出：GitHub: 200

# 测试 StackOverflow
curl --socks5 127.0.0.1:1080 -s -o /dev/null -w "StackOverflow: %{http_code}\n" https://stackoverflow.com

# 预期输出：StackOverflow: 200
```

---

## 🔧 常见问题

### 1. Chrome 无法启动

**症状：** Chrome 提示"WARNING: Chrome may have failed to start"

**原因：** 
- 没有图形界面环境
- Chrome 路径不正确

**解决：**
```bash
# 检查 Chrome 是否在运行
pgrep -f "google-chrome.*--proxy-server"

# 如果没有运行，检查 Chrome 安装
command -v google-chrome || command -v google-chrome-stable

# 手动启动 Chrome 测试
google-chrome --version
```

### 2. SSH 隧道无法建立

**症状：** "ERROR: Failed to establish SSH tunnel"

**原因：**
- VPS 连接失败
- 密码错误
- 端口被占用

**解决：**
```bash
# 测试 VPS 连接
sshpass -p 'Whj001.Whj001' ssh -o ConnectTimeout=5 root@76.13.219.143 "echo 'OK'"

# 检查端口占用
netstat -tlnp | grep 1080

# 停止旧的 SSH 隧道
pkill -f "ssh.*-D 1080"
```

### 3. 代理不工作

**症状：** curl 命令超时或失败

**原因：**
- SSH 隧道未启动
- 端口配置错误
- 代理参数错误

**解决：**
```bash
# 检查 SSH 隧道
pgrep -f "ssh.*-D 1080"
netstat -tlnp | grep 1080

# 检查代理配置
curl --socks5 127.0.0.1:1080 -v https://github.com
```

---

## 🎨 自定义配置

### 修改 VPS 配置

编辑 `start-chrome.sh` 和 `scripts/start-ssh.sh`：

```bash
# VPS 配置
VPS_HOST="your.vps.ip"        # VPS IP 地址
VPS_USER="root"               # VPS 用户名
VPS_PASS="your_password"      # VPS 密码
SOCKS_PORT=1080               # SOCKS5 代理端口
```

### 修改 Chrome 配置

编辑 `start-chrome.sh`：

```bash
# Chrome 配置
CHROME_CMD="google-chrome"                # Chrome 命令
CHROME_PROFILE="/tmp/chrome-proxy-profile"  # 用户数据目录
```

### 修改代理参数

编辑 `start-chrome.sh`，Chrome 启动参数部分：

```bash
# Chrome 代理参数
--proxy-server="socks5://127.0.0.1:1080"
--proxy-bypass-list="<local>"
--user-data-dir="$CHROME_PROFILE"
```

---

## 🔐 安全建议

1. **不要分享配置文件**
   - 脚本包含 VPS 密码
   - 不要上传到公开仓库

2. **定期更改 VPS 密码**
   - 提高账户安全性
   - 同时更新脚本中的密码

3. **使用完记得停止**
   - 停止 Chrome 和 SSH 隧道
   - 避免资源浪费

---

## 📝 进阶用法

### 仅启动 SSH 隧道

```bash
# 仅启动 SSH 隧道（不启动 Chrome）
~/.openclaw/skills/chrome-proxy-linux/scripts/start-ssh.sh
```

### 手动配置浏览器代理

在浏览器中手动设置代理：
- **代理类型：** SOCKS5
- **主机：** 127.0.0.1
- **端口：** 1080

### 创建桌面快捷方式

创建 `~/.local/share/applications/chrome-proxy.desktop`：

```desktop
[Desktop Entry]
Version=1.0
Type=Application
Name=Chrome Proxy
Comment=Chrome with SOCKS5 Proxy
Exec=/home/admin/.openclaw/skills/chrome-proxy-linux/start-chrome.sh
Icon=google-chrome
Terminal=true
Categories=Network;
```

---

## 📊 测试结果

### ✅ 已验证功能

| 功能 | 状态 | 测试时间 |
|------|------|---------|
| SSH 隧道启动 | ✅ 正常 | 2026-03-14 16:21 |
| Chrome 启动 | ✅ 正常 | 2026-03-14 16:21 |
| 代理出口 IP | ✅ 76.13.219.143 | 2026-03-14 16:21 |
| GitHub 访问 | ✅ 200 | 2026-03-14 16:21 |
| StackOverflow 访问 | ✅ 200 | 2026-03-14 16:21 |
| NPM 访问 | ✅ 正常 | 2026-03-14 16:21 |

### ⚠️ 已知限制

| 服务 | 状态 | 说明 |
|------|------|------|
| Google | ⚠️ 受限 | VPS 网络策略 |
| YouTube | ⚠️ 受限 | VPS 网络策略 |

---

## 📞 获取帮助

如果遇到问题：

1. **查看日志**
   ```bash
   # 查看 SSH 隧道日志
   # SSH 隧道使用后台模式，需要手动调试
   ```

2. **检查配置**
   ```bash
   # 检查脚本权限
   ls -la ~/.openclaw/skills/chrome-proxy-linux/

   # 检查脚本内容
   cat ~/.openclaw/skills/chrome-proxy-linux/start-chrome.sh
   ```

3. **手动测试**
   ```bash
   # 手动启动 SSH 隧道
   sshpass -p 'Whj001.Whj001' ssh -D 1080 -C -N root@76.13.219.143

   # 手动测试代理
   curl --socks5 127.0.0.1:1080 https://github.com
   ```

---

## 🎉 总结

**✅ Chrome Proxy Linux 技能已经可以使用！**

**核心功能：**
- ✅ SSH SOCKS5 隧道（使用 sshpass 密码认证）
- ✅ Chrome 浏览器代理启动
- ✅ 代理连接测试
- ✅ 完整的启动/停止脚本

**使用方法：**
```bash
# 启动
~/.openclaw/skills/chrome-proxy-linux/start-chrome.sh

# 停止
~/.openclaw/skills/chrome-proxy-linux/stop-chrome.sh

# 测试
~/.openclaw/skills/chrome-proxy-linux/scripts/test-proxy.sh
```

**适用场景：**
- 🌐 访问 GitHub、StackOverflow 等开发网站
- 🔧 临时需要代理上网
- 🛡️ 不影响系统其他应用的独立代理

---

**文档版本：** 1.0  
**更新时间：** 2026-03-14 16:21 GMT+8  
**作者：** openclaw
