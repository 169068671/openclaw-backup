# SSH隧道自动启动配置完成

## 配置信息

**服务名称：** ssh-tunnel.service
**状态：** ✅ 已启用并运行
**SOCKS5代理：** 127.0.0.1:1080

## Systemd服务配置

**服务文件：** `/etc/systemd/system/ssh-tunnel.service`

```ini
[Unit]
Description=SSH Tunnel to VPS (SOCKS5 Proxy)
After=network.target

[Service]
Type=simple
User=admin
ExecStart=/usr/bin/sshpass -p 'Whj001.Whj001' /usr/bin/ssh -N -D 1080 root@76.13.219.143
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

## 使用方法

### 1. 服务管理命令

```bash
# 查看服务状态
sudo systemctl status ssh-tunnel.service

# 启动服务
sudo systemctl start ssh-tunnel.service

# 停止服务
sudo systemctl stop ssh-tunnel.service

# 重启服务
sudo systemctl restart ssh-tunnel.service

# 禁用开机自启
sudo systemctl disable ssh-tunnel.service
```

### 2. 测试连接

```bash
# 测试SOCKS5代理
curl --socks5 127.0.0.1:1080 http://example.com

# 测试HTTPS访问
curl --socks5 127.0.0.1:1080 https://www.google.com
```

### 3. 浏览器配置（Chrome/Edge）

1. 打开设置 → 系统 → 代理设置
2. 选择"SOCKS代理"
3. SOCKS主机：`127.0.0.1`
4. 端口：`1080`
5. 确定保存

4. 访问：https://www.google.com

## 特性

- ✅ 开机自动启动
- ✅ 断线自动重连（10秒后重试）
- ✅ 代理地址：127.0.0.1:1080
- ✅ 支持HTTP和HTTPS

## 测试结果

**配置时间：** 2026-03-02 19:22

**测试验证：**
- ✅ 服务启动成功
- ✅ 端口监听正常（IPv4和IPv6）
- ✅ HTTP访问测试成功
- ✅ SOCKS5代理工作正常

**状态：** 已启用开机自启

---

**注意：** 服务会在网络启动后自动运行，无需手动干预。
