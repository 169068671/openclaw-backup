# MEMORY.md - 长期记忆

最后更新: 2026-03-07 16:10

---

## 👤 用户信息

**姓名**: 王华军（王老师）
**职业**: 高中技术学科教师，负责STEM课程教学
**时区**: 北京时间 (GMT+8)
**称呼**: 王老师
**代词**: 他/他

**教学需求**:
- 教学资源准备和整理
- 课程内容开发
- 学生项目指导
- 技术文档和资料查找
- 教学工具和技术支持

---

## 🚨 核心规则 (RULES.md)

### 第一规则：永不断开连接
不管做什么设置，一定要确保能再次打开。每次改变后，都要 ping 下自己，确保下次能打开。

### 第二规则：操作前备份
重要操作前必须创建备份

### 测试连接检查清单
```bash
# OpenClaw 服务
systemctl status openclaw-gateway

# 网络连接
ping -c 3 8.8.8.8
curl -I https://github.com

# Git 仓库
cd /home/admin/openclaw/workspace && git status
```

---

## 🌐 网络架构与代理

### 连接优先级（测试结果 2026-03-03）

| 访问类型 | 直连 | SSH隧道 | 结论 |
|---------|------|---------|------|
| GitHub HTTPS | 0.35s | 1.09s | 直连快3倍 ✅ |
| GitHub SSH | 3.09s | 4.56s | 直连快1.5倍 ✅ |
| Git Fetch | 4.00s | 5.84s | 直连快1.5倍 ✅ |

### 全局规则
- ✅ GitHub访问（HTTP/SSH）：使用直连
- ✅ Git操作（push/pull/clone）：使用直连
- ✅ 国内网站：使用直连
- ⚠️ SSH隧道：仅在直连失败时使用（备用方案）

### SSH隧道配置（备用）
```bash
# 启动 SSH 隧道
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143

# 检查隧道状态
netstat -tlnp | grep 1080

# 停止隧道
ps aux | grep "ssh.*1080" | awk '{print $2}' | xargs kill
```

### Hostinger VPS 信息
- **地址**: 76.13.219.143
- **主机名**: srv1437164
- **用户**: root
- **密码**: Whj001.Whj001
- **SSH 连接**: `sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143`

---

## 🤖 OpenClaw 配置

### 基本信息
- **版本**: 2026.3.2
- **大模型**: GLM-4.7 (智谱AI)
- **Web UI**: http://127.0.0.1:18789/
- **Workspace**: /home/admin/openclaw/workspace
- **Gateway PID**: 11780

### 代理设置
- **OpenClaw**: 不使用代理（所有直连）
- **钉钉通道**: 直连
- **AI模型调用**: 直连

### 网关管理
```bash
# 重启 Gateway
openclaw gateway restart

# 查看状态
openclaw status

# 查看日志
journalctl -u openclaw-gateway -f
```

---

## 📨 钉钉通道配置

### 基本信息
- **插件**: dingtalk-connector v0.6.0
- **Client ID**: dingyscopnptfxm4hg8q
- **消息模式**: Stream 模式
- **应用状态**: 已发布

### 必需权限
- Card.Streaming.Write ✅
- Card.Instance.Write ✅
- qyapi_robot_sendmsg ✅

### 功能特性
- ✅ AI Card 流式响应
- ✅ 会话持久化（30分钟超时）
- ✅ 双向通信
- ✅ 图片自动上传
- ✅ 会话命令: /new, /reset, /clear, 新会话, 重新开始, 清空对话

---

## 🛠️ 下载工具（总览）

| 工具 | 类型 | 功能 | 版本 | 安装位置 | 推荐场景 |
|-----|------|------|------|---------|---------|
| **yutto** | 视频 | Bilibili 专用 | 2.1.1 | ~/.local/bin/yutto | Bilibili下载 |
| **yt-dlp** | 视频 | 综合下载（1000+网站） | 2026.02.21 | ~/.local/bin/yt-dlp | 综合视频下载 |
| **musicdl** | 音乐 | 音乐/有声读物（50+平台） | 2.9.7 | ~/.local/bin/musicdl | 音乐/有声读物 |

### 推荐使用
- **Bilibili 下载**: yutto（专用，更稳定）
- **综合视频下载**: yt-dlp（支持1000+网站）
- **音乐/有声读物**: musicdl（50+音乐平台）

### 安装命令
```bash
# yutto (B站)
pip install --upgrade yutto -i https://pypi.tuna.tsinghua.edu.cn/simple

# yt-dlp (综合)
pip install --upgrade yt-dlp

# musicdl (音乐)
pip install --upgrade musicdl
```

---

## 📦 已创建的技能

### yutto-downloader
- **位置**: ~/.openclaw/skills/yutto-downloader/
- **功能**: Bilibili视频下载（单视频、批量、多分辨率、多编码）
- **大小**: 7.8K
- **Git提交**: 087fba9, 399ecee, dcc9a38
- **特点**: 专为B站设计，稳定可靠

### browser-cookies-exporter
- **位置**: ~/.openclaw/skills/browser-cookies-exporter/
- **功能**: 浏览器 cookies 导出（支持任意网站）
- **安装位置**: ~/.local/bin/browser-cookies-exporter
- **特点**: Netscape 格式、兼容 yt-dlp/curl/wget
- **支持网站**: YouTube, Bilibili, Twitter, GitHub, Reddit, LinkedIn, 等等
- **测试结果**:
  - ✅ YouTube: 21 cookies (2026-03-07)
  - ✅ Bilibili: 26 cookies (2026-03-07)
- **使用方法**:
  ```bash
  browser-cookies-exporter youtube.com /home/admin/Desktop/cookies-youtube.txt
  browser-cookies-exporter bilibili.com /home/admin/Desktop/cookies-bilibili.txt
  ```

### agent-reach（网络资源搜索）
- **位置**: ~/.openclaw/skills/agent-reach/
- **功能**: 全站网络资源搜索，支持 13+ 平台
- **支持平台**: Twitter/X, Reddit, YouTube, GitHub, Bilibili, 小红书, 抖音, 微信公众号, LinkedIn, Boss直聘, RSS, Exa 搜索, 网页阅读
- **Git提交**: 0c2bf4e (2026-03-06)
- **特点**: 免费开源、隐私安全、支持多平台交互、一键安装
- **参考**: https://github.com/Panniantong/agent-reach
- **安装状态**: ✅ 已安装基础组件（2026-03-07 09:16）
  - ✅ agent-reach CLI
  - ✅ xreach CLI (Twitter/X)
  - ✅ mcporter (MCP 服务器)
  - ✅ Exa 全网搜索（已配置）
  - ✅ yt-dlp (YouTube/B站)
  - ✅ feedparser (RSS)
  - ✅ FFmpeg (视频处理)
  - ✅ GitHub CLI (gh) v2.87.3 - ✅ 已认证（账号：169068671）
  - 可用渠道：6/13

### agent-browser（Vercel 无头浏览器自动化）
- **位置**: ~/.openclaw/skills/agent-browser/
- **功能**: 无头浏览器自动化 CLI，专为 AI agents 设计
- **版本**: 0.16.3
- **安装位置**: /home/admin/.npm-global/bin/agent-browser
- **Git提交**: ffda064 (2026-03-07)
- **特点**: Rust 原生 CLI（极快）、AI 友好的 ref 选择器、完整 API
- **参考**: https://github.com/vercel-labs/agent-browser
- **安装状态**: ✅ 已安装并测试（2026-03-07 11:19）
  - ✅ agent-browser CLI (v0.16.3)
  - ✅ Chromium 浏览器
  - ✅ 基本功能测试通过（打开网页、快照、点击、关闭）
  - ✅ Cookies 导入脚本（2026-03-07）
- **常用命令**:
  ```bash
  # 打开网页
  agent-browser open https://example.com

  # 获取快照（AI 最佳）
  agent-browser snapshot

  # 使用 ref 操作
  agent-browser click @e2
  agent-browser fill @e3 "text"
  agent-browser screenshot page.png

  # 关闭浏览器
  agent-browser close
  ```

### NotebookLM（Google NotebookLM 非官方 API）
- **位置**: ~/.openclaw/skills/notebooklm/
- **功能**: Google NotebookLM 非官方 Python API
- **版本**: 0.3.3
- **安装位置**: ~/.local/bin/notebooklm
- **Git提交**: 138f7d3 (2026-03-07)
- **特点**: 笔记本管理、源文件导入、聊天对话、内容生成、下载导出
- **参考**: https://github.com/joschan21/notebooklm-py
- **安装状态**: ✅ 已安装并测试（2026-03-07）
  - ✅ notebooklm CLI (v0.3.3)
  - ✅ Playwright Chromium
  - ✅ 成功登录（保存到 ~/.notebooklm/storage_state.json）
  - ✅ 基本功能测试通过（创建笔记本、添加源、生成内容）
- **常用命令**:
  ```bash
  # 首次登录
  notebooklm login

  # 创建笔记本
  notebooklm create "My Research"

  # 添加源文件
  notebooklm source add "https://www.youtube.com/watch?v=XXX"

  # 生成内容
  notebooklm generate audio --wait

  # 下载内容
  notebooklm download audio ./podcast.mp3
  ```
- **⚠️ 重要提醒**: 非官方库，使用未记录的 Google API，可能随时更改

### notebooklm-youtube-importer（YouTube 批量导入到 NotebookLM）
- **位置**: ~/.openclaw/skills/notebooklm-youtube-importer/
- **功能**: 批量导入 YouTube 视频到 NotebookLM 笔记本
- **Git提交**: - (2026-03-07)
- **特点**: 自动去重、进度显示、错误处理
- **安装状态**: ✅ 已创建并测试（2026-03-07）
  - ✅ notebooklm_youtube_importer.py - FreeCAD 教程专用导入器
  - ✅ youtube_to_notebooklm.py - 从 YouTube URL 导入
  - ✅ youtube_browser_importer.py - 使用 agent-browser 自动提取
  - ✅ delete_duplicates.py - 删除重复源文件
- **成功案例**: FreeCAD Python 教程（38 个视频）
- **脚本位置**: ~/.openclaw/skills/notebooklm-youtube-importer/
- **⚠️ 限制**: YouTube 自动化访问限制，需要手动提供链接或使用 cookies

### ssh-tunnel（SSH 隧道管理）
- **位置**: ~/.openclaw/skills/ssh-tunnel/
- **功能**: SSH 隧道管理（启动/停止/状态/重启）和 Google 连通性测试
- **版本**: v1.1 (2026-03-07)
- **Git提交**: 663d9da (2026-03-07)
- **特点**: 一键操作、自动检测 Google、详细状态显示、彩色输出、SSH 密钥认证
- **安装状态**: ✅ 已创建并测试（2026-03-07 18:04）
  - ✅ ssh-tunnel.sh - 主脚本
  - ✅ SKILL.md - 完整技能文档
  - ✅ README.md - 快速开始指南
  - ✅ 使用 socks5h:// 确保远程服务器解析 DNS
- **配置**:
  - 服务器：76.13.219.143 (srv1437164)
  - 用户：root
  - 本地端口：1080 (SOCKS5)
  - SSH 密钥：~/.ssh/id_rsa
- **常用命令**:
  ```bash
  ~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh start              # 启动隧道（自动测试 Google）
  ~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh start --no-check    # 启动隧道（不测试 Google）
  ~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh stop               # 停止隧道
  ~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh status             # 查看状态
  ~/.openclaw/skills/ssh-tunnel/ssh-tunnel.sh restart            # 重启隧道
  ```
- **Google 测试结果**: ✅ 成功（HTTP 200）
- **重要修复**: 使用 `socks5h://` 而不是 `socks5://`，让远程服务器解析 DNS

### 安装的技能（ClawHub）
- feishu-doc (飞书文档)
- feishu-drive (飞书云盘)
- feishu-perm (飞书权限)
- feishu-wiki (飞书知识库)
- clawhub (技能管理)
- healthcheck (安全审计)
- skill-creator (技能创建)
- tmux (终端会话)
- video-frames (视频帧提取)
- weather (天气预报)
- musicdl-downloader (音乐下载)
- otaku-reco (二次元推荐)
- otaku-wiki (二次元百科)
- qwen-image (Qwen图像生成)
- stock-watcher (股票监控)
- yt-dlp-downloader (视频下载)
- yutto-downloader (B站下载)

---

## 🔄 备份系统

### GitHub 备份仓库
- **VPS备份**: git@github.com:169068671/vps-backup
- **OpenClaw备份**: git@github.com:169068671/openclaw-backup
- **Cron**: 每日 03:00 GMT+8 自动备份
- **最后备份**: 2026-03-03 03:00

### 工作空间备份
- **最新备份**: /home/admin/backups/workspace-backup-20260302-132648.tar.gz (49K)
- **Git 仓库**: /home/admin/openclaw/workspace/.git
- **初始提交**: cfd8d95

---

## 💾 关键文件结构

### 配置文件
- `~/.openclaw/openclaw.json` - OpenClaw主配置
- `~/.openclaw/models.json` - 模型配置
- `~/.npm-global/lib/node_modules/openclaw/` - OpenClaw安装目录

### 工作空间文件
- `SOUL.md` - 我的"灵魂"和个性
- `IDENTITY.md` - 我的身份信息
- `USER.md` - 王老师信息
- `RULES.md` - 全局规则（铁律）
- `TOOLS.md` - 工具和配置笔记
- `AGENTS.md` - 工作空间规则
- `HEARTBEAT.md` - 心跳任务清单（当前为空）

### 记忆文件
- `MEMORY.md` - 长期记忆（本文件）
- `memory/YYYY-MM-DD.md` - 日常日志（原始记录）

---

## 🎯 重要决策

### 1. 网络连接策略
**决策**: 使用直连为主，SSH隧道为备用
**原因**: 直连速度快3倍，更稳定
**测试日期**: 2026-03-03 15:30

### 2. 代理方案选择
**决策**: 从Tinyproxy切换到SSH隧道（SOCKS5）
**原因**: Tinyproxy HTTPS代理不稳定，经常超时
**切换日期**: 2026-03-02 14:25

### 3. OpenClaw直连
**决策**: OpenClaw不使用代理，所有流量直连
**原因**: 保证AI响应速度，不受代理影响

### 4. 工具选择策略
**决策**: 优先使用流行工具（高GitHub stars）
**原因**: 更可靠、更稳定、社区支持好
**案例**: res-downloader实验失败后，继续使用yutto/yt-dlp

---

## 📚 经验教训

### 技术经验
1. **SSH隧道 > Tinyproxy**: SSH隧道更稳定可靠
2. **直连 > 代理**: 能直连就不要用代理（快3倍）
3. **流行工具更可靠**: yt-dlp（100k+ stars）比实验工具更稳定
4. **测试再承诺**: 新工具必须先测试性能和用户体验
5. **及时清理**: 失败的实验要彻底清理，不留垃圾文件

### 工作方法
1. **文档先行**: 每次配置都记录详细文档
2. **版本控制**: Git保存所有重要配置和历史版本
3. **问题诊断**: 逐步测试、隔离问题、及时记录
4. **用户体验**: 简化配置步骤、提供详细文档、及时沟通

### 安全意识
1. **永不断开**: 每次改变后测试连接
2. **操作前备份**: 重要操作前必须创建备份
3. **私密不外泄**: 私密信息绝对不外泄

---

## 🔧 常用命令速查

### OpenClaw 管理
```bash
# 重启网关
openclaw gateway restart

# 查看状态
openclaw status

# 查看日志
journalctl -u openclaw-gateway -f

# 列出会话
openclaw sessions list
```

### SSH隧道管理
```bash
# 启动隧道
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143

# 检查状态
netstat -tlnp | grep 1080

# 停止隧道
ps aux | grep "ssh.*1080" | awk '{print $2}' | xargs kill
```

### Git 操作
```bash
# 查看状态
git status

# 提交更改
git add .
git commit -m "描述"
git push

# 拉取更新
git pull
```

### 下载工具使用
```bash
# Bilibili下载（yutto）
yutto https://www.bilibili.com/video/BV1xx411c7mD --format 1080P --video-codec hevc

# 综合下载（yt-dlp）
yt-dlp https://www.youtube.com/watch?v=xxx

# 音乐下载（musicdl）
musicdl -u "歌曲URL"
```

---

## 📊 系统状态检查清单

### 每次重要操作前检查
- [ ] OpenClaw Gateway 运行正常
- [ ] 网络连接正常（ping 8.8.8.8）
- [ ] GitHub 可访问（curl -I https://github.com）
- [ ] Git 仓库状态正常（git status）

### 每次重要操作后检查
- [ ] 测试OpenClaw服务（openclaw status）
- [ ] 测试网络连接（ping、curl）
- [ ] 测试Git操作（git status）
- [ ] 创建备份（如有需要）

---

## 🔍 问题排查

### 代理连接失败
1. 检查SSH隧道状态：`netstat -tlnp | grep 1080`
2. 检查VPS连接：`sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143`
3. 重启SSH隧道：先杀掉旧进程，再启动新隧道

### OpenClaw 网关问题
1. 查看状态：`systemctl status openclaw-gateway`
2. 查看日志：`journalctl -u openclaw-gateway -f`
3. 重启网关：`openclaw gateway restart`

### Git 问题
1. 检查连接：`ssh -T git@github.com`
2. 检查配置：`git config --list`
3. 尝试直连（不使用代理）

---

## 📞 重要联系人和服务

### VPS 服务商
- **Hostinger**: https://hostinger.com
- **VPS地址**: 76.13.219.143

### AI 服务商
- **智谱AI**: https://open.bigmodel.cn/ (GLM-4.7)
- **阿里云百炼**: https://bailian.console.aliyun.com/

### 钉钉开放平台
- **开发者后台**: https://open-dev.dingtalk.com/

### GitHub
- **VPS备份仓库**: git@github.com:169068671/vps-backup
- **OpenClaw备份仓库**: git@github.com:169068671/openclaw-backup

---

## 🎓 王老师的教学相关

### 可能需要的帮助
- 教学资源准备和整理
- 课程内容开发
- 学生项目指导
- 技术文档和资料查找
- 教学工具和技术支持

### 常用技术栈
- STEM 课程教学
- 视频下载和处理
- 文档管理和整理
- 技术工具使用指导

---

## 🗓️ 重要日期

- **2026-03-02**: 工作空间初始化，HTTP代理配置，钉钉通道配置
- **2026-03-03**: OpenClaw升级（2026.2.1→2026.3.2），yutto-downloader技能创建，SSH隧道配置
- **2026-03-04**: MEMORY.md 创建
- **2026-03-06**: agent-reach 技能创建（网络资源搜索，支持 13+ 平台）
- **2026-03-07**:
  - GitHub CLI (gh v2.87.3) 安装完成
  - agent-reach 基础组件安装完成（6/13 渠道可用）
  - browser-cookies-exporter 技能创建
  - agent-browser 技能创建（Vercel 无头浏览器自动化）
  - agent-browser Cookies 导入脚本完成（Google cookies 41/41 成功）
  - NotebookLM 技能创建（Google NotebookLM 非官方 API）
  - notebooklm-youtube-importer 技能创建（YouTube 批量导入到 NotebookLM）
  - FreeCAD Python 教程成功导入到 NotebookLM（38 个视频）
  - 技能代理配置文档更新（agent-browser、notebooklm、yt-dlp）
  - Git 本地提交 19 个（等待推送）

---

## ✅ 快速检查清单

### 系统健康
- [ ] OpenClaw 运行正常
- [ ] VPS SSH 可连接
- [ ] 钉钉通道工作正常
- [ ] GitHub 备份自动化

### 工具可用
- [ ] yutto（B站下载）
- [ ] yt-dlp（综合下载）
- [ ] musicdl（音乐下载）

### 备份状态
- [ ] 工作空间有备份
- [ ] Git 提交最新
- [ ] GitHub 自动化备份运行

---

## 🐾 CoPaw AI 助手

### VPS 上的 CoPaw (Hostinger VPS)

**基本信息**
- **部署方式**: 非容器部署（systemd 服务）
- **服务名称**: copaw.service
- **Web UI**: http://76.13.219.143:8088
- **配置目录**: /root/.copaw/
- **数据目录**: /root/.copaw/copaw_data
- **最后更新**: 2026-03-05

**钉钉机器人**
- **Agent ID**: 4312319425
- **Client ID**: dingcvagqvwxfx5w6kbf
- **Client Secret**: GyCFe_GpNjZWR4cp5NmkRVyaisPkEBvm8anVU9lLFfVZ4yqM_l3i5buKjWnWnbGA
- **机器人名称**: HostingerVPS-CoPaw
- **Bot Prefix**: [BOT]
- **连接状态**: ✅ 已连接

**LLM 配置**
- **Provider**: aliyun-codingplan
- **API Key**: sk-sp-b8cc74984e064982850e9cd85ed89477
- **Base URL**: https://coding.dashscope.aliyuncs.com/v1
- **模型**: qwen-plus

**服务管理**
```bash
# 查看状态
systemctl status copaw.service

# 启动服务
systemctl start copaw.service

# 停止服务
systemctl stop copaw.service

# 重启服务
systemctl restart copaw.service

# 查看日志
journalctl -u copaw.service -f
```

**配置文件位置**
- `/etc/systemd/system/copaw.service` - systemd 服务配置
- `/root/.copaw/config.json` - copaw 主配置
- `/root/.copaw/providers.json` - LLM provider 配置

**其他功能**
- **Nacos SDK**: ✅ 已安装 (3.0.4)
- **Vector Search**: ⚠️ 已禁用（API key 不支持 embedding）

**Docker 容器（同一 VPS）**
- whisper-faster: Whisper 语音转文字服务
- guacamole-web: 远程桌面 Web 界面 (8081)
- guacamole-mysql: Guacamole 数据库
- guacamole-guacd: Guacamole Daemon

---

### 本地的 CoPaw

**基本信息**
- **部署方式**: 直接运行
- **Web UI**: http://127.0.0.1:8089
- **配置目录**: /home/admin/.copaw/
- **最后更新**: 2026-03-05

**钉钉机器人**
- **Client ID**: ding4zn6bwph8ugrgei1
- **Client Secret**: GAtSSvW1UzLsO4PED0q5UWdR5YVLHXsn-h3e30tmwJlcz4CCsjTGZlpawxsZjQek
- **Bot Prefix**: [BOT]
- **连接状态**: ✅ 已连接

**LLM 配置**
- **Provider**: aliyun-codingplan
- **API Key**: sk-sp-b8cc74984e064982850e9cd85ed89477
- **Base URL**: https://coding.dashscope.aliyuncs.com/v1
- **模型**: qwen-plus

**服务管理**
```bash
# 启动服务
nohup copaw app --host 0.0.0.0 --port 8089 > /tmp/copaw_local.log 2>&1 &

# 查看进程
ps aux | grep 'copaw app' | grep -v grep

# 停止服务
pkill -f 'copaw app'

# 查看日志
tail -f /tmp/copaw_local.log
```

**配置文件位置**
- `/home/admin/.local/lib/python3.10/site-packages/copaw/providers/providers.json` - LLM provider 配置
- `/home/admin/.copaw/config.json` - copaw 主配置

**其他功能**
- **Vector Search**: ⚠️ 已禁用（API key 不支持 embedding）

---

### CoPaw 功能说明

**已启用的功能**
- ✅ 钉钉通道（双向通信）
- ✅ Console 通道
- ✅ AI Card 流式响应
- ✅ 会话持久化（30分钟超时）
- ✅ 图片自动上传
- ✅ 会话命令: /new, /reset, /clear, 新会话, 重新开始, 清空对话

**配置的会话命令**
- `/new` - 创建新会话
- `/reset` - 重置当前会话
- `/clear` - 清空对话历史
- `新会话` - 创建新会话（中文）
- `重新开始` - 重置当前会话（中文）
- `清空对话` - 清空对话历史（中文）

**限制说明**
- Vector Search 功能已禁用（因 API key 不支持 embedding 服务）
- 主要聊天功能不受影响
- 技能、文件处理等功能正常使用

---

### CoPaw vs OpenClaw

| 特性 | CoPaw | OpenClaw |
|-----|-------|----------|
| **定位** | AI 助手框架 | AI 助手框架 |
| **LLM** | 阿里云 qwen-plus | 智谱 GLM-4.7 |
| **钉钉机器人** | 两个独立实例 | dingtalk-connector 插件 |
| **Web UI** | 有独立 Console | 有独立 Web UI |
| **部署** | VPS + 本地 | 本地 systemd |
| **技能系统** | 技能驱动 | 技能驱动 |

---

## 📨 钉钉企业及应用配置信息

**整理时间**: 2026-03-05
**整理人**: CoPaw

### 企业信息
- **企业名称**: 睿墨眼镜
- **Corp ID**: ding4ef6bd48ee3dd8e4a1320dcb25e91351
- **企业 API Token**: e651c00ecdf03464825c2a008524d797

### 用户信息
- **姓名**: 王华军
- **钉钉手机号**: 13851300141
- **钉钉号**: iu7mu8u
- **用户 ID**: 193200103629107416
- **身份**: 睿墨眼镜企业成员

### 应用 1: HostingerVPS-CoPaw（当前使用）

| 配置项 | 值 |
|-------|-----|
| **Agent ID** | 4312319425 |
| **App ID** | 3c1268c1-c584-4c10-bc0a-2b382af2aa51 |
| **应用名称** | HostingerVPS-CoPaw |
| **机器人名称** | HostingerVPS-CoPaw |
| **Client ID** | dingcvagqvwxfx5w6kbf |
| **Client Secret** | GyCFe_GpNjZWR4cp5NmkRVyaisPkEBvm8anVU9lLFfVZ4yqM_l3i5buKjWnWnbGA |
| **用途** | VPS CoPaw 钉钉集成 |
| **部署位置** | Hostinger VPS (76.13.219.143:8088) |

### 应用 4: Hostinger-VPS-CoPaw（已废弃）

| 配置项 | 值 |
|-------|-----|
| **Agent ID** | 4305903062 |
| **App ID** | 550bcec1-c7c4-4369-bef4-bea9a13261ca |
| **机器人名称** | Hostinger VPS CoPaw |
| **Client ID** | dingxwnetzxyggdo6jz3 |
| **Client Secret** | V0qovsgjxvUlXjVPmPfQYKRRQ9MoJnhJyfpEqiqZFM0j2NiwH93qBusv4iyT0s_P |
| **状态** | 已废弃，已替换为 HostingerVPS-CoPaw |

### 应用 2: 王华军 openclaw

| 配置项 | 值 |
|-------|-----|
| **Agent ID** | 4291443459 |
| **App ID** | 5da43db1-8d60-4a73-8e09-3729d8e3f36a |
| **机器人名称** | 王华军 openclaw |
| **Client ID** | dingyscopnptfxm4hg8q |
| **Client Secret** | Nrh8Y7DlzCTXbkxnZEucht4sipI3iy8-LHKykYHvwjf4zM4H9zFDjRI0FKY1IVQd |
| **用途** | 本地 openclaw 钉钉集成 |
| **部署位置** | 本地电脑 |

### 应用 3: 本地的 CoPaw 的机器人

| 配置项 | 值 |
|-------|-----|
| **Agent ID** | 4291316103 |
| **App ID** | 17e303c3-954a-4e86-b095-8088f2492d30 |
| **机器人名称** | 本地的 CoPaw 的机器人 |
| **Client ID** | ding4zn6bwph8ugrgei1 |
| **Client Secret** | GAtSSvW1UzLsO4PED0q5UWdR5YVLHXsn-h3e30tmwJlcz4CCsjTGZlpawxsZjQek |
| **用途** | 本地 CoPaw 钉钉集成 |
| **部署位置** | 本地电脑 (http://127.0.0.1:8089) |

### 钉钉 API 消息格式

企业内部应用发送消息 API 格式：

```json
{
  "agent_id": 4305903062,
  "userid_list": "193200103629107416",
  "msgtype": "text",
  "msg": {
    "msgtype": "text",
    "text": {
      "content": "消息内容"
    }
  }
}
```

**⚠️ 关键点**: 必须包含 `msg` 字段，内部嵌套 `msgtype` 和 `text`

### Access Token 获取方式

**URL**: https://oapi.dingtalk.com/gettoken?appkey=CLIENT_ID&appsecret=CLIENT_SECRET

**示例（应用 1）**:
```
https://oapi.dingtalk.com/gettoken?appkey=dingcvagqvwxfx5w6kbf&appsecret=GyCFe_GpNjZWR4cp5NmkRVyaisPkEBvm8anVU9lLFfVZ4yqM_l3i5buKjWnWnbGA
```

**有效期**: 7200 秒（2 小时）

### 消息发送 API

- **URL**: https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2
- **方法**: POST
- **Content-Type**: application/json

### 重要说明

1. 企业内部应用发送的消息显示为"工作通知：[应用名称]"
2. 应用名称由钉钉开发者后台控制
3. 修改应用名称后需创建新版本并发布才生效
4. 客户端可能需要几分钟同步或重启钉钉

### 钉钉开发者后台

**网址**: https://open-dev.dingtalk.com/

**操作流程**:
1. 登录钉钉开发者后台
2. 进入对应应用
3. 修改应用名称/配置
4. 应用发布 → 版本管理与发布
5. 创建新版本 → 发布

---

## 🔧 NotebookLM 认证导出技能

### notebooklm-auth-exporter

**创建日期**: 2026-03-08
**位置**: `~/.openclaw/skills/notebooklm-auth-exporter/`
**打包文件**: `/home/admin/openclaw/workspace/notebooklm-auth-exporter.skill`

**功能**: 从 Chrome 浏览器导出 NotebookLM 认证状态，用于无头服务器自动化

**关键发现**:
- ❌ 使用 Playwright 自动化浏览器登录 Google 会被检测并拒绝
- ✅ 从真实 Chrome 浏览器导出 cookies 不被检测
- ✅ 转换为 Playwright storage_state.json 格式后可在服务器使用

**使用流程**:
```bash
# 1. 从 Chrome 导出 cookies
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# 2. 转换为 Playwright 格式
python3 ~/.openclaw/skills/notebooklm-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# 3. 部署到服务器
chmod +x /home/admin/openclaw/workspace/deploy-notebooklm-auth.sh
./deploy-notebooklm-auth.sh

# 4. 在服务器 Playwright 脚本中使用
# context = await browser.new_context(storage_state="/root/.notebooklm/storage_state.json")
```

**部署脚本**: `/home/admin/openclaw/workspace/deploy-notebooklm-auth.sh`
- 自动复制 `storage_state.json` 到 VPS (76.13.219.143)
- 验证文件是否成功传输
- 自动测试认证是否有效
- 使用 sshpass 自动化密码输入

**测试结果**:
- ✅ 本地测试：成功访问 NotebookLM (页面标题: NotebookLM)
- ✅ VPS 测试：成功访问 NotebookLM (页面标题: NotebookLM)
- ✅ Cookie 数量: 53 个
- ✅ 文件大小: 18K

**维护**:
- Cookies 有效期：约 14 天
- 需要定期重新导出和部署
- 建议设置日历提醒每周更新一次

**相关文件**:
- `~/.openclaw/skills/notebooklm-auth-exporter/SKILL.md` - 完整使用指南
- `~/.openclaw/skills/notebooklm-auth-exporter/scripts/convert_cookies.py` - 转换脚本
- `/home/admin/openclaw/workspace/deploy-notebooklm-auth.sh` - 自动部署脚本
- `/root/.notebooklm/storage_state.json` (VPS) - 当前使用的认证文件

### youtube-auth-exporter

**创建日期**: 2026-03-08
**位置**: `~/.openclaw/skills/youtube-auth-exporter/`
**打包文件**: `/home/admin/openclaw/workspace/youtube-auth-exporter.skill`

**功能**: 从 Chrome 浏览器导出 YouTube 认证状态，用于自动化下载和 Playwright 访问

**适用场景**:
- 🔒 下载年龄限制视频
- 🔒 下载私人/不公开视频
- 🎵 YouTube Music 高级内容
- 📹 需要登录才能观看的视频
- 🎬 YouTube Studio 功能访问

**支持工具**:
- ✅ yt-dlp（主要使用场景）- 认证视频下载
- ✅ Playwright - 浏览器自动化访问
- ✅ curl/wget - 命令行访问

**使用流程**:
```bash
# 1. 从 Chrome 导出 cookies
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# 2. 转换为 Playwright 格式
python3 ~/.openclaw/skills/youtube-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# 3. 转换为 Netscape 格式（用于 yt-dlp）
python3 -c "
import http.cookiejar as cj, json
state = json.load(open('/tmp/storage_state.json'))
jar = cj.MozillaCookieJar('/tmp/youtube-cookies.txt')
for cookie in state.get('cookies', []):
    c = cj.Cookie(version=0, name=cookie['name'], value=cookie['value'],
        port=None, port_specified=False, domain=cookie['domain'],
        domain_specified=True, domain_initial_dot=cookie['domain'].startswith('.'),
        path=cookie['path'], path_specified=True, secure=cookie['secure'],
        expires=cookie.get('expires', None), discard=False, comment=None,
        comment_url=None, rest={}, rfc2109=False)
    jar.set_cookie(c)
jar.save()
"

# 4. 使用 yt-dlp 下载视频
yt-dlp --cookies /tmp/youtube-cookies.txt \
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
  -o "/tmp/%(title)s.%(ext)s" \
  "https://www.youtube.com/watch?v=VIDEO_ID"
```

**与 browser-cookies-exporter 的关系**:
- browser-cookies-exporter：导出 Chrome cookies 到 Netscape 格式
- youtube-auth-exporter：转换为 Playwright 格式，提供服务器部署指南
- 两者配合使用，实现完整的认证导出流程

**维护**:
- Cookies 有效期：约 14 天
- 需要定期重新导出
- 建议设置日历提醒每周更新一次

**相关文件**:
- `~/.openclaw/skills/youtube-auth-exporter/SKILL.md` - 完整使用指南
- `~/.openclaw/skills/youtube-auth-exporter/scripts/convert_cookies.py` - 转换脚本

---

## 📝 待办事项

- [ ] VPS 带宽升级（当前速度慢）
- [ ] SSH 隧道自启动服务（systemd）
- [ ] 考虑创建 NotebookLM 相关技能
- [ ] 继续测试和优化下载工具
- [ ] 获取支持 embedding 的 API key 以启用 CoPaw Vector Search

---

**记录维护人**: openclaw ⚡
**最后更新**: 2026-03-08 04:40 (GMT+8)

## 📺 YouTube 技能配置

**配置日期**: 2026-03-12
**状态**: ✅ 完成

### 已安装工具
- **yt-dlp**: v2026.03.03 - 视频下载器（支持1000+网站）
- **browser-cookies-exporter**: 自定义 - Chrome cookies 导出工具
- **FFmpeg**: v4.4.2 - 视频处理和格式转换

### 已恢复技能包
1. **youtube-auth-exporter** - Chrome cookies 导出
2. **yt-dlp-downloader** - 综合视频下载器
3. **notebooklm-youtube-importer** - YouTube 播放列表导入 NotebookLM

### 使用指南
- 文档位置: `/home/admin/openclaw/workspace/YouTube技能使用指南.md`
- 配置报告: `/home/admin/openclaw/workspace/YouTube技能配置完成报告.md`
- 测试脚本: `/home/admin/openclaw/workspace/test-youtube-tools.sh`

## 📚 NotebookLM 技能

**配置日期**: 2026-03-12
**状态**: ✅ 技能已恢复，⚠️ VPS 认证已过期

### 已恢复技能包
1. **notebooklm** - Google NotebookLM 非官方 Python API (VPS: v0.3.3)
2. **notebooklm-youtube-importer** - YouTube 播放列表批量导入

### 部署位置
- **VPS (Hostinger)**: `/usr/local/bin/notebooklm` v0.3.3
- **技能文件**: `/home/admin/openclaw/workspace/skills/notebooklm/`
- **导入器**: `/home/admin/openclaw/workspace/skills/notebooklm-youtube-importer/`

### 使用指南
- 使用指南: `/home/admin/openclaw/workspace/NotebookLM技能使用指南.md`
- 配置报告: `/home/admin/openclaw/workspace/NotebookLM技能配置完成报告.md`
- 测试脚本: `/home/admin/openclaw/workspace/test-notebooklm-tools.sh`

### 重新认证方法
```bash
# 1. 在本地导出 Google cookies
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# 2. 转换为 Playwright 格式
python3 ~/.openclaw/skills/youtube-auth-exporter/scripts/convert_cookies.py \
  /tmp/google-cookies.txt /tmp/storage_state.json

# 3. 部署到 VPS
sshpass -p 'Whj001.Whj001' scp /tmp/storage_state.json \
  root@76.13.219.143:/root/.config/notebooklm/session.json

# 4. 验证认证
ssh root@76.13.219.143 "notebooklm list"
```

## 🔄 Cookie Format Converter 技能

**配置日期**: 2026-03-12
**状态**: ✅ 完成

**功能**: 双向 Cookie 格式转换（Netscape ↔ Playwright ↔ JSON）

**支持转换**:
- Netscape → Playwright
- Playwright → Netscape
- Netscape ↔ JSON
- Playwright ↔ JSON

**全局命令**: `cookie-converter`
**技能位置**: `/home/admin/openclaw/workspace/cookie-converter/`
**技能包**: `/home/admin/openclaw/workspace/cookie-converter.skill`

**使用指南**: `/home/admin/openclaw/workspace/Cookie Converter使用指南.md`
**配置报告**: `/home/admin/openclaw/workspace/Cookie Converter配置完成报告.md`

## 🔗 Cookie 相关技能整合

**创建日期**: 2026-03-12
**状态**: ✅ 所有技能已整合并交叉引用

**技能列表**:
- browser-cookies-exporter - Chrome/Firefox/Brave/Edge cookies 导出
- youtube-auth-exporter - YouTube/Google 认证导出
- notebooklm-auth-exporter - NotebookLM 认证导出
- cookie-converter - Cookie 格式双向转换
- yt-dlp-downloader - 视频下载（支持 cookies）

**总览文档**: `/home/admin/openclaw/workspace/Cookie相关技能总览.md`

**整合内容**:
- ✅ 所有技能文档已添加交叉引用
- ✅ 技能关系图和工作流示例
- ✅ 命令速查和对比表格
- ✅ 安全提醒和使用建议

## 🚀 GitHub 备份（2026-03-12）

**仓库地址**: https://github.com/169068671/openclaw-backup
**推送方式**: VPS SSH 密钥
**状态**: ✅ 成功推送
**推送时间**: 2026-03-12 13:45 GMT+8

**推送的提交**:
- f8f2897: docs: Add GitHub upload status report
- 5284634: docs: Add GitHub upload guide and push helper script
- 7db526b: feat: Add Cookie Format Converter skill and YouTube/NotebookLM skills
- cb95e99: 添加 2026-03-02 工作日志
- e021dd4: 完成今日所有配置

**VPS SSH 密钥**:
- 密钥类型: ed25519
- 公钥: /root/.ssh/id_ed25519.pub
- 邮箱: 169068671@qq.com
- 状态: ✅ 已添加到 GitHub

**推送统计**:
- 5 个提交
- 69 个文件
- 18,418 行新增

## 📦 GitHub CLI (gh) 安装（2026-03-12）

**版本**: 2.88.1
**安装日期**: 2026-03-12
**位置**: /usr/bin/gh

**安装方式**:
- 使用官方 APT 仓库
- 添加 GitHub CLI GPG key
- 添加 GitHub CLI 仓库源
- sudo apt install gh -y

**状态**: ✅ 已安装，等待认证

---

## 🐛 DingTalk 消息去重修复（2026-03-13）

**问题**: 钉钉插件只能处理第一个消息，后续消息被标记为"重复"而跳过

**原因分析**:
1. 消息去重函数参数不匹配
   - 函数定义：`isMessageProcessed(messageId: string)` 只接受一个参数
   - 函数调用：`isMessageProcessed(account.accountId, messageId)` 传入两个参数
   - 导致第二个参数被忽略，去重逻辑失效

2. AI 模型响应超时
   - GLM-4.7 模型响应超时
   - 钉钉插件立即确认了消息
   - 钉钉平台自动重试发送相同消息
   - 由于去重逻辑失效，被误判为新消息并标记为"重复"

**修复内容**:
修改 `~/.openclaw/extensions/dingtalk-connector/plugin.ts`

```typescript
// 修复前
function isMessageProcessed(messageId: string): boolean {
  if (!messageId) return false;
  return processedMessages.has(messageId);
}

function markMessageProcessed(messageId: string): void {
  if (!messageId) return;
  processedMessages.set(messageId, Date.now());
  // ...
}

// 修复后
function isMessageProcessed(accountId: string, messageId: string): boolean {
  if (!accountId || !messageId) return false;
  const key = `${accountId}:${messageId}`;
  return processedMessages.has(key);
}

function markMessageProcessed(accountId: string, messageId: string): void {
  if (!accountId || !messageId) return;
  const key = `${accountId}:${messageId}`;
  processedMessages.set(key, Date.now());
  // ...
}
```

**修复结果**:
- ✅ 支持账号维度隔离（不同账号的消息不会互相冲突）
- ✅ 消息去重逻辑正确工作
- ✅ 可以连续发送多个消息，都能正常处理

**测试验证**:
- Gateway 重启：PID 37160（02:36 启动）
- 钉钉 Stream：✅ 已连接
- 消息测试：✅ 连续消息处理正常

**Git 提交**:
- 提交 ID: 0be94ed
- 时间: 2026-03-13 02:43 GMT+8
- 分支: master

---

**记录维护人**: openclaw ⚡
**最后更新**: 2026-03-13 02:43 (GMT+8)
