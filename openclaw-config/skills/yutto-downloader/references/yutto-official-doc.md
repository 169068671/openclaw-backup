# Yutto 官方文档参考

> 基于 https://yutto.nyakku.moe/ 和 https://github.com/yutto-dev/yutto

---

## 基本用法

### 下载单个视频

```bash
yutto https://www.bilibili.com/video/BV1xxxxx/
```

### 下载番剧

```bash
yutto https://www.bilibili.com/bangumi/play/ep123456
```

### 使用大会员下载

```bash
yutto --sessdata YOUR_SESSDATA https://www.bilibili.com/video/BV1xxxxx/
```

---

## 命令行选项

### 主要选项

| 选项 | 简写 | 说明 | 示例 |
|-----|------|------|------|
| --quality | -q | 视频质量 | --quality 1080 |
| --codec | -c | 视频编码 | --codec hevc |
| --sessdata | - | Bilibili SESSDATA | --sessdata xxx |
| --download-dir | -d | 下载目录 | --download-dir ./videos |
| --with-danmaku | - | 下载弹幕 | --with-danmaku |
| --download-only-audio | - | 仅下载音频 | --download-only-audio |
| --overwrite | - | 覆盖已存在文件 | --overwrite |

### 视频质量

- `auto` - 自动选择（默认）
- `1080` - 1080P 高清
- `720` - 720P 准高清
- `480` - 480P 标清
- `360` - 360P 流畅

### 视频编码

- `auto` - 自动选择（默认）
- `hevc` - H.265 编码
- `avc` - H.264 编码
- `av1` - AV1 编码

---

## 配置文件

### 配置文件位置

- Linux/macOS: `~/.config/yutto/yutto.toml`
- Windows: `%APPDATA%\yutto\yutto.toml`

### 配置示例

```toml
[bilibili]
# Bilibili SESSDATA（用于大会员内容）
sessdata = "YOUR_SESSDATA"

# 下载目录
download_dir = "./downloads"

# 视频质量（auto, 1080, 720, 480, 360）
quality = "auto"

# 视频编码（auto, hevc, avc, av1）
codec = "auto"

# 是否下载弹幕
with_danmaku = false

# 是否仅下载音频
download_only_audio = false

# 是否覆盖已存在文件
overwrite = false
```

---

## 下载格式

### 单个视频

```
https://www.bilibili.com/video/BV1xxxxx/
```

### 番剧/剧集

```
https://www.bilibili.com/bangumi/play/ep123456
```

### 合集/收藏夹

```
https://space.bilibili.com/channel/collectiondetail?sid=xxxxx
https://space.bilibili.com/channel/favlist?fid=xxxxx
```

### 投稿合集

```
https://www.bilibili.com/medialist/play/xxxxx?business=space_collection
```

---

## 视频流信息

### 输出示例

```
INFO 共包含以下 15 个视频流：
INFO * 0 [AVC ] [1920x1080] <1080P 高码率> #3
INFO * 1 [HEVC] [1920x1080] <1080P 高码率> #3
INFO * 2 [AV1 ] [1920x1080] <1080P 高码率> #3
INFO * 3 [AVC ] [1920x1080] <1080P 高清> #3
INFO * 4 [HEVC] [1920x1080] <1080P 高清> #3
INFO * 5 [AV1 ] [1920x1080] <1080P 高清> #3
INFO * 6 [AVC ] [1280x720 ] <720P 准高清> #3
INFO * 7 [HEVC] [1280x720 ] <720P 准高清> #3
INFO * 8 [AV1 ] [1280x720 ] <720P 准高清> #3
```

### 音频流示例

```
INFO 共包含以下 3 个音频流：
INFO * 0 [MP4A] <320kbps >
INFO * 1 [MP4A] <64kbps >
INFO * 2 [MP4A] <128kbps >
```

---

## 弹幕

### 弹幕格式

- 下载格式：ASS (Advanced Substation Alpha)
- 文件名：`{视频标题}.zh-CN.ass`

### 弹幕设置

```bash
# 下载弹幕
yutto --with-danmaku https://www.bilibili.com/video/BV1xxxxx/
```

---

## 进度显示

下载过程中会显示进度条：

```
INFO 开始下载……
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━ 49.25 MiB/ 54.30 MiB 32.22 MiB/⚡
```

---

## 常见问题

### Q: 为什么只能下载低质量视频？

A: 需要登录 Bilibili 账号并配置 SESSDATA 才能下载高质量视频。

### Q: 如何获取 SESSDATA？

A:
1. 登录 Bilibili 网页版
2. 按 F12 打开开发者工具
3. 进入 Application → Cookies
4. 找到 SESSDATA 并复制

### Q: 下载失败怎么办？

A:
1. 检查网络连接
2. 验证 URL 是否正确
3. 确认视频是否可用
4. 尝试使用 SESSDATA

### Q: 视频无法播放？

A:
1. 确认视频编码是否支持
2. 尝试不同的编码格式（avc, hevc）
3. 检查播放器是否支持该格式

---

## 更多信息

- **官方文档**: https://yutto.nyakku.moe/
- **GitHub 仓库**: https://github.com/yutto-dev/yutto
- **PyPI**: https://pypi.org/project/yutto/
- **问题反馈**: https://github.com/yutto-dev/yutto/issues
