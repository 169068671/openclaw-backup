# GitHub Pusher Skill

**自动化 GitHub 推送到 openclaw-backup 仓库**

---

## 🚀 快速开始

### 基本使用

```bash
# 推送所有更改（使用默认消息）
~/.openclaw/skills/github-pusher/push.sh

# 推送所有更改（使用自定义消息）
~/.openclaw/skills/github-pusher/push.sh "feat: Add new feature"

# 仅提交，不推送
~/.openclaw/skills/github-pusher/commit.sh "docs: Update README"

# 查看状态
~/.openclaw/skills/github-pusher/status.sh

# 测试连接
~/.openclaw/skills/github-pusher/test.sh
```

---

## 📋 脚本说明

### push.sh - 完整推送流程

**功能：** 添加、提交并推送所有更改

**用法：**
```bash
~/.openclaw/skills/github-pusher/push.sh [message]
```

**参数：**
- `message` - 可选，提交消息

**示例：**
```bash
# 使用默认消息
~/.openclaw/skills/github-pusher/push.sh

# 使用自定义消息
~/.openclaw/skills/github-pusher/push.sh "feat: Add new feature"

# 使用详细消息
~/.openclaw/skills/github-pusher/push.sh "feat: Add user authentication

- Add login form
- Add JWT token validation
- Update documentation"
```

---

### commit.sh - 仅提交

**功能：** 添加文件并提交，不推送

**用法：**
```bash
~/.openclaw/skills/github-pusher/commit.sh [message]
```

**参数：**
- `message` - 可选，提交消息

**示例：**
```bash
~/.openclaw/skills/github-pusher/commit.sh "WIP: work in progress"
```

---

### status.sh - 查看状态

**功能：** 查看 Git 状态和远程同步情况

**用法：**
```bash
~/.openclaw/skills/github-pusher/status.sh
```

**输出：**
- Git 状态
- 提交历史（本地和远程）
- 同步状态
- 远程仓库信息

---

### test.sh - 测试连接

**功能：** 测试 Git 和 GitHub 连接

**用法：**
```bash
~/.openclaw/skills/github-pusher/test.sh
```

**测试内容：**
- 工作区检查
- Git 仓库检查
- Git 配置检查
- SSH 密钥检查
- GitHub 连接测试
- 远程仓库检查
- Git 命令检查
- 工作区权限检查

---

## 💡 使用示例

### 示例1：日常备份

```bash
# 每天工作结束后备份
~/.openclaw/skills/github-pusher/push.sh "daily backup $(date +%Y-%m-%d)"
```

### 示例2：快速推送

```bash
# 快速提交并推送
~/.openclaw/skills/github-pusher/push.sh "quick update"
```

### 示例3：批量提交

```bash
# 先提交，后推送
~/.openclaw/skills/github-pusher/commit.sh "WIP: work in progress"
# ...继续工作...
~/.openclaw/skills/github-pusher/push.sh "finish: complete feature"
```

---

## 🔧 配置

### 工作区

默认工作区：`/home/admin/openclaw/workspace`

如需修改，编辑脚本：
```bash
WORKSPACE="/your/workspace/path"
```

### Git 用户

确保 Git 用户已配置：
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### SSH 密钥

确保 SSH 密钥已配置：
```bash
ls -la ~/.ssh/id_ed25519_github
```

---

## 🧪 测试

### 运行测试

```bash
# 测试连接
~/.openclaw/skills/github-pusher/test.sh

# 查看状态
~/.openclaw/skills/github-pusher/status.sh
```

### 预期输出

**test.sh：**
```
=== GitHub Pusher 连接测试 ===

=== 测试1：工作区检查 ===
✅ 工作区存在：/home/admin/openclaw/workspace

=== 测试2：Git 仓库检查 ===
✅ Git 仓库有效

...

=== 测试总结 ===
ℹ️  总测试数：8
ℹ️  通过测试：8
✅ 🎉 所有测试通过！
```

**status.sh：**
```
=== Git 状态 ===
M README.md
A test.sh

=== 提交历史 ===
ℹ️  本地提交（最近 5 个）：
abc1234 feat: Add new feature
def5678 docs: Update README

...

=== 同步状态 ===
ℹ️  本地提交：10 个
ℹ️  远程提交：10 个
✅ 完全同步：没有待推送的提交
```

---

## ⚠️ 常见问题

### 问题1：推送被拒绝

**错误：**
```
! [rejected] master -> master (fetch first)
```

**解决：**
```bash
cd /home/admin/openclaw/workspace
git pull origin master --rebase
```

### 问题2：认证失败

**错误：**
```
Permission denied (publickey)
```

**解决：**
```bash
chmod 600 ~/.ssh/id_ed25519_github
~/.openclaw/skills/github-pusher/test.sh
```

### 问题3：无更改

**提示：**
```
ℹ️  没有需要提交的更改
```

**说明：** 这不是错误，说明工作区是干净的。

---

## 📚 文档

- **技能文档：** `SKILL.md` - 详细技能文档
- **使用说明：** `README.md` - 本文件

---

## 🔗 相关资源

- **GitHub 仓库：** https://github.com/169068671/openclaw-backup
- **Git 文档：** https://git-scm.com/doc
- **GitHub 文档：** https://docs.github.com/

---

## ✅ 功能清单

- [x] 自动添加文件
- [x] 自动提交
- [x] 自动推送
- [x] 状态检查
- [x] 连接测试
- [x] 错误处理
- [x] 自定义提交消息
- [x] 详细文档

---

## 🎯 最佳实践

### 提交消息

**好的提交消息：**
```
feat: Add user authentication

- Add login form
- Add JWT token validation
- Update user documentation
```

**不好的提交消息：**
```
update
fix bug
done
```

### 工作流

1. **频繁提交**
   - 小步快跑，频繁提交
   - 不要积累太多更改

2. **清晰的提交消息**
   - 描述做了什么和为什么
   - 遵循提交消息规范

3. **推送前检查**
   - 查看状态
   - 确认要推送的内容

---

## 🎉 开始使用

```bash
# 测试连接
~/.openclaw/skills/github-pusher/test.sh

# 查看状态
~/.openclaw/skills/github-pusher/status.sh

# 推送更改
~/.openclaw/skills/github-pusher/push.sh "your message"
```

---

**技能位置：** ~/.openclaw/skills/github-pusher
**文档更新：** 2026-03-13
