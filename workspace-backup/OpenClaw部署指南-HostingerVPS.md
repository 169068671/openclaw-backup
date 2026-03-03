# OpenClaw 部署指南 - Hostinger VPS

## 什么是 OpenClaw？

OpenClaw（原 Clawdbot/Moltbot）是一款实用的个人 AI 助理，能够 24 小时响应指令并执行任务，如处理文件、查询信息、自动化协同等。本指南将指导你在 Hostinger VPS 上部署 OpenClaw，打造专属 AI 助理。

---

## 一、部署前的核心准备

### 1.1 服务器要求

- **服务器配置：** Hostinger VPS，内存必须 ≥2GB，推荐 2核2GB 及以上配置，确保服务稳定运行
- **操作系统：** 推荐 Ubuntu 22.04 LTS 或 Debian 12
- **地域选择：** Hostinger 提供多个地域的数据中心（美国、欧洲、亚洲等），根据你的使用场景选择合适的地域

### 1.2 必备凭证

需提前准备大模型 API-Key，用于调用模型服务，保障 AI 助理的智能交互能力。

**可选的模型服务：**
- 阿里云百炼
- 通义千问
- Kimi
- MiniMax
- 其他兼容 OpenAI API 格式的模型服务

---

## 二、在 Hostinger VPS 上部署 OpenClaw

### 2.1 第一步：登录你的 Hostinger VPS

使用 SSH 登录到你的 VPS：

```bash
ssh root@76.13.219.143
# 输入密码登录
```

### 2.2 第二步：安装 Node.js 和依赖

OpenClaw 要求 Node.js 版本 ≥22，首先安装必要的依赖和 Node.js：

```bash
# 更新系统包
apt update && apt upgrade -y

# 安装必要工具
apt install -y curl git build-essential python3

# 安装 Node.js 22.x
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs

# 验证 Node.js 版本
node -v
```

### 2.3 第三步：安装 OpenClaw

```bash
# 全局安装 OpenClaw
npm install -g openclaw

# 验证安装
openclaw --version
```

### 2.4 第四步：初始化 OpenClaw

```bash
# 创建工作目录
mkdir -p /opt/openclaw
cd /opt/openclaw

# 初始化 OpenClaw
openclaw init

# 编辑配置文件
nano /opt/openclaw/config/gateway.yaml
```

### 2.5 第五步：配置 API-Key

在配置文件中添加你的大模型 API-Key：

```yaml
# gateway.yaml 示例配置
models:
  - id: "qwen"
    provider: "dashscope"
    apiKey: "你的阿里云百炼API-Key"

# 或者使用其他模型
# models:
#   - id: "kimi"
#     provider: "openai-compatible"
#     baseURL: "https://api.moonshot.cn/v1"
#     apiKey: "你的Kimi API-Key"
```

### 2.6 第六步：配置防火墙

OpenClaw 默认通过 18789 端口通信，需要开放该端口：

```bash
# 允许 18789 端口
ufw allow 18789/tcp

# 如果需要 Web 界面（可选），也开放 80/443 端口
ufw allow 80/tcp
ufw allow 443/tcp

# 启用防火墙（如果还未启用）
ufw enable

# 查看防火墙状态
ufw status
```

### 2.7 第七步：启动 OpenClaw

```bash
# 创建 systemd 服务文件
cat > /etc/systemd/system/openclaw.service <<EOF
[Unit]
Description=OpenClaw Gateway Service
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/openclaw
Environment="NODE_ENV=production"
ExecStart=/usr/bin/node /usr/lib/node_modules/openclaw/dist/gateway.js
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# 重载 systemd 并启动服务
systemctl daemon-reload
systemctl enable openclaw
systemctl start openclaw

# 查看服务状态
systemctl status openclaw
```

### 2.8 第八步：获取访问 Token

```bash
# 查看日志获取初始 Token
journalctl -u openclaw -f

# 或者在工作目录查看生成的 Token 文件
cat /opt/openclaw/.token
```

### 2.9 第九步：访问 OpenClaw

通过浏览器访问：
- **Web 界面：** `http://76.13.219.143:18789`
- 输入你的 Token 即可登录使用

---

## 三、进阶功能配置

### 3.1 多渠道交互集成

#### （1）Telegram 通道配置

- 在 [Telegram BotFather](https://t.me/botfather) 创建机器人，获取 Bot Token
- 在 OpenClaw 配置文件中添加 Telegram 通道配置：
```yaml
channels:
  - id: "telegram"
    type: "telegram"
    botToken: "你的BotToken"
```
- 在 Telegram 中发送 `/start` 给你的机器人即可开始对话

#### （2）钉钉通道配置

- 在钉钉开放平台创建企业内部应用，获取 App ID 与 App Secret
- 在 OpenClaw 配置面板中添加钉钉通道配置
- 在钉钉群中 @绑定的机器人发送指令，验证功能是否正常响应

#### （3）QQ 通道配置

- 在 QQ 开放平台创建机器人，获取相关凭证
- 在 OpenClaw 中配置 QQ 通道
- 在 QQ 频道或私聊窗口发送指令，测试机器人的互动效果

### 3.2 自动化任务编排

- **定时任务创建：** 发送自然语言指令如"每天晚上8点整理当天邮件并生成摘要"，OpenClaw 会自动创建定时任务
- **跨应用协同：** 结合云存储实现文件自动存储，或通过 Webhook 对接第三方服务

### 3.3 模型切换与功能扩展

- **调用第三方模型：** 在配置文件中添加多个模型配置，可实现模型自由切换
- **安装扩展技能：** 进入 OpenClaw Skills 目录，安装语音识别、数据同步、语音合成等扩展插件

---

## 四、常见问题与解决方案

### 4.1 部署失败：无法访问 Web 界面

**原因：** 防火墙未放行 18789 端口

**解决方案：**
```bash
# 检查防火墙状态
ufw status

# 开放端口
ufw allow 18789/tcp

# 重启 OpenClaw 服务
systemctl restart openclaw
```

### 4.2 模型调用失败：API-Key 配置后无响应

**原因：** API-Key 输入错误、账号无可用额度，或网络连接问题

**解决方案：**
- 核对 API-Key 是否正确
- 登录模型平台查看账号额度
- 测试 VPS 是否能正常访问模型 API：
```bash
curl -I https://dashscope.aliyuncs.com
```

### 4.3 服务启动失败：提示"依赖缺失"

**原因：** Node.js 版本过低（要求 ≥22），或缺少必要系统扩展

**解决方案：**
```bash
# 检查 Node.js 版本
node -v

# 如果版本低于 22，使用 nvm 升级
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install 22
nvm use 22

# 重新安装 OpenClaw
npm install -g openclaw
systemctl restart openclaw
```

### 4.4 端口冲突

**原因：** 18789 端口已被其他服务占用

**解决方案：**
```bash
# 查看端口占用
netstat -tlnp | grep 18789
# 或
lsof -i :18789

# 如果被占用，可以在配置文件中修改 OpenClaw 端口
nano /opt/openclaw/config/gateway.yaml
# 修改端口后重启服务
systemctl restart openclaw
```

---

## 五、管理命令速查

### 服务管理

```bash
# 启动服务
systemctl start openclaw

# 停止服务
systemctl stop openclaw

# 重启服务
systemctl restart openclaw

# 查看状态
systemctl status openclaw

# 查看日志
journalctl -u openclaw -f
```

### 配置管理

```bash
# 编辑配置
nano /opt/openclaw/config/gateway.yaml

# 应用配置更改
systemctl restart openclaw
```

### 版本更新

```bash
# 更新 OpenClaw
npm update -g openclaw

# 重启服务
systemctl restart openclaw
```

---

## 总结

通过本指南，你可以在 Hostinger VPS 上成功部署 OpenClaw，实现 24 小时不间断运行的 AI 助理服务。部署核心要点：

1. 确保 Node.js 版本 ≥22
2. 妥善保管 API-Key 与访问 Token
3. 正确配置防火墙端口
4. 使用 systemd 管理服务，确保开机自启

部署完成后，你可以通过多渠道集成、自动化任务编排、模型扩展等功能，适配更多使用场景。无论是个人日常事务处理，还是提升工作协同效率，OpenClaw 都能提供实用的智能辅助支持。

---

**提示：** 如需更详细的配置选项，请参考 [OpenClaw 官方文档](https://docs.openclaw.ai)
