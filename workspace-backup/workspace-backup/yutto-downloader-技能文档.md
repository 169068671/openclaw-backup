# Yutto Downloader 技能

> 技能创建日期：2026-03-03
> 基于 yutto 开源项目：https://github.com/yutto-dev/yutto

---

## 📋 技能概述

**技能名称**：yutto-downloader
**技能类型**：视频下载工具
**开源项目**：yutto - Bilibili 视频下载器
**GitHub Stars**：1.7k ⭐
**状态**：✅ 已打包并提交

---

## 🎯 功能特性

### 核心功能
- ✅ 下载 Bilibili 投稿视频
- ✅ 下载番剧/电视剧
- ✅ 下载课程/教程
- ✅ 下载收藏夹和合集
- ✅ 支持批量下载
- ✅ 下载弹幕（ASS 格式）
- ✅ 支持大会员认证

### 视频质量支持
- 1080P 高清（需要大会员）
- 720P 准高清
- 480P 标清
- 360P 流畅

### 视频编码支持
- HEVC (H.265)
- AVC (H.264)
- AV1

---

## 📦 技能结构

```
yutto-downloader/
├── SKILL.md                              # 技能主文档
├── scripts/
│   └── install_yutto.sh                  # 自动安装脚本
├── references/
│   ├── yutto-official-doc.md              # 官方文档参考
│   └── bilibili-url-guide.md              # Bilibili URL 格式指南
└── assets/
    └── yutto.toml                       # 配置文件模板
```

---

## 📄 文件说明

### SKILL.md

技能主文档，包含：
- 快速开始指南
- 安装方法（pip, Homebrew, 源码）
- 配置说明
- 常见任务示例
- 命令行参数
- 故障排查

### scripts/install_yutto.sh

自动安装脚本，支持：
1. pip 安装（推荐）
2. Homebrew 安装（macOS）
3. 源码安装

使用方法：
```bash
chmod +x scripts/install_yutto.sh
bash scripts/install_yutto.sh
```

### references/yutto-official-doc.md

官方文档参考，包含：
- 基本用法
- 命令行选项完整列表
- 配置文件详细说明
- 下载格式说明
- 常见问题解答

### references/bilibili-url-guide.md

Bilibili URL 格式指南，包含：
- 投稿视频 URL
- 番剧/电视剧 URL
- 课程/教程 URL
- 收藏夹和合集 URL
- 如何获取 URL
- URL 验证方法

### assets/yutto.toml

配置文件模板，包含：
- SESSDATA 配置
- 下载目录设置
- 视频质量和编码选择
- 弹幕和音频下载选项

---

## 🚀 快速开始

### 1. 安装 yutto

```bash
# 使用 pip（推荐）
pip install yutto

# 或使用技能提供的安装脚本
bash /path/to/yutto-downloader/scripts/install_yutto.sh
```

### 2. 配置（可选）

```bash
# 复制配置模板
cp /path/to/yutto.toml ~/.config/yutto/yutto.toml

# 编辑配置文件，添加 SESSDATA
nano ~/.config/yutto/yutto.toml
```

### 3. 下载视频

```bash
# 下载单个视频
yutto https://www.bilibili.com/video/BV1xxxxx/

# 下载番剧
yutto https://www.bilibili.com/bangumi/play/ep123456

# 带弹幕下载
yutto --with-danmaku https://www.bilibili.com/video/BV1xxxxx/

# 选择 1080P HEVC
yutto --quality 1080 --codec hevc https://www.bilibili.com/video/BV1xxxxx/
```

---

## 📚 使用示例

### 下载单个视频

```bash
yutto https://www.bilibili.com/video/BV1CTMHziEaB/
```

### 下载番剧

```bash
yutto https://www.bilibili.com/bangumi/play/ep123456
```

### 下载收藏夹

```bash
yutto https://space.bilibili.com/channel/favlist?fid=987654
```

### 下载合集

```bash
yutto https://space.bilibili.com/channel/collectiondetail?sid=123456789
```

### 批量下载

```bash
# 创建 URL 列表
cat > urls.txt << EOF
https://www.bilibili.com/video/BV1xxxxx/
https://www.bilibili.com/video/BV1yyyyy/
https://www.bilibili.com/video/BV1zzzzz/
EOF

# 批量下载
cat urls.txt | xargs -I {} yutto {}
```

---

## 🎛️ 常用命令选项

| 选项 | 说明 | 示例 |
|-----|------|------|
| `-q, --quality` | 视频质量 | `--quality 1080` |
| `-c, --codec` | 视频编码 | `--codec hevc` |
| `--sessdata` | SESSDATA | `--sessdata xxx` |
| `-d, --download-dir` | 下载目录 | `--download-dir ./videos` |
| `--with-danmaku` | 下载弹幕 | `--with-danmaku` |
| `--download-only-audio` | 仅下载音频 | `--download-only-audio` |
| `--overwrite` | 覆盖文件 | `--overwrite` |

---

## 🔧 配置文件示例

```toml
[bilibili]
# SESSDATA（大会员认证）
sessdata = "YOUR_SESSDATA"

# 下载目录
download_dir = "./downloads"

# 视频质量
quality = "auto"

# 视频编码
codec = "auto"

# 下载弹幕
with_danmaku = true

# 覆盖已存在文件
overwrite = false
```

---

## ❓ 常见问题

### Q: 如何获取 SESSDATA？

A:
1. 登录 Bilibili 网页版
2. 按 F12 打开开发者工具
3. 进入 Application → Cookies
4. 找到 SESSDATA 并复制

### Q: 为什么只能下载低质量视频？

A: 需要登录 Bilibili 账号并配置 SESSDATA 才能下载高质量视频。

### Q: 下载失败怎么办？

A:
1. 检查网络连接
2. 验证 URL 是否正确
3. 确认视频是否可用
4. 尝试使用 SESSDATA

### Q: 如何下载整个番剧？

A:
1. 使用番剧的 `md` ID：`https://www.bilibili.com/bangumi/media/md{id}/`
2. 或者逐个下载每一集

---

## 📞 参考资料

- **yutto 官方文档**：https://yutto.nyakku.moe/
- **GitHub 仓库**：https://github.com/yutto-dev/yutto
- **PyPI**：https://pypi.org/project/yutto/
- **技能文档**：参考技能中的 references/ 目录

---

## 📝 技能创建记录

| 日期 | 操作 | 备注 |
|------|------|------|
| 2026-03-03 16:00 | 初始化技能 | 创建技能目录结构 |
| 2026-03-03 16:00 | 编写 SKILL.md | 完整的使用指南 |
| 2026-03-03 16:00 | 创建安装脚本 | 支持 pip, Homebrew, 源码安装 |
| 2026-03-03 16:00 | 创建参考文档 | 官方文档和 URL 指南 |
| 2026-03-03 16:00 | 创建配置模板 | yutto.toml 配置文件 |
| 2026-03-03 16:00 | 打包技能 | 生成 .skill 文件 |
| 2026-03-03 16:00 | 提交到 Git | 保存到 openclaw-backup |

---

## ✅ 验证状态

- [x] 技能结构完整
- [x] SKILL.md 文档完整
- [x] 安装脚本可执行
- [x] 参考文档齐全
- [x] 配置模板正确
- [x] 技能打包成功
- [x] 已提交到 GitHub

---

## 🎓 技能设计原则

遵循 skill-creator 规范：

1. **简洁为主**：仅包含必要信息
2. **渐进式披露**：metadata → SKILL.md → references
3. **分层组织**：scripts, references, assets 分离
4. **实用导向**：提供具体示例和常见用例
5. **资源优化**：脚本可执行，参考按需加载

---

**技能文件**：`yutto-downloader.skill`
**GitHub 提交**：087fba9
**仓库地址**：https://github.com/169068671/openclaw-backup

---

## 📌 安装技能

**方式1：手动安装**
```bash
# 复制技能文件到 OpenClaw skills 目录
cp yutto-downloader.skill ~/.openclaw/skills/
```

**方式2：OpenClaw 自动识别**
- 将 .skill 文件放在技能目录
- OpenClaw 会自动加载

---

**技能创建完成！** ✅
