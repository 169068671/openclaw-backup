# GitHub 上传指南

**创建日期：** 2026-03-12
**状态：** ✅ 已提交，⚠️ 需要手动推送

---

## 📦 已提交的更改

### 提交信息
```
feat: Add Cookie Format Converter skill and YouTube/NotebookLM skills

- Create cookie-converter skill for bidirectional cookie format conversion
  - Support Netscape, Playwright, and JSON formats
  - 6 conversion types: netscape-to-playwright, playwright-to-netscape, etc.
  - Global CLI tool installed at ~/.local/bin/cookie-converter

- Restore YouTube skills from backup
  - youtube-auth-exporter: Export YouTube authentication from Chrome
  - yt-dlp-downloader: Comprehensive video downloader
  - Browser cookies exporter: Extract cookies from Chrome/Firefox/Brave/Edge

- Restore NotebookLM skills from backup
  - notebooklm: Google NotebookLM unofficial Python API
  - notebooklm-youtube-importer: Batch import YouTube playlists
  - notebooklm-auth-exporter: Export NotebookLM authentication

- Create comprehensive documentation
  - YouTube 技能使用指南.md
  - YouTube技能配置完成报告.md
  - NotebookLM 技能使用指南.md
  - NotebookLM 技能配置完成报告.md
  - NotebookLM 认证指南.md
  - Cookie Converter使用指南.md
  - Cookie Converter配置完成报告.md
  - Cookie相关技能总览.md
  - Cookie相关技能整合报告.md

- Update MEMORY.md with new skills
- Update TOOLS.md with new tools and configurations
- Update RULES.md with important rules

- Add memory files from backup (2026-03-02 to 2026-03-10)
- Add test scripts for YouTube and NotebookLM tools

All skills are fully integrated with cross-references between documentation.
```

### 提交统计
- **66 个文件** 已更改
- **17575 行** 新增
- **67 行** 删除
- **Commit ID:** 7db526b

---

## 🚀 推送到 GitHub

### 方式1：使用 Personal Access Token（推荐）

**步骤1：创建 GitHub Token**

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 选择权限：`repo`（完整仓库访问权限）
4. 生成并复制 token（格式：`ghp_xxxxxxxxxxxxxxxxxxxxxxxxx`）

**步骤2：使用 Token 推送**

```bash
cd /home/admin/openclaw/workspace

# 添加 token 到 git credential helper
git config credential.helper store
echo "https://169068671:TOKEN@github.com" > ~/.git-credentials

# 替换 TOKEN 为你的 GitHub token
# 例如: echo "https://169068671:ghp_abc123def456@github.com" > ~/.git-credentials

# 推送到 GitHub
git push -u origin master
```

---

### 方式2：使用 SSH 密钥（推荐用于长期使用）

**步骤1：生成 SSH 密钥**

```bash
# 生成 SSH 密钥
ssh-keygen -t ed25519 -C "169068671@qq.com" -f ~/.ssh/id_ed25519_github

# 或者使用 RSA（如果 ed25519 不支持）
ssh-keygen -t rsa -b 4096 -C "169068671@qq.com" -f ~/.ssh/id_rsa_github
```

**步骤2：添加公钥到 GitHub**

1. 复制公钥内容：
   ```bash
   cat ~/.ssh/id_ed25519_github.pub
   # 或
   cat ~/.ssh/id_rsa_github.pub
   ```

2. 访问 https://github.com/settings/keys
3. 点击 "New SSH key"
4. 粘贴公钥内容
5. 添加密钥

**步骤3：配置 Git 使用 SSH**

```bash
cd /home/admin/openclaw/workspace

# 更改远程仓库为 SSH
git remote set-url origin git@github.com:169068671/openclaw-backup.git

# 推送到 GitHub
git push -u origin master
```

**步骤4：配置 SSH 配置（可选）**

```bash
# 添加到 ~/.ssh/config
cat >> ~/.ssh/config <<EOF

Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github
    IdentitiesOnly yes
EOF
```

---

### 方式3：使用 GitHub CLI (gh)

**步骤1：安装 GitHub CLI**

```bash
# 如果 gh 未安装
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

**步骤2：使用 gh 认证**

```bash
gh auth login
```

**步骤3：使用 gh 推送**

```bash
cd /home/admin/openclaw/workspace
git push -u origin master
```

---

## ⚠️ 常见问题

### 问题1：认证失败

**错误信息：**
```
fatal: could not read Username for 'https://github.com': No such device or address
```

**解决方案：**
1. 使用 Personal Access Token（方式1）
2. 或使用 SSH 密钥（方式2）
3. 或使用 GitHub CLI（方式3）

---

### 问题2：Permission denied (publickey)

**错误信息：**
```
git@github.com: Permission denied (publickey)
```

**解决方案：**
1. 确认 SSH 密钥已添加到 GitHub
2. 确认使用正确的密钥文件
3. 检查 `~/.ssh/config` 配置
4. 尝试测试连接：`ssh -T git@github.com`

---

### 问题3：Host key verification failed

**错误信息：**
```
Host key verification failed
```

**解决方案：**
```bash
# 添加 GitHub 到 known_hosts
ssh-keyscan github.com >> ~/.ssh/known_hosts

# 或者禁用严格检查（不推荐）
GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no" git push -u origin master
```

---

### 问题4：远程仓库不存在

**错误信息：**
```
fatal: repository 'https://github.com/169068671/openclaw-backup.git/' not found
```

**解决方案：**
1. 确认仓库 URL 正确
2. 在 GitHub 上创建仓库：https://github.com/new
3. 或推送到不同的仓库

---

## 📊 提交详情

### 新增的文件（部分）

**Cookie 相关：**
- Cookie Converter使用指南.md
- Cookie Converter配置完成报告.md
- Cookie相关技能总览.md
- Cookie相关技能整合报告.md
- cookie-converter.skill
- cookie-converter/SKILL.md
- cookie-converter/cookie-converter.sh
- cookie-converter/scripts/convert_cookies.py

**YouTube 技能：**
- YouTube 技能使用指南.md
- YouTube技能配置完成报告.md
- test-youtube-tools.sh
- youtube-auth-exporter.skill
- youtube-auth-exporter/SKILL.md
- youtube-auth-exporter/scripts/convert_cookies.py
- yt-dlp-downloader.skill
- yt-dlp-downloader/SKILL.md

**NotebookLM 技能：**
- NotebookLM 技能使用指南.md
- NotebookLM 技能配置完成报告.md
- NotebookLM 认证指南.md
- test-notebooklm-tools.sh
- notebooklm-auth-exporter.skill
- notebooklm-auth-exporter/SKILL.md
- notebooklm-auth-exporter/scripts/convert_cookies.py
- notebooklm-auth.sh
- NotebookLM_Auth_VPS_Deployment.md

**Memory 文件：**
- MEMORY.md（恢复）
- memory/2026-03-02.md
- memory/2026-03-03-*.md（多个文件）
- memory/2026-03-05-copaw-update.md
- memory/2026-03-07.md
- memory/2026-03-08*.md（多个文件）
- memory/2026-03-09*.md（多个文件）
- memory/2026-03-10*.md（多个文件）

**Skills 目录：**
- skills/agent-browser/
- skills/agent-reach/
- skills/browser-cookies-exporter/
- skills/douban/
- skills/notebooklm/
- skills/notebooklm-youtube-importer/
- skills/ssh-tunnel/

**修改的文件：**
- RULES.md（更新）
- TOOLS.md（更新）

---

## 🎯 推荐方式

### 短期：使用 Personal Access Token
- 快速设置
- 无需 SSH 配置
- 适合一次性推送

### 长期：使用 SSH 密钥
- 更安全
- 无需每次输入密码
- 适合频繁推送

### 最佳：使用 GitHub CLI
- 集成最好
- 自动处理认证
- 支持更多功能

---

## 🚀 快速推送命令

### 方式1：Token 推送

```bash
cd /home/admin/openclaw/workspace
git config credential.helper store
echo "https://169068671:YOUR_TOKEN@github.com" > ~/.git-credentials
git push -u origin master
```

### 方式2：SSH 推送

```bash
cd /home/admin/openclaw/workspace
git remote set-url origin git@github.com:169068671/openclaw-backup.git
git push -u origin master
```

---

## ✅ 推送后的验证

推送成功后，访问：
```
https://github.com/169068671/openclaw-backup
```

你应该能看到：
- ✅ 所有新技能
- ✅ 更新的文档
- ✅ Memory 文件
- ✅ 配置报告

---

## 💡 提示

1. **第一次推送**：需要设置认证方式
2. **频繁推送**：使用 SSH 密钥更方便
3. **安全**：Token 可以设置过期时间，SSH 密钥可以随时删除
4. **协作**：如果与他人协作，使用 SSH 密钥更安全

---

**代码已提交，等待推送！** 🚀

选择你喜欢的方式，推送到 GitHub。
