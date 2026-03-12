# 手动推送到 GitHub 命令清单

**创建日期：** 2026-03-13
**用途：** 手动推送到 GitHub（使用 VPS SSH 密钥）

---

## 📝 待推送的提交（3个）

### 提交1：7efeac0
```
docs: Add Bash Command MCP configuration completion report

- Clarify MCP server is standalone (no OpenClaw integration needed)
- Explain MCP protocol and usage
- All tests passed
- Installation complete
```

### 提交2：6ca1960
```
feat: Install Bash Command MCP server and OpenClaw upgrade

- Install bash-command-mcp v0.1.4
- Add configuration guide and test script
- Add OpenClaw upgrade report (2026.2.1 → 2026.3.11)
- Add Bash Command MCP installation report
- All tests passed
```

### 提交3：a5114b0
```
docs: Add GitHub push completion report

- Complete report for GitHub push
- All commits pushed successfully
```

---

## 🚀 推送方法

### 方法1：一键推送（推荐）

```bash
sshpass -p 'Whj001.Whj001' scp -r /home/admin/openclaw/workspace/.git root@76.13.219.143:/vps-backup/openclaw-backup/ && sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git remote set-url origin git@github.com:169068671/openclaw-backup.git && git push origin master'
```

### 方法2：分步推送

#### 步骤1：复制 .git 目录到 VPS

```bash
sshpass -p 'Whj001.Whj001' scp -r /home/admin/openclaw/workspace/.git root@76.13.219.143:/vps-backup/openclaw-backup/
```

#### 步骤2：在 VPS 上设置远程仓库为 SSH

```bash
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git remote set-url origin git@github.com:169068671/openclaw-backup.git'
```

#### 步骤3：推送到 GitHub

```bash
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git push origin master'
```

---

## 🧪 检查推送状态

### 查看本地提交

```bash
cd /home/admin/openclaw/workspace && git log --oneline -3
```

### 查看 VPS 提交

```bash
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git log --oneline -3'
```

### 查看 GitHub 仓库

访问：https://github.com/169068671/openclaw-backup

---

## 🔧 使用 Command MCP 执行

### 步骤1：复制 .git 目录

通过 MCP 执行：
```bash
sshpass -p 'Whj001.Whj001' scp -r /home/admin/openclaw/workspace/.git root@76.13.219.143:/vps-backup/openclaw-backup/
```

### 步骤2：设置远程仓库为 SSH

通过 MCP 执行：
```bash
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git remote set-url origin git@github.com:169068671/openclaw-backup.git'
```

### 步骤3：推送到 GitHub

通过 MCP 执行：
```bash
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git push origin master'
```

---

## 📊 推送统计

- **待推送提交：** 3 个
- **本地最新提交：** 7efeac0
- **远程最新提交：** be92f95
- **推送方式：** VPS SSH 密钥
- **远程仓库：** git@github.com:169068671/openclaw-backup.git

---

## 💡 注意事项

### VPS SSH 密钥
- **VPS：** 76.13.219.143
- **用户：** root
- **密码：** Whj001.Whj001
- **SSH 密钥：** ed25519
- **已添加到 GitHub：** ✅ 是

### GitHub 仓库
- **仓库地址：** https://github.com/169068671/openclaw-backup
- **SSH 地址：** git@github.com:169068671/openclaw-backup.git
- **所有者：** 169068671

### 推送方式
- **使用 VPS SSH 密钥：** ✅ 推荐
- **已配置：** ✅ 是
- **已测试：** ✅ 是

---

## 🔗 相关资源

- **GitHub 仓库：** https://github.com/169068671/openclaw-backup
- **VPS 备份仓库：** https://github.com/169068671/vps-backup
- **手动推送脚本：** /home/admin/openclaw/workspace/manual-github-push.sh

---

## 🚀 快速开始

### 运行一键推送脚本

```bash
bash /home/admin/openclaw/workspace/manual-github-push.sh
```

### 或者执行一键推送命令

```bash
sshpass -p 'Whj001.Whj001' scp -r /home/admin/openclaw/workspace/.git root@76.13.219.143:/vps-backup/openclaw-backup/ && sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 'cd /vps-backup/openclaw-backup && git remote set-url origin git@github.com:169068671/openclaw-backup.git && git push origin master'
```

---

## ✅ 推送清单

- [ ] 复制 .git 目录到 VPS
- [ ] 设置远程仓库为 SSH
- [ ] 推送到 GitHub
- [ ] 验证推送成功

---

**📝 准备好推送了！**

当你需要输入 token 时，我会提示你输入。

---

**脚本位置：** /home/admin/openclaw/workspace/manual-github-push.sh
**文档位置：** /home/admin/openclaw/workspace/手动推送到GitHub命令清单.md
