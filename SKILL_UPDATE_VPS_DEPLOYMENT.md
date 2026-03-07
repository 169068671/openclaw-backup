# Skill Update: VPS Deployment Integration

**更新日期**: 2026-03-08
**更新的技能**: youtube-auth-exporter, notebooklm-auth-exporter

---

## 📝 更新内容

### 1. 添加了 VPS 部署询问流程

在两个技能的 `SKILL.md` 文档中添加了 "Step 5: Deploy to VPS (Optional)" 章节，包含：

#### youtube-auth-exporter
- ✅ 自动化部署脚本说明
- ✅ 手动部署方法
- ✅ 部署决策流程（询问用户）
- ✅ 部署测试步骤
- ✅ VPS 使用示例
- ✅ 完整的预期输出示例

#### notebooklm-auth-exporter
- ✅ 自动化部署脚本说明
- ✅ 手动部署方法
- ✅ 部署决策流程（询问用户，带警告）
- ✅ 部署测试步骤
- ✅ VPS 使用示例（3 种方案）
- ✅ VPS 限制说明（Google IP 限制）

---

## 🎯 用户交互流程

### youtube-auth-exporter

```
✅ YouTube authentication exported successfully!

Do you want to deploy to VPS for automated downloads? [Y/n]

如果用户选择 Y:
1. 运行 /tmp/deploy_youtube_auth.sh
2. 自动测试认证
3. 显示部署结果

如果用户选择 n:
1. 跳过部署
2. 仅本地使用
```

### notebooklm-auth-exporter

```
✅ NotebookLM authentication exported successfully!

Do you want to deploy to VPS? [Y/n]
Note: VPS access may be limited by Google IP restrictions.
      Local usage is recommended for best results.

如果用户选择 Y:
1. 运行 /home/admin/openclaw/workspace/deploy-notebooklm-auth.sh
2. 自动测试认证
3. 显示部署结果（可能失败，因为 IP 限制）

如果用户选择 n:
1. 跳过部署
2. 推荐本地使用
```

---

## 📊 部署测试结果

### youtube-auth-exporter

**本地测试**:
- ✅ 认证导出成功（55 个 cookies）
- ✅ Playwright 测试成功（页面标题: YouTube）
- ✅ Netscape 格式转换成功

**VPS 测试**:
- ✅ 文件部署成功（18K）
- ✅ Playwright 认证成功（页面标题: YouTube）
- ✅ yt-dlp 测试成功

**结论**: VPS 上完全可以使用 ⭐

### notebooklm-auth-exporter

**本地测试**:
- ✅ 认证导出成功（53 个 cookies）
- ✅ Playwright 测试成功（页面标题: NotebookLM）

**VPS 测试**:
- ✅ 文件部署成功（18K）
- ❌ Playwright 认证失败（Google IP 限制）
- ⚠️ 网络连接测试：HTTP/2 302（需要认证）

**结论**: VPS 上受限制，推荐本地使用 ⚠️

---

## 📁 相关脚本

### youtube-auth-exporter

| 脚本 | 位置 | 功能 |
|-----|------|------|
| youtube_auth_setup.sh | /tmp/ | 一键认证导出 |
| deploy_youtube_auth.sh | /tmp/ | VPS 部署脚本 |
| youtube_download_with_auth.sh | /tmp/ | 本地下载脚本 |
| vps_youtube_test.sh | /tmp/ → /tmp/ (VPS) | VPS 测试脚本 |

### notebooklm-auth-exporter

| 脚本 | 位置 | 功能 |
|-----|------|------|
| notebooklm_auth_deploy.sh | /tmp/ | 认证导出和部署 |
| deploy-notebooklm-auth.sh | workspace/ | VPS 部署脚本 |
| notebooklm_download_setup.sh | /tmp/ | 下载设置脚本 |
| vps_notebooklm_test.sh | /tmp/ → /tmp/ (VPS) | VPS 测试脚本 |

---

## 🔄 更新决策流程

### 1. 认证导出完成后

**询问用户**:
```
✅ {技能名} 认证导出成功！

是否部署到 VPS？[Y/n]
```

### 2. 用户选择 Y

**执行**:
```bash
# 运行部署脚本
{部署脚本路径}

# 测试部署
{测试脚本路径}
```

**显示**:
- ✅ 部署成功/失败
- 📊 测试结果
- 📍 文件位置
- 📖 使用方法

### 3. 用户选择 n

**显示**:
- ✅ 跳过部署
- 📍 本地文件位置
- 📖 本地使用方法

---

## 📚 文档更新位置

### youtube-auth-exporter
**文件**: `~/.openclaw/skills/youtube-auth-exporter/SKILL.md`
**新增章节**: "Step 5: Deploy to VPS (Optional)"

内容:
- 自动化部署脚本说明
- 手动部署方法
- 部署决策流程
- 部署测试步骤
- VPS 使用示例

### notebooklm-auth-exporter
**文件**: `~/.openclaw/skills/notebooklm-auth-exporter/SKILL.md`
**新增章节**: "Step 5: Deploy to VPS (Optional)"

内容:
- 自动化部署脚本说明
- 手动部署方法
- 部署决策流程（带警告）
- 部署测试步骤
- VPS 使用示例（3 种方案）

---

## 🎯 使用建议

### youtube-auth-exporter

**推荐**: 部署到 VPS
- ✅ VPS 上可以正常使用
- ✅ 适合自动化下载
- ✅ 不受 IP 限制

### notebooklm-auth-exporter

**推荐**: 本地使用
- ⚠️ VPS 上受 IP 限制
- ✅ 本地使用不受限制
- ✅ 推荐本地 Playwright

---

## 🚀 完整使用流程示例

### YouTube 认证导出和部署

```bash
# 1. 导出认证
browser-cookies-exporter .google.com /tmp/google-cookies.txt
python3 ~/.openclaw/skills/youtube-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# 2. 询问用户是否部署
# "Do you want to deploy to VPS for automated downloads? [Y/n]"

# 3. 如果选择 Y，运行部署
/tmp/deploy_youtube_auth.sh

# 4. 测试部署
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 \
  "/tmp/vps_youtube_test.sh"
```

### NotebookLM 认证导出和部署

```bash
# 1. 导出认证
browser-cookies-exporter .google.com /tmp/google-cookies.txt
python3 ~/.openclaw/skills/notebooklm-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# 2. 询问用户是否部署
# "Do you want to deploy to VPS? [Y/n]"
# "Note: VPS access may be limited by Google IP restrictions."

# 3. 如果选择 Y，运行部署
/home/admin/openclaw/workspace/deploy-notebooklm-auth.sh

# 4. 测试部署（可能失败）
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 \
  "/tmp/vps_notebooklm_test.sh"

# 5. 如果失败，推荐本地使用
```

---

## ✅ 更新检查清单

- [x] 更新 youtube-auth-exporter/SKILL.md
  - [x] 添加 Step 5 章节
  - [x] 包含部署决策流程
  - [x] 包含部署测试步骤
  - [x] 包含 VPS 使用示例

- [x] 更新 notebooklm-auth-exporter/SKILL.md
  - [x] 添加 Step 5 章节
  - [x] 包含部署决策流程（带警告）
  - [x] 包含部署测试步骤
  - [x] 包含 VPS 使用示例（3 种方案）

- [x] 创建更新说明文档
  - [x] 记录更新内容
  - [x] 记录决策流程
  - [x] 记录测试结果
  - [x] 记录使用建议

---

## 📝 备注

### youtube-auth-exporter

**优势**:
- VPS 上可以正常使用
- 适合自动化下载任务
- 不受 Google IP 限制

**使用场景**:
- 定期批量下载 YouTube 视频
- 下载年龄限制视频
- 下载私人/不公开视频
- 自动化 YouTube 工作流

### notebooklm-auth-exporter

**限制**:
- VPS 上受 Google IP 限制
- 需要代理才能在 VPS 上使用

**推荐方案**:
- 本地使用 Playwright（最佳）
- 本地使用 notebooklm CLI
- VPS 使用 notebooklm CLI（简单场景）

**不推荐**:
- VPS 上使用 Playwright（需要代理，性能差）

---

## 🔗 相关文档

- `YouTube_Auth_VPS_Deployment.md` - YouTube 认证部署报告
- `NotebookLM_Auth_VPS_Deployment.md` - NotebookLM 认证部署报告
- `memory/2026-03-08.md` - 每日记录

---

**更新人**: openclaw ⚡
**最后更新**: 2026-03-08 06:40 (GMT+8)
