# Musicdl Downloader 技能

> 技能创建日期：2026-03-03
> 基于 musicdl 开源项目：https://github.com/CharlesPikachu/musicdl

---

## 📋 技能概述

**技能名称**：musicdl-downloader
**技能类型**：音乐下载器
**开源项目**：musicdl - 轻量级无损音乐下载器
**GitHub Stars**：未标明（活跃项目）
**状态**：✅ 已打包并提交

---

## 🎯 功能特性

### 核心功能
- ✅ 支持50+音乐/有声读物平台
- ✅ 搜索和下载单曲
- ✅ 搜索和下载歌单
- ✅ 搜索和下载专辑
- ✅ 支持无损音质
- ✅ 支持歌词下载
- ✅ 纯 Python 实现
- ✅ 轻量级设计

### 支持的平台

**国内音乐平台**：
- 网易云音乐（无损）
- QQ音乐
- 酷狗音乐
- 酷我音乐
- 咪咕音乐

**国际音乐平台**：
- YouTube
- Spotify
- Apple Music
- TIDAL
- Qobuz（无损）
- SoundCloud
- Joox

**有声读物平台**：
- 喜马拉雅
- 懒人听书
- 蜻蜓FM
- 蜻蜓FM

---

## 📦 技能结构

```
musicdl-downloader/
├── SKILL.md                              # 技能主文档
├── scripts/
│   └── install_musicdl.sh                # 自动安装脚本
├── references/
│   ├── musicdl-platforms.md              # 完整平台列表
│   └── musicdl-official-doc.md           # 官方文档参考
└── assets/
    └── musicdl_config.json               # 配置文件模板
```

---

## 📄 文件说明

### SKILL.md

技能主文档，包含：
- 快速开始指南
- 安装方法（pip, 源码）
- 平台列表和特性
- 常见任务示例
- 命令行参数
- 配置文件说明

### scripts/install_musicdl.sh

自动安装脚本，支持：
1. pip 安装（推荐）
2. 源码安装
3. 最新版本安装

### references/musicdl-platforms.md

完整平台列表，包含：
- 国内音乐平台详细信息
- 国际音乐平台详细信息
- 有声读物平台详细信息
- 平台代码和使用示例

### references/musicdl-official-doc.md

官方文档参考，包含：
- 基本用法
- 命令行选项完整列表
- 平台选项
- 音质选项
- 高级用法示例
- 常见问题解答

### assets/musicdl_config.json

配置文件模板，包含：
- 平台设置
- 音质选择
- 输出目录
- 下载选项

---

## 🚀 快速开始

### 1. 安装 musicdl

```bash
# 使用 pip（推荐）
pip install musicdl

# 或使用技能提供的安装脚本
bash /path/to/musicdl-downloader/scripts/install_musicdl.sh
```

### 2. 下载音乐

```bash
# 搜索并下载单曲
musicdl 稻香

# 搜索并下载歌单
musicdl -p 流行歌

# 搜索并下载专辑
musicdl -a 情歌
```

---

## 📚 使用示例

### 国内音乐

```bash
# 网易云音乐（无损）
musicdl 稻香 -p netease -q lossless

# QQ音乐
musicdl 光辉岁月 -p qq

# 酷狗音乐
musicdl 歌曲 -p kugou
```

### 国际音乐

```bash
# YouTube
musicdl song -p youtube

# Spotify
musicdl song -p spotify

# Apple Music
musicdl song -p apple
```

### 有声读物

```bash
# 喜马拉雅
musicdl 有声书 -p ximalaya

# 懒人听书
musicdl 小说 -p lazy
```

---

## 🎛️ 常用命令选项

| 选项 | 简写 | 说明 | 示例 |
|-----|------|------|------|
| --platform | -p | 指定平台 | -p netease |
| --quality | -q | 音质选择 | -q lossless |
| --output | -o | 输出目录 | -o ./downloads |
| --playlist | - | 搜索歌单 | -p |
| --album | -a | 搜索专辑 | -a |
| --limit | - | 下载限制 | --limit 10 |

---

## 🔧 平台代码

| 平台 | 代码 | 类型 |
|-----|------|------|
| NetEase Cloud Music | netease | 国内音乐 |
| QQ Music | qq | 国内音乐 |
| Kugou Music | kugou | 国内音乐 |
| Kuwo Music | kuwo | 国内音乐 |
| Migu Music | migu | 国内音乐 |
| Bilibili | bilibili | 视频平台 |
| YouTube | youtube | 国际音乐 |
| Spotify | spotify | 国际音乐 |
| Apple Music | apple | 国际音乐 |
| TIDAL | tidal | 国际音乐 |
| Qobuz | qobuz | 国际音乐（无损） |
| SoundCloud | soundcloud | 国际音乐 |
| Joox | joox | 国际音乐 |
| Ximalaya | ximalaya | 有声读物 |
| Lazy Audio | lazy | 有声读物 |
| Litchi FM | litchi | 有声读物 |
| Qingting FM | qingting | 有声读物 |

---

## 💡 使用建议

### 国内音乐
**推荐平台**：
- ✅ 网易云音乐：支持无损，歌单丰富
- ✅ QQ音乐：歌单丰富，品质好
- ✅ 酷狗/酷我：搜索准确

### 国际音乐
**推荐平台**：
- ✅ YouTube：视频转音频
- ✅ Spotify：全球最大音乐平台
- ✅ Apple Music：苹果生态

### 有声读物
**推荐平台**：
- ✅ 喜马拉雅：最大有声平台
- ✅ 懒人听书：小说丰富
- ✅ 蜻蜓FM：播客聚合

---

## 📝 技能创建记录

| 日期 | 操作 | 备注 |
|------|------|------|
| 2026-03-03 16:35 | 初始化技能 | 创建技能目录结构 |
| 2026-03-03 16:35 | 编写 SKILL.md | 完整的使用指南 |
| 2026-03-03 16:35 | 创建安装脚本 | 支持 pip, 源码安装 |
| 2026-03-03 16:35 | 创建参考文档 | 平台列表和官方文档 |
| 2026-03-03 16:35 | 创建配置模板 | JSON 配置文件 |
| 2026-03-03 16:35 | 打包技能 | 生成 .skill 文件 |
| 2026-03-03 16:35 | 安装 musicdl | 版本 2.9.7 |
| 2026-03-03 16:35 | 提交到 Git | 保存到 openclaw-backup |

---

## ✅ 验证状态

- [x] 技能结构完整
- [x] SKILL.md 文档完整
- [x] 安装脚本可执行
- [x] 参考文档齐全
- [x] 配置模板正确
- [x] 技能打包成功
- [x] musicdl 已安装（版本 2.9.7）
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

## 🆚 与其他技能对比

| 特性 | musicdl-downloader | yt-dlp-downloader | yutto-downloader |
|-----|------------------|------------------|-----------------|
| 支持类型 | 音乐/有声读物 | 视频/音频 | 视频 |
| 支持平台 | 50+ | 1000+ | 仅 Bilibili |
| 音质 | 无损支持 | 多种 | 多种 |
| 推荐场景 | 音乐下载 | 综合下载 | Bilibili 专用 |

---

## ⚠️ 法律声明

**重要**：此工具仅用于教育研究目的

- ❌ 禁止商业用途
- ✅ 尊重各平台版权和条款
- ✅ 仅限个人使用
- ❌ 禁止重新分发下载内容

---

**技能文件**：`musicdl-downloader.skill`
**GitHub 提交**：888ed43
**仓库地址**：https://github.com/169068671/openclaw-backup

---

## 📌 安装技能

**方式1：手动安装**
```bash
# 复制技能文件到 OpenClaw skills 目录
cp musicdl-downloader.skill ~/.openclaw/skills/
```

**方式2：OpenClaw 自动识别**
- 将 .skill 文件放在技能目录
- OpenClaw 会自动加载

---

**技能创建完成！** ✅

现在你可以使用这个技能下载音乐和有声读物了！🎵
