# GitHub Pusher Skill

**技能名称：** github-pusher
**版本：** 1.0.0
**作者：** openclaw
**描述：** 自动化 GitHub 推送到 openclaw-backup 仓库

---

## 📦 技能概述

### 功能
- ✅ 自动添加文件到 Git
- ✅ 自动提交更改
- ✅ 推送到 GitHub
- ✅ 状态检查
- ✅ 错误处理

### 使用场景
- 日常代码备份
- 自动化工作流
- 定期推送更新
- 快速提交和推送

---

## 🚀 快速开始

### 安装

```bash
# 技能应该位于 ~/.openclaw/skills/github-pusher/
```

### 基本使用

```bash
# 推送所有更改
~/.openclaw/skills/github-pusher/push.sh

# 或使用自定义提交消息
~/.openclaw/skills/github-pusher/push.sh "your commit message"

# 只添加和提交，不推送
~/.openclaw/skills/github-pusher/commit.sh "your message"
```

---

## 📋 功能说明

### push.sh - 完整推送流程

**描述：** 添加、提交并推送所有更改

**用法：**
```bash
~/.openclaw/skills/github-pusher/push.sh [message]
```

**参数：**
- `message` - 可选，提交消息（默认：自动生成）

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

**描述：** 添加文件并提交，不推送

**用法：**
```bash
~/.openclaw/skills/github-pusher/commit.sh [message]
```

**参数：**
- `message` - 可选，提交消息（默认：自动生成）

**示例：**
```bash
# 使用默认消息
~/.openclaw/skills/github-pusher/commit.sh

# 使用自定义消息
~/.openclaw/skills/github-pusher/commit.sh "docs: Update README"
```

---

### status.sh - 查看状态

**描述：** 查看 Git 状态和远程同步情况

**用法：**
```bash
~/.openclaw/skills/github-pusher/status.sh
```

**输出：**
- 本地提交历史
- 远程提交历史
- 待推送的提交
- 当前分支

---

### test.sh - 测试连接

**描述：** 测试 Git 和 GitHub 连接

**用法：**
```bash
~/.openclaw/skills/github-pusher/test.sh
```

**测试内容：**
- Git 配置检查
- SSH 密钥检查
- GitHub 连接测试
- 远程仓库检查

---

## 🔧 配置

### 工作区配置

默认工作区：`/home/admin/openclaw/workspace`

如需修改，编辑 `push.sh` 和 `commit.sh`：
```bash
WORKSPACE="/your/workspace/path"
```

### Git 配置

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

## 📊 工作流程

### 推送流程

1. **检查状态** - 查看是否有待提交的更改
2. **添加文件** - 添加所有更改到暂存区
3. **创建提交** - 使用提交消息创建提交
4. **推送到 GitHub** - 推送到远程仓库
5. **验证成功** - 检查推送是否成功

### 错误处理

- **无更改：** 提示"没有需要提交的更改"
- **推送失败：** 显示错误信息并建议解决方法
- **网络错误：** 重试或检查网络连接
- **认证错误：** 检查 SSH 密钥配置

---

## 💡 使用示例

### 示例1：日常备份

```bash
# 每天工作结束后备份
~/.openclaw/skills/github-pusher/push.sh "daily backup $(date +%Y-%m-%d)"
```

### 示例2：快速提交

```bash
# 快速提交并推送
~/.openclaw/skills/github-pusher/push.sh "quick update"
```

### 示例3：详细提交

```bash
# 详细的提交消息
~/.openclaw/skills/github-pusher/push.sh "feat: Add user authentication

- Add login form
- Add JWT token validation
- Update user documentation

Fixes #123"
```

### 示例4：批量操作

```bash
# 先提交，后推送
~/.openclaw/skills/github-pusher/commit.sh "WIP: work in progress"
# ...继续工作...
~/.openclaw/skills/github-pusher/push.sh "finish: complete feature"
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
✅ Git 配置检查：通过
✅ SSH 密钥检查：通过
✅ GitHub 连接测试：通过
✅ 远程仓库检查：通过
🎉 所有测试通过！
```

**status.sh：**
```
=== Git 状态 ===
On branch master
Your branch is up to date with 'origin/master'.
nothing to commit, working tree clean

=== 远程同步 ===
本地提交：3 个
远程提交：3 个
待推送：0 个
✅ 完全同步
```

---

## ⚠️ 注意事项

### 安全建议

1. **提交消息规范**
   - 使用清晰的提交消息
   - 遵循提交消息规范
   - 避免敏感信息

2. **推送前检查**
   - 推送前查看状态
   - 确认要推送的内容
   - 避免推送敏感文件

3. **密钥安全**
   - 不要分享 SSH 密钥
   - 保持密钥权限为 600
   - 定期更换密钥

### 常见问题

1. **推送被拒绝**
   - 解决：先拉取远程更新
   - 命令：`git pull origin master --rebase`

2. **认证失败**
   - 解决：检查 SSH 密钥权限
   - 命令：`chmod 600 ~/.ssh/id_ed25519_github`

3. **连接超时**
   - 解决：检查网络连接
   - 命令：`ping github.com`

---

## 📚 文档和脚本

### 主要脚本

1. **push.sh** - 完整推送流程
2. **commit.sh** - 仅提交
3. **status.sh** - 查看状态
4. **test.sh** - 测试连接

### 文档

1. **SKILL.md** - 技能文档（本文件）
2. **README.md** - 使用说明

---

## 🔗 相关资源

- **GitHub 仓库：** https://github.com/169068671/openclaw-backup
- **Git 文档：** https://git-scm.com/doc
- **GitHub 文档：** https://docs.github.com/
- **OpenClaw 文档：** https://docs.openclaw.ai/

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

## 🎉 总结

**技能名称：** github-pusher
**版本：** 1.0.0
**用途：** 自动化 GitHub 推送到 openclaw-backup
**状态：** ✅ 已完成

**主要功能：**
- 🚀 一键推送
- 📊 状态检查
- 🧪 连接测试
- 💡 简单易用

**开始使用：**
```bash
~/.openclaw/skills/github-pusher/push.sh "your message"
```

---

**技能位置：** ~/.openclaw/skills/github-pusher
**文档更新：** 2026-03-13
