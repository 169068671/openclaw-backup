# Cookie Format Converter 使用指南

**技能名称：** cookie-converter
**功能：** 双向 Cookie 格式转换（Netscape ↔ Playwright ↔ JSON）
**版本：** 1.0
**创建日期：** 2026-03-12

---

## 📦 支持的转换

### 转换类型

| 从 | 到 | 用途 |
|---|---|---|
| Netscape | Playwright | NotebookLM、Playwright 自动化 |
| Playwright | Netscape | yt-dlp、curl、wget |
| Netscape | JSON | 手动检查、编辑 |
| JSON | Netscape | 脚本生成、测试 |
| Playwright | JSON | 手动检查、编辑 |
| JSON | Playwright | 脚本生成、测试 |

---

## 🚀 快速开始

### 命令行工具

**全局命令：** `cookie-converter`

```bash
# Netscape → Playwright
cookie-converter netscape-to-playwright cookies.txt storage.json

# Playwright → Netscape
cookie-converter playwright-to-netscape storage.json cookies.txt

# 显示详细信息
cookie-converter netscape-to-playwright cookies.txt storage.json -v
```

**本地命令：** `cookie-converter.sh`

```bash
# 在技能目录内运行
cd /home/admin/openclaw/workspace/cookie-converter
./cookie-converter.sh netscape-to-playwright cookies.txt storage.json
```

---

## 🎯 常用场景

### 场景1：Chrome → NotebookLM（部署认证）

```bash
# 1. 从 Chrome 导出 cookies
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# 2. 转换为 Playwright 格式
cookie-converter netscape-to-playwright \
  /tmp/google-cookies.txt \
  /tmp/storage_state.json

# 3. 部署到 VPS
sshpass -p 'Whj001.Whj001' scp /tmp/storage_state.json \
  root@76.13.219.143:/root/.config/notebooklm/session.json

# 4. 验证
ssh root@76.13.219.143 "notebooklm list"
```

---

### 场景2：NotebookLM → yt-dlp（提取认证）

```bash
# 1. 从 VPS 下载 storage state
sshpass -p 'Whj001.Whj001' scp \
  root@76.13.219.143:/root/.config/notebooklm/session.json \
  /tmp/storage_state.json

# 2. 转换为 Netscape 格式
cookie-converter playwright-to-netscape \
  /tmp/storage_state.json \
  /tmp/google-cookies.txt

# 3. 使用 cookies 下载视频
yt-dlp --cookies /tmp/google-cookies.txt \
  "https://www.youtube.com/watch?v=VIDEO_ID"
```

---

### 场景3：检查和编辑 Cookies

```bash
# 1. 转换为 JSON（易于阅读）
cookie-converter playwright-to-json \
  /tmp/storage_state.json \
  /tmp/cookies.json

# 2. 查看内容
cat /tmp/cookies.json | python3 -m json.tool | less

# 3. 编辑 JSON
nano /tmp/cookies.json

# 4. 转换回 Playwright
cookie-converter json-to-playwright \
  /tmp/cookies.json \
  /tmp/storage_state_updated.json
```

---

### 场景4：创建测试 Cookies

```bash
# 1. 创建 JSON 文件
cat > /tmp/test-cookies.json <<EOF
[
  {
    "name": "test_cookie",
    "value": "test_value",
    "domain": "example.com",
    "path": "/",
    "expires": 9999999999,
    "secure": false
  }
]
EOF

# 2. 转换为 Playwright
cookie-converter json-to-playwright \
  /tmp/test-cookies.json \
  /tmp/test_storage.json

# 3. 使用 Playwright
playwright codegen --load-storage=/tmp/test_storage.json https://example.com
```

---

## 📊 格式说明

### Netscape Cookie File

**用途：** yt-dlp、curl、wget

**格式：** 文本文件，制表符分隔

```
# Netscape HTTP Cookie File
# This is a generated file! Do not edit.

.google.com	TRUE	/	FALSE	1234567890	SID	value1
.google.com	TRUE	/	FALSE	1234567890	HSID	value2
```

**字段说明：**
```
域名 | 子域名 | 路径 | 安全 | 过期时间 | 名称 | 值
```

---

### Playwright storage_state.json

**用途：** Playwright、notebooklm

**格式：** JSON

```json
{
  "cookies": [
    {
      "name": "SID",
      "value": "value1",
      "domain": ".google.com",
      "path": "/",
      "expires": 1234567890.0,
      "httpOnly": false,
      "secure": true,
      "sameSite": "Lax"
    }
  ],
  "origins": []
}
```

---

### JSON Array

**用途：** 手动检查、编辑、脚本

**格式：** JSON 数组

```json
[
  {
    "name": "SID",
    "value": "value1",
    "domain": ".google.com",
    "path": "/",
    "expires": 1234567890,
    "secure": true
  }
]
```

---

## 🔧 高级用法

### 过滤特定域名的 Cookies

```bash
# 1. 转换为 JSON
cookie-converter playwright-to-json \
  /tmp/storage.json \
  /tmp/cookies.json

# 2. 过滤 Google cookies
cat /tmp/cookies.json | python3 -c "
import json, sys
cookies = json.load(sys.stdin)
google_cookies = [c for c in cookies if 'google.com' in c.get('domain', '')]
print(json.dumps(google_cookies, indent=2))
" > /tmp/google-cookies.json

# 3. 转换回 Playwright
cookie-converter json-to-playwright \
  /tmp/google-cookies.json \
  /tmp/google_storage.json
```

---

### 合并多个 Cookie 文件

```bash
# 1. 转换为 JSON
cookie-converter netscape-to-json cookies1.txt cookies1.json
cookie-converter netscape-to-json cookies2.txt cookies2.json

# 2. 合并
python3 <<EOF
import json

with open('cookies1.json') as f1:
    cookies1 = json.load(f1)
with open('cookies2.json') as f2:
    cookies2 = json.load(f2)

# 去重
seen = {}
merged = []
for c in cookies1 + cookies2:
    key = f"{c['name']}_{c['domain']}"
    if key not in seen:
        seen[key] = True
        merged.append(c)

with open('merged.json', 'w') as f:
    json.dump(merged, f, indent=2)
EOF

# 3. 转换回 Playwright
cookie-converter json-to-playwright merged.json merged_storage.json
```

---

## ⚠️ 常见问题

### 问题1：找不到文件

**错误：**
```
❌ Error: Input file not found: /tmp/cookies.txt
```

**解决方案：**
```bash
# 检查文件是否存在
ls -la /tmp/cookies.txt

# 使用绝对路径
cookie-converter netscape-to-playwright \
  /home/admin/Desktop/cookies.txt \
  /home/admin/Desktop/storage.json
```

---

### 问题2：格式错误

**错误：**
```
❌ Error during conversion: Malformed cookie file
```

**解决方案：**
```bash
# 验证 JSON 格式
python3 -m json.tool /tmp/cookies.json

# 检查 Netscape 格式
head -5 /tmp/cookies.txt
```

---

### 问题3：权限拒绝

**错误：**
```
❌ Error saving output file: Permission denied
```

**解决方案：**
```bash
# 创建输出目录
mkdir -p /tmp/output
chmod 755 /tmp/output

# 使用可写目录
cookie-converter netscape-to-playwright \
  /tmp/input.txt \
  /tmp/output/output.json
```

---

## 💡 提示

1. **备份原始文件**：转换前总是保留原始文件
2. **使用详细输出**：添加 `-v` 参数查看转换详情
3. **验证输出**：转换后检查输出文件格式
4. **安全存储**：Cookie 文件包含敏感信息，不要分享
5. **定期更新**：Cookies 通常 14 天后过期

---

## 🔗 相关技能

- **browser-cookies-exporter** - 从浏览器导出 cookies
- **youtube-auth-exporter** - YouTube/Google 认证导出
- **notebooklm-auth-exporter** - NotebookLM 认证导出
- **yt-dlp-downloader** - 视频下载（支持 cookies）

---

## 📖 完整文档

- **技能文档：** `/home/admin/openclaw/workspace/cookie-converter/SKILL.md`
- **README：** `/home/admin/openclaw/workspace/cookie-converter/README.md`

---

**Cookie 格式转换就是这么简单！** 🍪
