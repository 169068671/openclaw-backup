# TOOLS.md - Local Notes

## 备份信息

- **工作空间备份：** `/home/admin/backups/workspace-backup-20260302-132648.tar.gz` (49K)
- **Git 仓库：** `/home/admin/openclaw/workspace/.git` (初始提交: cfd8d95)
- **备份策略：** 重要操作前创建新备份，Git 保存历史版本

## VPS (Hostinger)

- **地址：** 76.13.219.143
- **主机名：** srv1437164
- **用户：** root
- **密码：** Whj001.Whj001
- **连接命令：** `sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143`
- **状态：** SSH 连接超时 (2026-03-02 13:40)

## HTTP 代理配置

- **代理服务器：** Hostinger VPS (76.13.219.143:8888)
- **代理类型：** Tinyproxy (HTTP 代理)
- **PAC 文件：** `/opt/proxy.pac`
- **OpenClaw 规则：** 必须直连（当前已确认走直连）
- **文档：** `HTTP代理配置方案-HostingerVPS.md`
- **故障排查1：** `HTTP代理故障排查-Google无法访问.md`
- **故障排查2：** `HTTP代理故障排查-Google无法访问-第二次.md`
- **状态：** ✅ 已完成配置，代理正常运行

### 配置详情

1. **Hostinger VPS (76.13.219.143)**
   - Tinyproxy 已安装并运行
   - 监听端口：8888
   - MaxClients: 100
   - Timeout: 600s
   - 防火墙：ufw inactive（允许所有流量）

2. **Tinyproxy 配置（最新）**
   - Port: 8888
   - Listen: 0.0.0.0
   - Allow: 0.0.0.0/0（允许所有客户端）
   - DisableViaHeader: Yes（隐藏代理头）
   - ConnectPort: 443, 80（支持 HTTPS/HTTP CONNECT）

3. **阿里云本地**
   - PAC 文件已创建：`/opt/proxy.pac`
   - OpenClaw 进程确认走直连（未设置代理）
   - admin 用户和系统环境均未设置代理

4. **代理规则**
   - 国内网站/大模型域名 → DIRECT
   - OpenClaw 相关域名 → DIRECT
   - 其他所有请求 → PROXY 76.13.219.143:8888

5. **测试结果（2026-03-02 14:20）**
   - Google 访问：✅ 成功（HTTPS）
   - 国内网站：✅ 直连
   - OpenClaw：✅ 直连

### 问题修复记录

**问题 1：** 2026-03-02 14:07，无法通过代理访问 www.google.com

**原因：** Tinyproxy 配置缺少 `Allow 0.0.0.0/0` 规则

**解决方案：**
```conf
Port 8888
Listen 0.0.0.0
Allow 0.0.0.0/0
LogLevel Info
MaxClients 100
DisableViaHeader Yes
Timeout 600
```

**问题 2：** 2026-03-02 14:18，HTTPS 网站无法访问

**原因：** Tinyproxy 配置缺少 `ConnectPort`，不支持 HTTPS CONNECT 方法

**解决方案：**
```conf
Port 8888
Listen 0.0.0.0
Allow 0.0.0.0/0
LogLevel Info
MaxClients 100
DisableViaHeader Yes
Timeout 600
ConnectPort 443  ← 新增
ConnectPort 80   ← 新增
```

**测试验证：**
```bash
curl -I -x http://76.13.219.143:8888 https://www.google.com
HTTP/2 200 ✅
```

## 钉钉通道配置

- **插件名称：** dingtalk-connector
- **版本：** 0.6.0
- **状态：** ✅ 已安装并加载
- **配置文件：** `~/.openclaw/openclaw.json`
- **文档：** `钉钉通道配置指南.md`
- **完成报告：** `钉钉通道配置完成报告.md`
- **状态：** ✅ 双向通信测试成功

### 配置详情

1. **钉钉应用信息**
   - Client ID (AppKey): dingyscopnptfxm4hg8q
   - Client Secret: 已配置
   - Gateway Token: 已配置
   - 消息接收模式: Stream 模式
   - 应用状态: ✅ 已发布

2. **必需权限**
   - Card.Streaming.Write ✅
   - Card.Instance.Write ✅
   - qyapi_robot_sendmsg ✅

3. **功能特性**
   - AI Card 流式响应 ✅
   - 会话持久化（30分钟超时）✅
   - 双向通信 ✅
   - 图片自动上传
   - 支持会话命令：/new, /reset, /clear, 新会话, 重新开始, 清空对话

4. **测试结果**
   - 接收消息（钉钉→OpenClaw）：✅ 测试成功 (2026-03-02 14:04)
   - 主动发送（OpenClaw→钉钉）：✅ 测试成功 (2026-03-02 14:07)
   - 测试用户ID：193200103629107416
