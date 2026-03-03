# GitHub备份系统全局配置

> 此文件定义了VPS和本地OpenClaw备份系统的完整配置规则
> 更新日期：2026-03-03

---

## 📊 配置总览

| 项目 | GitHub仓库 | 本地路径 | 备份脚本 | 自动任务 |
|------|-----------|---------|---------|---------|
| VPS | git@github.com:169068671/vps-backup.git | /vps-backup | /root/vps-backup-v4.sh | 每天03:00 |
| OpenClaw | git@github.com:169068671/openclaw-backup.git | /home/admin/openclaw/workspace | /home/admin/openclaw/backup-all.sh | 每天03:00 |

---

## 🖥️ VPS备份配置

### 仓库信息
```
仓库地址：git@github.com:169068671/vps-backup.git
网页地址：https://github.com/169068671/vps-backup
SSH密钥：/root/.ssh/id_ed25519
Git用户：王华军 <169068671@qq.com>
```

### 本地仓库配置
```bash
cd /vps-backup
git remote -v
# origin	git@github.com:169068671/vps-backup.git (fetch)
# origin	git@github.com:169068671/vps-backup.git (push)
```

### 备份脚本
```bash
#!/bin/bash
# 文件位置：/root/vps-backup-v4.sh
# 备份内容：系统配置、Docker配置、OpenClaw配置、Whisper配置等
# 排除内容：SSH私钥、VNC密码、npm缓存、node_modules、会话历史
```

### 自动备份
```bash
# Cron任务配置
0 3 * * * /root/vps-backup-v4.sh >> /var/log/vps-backup.log 2>&1
```

### 手动备份
```bash
# 执行备份
bash /root/vps-backup-v4.sh

# 查看日志
tail -f /var/log/vps-backup.log
```

### 恢复备份
```bash
# 克隆仓库
git clone git@github.com:169068671/vps-backup.git /vps-backup

# 恢复配置
cp /vps-backup/root-config/openclaw.json ~/.openclaw/
cp /vps-backup/root-config/guacamole-docker-compose.yml /root/

# 恢复SSH公钥
cp /vps-backup/root-config/.ssh/authorized_keys ~/.ssh/
```

---

## 💻 本地OpenClaw备份配置

### 仓库信息
```
仓库地址：git@github.com:169068671/openclaw-backup.git
网页地址：https://github.com/169068671/openclaw-backup
SSH密钥：/home/admin/.ssh/id_ed25519
Git用户：王华军 <169068671@qq.com>
```

### 本地仓库配置
```bash
cd /home/admin/openclaw/workspace
git remote -v
# origin	git@github.com:169068671/openclaw-backup.git (fetch)
# origin	git@github.com:169068671/openclaw-backup.git (push)
```

### 备份脚本
```bash
#!/bin/bash
# 文件位置：/home/admin/openclaw/backup-all.sh
# 备份内容：OpenClaw配置、扩展、技能、工作区所有文件
# 排除内容：sessions/、node_modules/、*.tar.gz、*.zip
```

### 自动备份
```bash
# Cron任务配置
0 3 * * * /home/admin/openclaw/backup-all.sh
```

### 手动备份
```bash
# 执行备份
bash /home/admin/openclaw/backup-all.sh

# 查看日志
tail -f /home/admin/openclaw/workspace/backup.log
```

### 恢复备份
```bash
# 克隆仓库
git clone git@github.com:169068671/openclaw-backup.git /tmp/restore

# 恢复配置
cp -r /tmp/restore/openclaw-config/* ~/.openclaw/

# 恢复工作区
cp -r /tmp/restore/workspace-backup/* ~/openclaw/workspace/
```

---

## 🔄 备份对比

### VPS备份特点
- ✅ 系统级配置（SSH、网络、系统信息）
- ✅ Docker容器配置（Guacamole、Whisper）
- ✅ 服务器管理脚本
- ✅ 排除敏感文件（私钥、密码）
- 📍 面向：服务器配置恢复

### OpenClaw备份特点
- ✅ 完整工作区文件
- ✅ OpenClaw配置和扩展
- ✅ 9个技能模块
- ✅ 所有项目文档
- 📍 面向：工作区数据恢复

---

## ⚠️ 重要规则

### 禁止更改
1. ❌ **VPS仓库地址**：必须是 `git@github.com:169068671/vps-backup.git`
2. ❌ **OpenClaw仓库地址**：必须是 `git@github.com:169068671/openclaw-backup.git`
3. ❌ **备份时间**：固定为每天03:00 GMT+8

### 必须排除
1. **VPS备份**：
   - SSH私钥 (`id_ed25519`, `id_rsa`)
   - VNC密码文件 (`.vnc/passwd`)
   - npm缓存 (`_cacache`)
   - node_modules
   - `.openclaw/sessions/`
   - 大文件 (>50MB)

2. **OpenClaw备份**：
   - `sessions/` (对话历史)
   - `node_modules/`
   - `*.tar.gz`
   - `*.zip`

---

## 🔧 故障处理

### 检查备份状态
```bash
# VPS
cd /vps-backup && git log -1

# 本地
cd /home/admin/openclaw/workspace && git log -1
```

### 重置仓库（紧急情况）
```bash
# VPS
rm -rf /vps-backup
mkdir -p /vps-backup
cd /vps-backup
git init
git config user.email "169068671@qq.com"
git config user.name "王华军"
git remote add origin git@github.com:169068671/vps-backup.git
git branch -M main

# 本地
cd /home/admin/openclaw/workspace
git remote set-url origin git@github.com:169068671/openclaw-backup.git
```

---

## 📝 维护日志

| 日期 | 操作 | 备注 |
|------|------|------|
| 2026-03-03 | 初始化VPS备份系统 | 推送61个文件 |
| 2026-03-03 | 初始化OpenClaw备份系统 | 推送48,381个文件 |
| 2026-03-03 | 配置自动备份任务 | VPS和本地都设置为03:00 |
| 2026-03-03 | 创建全局配置文档 | 本文件 |

---

## 📞 快速参考

### GitHub账户
- **用户名**：169068671
- **邮箱**：169068671@qq.com
- **密码**：(请使用SSH密钥，无需密码)

### VPS连接
- **IP**：76.13.219.143
- **用户**：root
- **SSH命令**：`sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143`

### 备份脚本路径
- **VPS**：`/root/vps-backup-v4.sh`
- **本地**：`/home/admin/openclaw/backup-all.sh`

---

**此配置为永久全局规则，除非经过确认，否则不得更改。**
