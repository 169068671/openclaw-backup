# 2026-03-08 - GOG 技能安装

## 10:45-11:01 - GOG 技能安装

### 需求
安装 GOG 技能（Google Workspace CLI）。

### 安装过程

#### 1. ClawHub 安装尝试（失败）

**问题**: ClawHub 遇到速率限制（Rate limit exceeded）

**尝试**:
- 尝试 1: 失败
- 尝试 2: 失败（等待 3 秒）
- 尝试 3: 失败（等待 5 秒）
- 尝试 4: 失败（等待 10 秒）
- 尝试 5: 失败（等待 30 秒）
- 尝试 6: 失败（等待 60 秒）

**结论**: ClawHub 服务端速率限制，无法通过该方式安装

#### 2. 手动安装（成功）

**技能信息**:
- 名称: gog
- 描述: Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs
- 所有者: steipete
- 版本: 1.0.0
- 仓库: https://github.com/mjfork/mjfork-claude-plugins

**步骤**:
1. 查找技能仓库
   - 搜索 GitHub: `gog cli steipete`
   - 找到仓库: https://github.com/mjfork/mjfork-claude-plugins

2. 克隆技能仓库
   ```bash
   cd ~/.openclaw/skills
   git clone https://github.com/mjfork/mjfork-claude-plugins.git gog
   ```

3. 调整技能结构
   - 原始位置: `~/.openclaw/skills/gog/skills/gog/SKILL.md`
   - 目标位置: `~/.openclaw/skills/gog/SKILL.md`
   - 复制 SKILL.md 到正确位置

4. 安装 gog CLI 工具
   - 版本: v0.11.0 (91c4c15)
   - 下载 URL: https://github.com/steipete/gogcli/releases/download/v0.11.0/gogcli_0.11.0_linux_amd64.tar.gz
   - 文件大小: 8.03 MB
   - 下载时间: 约 2:34 分钟
   - 安装路径: /usr/local/bin/gog

### 安装结果

#### 技能安装
- ✅ 技能已安装到 `~/.openclaw/skills/gog/`
- ✅ SKILL.md 文件位置正确
- ✅ 技能已在技能列表中

#### gog CLI 安装
- ✅ 版本: v0.11.0 (91c4c15)
- ✅ 路径: /usr/local/bin/gog
- ✅ 可执行权限已设置
- ✅ 命令可正常执行

### 技能功能

**描述**: Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs

**支持的服务**:
- Gmail
- Calendar
- Drive
- Chat
- Tasks
- Sheets
- Docs
- Slides
- Contacts
- People
- Groups
- Classroom
- Keep

**触发场景**:
- "check email", "read my mail"
- "send an email", "search gmail"
- "reply to email"
- "what's on my calendar", "schedule a meeting"
- "create an event", "find free time"
- "search drive", "download a file"
- "upload to drive", "share a file"
- "list my tasks", "add a task"
- "read a spreadsheet", "update a sheet"
- "search contacts"
- "send a chat message"
- "export document"

**前置条件**:
- 已安装 gog CLI ✅
- 需要授权: `gog auth add you@gmail.com`

### 全局标志

| 标志 | 用途 |
|-----|------|
| `--account=EMAIL` | 选择 Google 账号（或别名）|
| `--json` | 输出 JSON 到 stdout（最适合脚本）|
| `--plain` | 输出 TSV（可解析，无颜色）|
| `--force` | 跳过确认 |
| `--no-input` | 永不提示；失败代替 |
| `--verbose` | 启用详细日志 |

### Git 提交

待更新（尚未提交）

### 安装的文件

- `~/.openclaw/skills/gog/SKILL.md` - 技能文档
- `~/.openclaw/skills/gog/skills/gog/examples/` - 示例
- `~/.openclaw/skills/gog/skills/gog/references/` - 参考资料
- `/usr/local/bin/gog` - gog CLI 工具

### 已安装的技能列表

- agent-browser
- agent-reach
- amap-traffic
- browser-cookies-exporter
- **gog** ✅ 新安装
- hn
- musicdl-downloader
- notebooklm
- notebooklm-auth-exporter
- notebooklm-youtube-importer
- otaku-reco
- otaku-wiki
- pptx-creator
- qwen-image
- ssh-tunnel
- stock-watcher
- url-digest
- youtube-auth-exporter
- yt-dlp-downloader
- yutto-downloader

### 下一步

1. **授权 gog CLI**:
   ```bash
   gog auth add you@gmail.com
   ```

2. **测试功能**:
   - Gmail: `gog gmail search 'newer_than:7d'`
   - Calendar: `gog cal list --days 7`
   - Drive: `gog drive list`

### 关键发现

1. **ClawHub 速率限制**: 服务端限制，无法绕过
2. **手动安装可行**: 通过 GitHub 仓库可以成功安装技能
3. **gog CLI 独立**: 可以单独安装和使用
4. **技能结构重要**: SKILL.md 必须在技能根目录
5. **Linux 二进制**: gog CLI 提供 Linux amd64 版本

### 安装时间线

| 时间 | 操作 | 状态 |
|-----|------|------|
| 10:45 | 开始 ClawHub 安装 | ❌ 速率限制 |
| 10:50 | 尝试多次安装 | ❌ 仍受限 |
| 10:52 | 查找 GitHub 仓库 | ✅ 找到仓库 |
| 10:52 | 克隆技能仓库 | ✅ 成功 |
| 10:58 | 调整技能结构 | ✅ 成功 |
| 10:59 | 下载 gog CLI | ⏳ 进行中 |
| 11:01 | 安装 gog CLI | ✅ 完成 |
| 11:01 | 验证安装 | ✅ 成功 |

### 总结

- ✅ **技能已安装**: gog (Google Workspace CLI)
- ✅ **CLI 工具已安装**: gog v0.11.0
- ✅ **技能结构正确**: SKILL.md 在根目录
- ✅ **可用性验证**: 命令可正常执行
- ⚠️ **需要授权**: 首次使用前需要 `gog auth add`

---

**安装人**: openclaw ⚡
**安装时间**: 2026-03-08 11:01 (GMT+8)
