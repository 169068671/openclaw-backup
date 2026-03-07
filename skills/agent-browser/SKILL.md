# agent-browser - Vercel 无头浏览器自动化 CLI

## 简介

agent-browser 是 Vercel 官方的无头浏览器自动化 CLI 工具，专为 AI agents 设计。

**特点**：
- 🚀 极快速度：Rust 原生 CLI，亚毫秒级解析
- 🎯 AI 友好：通过 ref 选择元素，支持 snapshot
- 📱 跨平台：macOS, Linux, Windows
- 🔧 完整 API：点击、输入、截图、PDF 等

## 安装

```bash
# 全局安装
npm install -g agent-browser

# 下载 Chromium（首次使用）
agent-browser install
```

---

## 🌐 代理配置

### 命令行参数

```bash
# 使用代理
agent-browser --proxy "http://127.0.0.1:7890" open https://example.com

# 使用 SOCKS5 代理
agent-browser --proxy "socks5://127.0.0.1:1080" open https://example.com

# 使用带认证的代理
agent-browser --proxy "http://user:pass@127.0.0.1:7890" open https://example.com
```

### 环境变量

```bash
# 设置全局代理
export AGENT_BROWSER_PROXY="http://127.0.0.1:7890"

# 或使用 SOCKS5 代理
export AGENT_BROWSER_PROXY="socks5://127.0.0.1:1080"

# 设置代理绕过（某些主机不使用代理）
export AGENT_BROWSER_PROXY_BYPASS="localhost,*.internal.com"

# 然后正常使用
agent-browser open https://example.com
```

### 常见代理方案

#### SOCKS5 代理（SSH 隧道）⭐

```bash
# 1. 启动 SSH 隧道
sshpass -p 'password' ssh -N -D 1080 -f user@host

# 2. 使用代理
agent-browser --proxy "socks5://127.0.0.1:1080" open https://www.youtube.com
```

#### HTTP 代理

```bash
# 使用 HTTP 代理
agent-browser --proxy "http://127.0.0.1:7890" open https://example.com
```

### 推荐配置（本地）

```bash
# ~/.bashrc 或 ~/.zshrc
export AGENT_BROWSER_PROXY="socks5://127.0.0.1:1080"
export AGENT_BROWSER_PROXY_BYPASS="localhost,*.internal.com,127.0.0.1"
```

---

---

## 🍪 Cookies 导入（批量导入脚本）

### Cookies 导入脚本

**位置**：`~/.local/bin/agent-browser-cookies-import.py`

**功能**：
- 从 Netscape 格式的 cookies 文件批量导入到 agent-browser
- 自动处理 `#HttpOnly_` 前缀
- 支持复杂 cookies 格式

### 使用方法

```bash
# 基本用法
agent-browser-cookies-import.py <cookies-file> <target-url>

# 示例
agent-browser-cookies-import.py ~/.config/google-cookies.txt https://www.google.com
```

### Cookies 文件格式（Netscape）

```
# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.google.com	TRUE	/	FALSE	1807160049	APISID	value
.google.com	TRUE	/	TRUE	1807160049	SID	value
#HttpOnly_.google.com	TRUE	/	FALSE	1807160049	HSID	value
```

### 导出 Cookies（使用 browser-cookies-exporter）

```bash
# 导出 Google cookies
browser-cookies-exporter google.com ~/.config/google-cookies.txt

# 导出 YouTube cookies
browser-cookies-exporter youtube.com ~/.config/youtube-cookies.txt
```

### 使用流程

```bash
# 1. 打开浏览器（目标 URL）
agent-browser open https://www.google.com

# 2. 导入 cookies
agent-browser-cookies-import.py ~/.config/google-cookies.txt https://www.google.com

# 3. 获取快照
agent-browser snapshot

# 4. 执行操作
agent-browser find role combobox fill --name "Search" "test query"
agent-browser find role button click --name "Google Search"

# 5. 关闭浏览器
agent-browser close
```

### 测试结果

| 项目 | 结果 |
|------|------|
| **Google Cookies 导入** | ✅ 41/41 成功 |
| **关键 cookies** | ✅ HSID, SSID, SID 等 |
| **Google 登录 UI** | ⚠️ 受限（安全检测）|
| **其他服务** | ✅ 正常工作 |

### 注意事项

⚠️ **Google 登录限制**：
- 即使导入完整 cookies，Google 仍然拒绝自动化浏览器登录
- 原因：Google 检测到无头浏览器（agent-browser）
- 解决方案：使用 cookies 文件配合其他工具（yt-dlp, curl）

✅ **适用场景**：
- API 认证
- 爬取数据
- 自动化测试
- 非严格验证的服务

❌ **不适用场景**：
- Google 登录（UI）
- 严格检测自动化的服务

---

## 基本使用

### 打开网页并获取快照

```bash
# 打开网页
agent-browser open https://example.com

# 获取快照（推荐 AI 使用）
agent-browser snapshot

# 关闭浏览器
agent-browser close
```

### 快照格式

```json
{
  "title": "页面标题",
  "url": "https://example.com",
  "elements": [
    {
      "ref": "e1",
      "role": "heading",
      "name": "Example Domain",
      "selector": "h1",
      "tag": "h1"
    },
    {
      "ref": "e2",
      "role": "link",
      "name": "More information...",
      "selector": "a",
      "tag": "a"
    }
  ]
}
```

### 使用 ref 操作元素

```bash
# 点击元素
agent-browser click @e2

# 填写表单
agent-browser fill @e3 "test@example.com"

# 获取文本
agent-browser get text @e1

# 截图
agent-browser screenshot page.png

# 全页截图
agent-browser screenshot --full page.png

# 带标注的截图（元素编号）
agent-browser screenshot --annotate annotated.png
```

## 选择器

### CSS 选择器

```bash
agent-browser click "#submit"
agent-browser fill "#email" "test@example.com"
agent-browser get text "h1"
```

### 智能查找

```bash
# 按 ARIA 角色查找
agent-browser find role button click --name "Submit"
agent-browser find role link text --name "Learn More"

# 按文本内容查找
agent-browser find text "Sign In" click

# 按标签查找
agent-browser find label "Email" fill "test@example.com"

# 按占位符查找
agent-browser find placeholder "Enter email" fill "test@example.com"

# 按 alt 文本查找
agent-browser find alt "Logo" click

# 按 title 属性查找
agent-browser find title "Submit" click

# 按 data-testid 查找
agent-browser find testid "submit-btn" click

# 第一个/最后一个匹配
agent-browser find first ".item" click
agent-browser find last ".item" click
agent-browser find nth 2 ".item" click

# 匹配选项
--name "Submit"   # 按 name 过滤角色
--exact           # 要求精确文本匹配
```

## 常用命令

### 导航操作

```bash
agent-browser open <url>          # 打开 URL（别名：goto, navigate）
agent-browser click <sel>         # 点击元素（--new-tab 新标签页）
agent-browser dblclick <sel>     # 双击
agent-browser focus <sel>        # 聚焦元素
agent-browser type <sel> <text>  # 输入文本
agent-browser fill <sel> <text>  # 清空并填充
agent-browser press <key>        # 按键（Enter, Tab, Control+a）
agent-browser hover <sel>         # 悬停
agent-browser select <sel> <val> # 选择下拉选项
agent-browser check <sel>        # 勾选复选框
agent-browser uncheck <sel>      # 取消勾选
```

### 滚动操作

```bash
agent-browser scroll down 500     # 向下滚动 500px
agent-browser scroll up 500       # 向上滚动 500px
agent-browser scrollintoview <sel> # 滚动到元素可见
```

### 获取信息

```bash
agent-browser get text <sel>      # 获取文本内容
agent-browser get html <sel>      # 获取 innerHTML
agent-browser get value <sel>     # 获取输入值
agent-browser get attr <sel> <attr>  # 获取属性
agent-browser get title           # 获取页面标题
agent-browser get url             # 获取当前 URL
agent-browser get count <sel>     # 统计匹配元素数量
agent-browser get box <sel>       # 获取元素位置
agent-browser get styles <sel>    # 获取计算样式
```

### 状态检查

```bash
agent-browser is visible <sel>    # 检查是否可见
agent-browser is enabled <sel>    # 检查是否启用
agent-browser is checked <sel>    # 检查是否选中
```

### 等待操作

```bash
agent-browser wait <sel>         # 等待元素可见
agent-browser wait 1000          # 等待 1000ms
agent-browser wait --text "Welcome"  # 等待文本出现
agent-browser wait --url "**/dash"    # 等待 URL 匹配
agent-browser wait --load networkidle  # 等待网络空闲
agent-browser wait --fn "window.ready === true"  # 等待 JS 条件
```

### 键盘操作

```bash
agent-browser keydown <key>       # 按下键
agent-browser keyup <key>         # 释放键
agent-browser keyboard type <text>  # 模拟真实按键（无选择器）
agent-browser keyboard inserttext <text>  # 插入文本（无按键事件）
```

### 鼠标操作

```bash
agent-browser mouse move <x> <y>  # 移动鼠标
agent-browser mouse down [button]  # 按下按钮（left/right/middle）
agent-browser mouse up [button]    # 释放按钮
agent-browser mouse wheel <dy> [dx]  # 滚轮
```

### 拖放操作

```bash
agent-browser drag <src> <tgt>    # 拖放
```

### 文件上传

```bash
agent-browser upload <sel> <files>  # 上传文件
```

### 截图和导出

```bash
agent-browser screenshot [path]    # 截图（临时目录如果无路径）
agent-browser screenshot --full page.png  # 全页截图
agent-browser screenshot --annotate annotated.png  # 带标注截图
agent-browser pdf report.pdf       # 导出 PDF
```

### Cookie 操作

```bash
agent-browser cookies clear        # 清除 cookies
```

### 页面设置

```bash
agent-browser set viewport 1920 1080  # 设置视口大小
agent-browser set device "iPhone 14"    # 模拟设备
agent-browser set geo 37.7749 -122.4194  # 设置地理位置
agent-browser set offline on          # 切换离线模式
agent-browser set headers '{"Authorization":"Bearer xxx"}'  # 设置 HTTP 头
agent-browser set credentials user pass  # 设置 HTTP 基本认证
agent-browser set media dark          # 模拟深色模式
```

### 执行 JavaScript

```bash
agent-browser eval "document.title"           # 执行 JS
agent-browser eval -b "ZG9jdW1lbnQudGl0bGU="  # Base64 编码
agent-browser eval --stdin < script.js       # 从 stdin 读取
```

### 连接到浏览器

```bash
agent-browser connect 9222  # 通过 CDP 连接到浏览器
```

### 关闭浏览器

```bash
agent-browser close  # 关闭浏览器（别名：quit, exit）
```

## 完整工作流示例

### 示例 1：搜索并获取结果

```bash
# 打开 Google
agent-browser open https://www.google.com

# 获取快照
agent-browser snapshot

# 填写搜索框
agent-browser fill "[name='q']" "agent-browser"

# 点击搜索按钮
agent-browser find role button click --name "Google Search"

# 等待结果
agent-browser wait ".g"

# 获取结果标题
agent-browser get text ".g .DKV0Md"

# 截图
agent-browser screenshot results.png

# 关闭
agent-browser close
```

### 示例 2：表单提交

```bash
# 打开表单
agent-browser open https://example.com/signup

# 填写表单
agent-browser find label "Email" fill "test@example.com"
agent-browser find label "Password" fill "password123"
agent-browser find label "Confirm Password" fill "password123"

# 勾选同意
agent-browser find label "I agree" check

# 提交
agent-browser find role button click --name "Sign Up"

# 等待成功消息
agent-browser wait --text "Welcome!"

# 关闭
agent-browser close
```

### 示例 3：爬取数据

```bash
# 打开页面
agent-browser open https://example.com/products

# 滚动加载更多
agent-browser scroll down 1000
agent-browser wait 2000

# 获取所有产品
agent-browser snapshot

# 保存 HTML
agent-browser get html ".product" > products.html

# 导出 PDF
agent-browser pdf products.pdf

# 关闭
agent-browser close
```

## Linux 依赖

如果浏览器启动失败，安装系统依赖：

```bash
# 使用 agent-browser 安装依赖
agent-browser install --with-deps

# 或手动安装 Playwright 依赖
npx playwright install-deps chromium
```

## 性能优化

- 全局安装比 npx 更快
- 使用 ref 选择器比 CSS 选择器更快
- snapshot 是 AI 交互的最佳方式

## 常见问题

### 浏览器启动失败
```bash
agent-browser install --with-deps
```

### 元素未找到
```bash
agent-browser wait <selector>
```

### 网络加载慢
```bash
agent-browser wait --load networkidle
```

## 资源

- GitHub: https://github.com/vercel-labs/agent-browser
- NPM: https://www.npmjs.com/package/agent-browser
- 作者: Vercel Labs

## 版本

- 当前版本：0.16.3
- 安装位置：`/home/admin/.npm-global/lib/node_modules/agent-browser`
- 可执行文件：`/home/admin/.npm-global/bin/agent-browser`
