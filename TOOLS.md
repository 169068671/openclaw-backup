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
- **状态：** ✅ 已完成配置，代理正常运行

### 配置详情

1. **Hostinger VPS (76.13.219.143)**
   - Tinyproxy 已安装并运行
   - 监听端口：8888
   - systemd 服务已配置开机自启
   - 防火墙规则已添加

2. **阿里云本地**
   - PAC 文件已创建：`/opt/proxy.pac`
   - OpenClaw 进程确认走直连（未设置代理）
   - admin 用户和系统环境均未设置代理

3. **代理规则**
   - 国内网站/大模型域名 → DIRECT
   - OpenClaw 相关域名 → DIRECT
   - 其他所有请求 → PROXY 76.13.219.143:8888
