# NotebookLM 认证指南

## 📋 概述

**notebooklm-auth-exporter** 技能已恢复！这是一个专门用于导出 NotebookLM 认证状态的工具。

**认证步骤：**
1. 在 Chrome 中登录 Google
2. 导出 Google cookies
3. 转换为 Playwright 格式
4. 部署到 VPS

---

## 🚀 快速开始

### 步骤1：在 Chrome 中登录 Google

1. 打开 Chrome 浏览器
2. 访问 https://accounts.google.com 并登录
3. 访问 https://notebooklm.google.com 确保可以访问

### 步骤2：运行认证脚本

登录成功后，运行一键式认证脚本：

```bash
bash /home/admin/openclaw/workspace/notebooklm-auth.sh
```

这个脚本会自动完成以下步骤：
- ✅ 导出 Google cookies
- ✅ 转换为 Playwright 格式
- ✅ 部署到 VPS
- ✅ 验证认证状态

---

## 🔧 手动步骤（如果脚本失败）

### 1. 导出 Google cookies

```bash
browser-cookies-exporter .google.com /tmp/google-cookies.txt
```

如果失败，请确保：
- Chrome 正在运行
- 你已经在 Google 中登录
- 访问过 https://notebooklm.google.com

### 2. 转换为 Playwright 格式

```bash
python3 /home/admin/openclaw/workspace/notebooklm-auth-exporter/notebooklm-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json
```

### 3. 部署到 VPS

```bash
# 创建 VPS 目录
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 "mkdir -p /root/.config/notebooklm/"

# 上传认证文件
sshpass -p 'Whj001.Whj001' scp /tmp/storage_state.json \
  root@76.13.219.143:/root/.config/notebooklm/session.json
```

### 4. 验证认证

```bash
ssh root@76.13.219.143 "notebooklm list"
```

如果成功，会显示笔记本列表；如果失败，需要重新认证。

---

## 📁 文件位置

### 本地文件

| 文件 | 位置 |
|------|------|
| 认证脚本 | `/home/admin/openclaw/workspace/notebooklm-auth.sh` |
| 技能包 | `/home/admin/openclaw/workspace/notebooklm-auth-exporter/` |
| 部署指南 | `/home/admin/openclaw/workspace/NotebookLM_Auth_VPS_Deployment.md` |
| 部署脚本 | `/home/admin/openclaw/workspace/deploy-notebooklm-auth.sh` |

### VPS 文件

| 文件 | 位置 |
|------|------|
| 认证文件 | `/root/.config/notebooklm/session.json` |
| 旧备份 | `/root/.notebooklm/storage_state.json` |

---

## ⚠️ 常见问题

### 问题1：Chrome 未运行

**错误信息：**
```
❌ Chrome 未运行
```

**解决方案：**
启动 Chrome 浏览器：
```bash
/opt/google/chrome/chrome &
```

### 问题2：未找到 Google cookies

**错误信息：**
```
Error: No cookies found for domain '.google.com'
```

**解决方案：**
1. 在 Chrome 中访问 https://accounts.google.com 并登录
2. 访问 https://notebooklm.google.com
3. 确保保持 Chrome 运行
4. 重新运行认证脚本

### 问题3：认证已过期

**错误信息：**
```
Error: Authentication expired or invalid
```

**解决方案：**
Google cookies 有效期约 14 天，需要重新导出：
1. 重新登录 Google
2. 运行认证脚本：`bash /home/admin/openclaw/workspace/notebooklm-auth.sh`

### 问题4：部署失败

**错误信息：**
```
❌ 部署失败
```

**解决方案：**
1. 检查 VPS 连接：
   ```bash
   sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 "echo 'connected'"
   ```

2. 检查文件是否存在：
   ```bash
   ls -la /tmp/storage_state.json
   ```

3. 手动上传：
   ```bash
   sshpass -p 'Whj001.Whj001' scp /tmp/storage_state.json \
     root@76.13.219.143:/root/.config/notebooklm/session.json
   ```

---

## 🎯 认证成功后的使用

### 创建笔记本

```bash
ssh root@76.13.219.143

notebooklm create "我的笔记本"
```

### 添加源文件

```bash
notebooklm source add "https://www.youtube.com/watch?v=VIDEO_ID"
```

### 生成内容

```bash
notebooklm generate audio --wait
notebooklm download audio ./podcast.mp3
```

---

## 💡 提示

1. **定期更新**：Google cookies 有效期约 14 天，建议设置日历提醒
2. **保持登录**：确保在 Chrome 中保持 Google 登录状态
3. **验证访问**：定期访问 https://notebooklm.google.com 确保可以正常使用
4. **安全提醒**：认证文件包含你的登录信息，不要分享给他人

---

## 🔗 相关资源

- **notebooklm 使用指南：** `/home/admin/openclaw/workspace/NotebookLM技能使用指南.md`
- **youtube-auth-exporter：** `/home/admin/openclaw/workspace/youtube-auth-exporter/SKILL.md`
- **Cookie Format Converter：** `/home/admin/openclaw/workspace/Cookie Converter使用指南.md`
- **官方 GitHub：** https://github.com/joschan21/notebooklm-py

---

**认证完成！** 🎉

现在你可以在 VPS 上使用 NotebookLM 了！
