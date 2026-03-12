# GitHub 登录方式总结

**日期：** 2026-03-12

---

## 📋 当前状态

### GitHub CLI (gh)
- **状态：** ❌ 未安装
- **MEMORY.md 记录：** GitHub CLI (gh) v2.87.3 已认证（可能安装在 VPS 上）

### Git Credential Helper
- **状态：** ✅ 已配置
- **文件：** ~/.git-credentials
- **内容：** https://169068671:[TOKEN]@github.com
- **注意：** Token 是占位符，需要替换为真实的 GitHub token

### SSH 密钥
- **状态：** ❌ 未配置
- **.ssh 目录：** 存在，但无私钥文件

---

## 🔐 GitHub 登录方式

### 方式1：GitHub CLI (gh) 登录（推荐）

**安装 GitHub CLI：**

```bash
# Ubuntu/Debian
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

**登录：**

```bash
gh auth login

# 按提示选择：
# 1. What account do you want to log into? -> GitHub.com
# 2. What is your preferred protocol for Git operations? -> HTTPS
# 3. Authenticate Git with your GitHub credentials? -> Yes
# 4. How would you like to authenticate GitHub CLI? -> Login with a web browser
# 5. 按提示在浏览器中授权
```

**优势：**
- ✅ 简单易用
- ✅ 自动管理认证
- ✅ 支持 2FA
- ✅ 自动生成和存储 token

---

### 方式2：Personal Access Token

**步骤1：创建 Token**

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 选择权限：`repo`（完整仓库访问权限）
4. 设置过期时间（可选）
5. 生成并复制 token

**步骤2：配置 Git**

```bash
# 配置 credential helper
git config credential.helper store

# 添加 token 到 credential helper
echo "https://169068671:YOUR_TOKEN@github.com" > ~/.git-credentials

# 替换 YOUR_TOKEN 为你生成的 token
```

**步骤3：推送**

```bash
cd /home/admin/openclaw/workspace
git push -u origin master
```

**优势：**
- ✅ 不需要安装额外工具
- ✅ Token 可以设置过期时间
- ✅ 可以随时删除

---

### 方式3：SSH 密钥（推荐长期使用）

**步骤1：生成 SSH 密钥**

```bash
# 生成 ed25519 密钥（推荐）
ssh-keygen -t ed25519 -C "169068671@qq.com"

# 或使用 RSA（如果 ed25519 不支持）
ssh-keygen -t rsa -b 4096 -C "169068671@qq.com"
```

**步骤2：添加公钥到 GitHub**

1. 复制公钥：
   ```bash
   cat ~/.ssh/id_ed25519.pub
   # 或
   cat ~/.ssh/id_rsa.pub
   ```

2. 访问 https://github.com/settings/keys
3. 点击 "New SSH key"
4. 输入标题（例如："Home PC"）
5. 粘贴公钥内容
6. 点击 "Add SSH key"

**步骤3：配置 Git 使用 SSH**

```bash
cd /home/admin/openclaw/workspace
git remote set-url origin git@github.com:169068671/openclaw-backup.git
git push -u origin master
```

**优势：**
- ✅ 最安全
- ✅ 无需每次输入密码
- ✅ 适合频繁推送
- ✅ 支持 2FA

---

## 🎯 推荐方案

### 场景1：新手/一次性使用
**推荐：** GitHub CLI (gh) 或 Personal Access Token

**原因：** 设置简单，不需要配置 SSH

---

### 场景2：频繁推送/长期使用
**推荐：** SSH 密钥

**原因：** 一次设置，永久使用，最安全

---

### 场景3：团队协作
**推荐：** SSH 密钥

**原因：** 安全，支持多用户，便于管理

---

## 🔍 当前系统检查

### 已有配置
- ✅ Git 已安装
- ✅ Git credential helper 已配置
- ✅ 远程仓库已添加：origin
- ❌ GitHub CLI (gh) 未安装
- ❌ SSH 密钥未配置

### Git 配置
```bash
git config --list | grep -E "(user|credential|remote)"
```

---

## 🚀 快速开始

### 选项1：使用 GitHub CLI（推荐）

```bash
# 1. 安装 GitHub CLI
sudo apt update
sudo apt install gh

# 2. 登录
gh auth login

# 3. 推送
cd /home/admin/openclaw/workspace
git push -u origin master
```

---

### 选项2：使用推送脚本

```bash
bash /home/admin/openclaw/workspace/git-push-helper.sh
```

脚本会自动引导你选择认证方式。

---

### 选项3：使用 Personal Access Token

```bash
# 1. 创建 token（访问 GitHub settings）
# 2. 配置 git
cd /home/admin/openclaw/workspace
git config credential.helper store
echo "https://169068671:YOUR_TOKEN@github.com" > ~/.git-credentials

# 3. 推送
git push -u origin master
```

---

## 📚 参考

- GitHub CLI 文档：https://docs.github.com/en/github-cli
- Personal Access Tokens：https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
- SSH 密钥设置：https://docs.github.com/en/authentication/connecting-to-github-with-ssh

---

## 💡 提示

1. **第一次使用 GitHub CLI？** 按照提示一步步操作即可
2. **忘记 Token？** 删除旧的，生成新的
3. **SSH 密钥泄漏？** 立即删除并重新生成
4. **推送失败？** 检查网络连接和认证信息

---

**选择适合你的方式，开始使用 GitHub！** 🚀
