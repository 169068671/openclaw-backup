# HTTP 代理配置方案 - Hostinger VPS

## 需求说明

**当前环境：** 阿里云内网（国内网络）

**目标：**
1. 国内网站 → 直连（不走代理）
2. 国外网站 → 通过 Hostinger VPS 代理访问
3. **OpenClaw 流量 → 直连（必须走国内网络）**
4. 使用国内大模型（如阿里云百炼），OpenClaw 不需要外网

---

## 方案架构

```
阿里云内网
    ├── OpenClaw → 直连国内网络（不走代理）
    ├── 国内网站 → 直连
    └── 国外网站 → Hostinger VPS (HTTP 代理) → 目标网站
```

---

## 第一步：在 Hostinger VPS 上搭建 HTTP 代理

### 1.1 登录 Hostinger VPS

```bash
ssh root@76.13.219.143
# 输入密码：Whj001.Whj001
```

### 1.2 安装 Tinyproxy（轻量级 HTTP 代理）

```bash
# 更新系统包
apt update

# 安装 Tinyproxy
apt install -y tinyproxy

# 备份原配置
cp /etc/tinyproxy/tinyproxy.conf /etc/tinyproxy/tinyproxy.conf.bak
```

### 1.3 配置 Tinyproxy

```bash
nano /etc/tinyproxy/tinyproxy.conf
```

**关键配置项：**

```conf
# 监听端口（默认 8888）
Port 8888

# 监听所有接口
Listen 0.0.0.0

# 允许的客户端 IP（阿里云内网 IP，或设置为 0.0.0.0/0 允许所有）
Allow 0.0.0.0/0

# 关闭日志记录（减少磁盘 IO）
LogLevel Info

# 最大连接数
MaxClients 100

# 禁用 Via 头（隐藏代理服务器）
DisableViaHeader Yes
```

### 1.4 启动并验证服务

```bash
# 启动 Tinyproxy
systemctl start tinyproxy

# 设置开机自启
systemctl enable tinyproxy

# 检查状态
systemctl status tinyproxy

# 检查端口监听
netstat -tlnp | grep 8888

# 测试代理是否工作
curl --proxy http://76.13.219.143:8888 https://www.google.com -I
```

### 1.5 配置防火墙

```bash
# 允许 8888 端口
ufw allow 8888/tcp

# 查看防火墙状态
ufw status
```

---

## 第二步：配置客户端代理规则（PAC 文件）

### 2.1 什么是 PAC 文件？

PAC（Proxy Auto-Config）文件是一个 JavaScript 文件，用于自动决定哪些请求走代理，哪些直连。

### 2.2 创建 PAC 文件

在阿里云服务器上创建 `/opt/proxy.pac`：

```javascript
function FindProxyForURL(url, host) {
    // === 关键：OpenClaw 流量必须直连 ===
    // 国内大模型域名直连
    if (shExpMatch(host, "*.aliyuncs.com") ||
        shExpMatch(host, "*.dashscope.aliyuncs.com") ||
        shExpMatch(host, "*.bailian.console.aliyun.com")) {
        return "DIRECT";
    }

    // OpenClaw 相关域名
    if (shExpMatch(host, "*.openclaw.ai") ||
        shExpMatch(host, "*.clawhub.com")) {
        return "DIRECT";
    }

    // === 国内网站直连 ===
    // 常见国内域名后缀
    if (shExpMatch(host, "*.cn") ||
        shExpMatch(host, "*.com.cn") ||
        shExpMatch(host, "*.net.cn") ||
        shExpMatch(host, "*.org.cn")) {
        return "DIRECT";
    }

    // 国内大厂域名
    if (shExpMatch(host, "*.baidu.com") ||
        shExpMatch(host, "*.qq.com") ||
        shExpMatch(host, "*.taobao.com") ||
        shExpMatch(host, "*.tmall.com") ||
        shExpMatch(host, "*.jd.com") ||
        shExpMatch(host, "*.weibo.com") ||
        shExpMatch(host, "*.zhihu.com") ||
        shExpMatch(host, "*.bilibili.com") ||
        shExpMatch(host, "*.douyin.com") ||
        shExpMatch(host, "*.163.com") ||
        shExpMatch(host, "*.sina.com.cn") ||
        shExpMatch(host, "*.sohu.com") ||
        shExpMatch(host, "*.360.cn")) {
        return "DIRECT";
    }

    // 本地地址直连
    if (isPlainHostName(host) ||
        shExpMatch(host, "localhost") ||
        shExpMatch(host, "127.*") ||
        shExpMatch(host, "10.*") ||
        shExpMatch(host, "172.16.*") ||
        shExpMatch(host, "172.17.*") ||
        shExpMatch(host, "172.18.*") ||
        shExpMatch(host, "172.19.*") ||
        shExpMatch(host, "172.20.*") ||
        shExpMatch(host, "172.21.*") ||
        shExpMatch(host, "172.22.*") ||
        shExpMatch(host, "172.23.*") ||
        shExpMatch(host, "172.24.*") ||
        shExpMatch(host, "172.25.*") ||
        shExpMatch(host, "172.26.*") ||
        shExpMatch(host, "172.27.*") ||
        shExpMatch(host, "172.28.*") ||
        shExpMatch(host, "172.29.*") ||
        shExpMatch(host, "172.30.*") ||
        shExpMatch(host, "172.31.*") ||
        shExpMatch(host, "192.168.*")) {
        return "DIRECT";
    }

    // === 其他所有请求走代理 ===
    return "PROXY 76.13.219.143:8888";
}
```

### 2.3 部署 PAC 文件

将 PAC 文件部署到本地 HTTP 服务器（可选）：

```bash
# 安装 Nginx
apt install -y nginx

# 复制 PAC 文件到 Web 目录
cp /opt/proxy.pac /var/www/html/proxy.pac

# 设置权限
chmod 644 /var/www/html/proxy.pac

# 测试访问
curl http://localhost/proxy.pac
```

**访问地址：** `http://你的阿里云内网IP/proxy.pac`

---

## 第三步：配置客户端使用代理

### 3.1 配置系统环境变量

编辑 `/etc/environment`：

```bash
nano /etc/environment
```

添加以下配置：

```bash
# 设置 PAC 文件路径
export PAC_FILE="/opt/proxy.pac"

# 或设置 HTTP/HTTPS 代理（配合规则使用）
export http_proxy="http://127.0.0.1:8888"
export https_proxy="http://127.0.0.1:8888"

# 关键：OpenClaw 进程禁用代理
export NO_PROXY="aliyuncs.com,dashscope.aliyuncs.com,bailian.console.aliyun.com,openclaw.ai,clawhub.com,127.0.0.1,localhost"
```

### 3.2 配置 OpenClaw 服务（重要！）

编辑 OpenClaw 的 systemd 服务文件：

```bash
nano /etc/systemd/system/openclaw.service
```

**确保环境变量中排除代理：**

```ini
[Unit]
Description=OpenClaw Gateway Service
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/openclaw
Environment="NODE_ENV=production"
# 关键：禁用所有代理，确保走国内网络
Environment="NO_PROXY=*"
Environment="no_proxy=*"
ExecStart=/usr/bin/node /usr/lib/node_modules/openclaw/dist/gateway.js
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

重新加载服务：

```bash
systemctl daemon-reload
systemctl restart openclaw
systemctl status openclaw
```

### 3.3 验证 OpenClaw 是否直连

```bash
# 查看 OpenClaw 进程的环境变量
cat /proc/$(pgrep -f "openclaw/gateway.js")/environ | tr '\0' '\n' | grep -i proxy

# 应该显示：
# no_proxy=*
# NO_PROXY=*
```

---

## 第四步：测试配置

### 4.1 测试代理功能

```bash
# 测试国外网站（应走代理）
curl --proxy http://76.13.219.143:8888 https://www.google.com -I

# 测试国内网站（应直连）
curl https://www.baidu.com -I
```

### 4.2 测试 OpenClaw 直连

```bash
# 测试阿里云百炼 API（应直连）
curl https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation -I

# 查看 OpenClaw 日志，确认没有代理错误
journalctl -u openclaw -f
```

### 4.3 测试 PAC 文件规则

```bash
# 使用 PAC 文件测试
curl -p http://localhost/proxy.pac https://www.google.com
curl -p http://localhost/proxy.pac https://dashscope.aliyuncs.com
```

---

## 第五步：常用管理命令

### 5.1 Hostinger VPS 上管理 Tinyproxy

```bash
# 查看代理日志
tail -f /var/log/tinyproxy/tinyproxy.log

# 重启代理服务
systemctl restart tinyproxy

# 查看连接状态
netstat -tlnp | grep 8888
ss -tn | grep 8888
```

### 5.2 阿里云上查看代理状态

```bash
# 测试代理连接
telnet 76.13.219.143 8888

# 检查 DNS 解析
nslookup www.google.com
```

---

## 第六步：安全加固（可选但推荐）

### 6.1 配置 IP 白名单（仅允许阿里云访问）

```bash
# 获取阿里云内网出口 IP（假设是 x.x.x.x）
curl ifconfig.me

# 编辑 Tinyproxy 配置，只允许阿里云 IP
nano /etc/tinyproxy/tinyproxy.conf
```

修改 `Allow` 行：

```conf
Allow 阿里云出口IP/32
# 例如：Allow 47.100.0.0/16
```

重启服务：

```bash
systemctl restart tinyproxy
```

### 6.2 配置代理认证（可选）

安装 `htpasswd` 工具：

```bash
apt install -y apache2-utils
```

创建密码文件：

```bash
htpasswd -c /etc/tinyproxy/passwd proxy_user
# 输入密码
```

修改 Tinyproxy 配置启用认证：

```conf
BasicAuth proxy_user your_password
```

重启服务：

```bash
systemctl restart tinyproxy
```

客户端使用时添加认证：

```bash
export http_proxy="http://proxy_user:your_password@76.13.219.143:8888"
```

---

## 第七步：故障排查

### 7.1 代理连接失败

```bash
# 检查 Hostinger VPS 防火墙
ssh root@76.13.219.143 "ufw status"

# 检查 Tinyproxy 状态
ssh root@76.13.219.143 "systemctl status tinyproxy"

# 检查端口监听
ssh root@76.13.219.143 "netstat -tlnp | grep 8888"
```

### 7.2 OpenClaw 无法访问国内大模型

```bash
# 确认 OpenClaw 没有使用代理
cat /proc/$(pgrep -f "openclaw/gateway.js")/environ | tr '\0' '\n' | grep -i proxy

# 测试直连
curl https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation -I

# 查看 OpenClaw 日志
journalctl -u openclaw -n 50
```

### 7.3 PAC 文件不生效

```bash
# 验证 PAC 文件语法
curl http://localhost/proxy.pac

# 测试 PAC 规则
node -e "
var url = 'https://www.google.com';
eval(require('fs').readFileSync('/opt/proxy.pac', 'utf8'));
console.log(FindProxyForURL(url, url.split('/')[2]));
"
```

---

## 总结

**配置要点：**

1. ✅ Hostinger VPS 上安装 Tinyproxy（端口 8888）
2. ✅ 创建 PAC 文件定义代理规则
3. ✅ **OpenClaw 服务设置 `NO_PROXY=*` 确保直连**
4. ✅ 国内网站和大模型域名直连
5. ✅ 国外网站通过 Hostinger VPS 访问

**关键原则：**

- **OpenClaw 流量必须直连，不走代理**
- 使用国内大模型（阿里云百炼），不需要外网
- PAC 文件规则优先级：直连 > 代理
- 定期检查代理连接和服务状态

**文件位置：**

- PAC 文件：`/opt/proxy.pac` 或 `/var/www/html/proxy.pac`
- Tinyproxy 配置：`/etc/tinyproxy/tinyproxy.conf`
- OpenClaw 服务：`/etc/systemd/system/openclaw.service`
- 环境变量：`/etc/environment`
