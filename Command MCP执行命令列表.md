# Command MCP 执行命令列表

**用于通过 bash-command-mcp 执行 GitHub 推送**

---

## 🚀 推送命令（通过 Command MCP）

### 命令1：复制 .git 目录到 VPS

```bash
sshpass -p 'Whj001.Whj001' scp -r /home/admin/openclaw/workspace/.git root@76.13.219.143:/vps-backup/openclaw-backup/
```

**说明：** 将本地的 .git 目录复制到 VPS 上的备份目录

---

### 命令2：设置远程仓库为 SSH

```bash
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git remote set-url origin git@github.com:169068671/openclaw-backup.git'
```

**说明：** 在 VPS 上将远程仓库从 HTTPS 切换到 SSH（使用 SSH 密钥）

---

### 命令3：推送到 GitHub

```bash
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git push origin master'
```

**说明：** 在 VPS 上推送到 GitHub（使用 SSH 密钥，无需 token）

---

## 🧪 检查命令（通过 Command MCP）

### 命令4：检查本地提交

```bash
cd /home/admin/openclaw/workspace && git log --oneline -3
```

**说明：** 查看本地最近的 3 个提交

---

### 命令5：检查 VPS 提交

```bash
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git log --oneline -3'
```

**说明：** 查看 VPS 上最近的 3 个提交

---

### 命令6：检查远程仓库配置

```bash
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git remote -v'
```

**说明：** 查看 VPS 上 Git 远程仓库的配置

---

## 📝 执行顺序

1. ✅ **执行命令1**：复制 .git 目录到 VPS
2. ✅ **执行命令2**：设置远程仓库为 SSH
3. ✅ **执行命令3**：推送到 GitHub
4. ✅ **执行命令5**：检查 VPS 提交（验证推送成功）

---

## 💡 关于 Token

### 不需要 Token！

**原因：**
- ✅ 使用 VPS 的 SSH 密钥
- ✅ SSH 密钥已添加到 GitHub
- ✅ 认证自动完成，无需输入 token

### 如果需要 Token

如果出现错误提示需要 token，执行：

```bash
# 在 VPS 上配置 HTTPS 认证
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git remote set-url origin https://github.com:169068671/openclaw-backup.git'

# 推送时会提示输入 token
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git push origin master'
```

**但推荐使用 SSH，无需 token！**

---

## 🔍 常见错误

### 错误1：fatal: could not read Username

**原因：** 远程仓库配置为 HTTPS，但没有提供认证

**解决：** 使用 SSH 方式（执行命令2）

```bash
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git remote set-url origin git@github.com:169068671/openclaw-backup.git'
```

### 错误2：Permission denied

**原因：** SSH 密钥权限问题

**解决：** 检查 SSH 密钥权限

```bash
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'ls -la ~/.ssh/'
```

### 错误3：Connection refused

**原因：** 网络连接问题

**解决：** 检查网络连接

```bash
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'ping -c 3 github.com'
```

---

## 🎯 快速开始

### 方法1：一键推送（推荐）

```bash
sshpass -p 'Whj001.Whj001' scp -r /home/admin/openclaw/workspace/.git root@76.13.219.143:/vps-backup/openclaw-backup/ && sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git remote set-url origin git@github.com:169068671/openclaw-backup.git && git push origin master'
```

### 方法2：分步执行

1. 执行命令1：复制 .git 目录
2. 执行命令2：设置 SSH 远程仓库
3. 执行命令3：推送到 GitHub
4. 执行命令5：验证推送成功

---

## 📊 当前状态

### 本地提交（3个）
```
7efeac0 docs: Add Bash Command MCP configuration completion report
6ca1960 feat: Install Bash Command MCP server and OpenClaw upgrade
a5114b0 docs: Add GitHub push completion report
```

### VPS 提交（待更新）
```
be92f95 docs: Add GitHub MCP configuration example (no sensitive info)
f032e15 feat: Add GitHub MCP server installation and configuration
543afed docs: Add GitHub upload success report and update MEMORY.md
```

### 待推送
- ✅ 3 个新提交
- ✅ 已准备好推送
- ✅ 使用 SSH 密钥（无需 token）

---

## 🔗 相关资源

- **GitHub 仓库：** https://github.com/169068671/openclaw-backup
- **命令清单：** /home/admin/openclaw/workspace/手动推送到GitHub命令清单.md
- **手动推送脚本：** /home/admin/openclaw/workspace/manual-github-push.sh
- **Command MCP 配置：** /home/admin/openclaw/workspace/Bash Command MCP配置指南.md

---

## ✅ 执行清单

- [ ] 执行命令1：复制 .git 目录
- [ ] 执行命令2：设置 SSH 远程仓库
- [ ] 执行命令3：推送到 GitHub
- [ ] 执行命令5：验证推送成功

---

**🚀 准备好通过 Command MCP 执行了！**

使用 SSH 密钥，无需 token！

---

**文档位置：** /home/admin/openclaw/workspace/Command MCP执行命令列表.md
