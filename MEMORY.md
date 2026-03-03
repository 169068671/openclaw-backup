# MEMORY.md - 长期记忆

最后更新: 2026-03-04 03:16

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

## 📝 待办事项

- [ ] VPS 带宽升级（当前速度慢）
- [ ] SSH 隧道自启动服务（systemd）
- [ ] 考虑创建 NotebookLM 相关技能
- [ ] 继续测试和优化下载工具

---

**记录维护人**: openclaw ⚡
**最后更新**: 2026-03-04 03:16 (GMT+8)
