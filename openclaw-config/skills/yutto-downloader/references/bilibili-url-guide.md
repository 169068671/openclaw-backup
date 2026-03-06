# Bilibili URL 格式指南

> 如何从 Bilibili 网站获取正确的视频/番剧 URL

---

## URL 格式汇总

### 1. 投稿视频

**格式**：
```
https://www.bilibili.com/video/BV{视频ID}/
https://b23.tv/{短链接}
```

**示例**：
```
https://www.bilibili.com/video/BV1CTMHziEaB/
https://b23.tv/xxxxxx
```

**说明**：
- `BV` 开头的 ID 是 Bilibili 视频的唯一标识符
- `b23.tv` 是短链接，会自动跳转到完整链接

---

### 2. 番剧/电视剧

**格式**：
```
https://www.bilibili.com/bangumi/play/ep{剧集ID}/
https://www.bilibili.com/bangumi/media/md{媒体ID}/
```

**示例**：
```
https://www.bilibili.com/bangumi/play/ep123456
https://www.bilibili.com/bangumi/media/md28223067
```

**说明**：
- `ep` 开头的 ID 是具体某一集
- `md` 开头的 ID 是整个番剧/剧集的媒体 ID
- 使用 `md` ID 可能会下载整个剧集

---

### 3. 课程/教程

**格式**：
```
https://www.bilibili.com/cheese/play/ep{剧集ID}/
https://www.bilibili.com/cheese/play/ss{课程ID}/
```

**示例**：
```
https://www.bilibili.com/cheese/play/ep789456
https://www.bilibili.com/cheese/play/ss12345
```

**说明**：
- `cheese` 是 Bilibili 的付费课程平台
- 需要购买或拥有访问权限

---

### 4. 收藏夹

**格式**：
```
https://space.bilibili.com/{用户ID}/favlist?fid={收藏夹ID}
https://space.bilibili.com/channel/favlist?fid={收藏夹ID}
```

**示例**：
```
https://space.bilibili.com/123456789/favlist?fid=987654
https://space.bilibili.com/channel/favlist?fid=987654
```

**说明**：
- 需要登录才能访问收藏夹
- 可能需要配置 SESSDATA

---

### 5. 合集

**格式**：
```
https://space.bilibili.com/channel/collectiondetail?sid={合集ID}
https://www.bilibili.com/medialist/play/{合集ID}?business=space_collection
```

**示例**：
```
https://space.bilibili.com/channel/collectiondetail?sid=123456789
https://www.bilibili.com/medialist/play/123456789?business=space_collection
```

**说明**：
- 合集是用户创建的视频集合
- 通常按主题或系列组织

---

### 6. 投稿列表

**格式**：
```
https://space.bilibili.com/{用户ID}/video
```

**示例**：
```
https://space.bilibili.com/123456789/video
```

**说明**：
- 显示用户的所有投稿视频
- yutto 可能不支持直接下载整个投稿列表

---

## 如何获取 URL

### 方法1：从浏览器地址栏复制

**步骤**：
1. 打开 Bilibili 视频/番剧页面
2. 复制浏览器地址栏中的 URL
3. 直接粘贴到 yutto 命令中

### 方法2：从分享链接复制

**步骤**：
1. 点击视频下方的分享按钮
2. 复制链接（可能是短链接）
3. yutto 会自动处理短链接

### 方法3：右键复制视频链接

**步骤**：
1. 在视频列表中右键点击视频
2. 选择"复制链接地址"
3. 粘贴到 yutto 命令中

---

## URL 验证

### 验证 URL 是否有效

```bash
# 使用 curl 检查
curl -I https://www.bilibili.com/video/BV1xxxxx/

# 返回 200 表示 URL 有效
# 返回 404 表示视频不存在或已删除
```

---

## 常见 URL 问题

### Q: 短链接能用吗？

A: 可以。yutto 会自动解析 `b23.tv` 短链接。

### Q: URL 需要登录吗？

A:
- 普通视频：不需要
- 会员专享：需要配置 SESSDATA
- 私人收藏/合集：需要登录

### Q: 如何获取番剧的整个剧集？

A:
1. 使用 `md` ID 可能会下载整个番剧
2. 或者逐个下载每一集（使用 `ep` ID）

---

## URL 格式快速参考

| 类型 | URL 格式 | 示例 |
|-----|---------|------|
| 投稿视频 | `/video/BV{id}/` | BV1CTMHziEaB |
| 番剧集 | `/bangumi/play/ep{id}/` | ep123456 |
| 番剧整体 | `/bangumi/media/md{id}/` | md28223067 |
| 课程集 | `/cheese/play/ep{id}/` | ep789456 |
| 课程整体 | `/cheese/play/ss{id}/` | ss12345 |
| 收藏夹 | `/channel/favlist?fid={id}` | fid=987654 |
| 合集 | `/channel/collectiondetail?sid={id}` | sid=123456789 |
| 投稿列表 | `/{userId}/video` | 123456789/video |

---

## 注意事项

1. **URL 大小写**：BV ID 中的字母大小写敏感
2. **特殊字符**：URL 中的特殊字符需要正确转义
3. **过期链接**：视频删除后 URL 会失效
4. **地区限制**：某些视频可能有地区限制
5. **访问权限**：需要登录才能访问私密内容

---

## 获取帮助

如果遇到 URL 相关问题：
1. 确认 URL 格式是否正确
2. 检查视频是否可用
3. 确认是否需要登录
4. 查看 yutto 官方文档：https://yutto.nyakku.moe/
