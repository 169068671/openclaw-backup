# HTTP 代理故障排查 - Google 无法访问

**问题时间：** 2026-03-02 14:07 (GMT+8)
**问题：** 通过代理访问 www.google.com 失败
**状态：** ✅ 已解决

---

## 🔍 问题描述

**症状：**
- 访问 www.google.com 时无法连接
- 通过代理 `http://76.13.219.143:8888` 访问时返回连接重置错误

**错误信息：**
```bash
$ curl -I -x http://76.13.219.143:8888 https://www.google.com
curl: (56) Recv failure: Connection reset by peer
```

---

## 🔬 问题诊断

### 测试 1：VPS 直连 Google

```bash
$ ssh root@76.13.219.143 "curl -I https://www.google.com"
HTTP/2 200
```

✅ **结论：** VPS 本身可以访问 Google，网络连接正常

### 测试 2：通过代理访问

```bash
$ curl -I -x http://76.13.219.143:8888 https://www.google.com
curl: (56) Recv failure: Connection reset by peer
```

❌ **结论：** 代理服务器拒绝了连接

### 测试 3：检查 Tinyproxy 配置

```bash
$ ssh root@76.13.219.143 "cat /etc/tinyproxy/tinyproxy.conf"
Port 8888
Listen 0.0.0.0
LogLevel Info
```

❌ **发现问题：** 配置缺少 `Allow 0.0.0.0/0` 规则

---

## 💡 根本原因

**Tinyproxy 配置不完整**

缺少客户端访问控制规则，导致代理拒绝了来自阿里云的连接请求。

**问题配置：**
```
Port 8888
Listen 0.0.0.0
LogLevel Info
```

**缺失配置：**
```
Allow 0.0.0.0/0
```

---

## ✅ 解决方案

### 1. 更新 Tinyproxy 配置

```bash
ssh root@76.13.219.143
```

```bash
cat > /etc/tinyproxy/tinyproxy.conf << 'EOF'
Port 8888
Listen 0.0.0.0
Allow 0.0.0.0/0
LogLevel Info
MaxClients 100
DisableViaHeader Yes
Timeout 600
EOF
```

### 2. 重启 Tinyproxy

```bash
killall tinyproxy
sleep 1
/usr/bin/tinyproxy -c /etc/tinyproxy/tinyproxy.conf &
```

### 3. 验证修复

```bash
# 测试代理连接
curl -I -x http://76.13.219.143:8888 https://www.google.com

# 预期结果：
# HTTP/1.0 200 Connection established
# HTTP/2 200
```

---

## 🧪 验证测试

### 测试国外网站（走代理）

```bash
$ curl -I -x http://76.13.219.143:8888 https://www.google.com
HTTP/1.0 200 Connection established
Proxy-agent: tinyproxy/1.11.0

HTTP/2 200
content-type: text/html; charset=ISO-8859-1
```

✅ **成功！** 代理可以访问国外网站

### 测试国内网站（直连）

```bash
$ curl -I https://www.baidu.com
HTTP/1.1 200 OK
```

✅ **成功！** 国内网站直连访问

### 测试 OpenClaw（直连）

```bash
$ cat /proc/$(pgrep -f openclaw-gateway)/environ | tr '\0' '\n' | grep -i proxy
(无输出)
```

✅ **成功！** OpenClaw 未设置代理，走直连

---

## 📋 配置文件对比

### 修复前

```conf
Port 8888
Listen 0.0.0.0
LogLevel Info
```

**问题：**
- ❌ 没有 Allow 规则
- ❌ 没有客户端连接限制
- ❌ 没有超时设置

### 修复后

```conf
Port 8888
Listen 0.0.0.0
Allow 0.0.0.0/0
LogLevel Info
MaxClients 100
DisableViaHeader Yes
Timeout 600
```

**改进：**
- ✅ 允许所有客户端访问（0.0.0.0/0）
- ✅ 最大客户端数：100
- ✅ 隐藏代理头（DisableViaHeader）
- ✅ 连接超时：600 秒

---

## 🔧 管理命令

### 查看 Tinyproxy 状态

```bash
# SSH 登录 VPS
ssh root@76.13.219.143

# 查看进程
ps aux | grep tinyproxy

# 查看端口
netstat -tlnp | grep 8888

# 查看配置
cat /etc/tinyproxy/tinyproxy.conf
```

### 重启 Tinyproxy

```bash
# 方法 1：killall
killall tinyproxy
/usr/bin/tinyproxy -c /etc/tinyproxy/tinyproxy.conf &

# 方法 2：systemd（如果配置了服务）
systemctl restart tinyproxy
systemctl status tinyproxy
```

### 测试代理

```bash
# 测试 Google
curl -I -x http://76.13.219.143:8888 https://www.google.com

# 测试其他国外网站
curl -I -x http://76.13.219.143:8888 https://www.twitter.com

# 测试国内网站（应该直连）
curl -I https://www.baidu.com
```

---

## 🎯 如何使用代理

### 方法 1：浏览器直接配置代理

**Chrome/Edge:**
1. 设置 → 系统 → 打开计算机的代理设置
2. 手动设置代理
3. HTTP 代理：`76.13.219.143`
4. 端口：`8888`
5. ✅ 勾选"对 HTTP 协议使用此代理服务器"
6. ✅ 勾选"对 HTTPS 协议使用此代理服务器"

**Firefox:**
1. 设置 → 常规 → 网络设置
2. 手动配置代理
3. HTTP 代理：`76.13.219.143`，端口：`8888`
4. HTTPS 代理：`76.13.219.143`，端口：`8888`
5. SOCKS 主机：不填
6. ✅ 勾选"所有协议使用相同代理"

### 方法 2：使用 PAC 文件（推荐）

**配置 PAC 文件：**
1. 设置 → 系统 → 打开计算机的代理设置
2. 使用自动配置脚本
3. 脚本地址：`http://你的阿里云内网IP/proxy.pac`

**PAC 文件路径：** `/opt/proxy.pac`

**PAC 规则会自动：**
- 国内网站 → DIRECT
- 国外网站 → PROXY 76.13.219.143:8888
- OpenClaw 相关域名 → DIRECT
- 本地地址 → DIRECT

### 方法 3：命令行使用代理

```bash
# 设置代理环境变量
export http_proxy="http://76.13.219.143:8888"
export https_proxy="http://76.13.219.143:8888"

# 测试
curl https://www.google.com

# 取消代理
unset http_proxy
unset https_proxy
```

---

## 📊 配置对比表

| 项目 | 修复前 | 修复后 |
|------|--------|--------|
| Tinyproxy Allow 规则 | ❌ 无 | ✅ 0.0.0.0/0 |
| MaxClients | 默认 | ✅ 100 |
| DisableViaHeader | 默认 | ✅ Yes |
| Timeout | 默认 | ✅ 600s |
| 访问 Google | ❌ 失败 | ✅ 成功 |
| 访问国外网站 | ❌ 失败 | ✅ 成功 |
| 访问国内网站 | ✅ 直连 | ✅ 直连 |
| OpenClaw 直连 | ✅ 直连 | ✅ 直连 |

---

## ⚠️ 注意事项

### 安全性

**当前配置允许所有客户端访问：**
```conf
Allow 0.0.0.0/0
```

**生产环境建议：**
```conf
# 只允许阿里云 IP 访问
Allow 你的阿里云出口IP/32

# 或配置认证
BasicAuth username password
```

### 性能优化

- **MaxClients: 100** - 可根据实际使用情况调整
- **Timeout: 600** - 超时时间，避免长时间占用连接

### 监控

定期查看代理日志（如果启用了日志）：
```bash
tail -f /var/log/tinyproxy.log
```

---

## 🔄 故障排查流程

如果再次出现类似问题：

1. **检查 Tinyproxy 进程**
   ```bash
   ps aux | grep tinyproxy
   ```

2. **检查端口监听**
   ```bash
   netstat -tlnp | grep 8888
   ```

3. **检查配置文件**
   ```bash
   cat /etc/tinyproxy/tinyproxy.conf
   ```

4. **测试本地连接**
   ```bash
   ssh root@76.13.219.143 "curl -I -x http://localhost:8888 https://www.google.com"
   ```

5. **测试远程连接**
   ```bash
   curl -I -x http://76.13.219.143:8888 https://www.google.com
   ```

6. **查看日志**
   ```bash
   journalctl -u tinyproxy -f
   ```

---

## 📝 配置变更记录

| 时间 | 变更内容 | 操作人 |
|------|---------|--------|
| 2026-03-02 14:07 | 发现代理无法访问 Google | openclaw |
| 2026-03-02 14:08 | 更新 Tinyproxy 配置，添加 Allow 规则 | openclaw |
| 2026-03-02 14:08 | 测试验证修复成功 | openclaw |
| 2026-03-02 14:09 | 创建故障排查文档 | openclaw |

---

## ✅ 问题解决确认

- [x] 诊断问题根源（缺少 Allow 规则）
- [x] 更新 Tinyproxy 配置
- [x] 重启代理服务
- [x] 验证国外网站访问（Google）
- [x] 验证国内网站访问（百度）
- [x] 验证 OpenClaw 直连
- [x] 更新文档
- [x] Git 提交变更

---

## 🔗 相关文档

1. **HTTP代理配置方案-HostingerVPS.md** - 详细配置步骤
2. **HTTP代理配置完成报告.md** - 配置状态和测试结果
3. **故障排查流程** - 本文档

---

**问题已解决！代理现在可以正常访问国外网站了！** 🎉
