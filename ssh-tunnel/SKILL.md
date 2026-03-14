# SSH Tunnel Manager

## 简介

SSH隧道管理工具，通过SSH隧道建立SOCKS5代理，并自动测试Google连通性。

## 功能

- ✅ 一键启动/停止SSH隧道
- ✅ 实时状态监控（进程信息、网络监听、运行时间）
- ✅ 自动测试Google连通性
- ✅ 彩色输出，界面友好
- ✅ 密码认证（无需SSH密钥）

## 配置

- **服务器**: 76.13.219.143 (srv1437164)
- **用户**: root
- **本地端口**: 1080 (SOCKS5)
- **认证**: 密码

## 使用方法

### 基本命令

```bash
# 启动隧道（自动测试 Google）
/home/admin/openclaw/workspace/ssh-tunnel/ssh-tunnel.sh start

# 启动隧道（不测试 Google，加快启动速度）
/home/admin/openclaw/workspace/ssh-tunnel/ssh-tunnel.sh start --no-check

# 停止隧道
/home/admin/openclaw/workspace/ssh-tunnel/ssh-tunnel.sh stop

# 查看状态
/home/admin/openclaw/workspace/ssh-tunnel/ssh-tunnel.sh status

# 重启隧道
/home/admin/openclaw/workspace/ssh-tunnel/ssh-tunnel.sh restart
```

### 快捷方式

```bash
# 创建符号链接（可选）
ln -s /home/admin/openclaw/workspace/ssh-tunnel/ssh-tunnel.sh ~/ssh-tunnel

# 使用快捷命令
~/ssh-tunnel start
~/ssh-tunnel status
```

## Google 连通性测试

脚本会自动测试Google连通性：

1. **自动测试时机**:
   - 启动隧道后（除非使用 `--no-check`）
   - 查看状态时

2. **测试方法**:
   - 通过 SOCKS5 代理（`socks5h://127.0.0.1:1080`）
   - 访问 `https://www.google.com`
   - 超时时间: 10秒

3. **测试结果**:
   - ✅ **HTTP 200/301/302**: VPS可以访问Google
   - ⚠️ **其他HTTP状态**: VPS可以连接Google，但返回异常
   - ❌ **Connection timed out**: VPS无法访问Google（网络限制）

## 输出示例

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🟢 SSH 隧道状态：运行中
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 服务器: 76.13.219.143 (srv1437164)
🔌 本地端口: 127.0.0.1:1080 (SOCKS5)
👤 用户: root
🔑 认证: 密码
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 进程信息:
  PID: 38462
  CPU: 0.0%
  MEM: 0.0%
  运行时间: 01:52
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 网络监听:
  IPv4: 127.0.0.1:1080 ✅
  IPv6: [::1]:1080 ❌
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 测试 Google 连通性...
   ✅ 测试成功: HTTP 200
   说明: VPS 可以访问 Google
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 使用代理

### 命令行工具

```bash
# curl
curl --proxy socks5h://127.0.0.1:1080 https://www.google.com

# wget
export ALL_PROXY=socks5h://127.0.0.1:1080
wget https://www.google.com

# git
git config --global http.proxy socks5://127.0.0.1:1080
git config --global https.proxy socks5://127.0.0.1:1080
```

### 浏览器配置

**Chrome/Edge**:
1. 设置 → 系统 → 打开您计算机的代理设置
2. 配置 SOCKS5 代理:
   - 地址: `127.0.0.1`
   - 端口: `1080`

**Firefox**:
1. 设置 → 网络设置
2. 选择 "手动配置代理"
3. 配置 SOCKS v5 代理:
   - 主机: `127.0.0.1`
   - 端口: `1080`

## 故障排查

### 隧道无法启动

1. 检查密码是否正确
2. 检查VPS是否可访问: `sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143`
3. 检查端口是否被占用: `netstat -tlnp | grep 1080`

### Google 测试失败

1. 这是VPS网络质量问题，不是隧道配置问题
2. 隧道仍然可以正常使用
3. 只影响通过VPS访问Google的服务

### 权限问题

确保脚本有执行权限:
```bash
chmod +x /home/admin/openclaw/workspace/ssh-tunnel/ssh-tunnel.sh
```

## 注意事项

1. **socks5h vs socks5**: 使用 `socks5h://` 确保远程服务器解析DNS
2. **密码安全**: 脚本中包含明文密码，请妥善保管
3. **自动重连**: 脚本不提供自动重连功能，需要手动重启

## 版本

- **版本**: v1.2
- **创建日期**: 2026-03-13
- **更新**: 添加Google连通性测试功能
