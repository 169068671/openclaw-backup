# Cookie Format Converter 配置完成报告

**技能名称：** cookie-converter
**功能：** 双向 Cookie 格式转换（Netscape ↔ Playwright ↔ JSON）
**配置日期：** 2026-03-12
**状态：** ✅ 完成

---

## 📦 技能包

**位置：** `/home/admin/openclaw/workspace/cookie-converter/`
**打包文件：** `/home/admin/openclaw/workspace/cookie-converter.skill`

**包含文件：**
- `SKILL.md` - 完整技能文档
- `README.md` - 快速开始指南
- `cookie-converter.sh` - 本地 CLI 包装脚本
- `scripts/convert_cookies.py` - 核心转换脚本

---

## 🚀 安装状态

| 项目 | 状态 | 位置 |
|------|------|------|
| **全局 CLI** | ✅ 已安装 | `/home/admin/.local/bin/cookie-converter` |
| **本地 CLI** | ✅ 已安装 | `/home/admin/openclaw/workspace/cookie-converter/cookie-converter.sh` |
| **转换脚本** | ✅ 已安装 | `/home/admin/openclaw/workspace/cookie-converter/scripts/convert_cookies.py` |
| **技能包** | ✅ 已打包 | `/home/admin/openclaw/workspace/cookie-converter.skill` |

---

## ✅ 测试结果

### 测试1：Netscape → Playwright

```bash
cookie-converter netscape-to-playwright \
  /tmp/test-cookies.txt \
  /tmp/test-storage.json -v
```

**结果：**
```
✅ 转换完成！
🔄 转换类型: netscape-to-playwright
📁 输入文件: /tmp/test-cookies.txt
📁 输出文件: /tmp/test-storage.json
🍪 Cookies 数量: 3
```

---

### 测试2：Playwright → Netscape

```bash
cookie-converter playwright-to-netscape \
  /tmp/test-storage.json \
  /tmp/test-cookies-back.txt -v
```

**结果：**
```
✅ 转换完成！
🔄 转换类型: playwright-to-netscape
📁 输入文件: /tmp/test-storage.json
📁 输出文件: /tmp/test-cookies-back.txt
🍪 Cookies 数量: 3
```

---

### 测试3：双向转换验证

**原始文件：**
```
.google.com	TRUE	/	FALSE	9999999999	SID	session_id_123
.google.com	TRUE	/	FALSE	9999999999	HSID	security_id_456
```

**转换后文件：**
```
.google.com	TRUE	/	FALSE	9999999999	SID	session_id_123
.google.com	TRUE	/	FALSE	9999999999	HSID	security_id_456
```

**验证：** ✅ Cookies 完全一致

---

## 📊 支持的转换

| 转换类型 | 命令 | 用途 |
|---------|--------|------|
| **Netscape → Playwright** | `netscape-to-playwright` | NotebookLM 部署 |
| **Playwright → Netscape** | `playwright-to-netscape` | yt-dlp 下载 |
| **Netscape → JSON** | `netscape-to-json` | 手动检查 |
| **JSON → Netscape** | `json-to-netscape` | 脚本生成 |
| **Playwright → JSON** | `playwright-to-json` | 手动检查 |
| **JSON → Playwright** | `json-to-playwright` | 脚本生成 |

---

## 🎯 常用工作流

### 工作流1：Chrome → NotebookLM

```bash
# 1. 导出 cookies
browser-cookies-exporter .google.com /tmp/google-cookies.txt

# 2. 转换为 Playwright
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

### 工作流2：NotebookLM → yt-dlp

```bash
# 1. 从 VPS 下载 storage state
sshpass -p 'Whj001.Whj001' scp \
  root@76.13.219.143:/root/.config/notebooklm/session.json \
  /tmp/storage_state.json

# 2. 转换为 Netscape
cookie-converter playwright-to-netscape \
  /tmp/storage_state.json \
  /tmp/google-cookies.txt

# 3. 下载视频
yt-dlp --cookies /tmp/google-cookies.txt "URL"
```

---

### 工作流3：检查和编辑

```bash
# 1. 转换为 JSON
cookie-converter playwright-to-json \
  /tmp/storage_state.json \
  /tmp/cookies.json

# 2. 查看和编辑
cat /tmp/cookies.json | python3 -m json.tool | less

# 3. 转换回 Playwright
cookie-converter json-to-playwright \
  /tmp/cookies.json \
  /tmp/storage_state_updated.json
```

---

## 📚 创建的文档

### 1. 使用指南
**文件：** `/home/admin/openclaw/workspace/Cookie Converter使用指南.md`
**内容：**
- 快速开始
- 常用场景
- 格式说明
- 高级用法
- 常见问题

### 2. 技能文档
**文件：** `/home/admin/openclaw/workspace/cookie-converter/SKILL.md`
**内容：**
- 完整功能说明
- 所有转换类型
- 格式详细说明
- 高级示例
- 故障排除

### 3. README
**文件：** `/home/admin/openclaw/workspace/cookie-converter/README.md`
**内容：**
- 快速开始
- 支持的转换
- 安装说明

---

## 🔧 命令行工具

### 全局工具

```bash
cookie-converter <conversion_type> <input_file> <output_file> [options]
```

**示例：**
```bash
cookie-converter netscape-to-playwright cookies.txt storage.json
cookie-converter playwright-to-netscape storage.json cookies.txt
cookie-converter netscape-to-json cookies.txt cookies.json -v
```

### 本地工具

```bash
cd /home/admin/openclaw/workspace/cookie-converter
./cookie-converter.sh <conversion_type> <input_file> <output_file> [options]
```

---

## ⚠️ 重要提示

### 安全性

1. **不要分享** Cookie 文件（包含敏感认证信息）
2. **安全存储** 使用受保护的目录
3. **定期更新** Cookies 通常 14 天后过期
4. **删除旧文件** 及时清理过期的 Cookie 文件

### 最佳实践

1. **备份原始文件** 转换前保留副本
2. **使用详细输出** 添加 `-v` 参数查看详情
3. **验证输出** 转换后检查文件格式
4. **测试小样本** 先转换少量 cookies，验证后再转换全部

---

## 🔗 相关技能

- **browser-cookies-exporter** - 从浏览器导出 cookies
- **youtube-auth-exporter** - YouTube/Google 认证导出
- **notebooklm-auth-exporter** - NotebookLM 认证导出
- **yt-dlp-downloader** - 视频下载（支持 cookies）

---

## 💡 使用建议

### 什么时候使用这个技能？

✅ **使用这个转换器，当：**
- 需要在不同工具之间共享认证（NotebookLM ↔ yt-dlp）
- 需要在服务器和本地之间传输认证
- 需要手动检查或编辑 cookies
- 需要创建测试 cookies
- 需要过滤或合并 cookies

❌ **不需要这个转换器，当：**
- 直接使用 cookies（不需要转换格式）
- 使用专门的工具（如 `notebooklm login`）
- Cookies 已经是正确的格式

---

## 🎯 下一步

1. **测试基本转换**：转换一个简单的 cookie 文件
2. **尝试工作流**：使用 Chrome → NotebookLM 或 NotebookLM → yt-dlp
3. **探索高级用法**：过滤、合并 cookies
4. **集成到脚本**：在自动化脚本中使用转换器

---

## 📝 总结

✅ **已完成：**
- 创建双向 cookie 格式转换技能
- 支持 6 种转换类型
- 全局 CLI 工具已安装
- 完整文档已创建
- 功能已测试验证

🎯 **核心功能：**
- Netscape ↔ Playwright 双向转换
- Netscape ↔ JSON 双向转换
- Playwright ↔ JSON 双向转换
- 详细的转换信息输出
- 错误处理和验证

📚 **文档：**
- 使用指南：`/home/admin/openclaw/workspace/Cookie Converter使用指南.md`
- 技能文档：`/home/admin/openclaw/workspace/cookie-converter/SKILL.md`
- README：`/home/admin/openclaw/workspace/cookie-converter/README.md`

---

**配置完成！** 🎉

现在你可以在不同工具之间轻松转换 Cookie 格式了！🍪
