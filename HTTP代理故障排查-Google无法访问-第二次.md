# HTTP 代理故障排查 - Google 无法访问（第二次）

**问题时间：** 2026-03-02 14:18 (GMT+8)
**问题：** 通过代理访问 www.google.com 失败（第二次出现）
**状态：** ⚠️ 诊断中

---

## 🔍 问题描述

**症状：**
- 浏览器配置 PAC 文件后，无法访问 www.google.com
- curl 测试也失败：`Connection reset by peer`

**错误信息：**
```bash
$ curl -I -x http://76.13.219.143:8888 https://www.google.com
curl: (56) Recv failure: Connection reset by peer
```

---

## 🔬 诊断结果

### 测试 1：VPS 本地请求 Google

```bash
$ ssh root@76.13.219.143 "curl -I -x http://localhost:8888 https://www.google.com"
HTTP/2 200
```

✅ **VPS 本地可以访问 Google**

### 测试 2：从阿里云访问代理（HTTP）

```bash
$ curl -I -x http://76.13.219.143:8888 http://example.com
HTTP/1.1 200 OK
```

✅ **HTTP 请求成功**

### 测试 3：从阿里云访问代理（HTTPS/Google）

```bash
$ curl -I -x http://76.13.219.143:8888 https://www.google.com
curl: (56) Recv failure: Connection reset by peer
```

❌ **HTTPS 请求被重置**

### 测试 4：检查 VPS 连接

```bash
$ ssh root@76.13.219.143 "netstat -an | grep 8888"
tcp  0  0 0.0.0.0:8888      0.0.0.0:*        LISTEN
tcp  0  0 127.0.0.1:49828   127.0.0.1:8888   TIME_WAIT
tcp  0  0 76.13.219.143:8888  47.123.87.87:31730  TIME_WAIT
```

⚠️ **发现阿里云出口 IP：47.123.87.87**

---

## 💡 问题分析

**可能原因：**

1. **Hostinger VPS 安全限制**
   - VPS 可能对来自特定地区的流量有限制
   - 或有反 DDoS 机制

2. **阿里云出口 IP 被限制**
   - 47.123.87.87 可能被 VPS 的安全规则限制

3. **HTTPS CONNECT 方法问题**
   - HTTP 请求成功，HTTPS 请求失败
   - 可能是 CONNECT 方法被阻止

---

## ✅ 临时解决方案

### 方案 1：手动配置浏览器代理（跳过 PAC）

**Chrome/Edge:**
1. 设置 → 系统 → 打开计算机的代理设置
2. 手动设置代理
3. HTTP 代理：`76.13.219.143`
4. 端口：`8888`
5. ✅ 勾选"对 HTTP 协议使用此代理服务器"
6. ✅ 勾选"对 HTTPS 协议使用此代理服务器"
7. 保存

**测试：**
- 访问 https://www.google.com
- 如果成功，说明代理本身没问题，是 PAC 文件或浏览器配置问题

### 方案 2：使用 SSH 隧道（更稳定）

在阿里云上运行：

```bash
# 创建 SSH 隧道（后台运行）
ssh -N -D 1080 root@76.13.219.143 &

# 或使用 sshpass
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 root@76.13.219.143 &
```

**浏览器配置 SOCKS5 代理：**
- SOCKS 主机：`127.0.0.1`
- 端口：`1080`
- SOCKS 版本：`v5`

### 方案 3：直接在 VPS 上访问（开发用）

如果只是需要访问国外网站，可以直接 SSH 到 VPS 使用：

```bash
ssh root@76.13.219.143
curl https://www.google.com
```

---

## 🔧 正在排查

### 可能的解决方案 1：修改 Tinyproxy 配置

尝试添加 `ConnectPort` 允许 HTTPS CONNECT：

```conf
Port 8888
Listen 0.0.0.0
Allow 0.0.0.0/0
LogLevel Info
MaxClients 100
DisableViaHeader Yes
Timeout 600
ConnectPort 443  # 允许 HTTPS CONNECT
ConnectPort 80
```

### 可能的解决方案 2：使用 Squid 代理（更强大）

如果 Tinyproxy 问题无法解决，可以考虑安装 Squid：

```bash
# 在 VPS 上安装 Squid
apt install squid

# 配置 Squid
# (具体配置待补充)
```

### 可能的解决方案 3：使用 V2Ray/Clash

更现代的代理方案，支持更多协议和功能。

---

## 🧪 测试步骤

1. **测试手动代理配置**
   - 在浏览器中直接配置代理（不使用 PAC）
   - 访问 https://www.google.com
   - 如果成功，说明 PAC 文件有问题

2. **测试 HTTP 网站**
   - 访问 http://example.com（通过代理）
   - 如果成功，说明是 HTTPS CONNECT 问题

3. **检查浏览器代理设置**
   - 确认 PAC 文件路径正确：`file:///opt/proxy.pac`
   - 确认浏览器加载了 PAC 文件

4. **查看浏览器开发者工具**
   - F12 → Network
   - 查看 Google 请求的详细信息
   - 检查是否有代理相关的错误

---

## 📋 下一步行动

**请尝试：**

1. **临时方案 1：** 手动配置浏览器代理（不用 PAC）
   - 测试能否访问 Google

2. **临时方案 2：** 使用 SSH 隧道
   - 测试能否访问 Google

3. **告诉我结果：**
   - 哪种方案成功了？
   - 浏览器提示什么错误？

**根据测试结果，我会继续深入排查。**

---

## 📝 配置变更记录

| 时间 | 变更内容 | 操作人 |
|------|---------|--------|
| 2026-03-02 14:18 | Google 无法访问（第二次） | 用户反馈 |
| 2026-03-02 14:19 | 诊断问题，发现 HTTPS CONNECT 被重置 | openclaw |
| 2026-03-02 14:20 | 创建临时解决方案文档 | openclaw |

---

## 🔗 相关文档

1. **HTTP代理配置方案-HostingerVPS.md** - 详细配置步骤
2. **HTTP代理故障排查-Google无法访问.md** - 第一次故障排查
3. **本故障排查文档** - 第二次故障排查

---

**正在排查中，请先尝试临时解决方案！** 🔍
