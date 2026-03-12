# GitHub 推送工作流

**创建日期：** 2026-03-13
**用途：** 标准 GitHub 推送工作流程

---

## 🚀 快速开始

### 一键推送

```bash
cd /home/admin/openclaw/workspace && git add . && git commit -m "your message" && git push origin master
```

---

## 📋 标准工作流

### 步骤1：查看状态

```bash
cd /home/admin/openclaw/workspace
git status
```

**输出示例：**
```
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)

        modified:   README.md
        new file:   test.sh
```

---

### 步骤2：添加文件

```bash
# 添加所有更改
git add .

# 或添加特定文件
git add README.md test.sh
```

---

### 步骤3：提交更改

```bash
# 提交并添加消息
git commit -m "你的提交消息"

# 或添加详细描述
git commit -m "feat: Add new feature

- Add new feature description
- Update documentation
- Fix bugs"
```

**提交消息格式：**

| 类型 | 用途 | 示例 |
|------|------|------|
| `feat:` | 新功能 | `feat: Add new feature` |
| `fix:` | 修复 bug | `fix: Fix login issue` |
| `docs:` | 文档更新 | `docs: Update README` |
| `style:` | 代码格式 | `style: Format code` |
| `refactor:` | 重构 | `refactor: Simplify code` |
| `test:` | 测试 | `test: Add unit tests` |
| `chore:` | 构建/工具 | `chore: Update dependencies` |

---

### 步骤4：推送到 GitHub

```bash
git push origin master
```

**输出示例：**
```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (3/3), 456 bytes | 456.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To github.com:169068671/openclaw-backup.git
   40fdf52..abc1234  master -> master
```

---

## 🔍 查看和检查

### 查看提交历史

```bash
# 查看最近的提交
git log --oneline -5

# 查看详细提交信息
git log -3

# 查看图形化历史
git log --oneline --graph --all
```

**输出示例：**
```
abc1234 feat: Add new feature
40fdf52 docs: Add 2026-03-13 work log
d014162 feat: Copy VPS SSH key to local for direct GitHub push
7efeac0 docs: Add Bash Command MCP configuration completion report
```

---

### 查看远程状态

```bash
# 查看远程仓库
git remote -v

# 查看远程分支
git branch -r

# 查看远程提交
git log origin/master --oneline -3
```

---

### 检查同步状态

```bash
# 获取远程更新
git fetch origin

# 查看本地和远程的差异
git status

# 查看待推送的提交
git log origin/master..master --oneline
```

---

## 🛠️ 常用命令

### 日常命令

| 命令 | 用途 | 示例 |
|------|------|------|
| `git status` | 查看状态 | `git status` |
| `git add .` | 添加所有更改 | `git add .` |
| `git commit -m "msg"` | 提交 | `git commit -m "update"` |
| `git push` | 推送 | `git push origin master` |
| `git pull` | 拉取 | `git pull origin master` |
| `git log --oneline` | 查看历史 | `git log --oneline -5` |

### 高级命令

| 命令 | 用途 | 示例 |
|------|------|------|
| `git fetch` | 获取远程更新 | `git fetch origin` |
| `git diff` | 查看差异 | `git diff HEAD` |
| `git reset` | 重置提交 | `git reset HEAD~1` |
| `git rebase` | 变基 | `git rebase master` |
| `git stash` | 暂存更改 | `git stash` |

---

## 🔧 配置信息

### 当前配置

```bash
# 查看配置
git config --list

# 查看远程仓库
git remote -v

# 查看当前分支
git branch -a
```

**当前配置：**
```
origin  git@github.com:169068671/openclaw-backup.git (fetch)
origin  git@github.com:169068671/openclaw-backup.git (push)
```

### SSH 密钥

```bash
# SSH 密钥位置
~/.ssh/id_ed25519_github

# 测试 GitHub 连接
ssh -i ~/.ssh/id_ed25519_github -T git@github.com

# 预期输出
Hi 169068671! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## ⚠️ 常见问题

### 问题1：推送被拒绝

**错误信息：**
```
! [rejected] master -> master (fetch first)
error: failed to push some refs to 'github.com:169068671/openclaw-backup.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
```

**解决方法：**
```bash
# 先拉取远程更新
git pull origin master --rebase

# 或强制推送（谨慎使用）
git push origin master --force
```

---

### 问题2：认证失败

**错误信息：**
```
Permission denied (publickey)
fatal: Could not read from remote repository.
```

**解决方法：**
```bash
# 检查 SSH 密钥权限
ls -la ~/.ssh/id_ed25519_github
# 应该是：-rw------- (600)

# 设置正确权限
chmod 600 ~/.ssh/id_ed25519_github

# 测试连接
ssh -i ~/.ssh/id_ed25519_github -T git@github.com
```

---

### 问题3：连接超时

**错误信息：**
```
ssh: connect to host github.com port 22: Connection timed out
```

**解决方法：**
```bash
# 检查网络连接
ping github.com

# 或使用 HTTPS 方式
git remote set-url origin https://github.com/169068671/openclaw-backup.git
```

---

### 问题4：提交错误

**错误信息：**
```
error: nothing to commit, working tree clean
```

**解决方法：**
```bash
# 先查看状态
git status

# 如果有更改但未检测到
git add .
git status
```

---

## 📊 工作流对比

### 配置前（VPS 中转）

```
1. 提交到本地 Git
   git add . && git commit -m "message"

2. 复制 .git 目录到 VPS
   sshpass -p 'password' scp -r .git root@vps:/path/

3. 在 VPS 上设置远程仓库
   ssh root@vps 'cd /path && git remote set-url origin git@github.com:user/repo.git'

4. 在 VPS 上推送
   ssh root@vps 'cd /path && git push origin master'

→ 复杂、慢、易出错
```

### 配置后（本地直接推送）

```
1. 提交到本地 Git
   git add . && git commit -m "message"

2. 直接推送
   git push origin master

→ 简单、快、可靠
```

---

## 🎯 最佳实践

### 提交消息规范

**好的提交消息：**
```
feat: Add user authentication

- Add login form
- Add JWT token validation
- Update documentation
```

**不好的提交消息：**
```
update
fix bug
done
```

---

### 工作流建议

1. **频繁提交**
   - 小步快跑，频繁提交
   - 不要积累太多更改

2. **清晰的提交消息**
   - 使用规范的格式
   - 描述做了什么和为什么

3. **先拉后推**
   - 推送前先拉取远程更新
   - 避免冲突

4. **查看状态**
   - 提交前查看状态
   - 确认要推送的内容

---

## 🚀 自动化脚本

### 一键推送脚本

```bash
#!/bin/bash
# one-push.sh - 一键推送脚本

cd /home/admin/openclaw/workspace

# 检查是否有更改
if [ -z "$(git status --porcelain)" ]; then
    echo "没有需要提交的更改"
    exit 0
fi

# 提示输入提交消息
read -p "输入提交消息: " message

# 添加、提交、推送
git add .
git commit -m "$message"
git push origin master

echo "✅ 推送完成！"
```

### 使用方法

```bash
chmod +x one-push.sh
./one-push.sh
```

---

## 📚 相关文档

- **Git 官方文档：** https://git-scm.com/doc
- **GitHub 文档：** https://docs.github.com/
- **本工作区：** /home/admin/openclaw/workspace
- **远程仓库：** https://github.com/169068671/openclaw-backup

---

## ✅ 快速参考

### 常用命令清单

```bash
# 查看状态
git status

# 添加文件
git add .

# 提交
git commit -m "message"

# 推送
git push origin master

# 拉取
git pull origin master

# 查看历史
git log --oneline -5

# 查看差异
git diff HEAD
```

---

## 🎉 总结

### 标准工作流

1. 查看状态：`git status`
2. 添加文件：`git add .`
3. 提交更改：`git commit -m "message"`
4. 推送到 GitHub：`git push origin master`

### 配置信息

- **本地密钥：** ~/.ssh/id_ed25519_github
- **远程仓库：** git@github.com:169068671/openclaw-backup.git
- **工作区：** /home/admin/openclaw/workspace
- **推送方式：** 直接推送（SSH 密钥）

---

**🎉 工作流完成！现在可以轻松推送到 GitHub！**

---

**创建日期：** 2026-03-13
**更新日期：** 2026-03-13
**文档类型：** 工作流指南
