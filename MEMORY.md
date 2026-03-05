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
- **Client ID**: dingxwnetzxyggdo6jz3
- **Client Secret**: 已配置
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

### 应用 1: Hostinger-VPS-CoPaw

| 配置项 | 值 |
|-------|-----|
| **Agent ID** | 4305903062 |
| **App ID** | 550bcec1-c7c4-4369-bef4-bea9a13261ca |
| **机器人名称** | Hostinger VPS CoPaw |
| **Client ID** | dingxwnetzxyggdo6jz3 |
| **Client Secret** | V0qovsgjxvUlXjVPmPfQYKRRQ9MoJnhJyfpEqiqZFM0j2NiwH93qBusv4iyT0s_P |
| **用途** | VPS CoPaw 钉钉集成 |
| **部署位置** | Hostinger VPS (76.13.219.143:8088) |

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
https://oapi.dingtalk.com/gettoken?appkey=dingxwnetzxyggdo6jz3&appsecret=V0qovsgjxvUlXjVPmPfQYKRRQ9MoJnhJyfpEqiqZFM0j2NiwH93qBusv4iyT0s_P
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

## 📝 待办事项

- [ ] VPS 带宽升级（当前速度慢）
- [ ] SSH 隧道自启动服务（systemd）
- [ ] 考虑创建 NotebookLM 相关技能
- [ ] 继续测试和优化下载工具
- [ ] 获取支持 embedding 的 API key 以启用 CoPaw Vector Search

---

**记录维护人**: openclaw ⚡
**最后更新**: 2026-03-05 18:42 (GMT+8)
