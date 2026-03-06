# Musicdl 官方文档参考

> 基于 https://github.com/CharlesPikachu/musicdl

---

## 基本用法

### 搜索并下载单曲

```bash
musicdl <song_name>
```

### 搜索并下载歌单

```bash
musicdl -p <playlist_name>
```

### 搜索并下载专辑

```bash
musicdl -a <album_name>
```

---

## 命令行选项

### 主要选项

| 选项 | 简写 | 说明 | 示例 |
|-----|------|------|------|
| --help | -h | 显示帮助 | -h |
| --version | -v | 显示版本 | -v |
| --platform | -p | 指定平台 | -p netease |
| --quality | -q | 音质选择 | -q 320 |
| --output | -o | 输出目录 | -o ./downloads |
| --playlist | - | 搜索歌单 | -p |
| --album | -a | 搜索专辑 | -a |
| --limit | - | 下载限制 | --limit 10 |

---

## 平台选项

### 国内音乐平台

| 平台 | 代码 | 说明 |
|-----|------|------|
| NetEase Cloud Music | netease | 网易云音乐 |
| QQ Music | qq | QQ音乐 |
| Kugou Music | kugou | 酷狗音乐 |
| Kuwo Music | kuwo | 酷我音乐 |
| Migu Music | migu | 咪咕音乐 |

### 国际音乐平台

| 平台 | 代码 | 说明 |
|-----|------|------|
| YouTube | youtube | YouTube音乐 |
| Spotify | spotify | Spotify |
| Apple Music | apple | Apple Music |
| TIDAL | tidal | TIDAL |
| Qobuz | qobuz | Qobuz（无损） |
| SoundCloud | soundcloud | SoundCloud |
| Joox | joox | Joox |

### 有声读物平台

| 平台 | 代码 | 说明 |
|-----|------|------|
| Ximalaya | ximalaya | 喜马拉雅 |
| Lazy Audio | lazy | 懒人听书 |
| Litchi FM | litchi | 蜻蜓FM |
| Qingting FM | qingting | 蜻蜓FM |

---

## 音质选项

### 音质等级

| 音质 | 说明 | 比特率 |
|-----|------|---------|
| lossless | 无损 | 平台相关 |
| 320 | 高品质 | 320kbps |
| 192 | 中品质 | 192kbps |
| 128 | 标准品质 | 128kbps |

### 使用示例

```bash
# 无损音质
musicdl 歌曲 -q lossless

# 320kbps
musicdl 歌曲 -q 320

# 192kbps
musicdl 歌曲 -q 192
```

---

## 使用示例

### 网易云音乐

```bash
# 搜索并下载
musicdl 稻香 -p netease

# 指定音质
musicdl 稻香 -p netease -q lossless

# 下载歌单
musicdl -p 流行歌 -p netease
```

### QQ音乐

```bash
# 搜索并下载
musicdl 光辉岁月 -p qq

# 下载专辑
musicdl -a 情歌 -p qq
```

### Bilibili

```bash
# 搜索并下载
musicdl 哔哩哩哩之歌 -p bilibili
```

### YouTube

```bash
# 搜索并下载
musicdl song -p youtube
```

### 喜马拉雅（有声读物）

```bash
# 搜索并下载
musicdl 有声书 -p ximalaya
```

---

## 高级用法

### 批量下载

```bash
# 下载多个歌曲
echo "歌曲1" | xargs -I {} musicdl {}
echo "歌曲2" | xargs -I {} musicdl {}

# 下载列表
cat songs.txt | xargs -I {} musicdl {}
```

### 输出目录

```bash
# 指定输出目录
musicdl 歌曲 -o ./my_music

# 使用绝对路径
musicdl 歌曲 -o /home/user/music
```

### 下载限制

```bash
# 限制下载数量
musicdl 歌曲 --limit 5

# 用于歌单/专辑
musicdl -p 歌单 --limit 10
```

---

## 配置文件

### 配置文件位置

```bash
# Linux/macOS
~/.config/musicdl/musicdl_config.json

# Windows
%APPDATA%\musicdl\musicdl_config.json
```

### 配置示例

```json
{
  "platform": "netease",
  "quality": "lossless",
  "output_dir": "./downloads",
  "download_lyrics": true,
  "limit": 10
}
```

---

## 常见问题

### Q: 如何更新 musicdl？

A:
```bash
pip install --upgrade musicdl
```

### Q: 支持哪些平台？

A: 支持以下平台：
- 国内：网易云、QQ音乐、酷狗、酷我、咪咕
- 国际：YouTube、Spotify、Apple Music、TIDAL、Qobuz
- 有声：喜马拉雅、懒人听书、蜻蜓FM、蜻蜓FM

### Q: 音质如何选择？

A:
- `lossless`：无损音质（仅部分平台支持）
- `320`：320kbps MP3（高品质）
- `192`：192kbps MP3（中品质）
- `128`：128kbps MP3（标准品质）

### Q: 下载失败怎么办？

A:
1. 检查网络连接
2. 验证平台代码是否正确
3. 尝试不同的音质设置
4. 检查歌曲/歌单是否存在
5. 更新 musicdl：`pip install --upgrade musicdl`

### Q: 如何查看版本？

A:
```bash
musicdl --version
```

### Q: 搜索结果不准确？

A:
1. 尝试更详细的搜索词
2. 指定正确的平台
3. 尝试不同的搜索方式（歌名、歌手）

---

## 功能特性

### 核心特性

- ✅ 支持多平台（50+）
- ✅ 单曲/歌单/专辑下载
- ✅ 高品质/无损音质
- ✅ 歌词下载
- ✅ 纯 Python 实现
- ✅ 轻量级设计
- ✅ 跨平台支持

### 平台特性

| 特性 | 说明 |
|-----|------|
| 搜索 | 按歌名、歌手、专辑搜索 |
| 歌单 | 支持下载整张歌单 |
| 专辑 | 支持下载整张专辑 |
| 无损 | 部分平台支持无损音质 |
| 歌词 | 自动下载歌词（如果可用） |

---

## 法律声明

**重要**：此工具仅用于教育研究目的

- ❌ 禁止商业用途
- ✅ 尊重各平台版权和条款
- ✅ 仅限个人使用
- ❌ 禁止重新分发下载内容

---

## 更多信息

- **官方文档**: https://musicdl.readthedocs.io/
- **GitHub 仓库**: https://github.com/CharlesPikachu/musicdl
- **问题反馈**: https://github.com/CharlesPikachu/musicdl/issues
- **作者**: CharlesPikachu
- **项目**: Musicdl - 轻量级无损音乐下载器
