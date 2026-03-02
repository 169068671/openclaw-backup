# SSH 隧道代理方案（推荐）

**创建时间：** 2026-03-02 14:25 (GMT+8)
**状态：** ✅ 可用，更稳定

---

## 🎯 为什么使用 SSH 隧道

**Tinyproxy 的问题：**
- HTTPS 代理连接不稳定
- 容易超时
- 配置复杂

**SSH 隧道的优势：**
- ✅ 更稳定可靠
- ✅ 支持 SOCKS5 协议
- ✅ 自动加密
- ✅ 配置简单
- ✅ 浏览器原生支持

---

## 🚀 快速配置

### 方法 1：临时使用（推荐用于测试）

在阿里云上运行：

```bash
# 创建 SSH 隧道（后台运行）
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143

# 或不使用 sshpass（需要手动输入密码）
ssh -N -D 1080 -f root@76.13.219.143
```

**参数说明：**
- `-N`：不执行远程命令，只做端口转发
- `-D 1080`：创建 SOCKS5 代理，监听本地 1080 端口
- `-f`：后台运行

**验证隧道是否建立：**
```bash
netstat -tlnp | grep 1080
# 应该看到：127.0.0.1:1080
```

**停止隧道：**
```bash
# 查找 SSH 隧道进程
ps aux | grep "ssh -N -D 1080"

# 杀掉进程
kill <PID>
```

---

### 方法 2：永久使用（开机自启动）

创建 systemd 服务：

```bash
sudo cat > /etc/systemd/system/ssh-tunnel.service << 'EOF'
[Unit]
Description=SSH Tunnel to Hostinger VPS
After=network.target

[Service]
Type=simple
User=admin
ExecStart=/usr/bin/sshpass -p 'Whj001.Whj001' /usr/bin/ssh -N -D 1080 -o ServerAliveInterval=60 -o ServerAliveCountMax=3 root@76.13.219.143
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
```

**启用并启动服务：**

```bash
sudo systemctl daemon-reload
sudo systemctl enable ssh-tunnel
sudo systemctl start ssh-tunnel
sudo systemctl status ssh-tunnel
```

**查看日志：**
```bash
sudo journalctl -u ssh-tunnel -f
```

---

## 🌐 浏览器配置

### Chrome / Edge

1. **打开设置**
   - 设置 → 系统 → 打开计算机的代理设置

2. **配置 SOCKS5 代理**
   - 选择"手动设置代理"
   - SOCKS 主机：`127.0.0.1`
   - 端口：`1080`
   - SOCKS 版本：`SOCKS v5`
   - 不要勾选 SOCKS 代理的"对此服务器使用代理"
   - 清空 HTTP/HTTPS 代理设置

3. **保存**

### Firefox

1. **打开设置**
   - 菜单 → 设置 → 常规 → 网络设置

2. **配置 SOCKS5**
   - 手动配置代理
   - SOCKS 主机：`127.0.0.1`
   - 端口：`1080`
   - SOCKS v5
   - ✅ 勾选"远程 DNS"
   - 清空 HTTP/HTTPS/FTP 代理

3. **保存**

---

## 🧪 测试代理

### 测试 1：检查隧道

```bash
netstat -tlnp | grep 1080
# 应该看到：tcp  0  0 127.0.0.1:1080
```

### 测试 2：测试代理

```bash
# 测试 HTTP 请求
curl --socks5 127.0.0.1:1080 http://example.com

# 测试 HTTPS 请求
curl --socks5 127.0.0.1:1080 https://www.google.com
```

### 测试 3：浏览器测试

- 配置浏览器 SOCKS5 代理（见上文）
- 访问：https://www.google.com
- ✅ 应该可以正常访问

---

## 🎯 配置 PAC 文件（可选）

如果你想要智能路由（国内直连，国外走代理），可以修改 PAC 文件：

```bash
cat > /opt/proxy-socks5.pac << 'EOF'
function FindProxyForURL(url, host) {
    // OpenClaw 流量直连
    if (shExpMatch(host, "*.aliyuncs.com") ||
        shExpMatch(host, "*.openclaw.ai")) {
        return "DIRECT";
    }

    // 国内网站直连
    if (shExpMatch(host, "*.cn") ||
        shExpMatch(host, "*.baidu.com") ||
        shExpMatch(host, "*.qq.com") ||
        shExpMatch(host, "*.taobao.com")) {
        return "DIRECT";
    }

    // 本地地址直连
    if (isPlainHostName(host) ||
        shExpMatch(host, "localhost") ||
        shExpMatch(host, "127.*") ||
        shExpMatch(host, "10.*") ||
        shExpMatch(host, "192.168.*")) {
        return "DIRECT";
    }

    // 其他走 SOCKS5 代理
    return "SOCKS5 127.0.0.1:1080";
}
EOF
```

**浏览器配置 PAC 文件：**

Chrome/Edge:
- 设置 → 系统 → 打开计算机的代理设置
- 使用自动配置脚本
- 脚本地址：`file:///opt/proxy-socks5.pac`

---

## 📊 对比表

| 特性 | Tinyproxy | SSH 隧道 (SOCKS5) |
|------|-----------|------------------|
| 稳定性 | ⚠️ 不稳定 | ✅ 稳定 |
| HTTP 支持 | ✅ | ✅ |
| HTTPS 支持 | ⚠️ 有问题 | ✅ |
| 配置复杂度 | 中等 | 简单 |
| 加密 | ❌ 无 | ✅ 自动加密 |
| 浏览器支持 | ✅ | ✅ |
| 性能 | 中等 | 好 |
| 推荐度 | ⚠️ | ✅ 强烈推荐 |

---

## 🔧 故障排查

### 问题 1：隧道无法建立

**检查连接：**
```bash
ssh root@76.13.219.143
```

**如果无法 SSH 连接：**
- 检查密码是否正确
- 检查 VPS 是否在线
- 检查防火墙

### 问题 2：隧道断开

**添加保活参数：**
```bash
ssh -N -D 1080 -o ServerAliveInterval=60 -o ServerAliveCountMax=3 root@76.13.219.143
```

**或使用 autossh：**
```bash
apt install autossh
autossh -M 0 -N -D 1080 root@76.13.219.143
```

### 问题 3：浏览器无法访问

**检查 SOCKS5 配置：**
- 确认主机：127.0.0.1
- 确认端口：1080
- 确认版本：SOCKS v5

**检查隧道状态：**
```bash
netstat -tlnp | grep 1080
ps aux | grep "ssh -N -D"
```

---

## ✅ 快速开始

**最快的方式（3步）：**

1. **启动隧道**
   ```bash
   sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143
   ```

2. **配置浏览器**
   - Chrome/Edge → 设置 → 系统 → 代理
   - SOCKS 主机：`127.0.0.1`，端口：`1080`

3. **测试**
   - 访问：https://www.google.com

---

## 📝 配置变更记录

| 时间 | 变更内容 | 操作人 |
|------|---------|--------|
| 2026-03-02 14:25 | 创建 SSH 隧道方案文档 | openclaw |

---

**SSH 隧道方案更稳定，强烈推荐使用！** 🎉
