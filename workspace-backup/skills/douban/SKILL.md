---
name: douban
description: 豆瓣书影音查询技能 - 支持搜索电影/书籍/音乐、获取评分和评论、查看个人收藏。适用于：查询电影评分、搜索书籍信息、获取音乐评论、查看个人书影音标记等场景。
---

# Douban - 豆瓣书影音查询

## 概述

豆瓣技能提供豆瓣书影音的查询功能，包括：
- 搜索电影、书籍、音乐
- 获取评分和评论
- 查看个人收藏标记

## 使用场景

触发此技能当用户：
- 查询某部电影/书籍/音乐的评分
- 搜索特定类型的电影/书籍/音乐
- 获取某部作品的详细信息和评论
- 查看个人的书影音收藏

## 功能

### 1. 搜索电影

搜索豆瓣电影信息，包括评分、导演、演员、剧情简介等。

**使用方式**：
- "搜索豆瓣电影 <电影名>"
- "查询 <电影名> 的豆瓣评分"

**返回信息**：
- 电影名称
- 评分（豆瓣评分）
- 导演
- 主演
- 年份
- 剧情简介
- 短评

### 2. 搜索书籍

搜索豆瓣书籍信息，包括评分、作者、出版社、简介等。

**使用方式**：
- "搜索豆瓣书籍 <书名>"
- "查询 <书名> 的豆瓣评分"

**返回信息**：
- 书籍名称
- 评分（豆瓣评分）
- 作者
- 出版社
- 出版时间
- 内容简介
- 短评

### 3. 搜索音乐

搜索豆瓣音乐信息，包括评分、歌手、专辑信息等。

**使用方式**：
- "搜索豆瓣音乐 <音乐名/歌手名>"
- "查询 <歌手> 的豆瓣评分"

**返回信息**：
- 音乐/专辑名称
- 评分（豆瓣评分）
- 歌手/乐队
- 发行时间
- 专辑信息
- 短评

### 4. 获取评论

获取某部作品的豆瓣热门评论。

**使用方式**：
- "查看 <电影/书籍/音乐名> 的豆瓣评论"
- "获取 <作品> 的豆瓣短评"

**返回信息**：
- 热门短评（精选）
- 评论数量
- 用户评分分布

### 5. 查看个人收藏

查看用户的个人书影音收藏标记（需要提供豆瓣用户信息）。

**使用方式**：
- "查看我的豆瓣电影收藏"
- "查看我的豆瓣读书列表"

**注意**：此功能需要用户提供豆瓣账号信息或 Cookie。

## 工作流程

### 搜索流程

1. 构造豆瓣搜索 API URL
2. 发送 HTTP 请求获取搜索结果
3. 解析 JSON/HTML 响应
4. 提取关键信息（评分、标题、作者等）
5. 格式化输出

### 获取详情流程

1. 从搜索结果获取作品 ID
2. 使用作品 ID 构造详情 API URL
3. 发送 HTTP 请求
4. 解析响应获取详细信息
5. 格式化输出

## 技术说明

### 豆瓣 API

豆瓣未提供公开的 API，主要通过网页抓取实现。

**URL 格式**：
- 搜索：`https://search.douban.com/movie/subject_search?search_text=<关键词>&cat=1002`
- 电影详情：`https://movie.douban.com/subject/<电影ID>/`
- 书籍详情：`https://book.douban.com/subject/<书籍ID>/`
- 音乐详情：`https://music.douban.com/subject/<音乐ID>/`

### 类别代码

- 电影：1002
- 书籍：1003
- 音乐：1004

### 数据格式

豆瓣返回 JSON 格式的搜索结果，包含：
- `subjects` - 搜索结果列表
- 每个结果包含：`id`, `title`, `rating`, `year`, `directors`, `casts`, `cover_url` 等

## 注意事项

1. **频率限制**：豆瓣可能限制请求频率，不要过于频繁查询
2. **反爬虫**：豆瓣有反爬虫机制，可能需要使用 Cookie 或代理
3. **数据准确性**：豆瓣数据由用户贡献，可能存在误差
4. **法律合规**：仅用于个人学习和研究，不得用于商业用途

## 代理配置

如果豆瓣访问受限，可使用 SSH 隧道代理：

```bash
# 启动 SSH 隧道
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143

# 设置代理环境变量
export HTTP_PROXY="socks5://127.0.0.1:1080"
export HTTPS_PROXY="socks5://127.0.0.1:1080"
```

## 示例

### 搜索电影

**用户**："搜索豆瓣电影《肖申克的救赎》"

**返回**：
```
电影：肖申克的救赎（The Shawshank Redemption, 1994）
豆瓣评分：9.7
导演：弗兰克·德拉邦特
主演：蒂姆·罗宾斯, 摩根·弗里曼
剧情：银行家安迪因被误判谋杀罪而入狱，他在狱中结识了瑞德，并逐渐获得了狱友们的信任...
```

### 搜索书籍

**用户**："搜索豆瓣书籍《三体》"

**返回**：
```
书籍：三体（全集）
豆瓣评分：8.8
作者：刘慈欣
出版社：重庆出版社
出版时间：2008年
简介：文化大革命如火如荼进行的同时，军方探寻外星文明的绝秘计划"红岸工程"取得了突破性进展...
```

## 脚本使用

### douban_search.py - 搜索豆瓣

搜索豆瓣电影、书籍、音乐。

**位置**：`scripts/douban_search.py`

**依赖**：requests

**安装依赖**：
```bash
pip3 install --user requests
```

**使用方法**：
```bash
# 搜索电影（默认）
./scripts/douban_search.py "肖申克的救赎"

# 搜索书籍
./scripts/douban_search.py "三体" -c book

# 搜索音乐
./scripts/douban_search.py "周杰伦" -c music

# 限制结果数量
./scripts/douban_search.py "复仇者联盟" -l 5

# 输出 JSON 格式
./scripts/douban_search.py "泰坦尼克号" -j

# 简洁输出
./scripts/douban_search.py "阿凡达" -q
```

**参数**：
- `keyword` - 搜索关键词（必需）
- `-c, --category` - 搜索类别：movie/book/music（默认：movie）
- `-l, --limit` - 返回结果数量（默认：10）
- `-j, --json` - 输出 JSON 格式
- `-q, --quiet` - 简洁输出（不显示详细信息）

### douban_detail.py - 获取详情

获取豆瓣电影、书籍、音乐的详细信息。

**位置**：`scripts/douban_detail.py`

**依赖**：requests, beautifulsoup4

**安装依赖**：
```bash
pip3 install --user requests beautifulsoup4
```

**使用方法**：
```bash
# 获取电影详情（默认）
./scripts/douban_detail.py "1292052"

# 获取书籍详情
./scripts/douban_detail.py "2567698" -t book

# 获取音乐详情
./scripts/douban_detail.py "34847798" -t music

# 输出 JSON 格式
./scripts/douban_detail.py "1292052" -j
```

**参数**：
- `id` - 作品 ID（必需）
- `-t, --type` - 作品类型：movie/book/music（默认：movie）
- `-j, --json` - 输出 JSON 格式

**获取 ID 方法**：
1. 先使用 `douban_search.py` 搜索
2. 从搜索结果中获取作品的 `id` 字段
3. 使用该 ID 调用 `douban_detail.py`

### douban_comments.py - 获取评论

获取豆瓣作品的热门评论。

**位置**：`scripts/douban_comments.py`

**依赖**：requests, beautifulsoup4

**安装依赖**：
```bash
pip3 install --user requests beautifulsoup4
```

**使用方法**：
```bash
# 获取评论（默认20条）
./scripts/douban_comments.py "https://movie.douban.com/subject/1292052/"

# 限制评论数量
./scripts/douban_comments.py "https://movie.douban.com/subject/1292052/" -l 10

# 输出 JSON 格式
./scripts/douban_comments.py "https://movie.douban.com/subject/1292052/" -j

# 简洁输出
./scripts/douban_comments.py "https://movie.douban.com/subject/1292052/" -q
```

**参数**：
- `url` - 豆瓣作品 URL（必需）
- `-l, --limit` - 获取评论数量（默认：20）
- `-j, --json` - 输出 JSON 格式
- `-q, --quiet` - 简洁输出（不显示统计摘要）

## 完整工作流程示例

### 搜索电影并获取详情

```bash
# 1. 搜索电影
./scripts/douban_search.py "肖申克的救赎"

# 2. 从结果中获取 ID（假设是 1292052）

# 3. 获取详情
./scripts/douban_detail.py "1292052"

# 4. 获取评论
./scripts/douban_comments.py "https://movie.douban.com/subject/1292052/"
```

### 搜索书籍并获取详情

```bash
# 1. 搜索书籍
./scripts/douban_search.py "三体" -c book

# 2. 从结果中获取 ID（假设是 2567698）

# 3. 获取详情
./scripts/douban_detail.py "2567698" -t book
```

## 相关资源

- 豆瓣电影：https://movie.douban.com
- 豆瓣读书：https://book.douban.com
- 豆瓣音乐：https://music.douban.com
