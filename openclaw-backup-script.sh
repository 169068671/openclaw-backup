#!/bin/bash

# OpenClaw 工作区自动备份脚本
# 备份到 GitHub: https://github.com/169068671/openclaw-backup

WORKSPACE_DIR="/home/admin/openclaw/workspace"
DATE=$(date +%Y-%m-%d_%H-%M-%S)
LOG_FILE="$WORKSPACE_DIR/backup.log"

echo "[$DATE] Starting OpenClaw workspace backup..." >> $LOG_FILE

# 进入工作目录
cd $WORKSPACE_DIR || exit 1

# 添加所有更改
git add .

# 检查是否有变化
if git diff --cached --quiet; then
    echo "[$DATE] No changes to backup." >> $LOG_FILE
    exit 0
fi

# 提交更改
git commit -m "Auto backup - $DATE"

# 推送到 GitHub
git push origin main

echo "[$DATE] Backup completed successfully." >> $LOG_FILE
