# OpenClaw 完整备份说明

## 📋 备份配置

**备份脚本：** `/home/admin/openclaw/backup-all.sh`
**GitHub 仓库：** https://github.com/169068671/openclaw-backup
**自动备份时间：** 每天 03:00 GMT+8

---

## 📦 备份内容

### 1. OpenClaw 配置 (`openclaw-config/`)
- ✅ `openclaw.json` - 主配置文件
- ✅ `exec-approvals.json` - 执行批准配置
- ✅ `update-check.json` - 更新检查
- ✅ `identity/` - 设备身份信息
- ✅ `cron/` - Cron 任务配置

### 2. 扩展插件 (`openclaw-config/extensions/`)
- ✅ `dingtalk-connector/` - 钉钉连接器
- ✅ `feishu/` - 飞书集成
- ✅ `qqbot/` - QQ 机器人
- ⚠️ 已排除 `node_modules` 和大型文件

### 3. 技能 (`openclaw-config/skills/`)
- ✅ `amap-traffic/` - 高德地图交通
- ✅ `hn/` - Hacker News
- ✅ `otaku-reco/` - 二次元推荐
- ✅ `otaku-wiki/` - 番剧百科
- ✅ `pptx-creator/` - PPT 生成器
- ✅ `qwen-image/` - Qwen 图像生成
- ✅ `stock-watcher/` - 股票监控
- ✅ `url-digest/` - URL 摘要

### 4. 代理配置 (`openclaw-config/agents/`)
- ✅ `models.json` - 模型配置
- ⚠️ 已排除 `sessions/`（包含敏感信息）

### 5. 工作区 (`workspace-backup/`)
- ✅ 所有 Markdown 文档
- ✅ Shell 脚本
- ✅ Docker Compose 配置
- ✅ 记忆文件 (`memory/`)
- ✅ 备份脚本

---

## 🚀 手动备份

```bash
/home/admin/openclaw/backup-all.sh
```

---

## 📥 恢复备份

### 1. 克隆仓库
```bash
git clone git@github.com:169068671/openclaw-backup.git /tmp/openclaw-restore
```

### 2. 恢复配置文件
```bash
# 恢复 OpenClaw 配置
cp /tmp/openclaw-restore/openclaw-config/* ~/.openclaw/

# 恢复扩展
cp -r /tmp/openclaw-restore/openclaw-config/extensions/* ~/.openclaw/extensions/

# 恢复技能
cp -r /tmp/openclaw-restore/openclaw-config/skills/* ~/.openclaw/skills/

# 恢复代理配置
cp -r /tmp/openclaw-restore/openclaw-config/agents/* ~/.openclaw/agents/

# 恢复 Cron 任务
cp -r /tmp/openclaw-restore/openclaw-config/cron/* ~/.openclaw/cron/
```

### 3. 恢复工作区
```bash
cp -r /tmp/openclaw-restore/workspace-backup/* ~/openclaw/workspace/
```

### 4. 重启 OpenClaw
```bash
# 重启 OpenClaw gateway
openclaw gateway restart
```

---

## 📊 查看备份历史

### Git 日志
```bash
cd ~/openclaw/workspace
git log --oneline
```

### 备份日志
```bash
cat ~/openclaw/workspace/backup.log
```

### GitHub 仓库
访问：https://github.com/169068671/openclaw-backup/commits/main

---

## ⚠️ 注意事项

### 已排除的内容（安全考虑）
1. **会话文件** (`sessions/`) - 包含敏感对话历史
2. **Node modules** (`node_modules/`) - 可通过 npm 重新安装
3. **大型文件** (`*.tar.gz`, `*.zip`) - 节省空间

### 需要手动备份的内容
1. **OpenClaw Media** (`~/.openclaw/media/`) - 截图和媒体文件
2. **浏览器数据** (`~/.openclaw/browser/`) - 浏览器配置
3. **设备授权** (`~/.openclaw/devices/`) - 配对设备信息

---

## 🔄 自动备份管理

### 查看当前 Cron 任务
```bash
crontab -l
```

### 编辑 Cron 任务
```bash
crontab -e
```

### 暂停自动备份
```bash
crontab -l | grep -v backup-all.sh | crontab -
```

### 恢复自动备份
```bash
(crontab -l 2>/dev/null; echo "0 3 * * * /home/admin/openclaw/backup-all.sh") | crontab -
```

---

## 💡 建议

### 1. 定期检查备份
每月检查一次 GitHub 仓库，确保备份成功。

### 2. 测试恢复流程
定期（每季度）在测试环境中恢复备份，验证数据完整性。

### 3. 私有仓库
如果包含敏感信息，建议将 GitHub 仓库设置为 Private：
- 访问：https://github.com/169068671/openclaw-backup/settings
- General → Danger Zone → Change visibility

### 4. 备份 Media 目录
定期手动备份媒体文件：
```bash
# 压缩并备份
tar czf ~/openclaw-media-backup-$(date +%Y%m%d).tar.gz ~/.openclaw/media/
```

---

## 📞 快速命令参考

**手动备份：**
```bash
/home/admin/openclaw/backup-all.sh
```

**查看备份状态：**
```bash
cd ~/openclaw/workspace && git status
```

**推送到 GitHub：**
```bash
cd ~/openclaw/workspace && git push origin main
```

**查看最近的提交：**
```bash
cd ~/openclaw/workspace && git log --oneline -5
```

---

**最后更新：** 2026-03-03 10:53 GMT+8
**备份状态：** ✅ 已推送到 GitHub
