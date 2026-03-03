# TOOLS.md - Local Notes

## 🚨 最高优先级规则

**重要**：所有操作必须遵守 `RULES.md` 中的规则：
- **第一规则：永不断开连接** - 每次更改后都要测试连接
- **第二规则：操作前备份** - 重要操作前必须创建备份

**测试连接**：
```bash
# OpenClaw 服务
systemctl status openclaw-gateway

# 网络连接
ping -c 3 8.8.8.8
curl -I https://github.com

# Git 仓库
cd /home/admin/openclaw/workspace && git status
```

详见：`RULES.md` - 这是绝对不能违反的铁律

---

## 备份信息

- **工作空间备份：** `/home/admin/backups/workspace-backup-20260302-132648.tar.gz` (49K)
- **Git 仓库：** `/home/admin/openclaw/workspace/.git` (初始提交: cfd8d95)
- **备份策略：** 重要操作前创建新备份，Git 保存历史版本

## Hostinger VPS

- **地址：** 76.13.219.143
- **主机名：** srv1437164
- **用户：** root
- **密码：** Whj001.Whj001
- **连接命令：** `sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143`
- **状态：** ✅ SSH 连接正常 (2026-03-02 22:54)
- **Guacamole：** ✅ 已部署，http://76.13.219.143:8081/guacamole
- **Docker Compose：** ✅ 已安装
- **MySQL：** ✅ 运行中（3306 端口）
- **Guacamole Daemon：** ✅ 运行中（4822 端口）
- **Guacamole Web：** ✅ 运行中（8081:8080 端口）

## HTTP 代理配置

- **推荐方案：** SSH 隧道（SOCKS5）- 更稳定 ⭐
- **替代方案：** Tinyproxy (HTTP) - 有时不稳定
- **文档：** `SSH隧道代理方案.md`
- **Tinyproxy 文档：** `HTTP代理配置方案-HostingerVPS.md`
- **状态：** Tinyproxy HTTPS 不稳定，推荐使用 SSH 隧道

### 推荐方案：直连（全局规则）⭐

**测试结果（2026-03-03 15:30）**：

| 访问类型 | 直连 | SSH隧道 | 结论 |
|---------|------|---------|------|
| GitHub HTTPS | 0.35s | 1.09s | 直连快3倍 ✅ |
| GitHub SSH | 3.09s | 4.56s | 直连快1.5倍 ✅ |
| Git Fetch | 4.00s | 5.84s | 直连快1.5倍 ✅ |

**全局规则**：
- ✅ GitHub访问（HTTP/SSH）：使用直连
- ✅ Git操作（push/pull/clone）：使用直连
- ✅ 国内网站：使用直连

**备用方案：SSH 隧道（SOCKS5）**

仅在直连失败或访问其他被限制的国外网站时使用。

**启动方法：**
```bash
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143
```

**浏览器配置：**
- Chrome/Edge → 设置 → 系统 → 代理
- SOCKS 主机：`127.0.0.1`，端口：`1080`

**详细文档：** `SSH隧道代理方案.md`

### 替代方案：Tinyproxy（HTTP）⚠️

**配置：**
- 代理服务器：76.13.219.143:8888
- 类型：HTTP 代理
- PAC 文件：`/opt/proxy.pac`

**问题：**
- ❌ HTTPS 代理连接不稳定
- ❌ 容易超时
- ⚠️ 不推荐使用

**Tinyproxy 配置（最新）：**
```conf
Port 8888
Listen 0.0.0.0
Allow 0.0.0.0/0
```

**测试结果（2026-03-02 14:25）：**
- HTTP 访问：✅ 成功
- HTTPS 访问：❌ 不稳定（经常超时）
- 国内网站：✅ 直连
- OpenClaw：✅ 直连

## 钉钉通道配置

- **插件名称：** dingtalk-connector
- **版本：** 0.6.0
- **状态：** ✅ 已安装并加载
- **配置文件：** `~/.openclaw/openclaw.json`
- **文档：** `钉钉通道配置指南.md`
- **完成报告：** `钉钉通道配置完成报告.md`
- **状态：** ✅ 双向通信测试成功

### 配置详情

1. **钉钉应用信息**
   - Client ID (AppKey): dingyscopnptfxm4hg8q
   - Client Secret: 已配置
   - Gateway Token: 已配置
   - 消息接收模式: Stream 模式
   - 应用状态: ✅ 已发布

2. **必需权限**
   - Card.Streaming.Write ✅
   - Card.Instance.Write ✅
   - qyapi_robot_sendmsg ✅

3. **功能特性**
   - AI Card 流式响应 ✅
   - 会话持久化（30分钟超时）✅
   - 双向通信 ✅
   - 图片自动上传
   - 支持会话命令：/new, /reset, /clear, 新会话, 重新开始, 清空对话

4. **测试结果**
   - 接收消息（钉钉→OpenClaw）：✅ 测试成功 (2026-03-02 14:04)
   - 主动发送（OpenClaw→钉钉）：✅ 测试成功 (2026-03-02 14:07)
   - 测试用户ID：193200103629107416

---

## res-downloader（视频号/抖音下载器）

- **项目名称：** res-downloader
- **作者：** putyy
- **GitHub：** https://github.com/putyy/res-downloader
- **GitHub Stars：** 15,543 ⭐⭐⭐⭐⭐
- **状态：** ✅ 已编译
- **编译日期：** 2026-03-03 19:47
- **可执行文件：** `/home/admin/openclaw/workspace/res-downloader/build/bin/res-downloader`
- **文件大小：** 18M
- **编译时间：** 1分28秒

### 功能特性

| 功能 | 支持 |
|-----|------|
| 微信视频号 | ✅ |
| 小程序 | ✅ |
| 抖音 | ✅ |
| 快手 | ✅ |
| 小红书 | ✅ |
| m3u8 | ✅ |
| 直播流 | ✅ |
| 酷狗音乐 | ✅ |
| QQ音乐 | ✅ |
| 代理抓包 | ✅ |

### 运行方法

```bash
# 进入项目目录
cd /home/admin/openclaw/workspace/res-downloader

# 运行可执行文件
./build/bin/res-downloader
```

### 使用步骤

1. **启动程序**：运行 `./build/bin/res-downloader`
2. **启动代理**：首页左上角点击"启动代理"
3. **选择资源类型**：默认全部
4. **获取资源**：在外部打开资源页面（视频号、小程序、网页等）
5. **查看资源**：返回软件首页，即可看到资源列表

### 编译环境

| 依赖 | 版本 |
|-----|------|
| Go | 1.22.0 |
| Wails CLI | 2.11.0 |
| Node.js | v24.14.0 |
| npm | 11.9.0 |
| pkg-config | 0.29.2 |
| libwebkit2gtk-4.1-dev | 2.50.4 |

### 项目位置

- **源代码：** `/home/admin/openclaw/workspace/res-downloader/`
- **可执行文件：** `/home/admin/openclaw/workspace/res-downloader/build/bin/res-downloader`
- **编译记录：** `res-downloader-编译记录.md`、`res-downloader-编译记录-完成.md`

---

## 下载工具总览

| 工具 | 类型 | 功能 | 安装状态 | 位置 |
|-----|------|------|---------|------|
| **yutto** | 视频 | Bilibili 专用 | ✅ 2.1.1 | ~/.local/bin/yutto |
| **yt-dlp** | 视频 | 综合下载（1000+网站） | ✅ 2026.02.21 | ~/.local/bin/yt-dlp |
| **musicdl** | 音乐 | 音乐/有声读物（50+平台） | ✅ 2.9.7 | ~/.local/bin/musicdl |
| **res-downloader** | 视频/音频 | 视频号/抖音/小红书等 | ✅ 已编译 | build/bin/res-downloader |

### 推荐使用

- **Bilibili 下载**：yutto（专用，更稳定）
- **综合视频下载**：yt-dlp（支持1000+网站）
- **音乐/有声读物**：musicdl（50+音乐平台）
- **微信视频号/抖音/小红书**：res-downloader（桌面应用，代理抓包）
