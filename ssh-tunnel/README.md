# SSH Tunnel Manager

SSH隧道管理工具，支持Google连通性测试。

## 快速开始

```bash
# 启动隧道（自动测试 Google）
./ssh-tunnel.sh start

# 查看状态
./ssh-tunnel.sh status

# 停止隧道
./ssh-tunnel.sh stop
```

## Google 连通性测试 ✅

脚本会自动测试Google连通性，并返回测试结果：

- ✅ **HTTP 200/301/302**: VPS可以访问Google
- ⚠️ **其他HTTP状态**: VPS可以连接Google，但返回异常
- ❌ **Connection timed out**: VPS无法访问Google（网络限制）

## 完整文档

详细使用方法请参考 [SKILL.md](SKILL.md)

## 配置

- **服务器**: 76.13.219.143 (srv1437164)
- **用户**: root
- **本地端口**: 1080 (SOCKS5)

## 版本

v1.2 (2026-03-13) - 添加Google连通性测试功能
