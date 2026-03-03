# res-downloader 编译记录 - 2026-03-03 19:45

## 进度总结

### ✅ 已完成

1. **克隆项目**
   - 仓库：https://github.com/putyy/res-downloader
   - 位置：/home/admin/openclaw/workspace/res-downloader
   - 方法：使用 SSH 隧道（socks5://127.0.0.1:1080）

2. **安装 Go**
   - 版本：1.22.0
   - 位置：/usr/local/go
   - 状态：✅ 安装成功

3. **安装 Wails CLI**
   - 版本：2.11.0
   - 方法：使用 GOPROXY=https://goproxy.cn
   - 状态：✅ 安装成功

4. **安装前端依赖**
   - 位置：frontend/
   - 包数：264 个
   - 状态：✅ 安装成功

### ⚠️ 遇到的问题

1. **网络问题**
   - Wails doctor 检查时下载 Go toolchain 超时
   - 错误：dial tcp 142.250.69.177:443: i/o timeout

2. **解决方案**
   - 使用中国代理：GOPROXY=https://goproxy.cn
   - 跳过 doctor 检查，直接尝试编译

### 🔄 待完成

1. **编译项目**
   - 命令：wails build
   - 目标：生成可执行文件

---

## 安装的环境

### Go

```bash
# 安装位置
/usr/local/go/

# 版本
go version go1.22.0 linux/amd64

# 环境变量
export PATH=$PATH:/usr/local/go/bin
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
```

### Wails CLI

```bash
# 安装位置
$HOME/go/bin/wails

# 版本
v2.11.0

# 命令
wails version
```

### Node.js

```bash
# 版本
v24.14.0

# 包管理器
npm 11.9.0
```

---

## 项目信息

### res-downloader

| 项目 | 信息 |
|-----|------|
| **名称** | res-downloader |
| **作者** | putyy |
| **GitHub Stars** | 15,543 ⭐⭐⭐⭐⭐ |
| **语言** | Go + Wails |
| **类型** | 桌面应用 |
| **支持平台** | Windows / macOS / Linux |

### 功能特性

- ✅ 微信视频号、小程序
- ✅ 抖音、快手、小红书
- ✅ m3u8、直播流
- ✅ 酷狗音乐、QQ音乐
- ✅ 代理抓包

---

## 编译步骤

### 1. 进入项目目录

```bash
cd /home/admin/openclaw/workspace/res-downloader
```

### 2. 编译项目

```bash
export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin
export GOPROXY=https://goproxy.cn,direct
wails build
```

### 3. 输出位置

编译完成后，可执行文件在：
```
/home/admin/openclaw/workspace/res-downloader/build/bin/res-downloader
```

---

## 常见问题

### Q: 编译失败怎么办？

**A**: 检查以下几点：
1. Go 版本是否 >= 1.18
2. Wails CLI 是否正确安装
3. Node.js 和 npm 是否可用
4. 前端依赖是否已安装

### Q: 网络问题如何解决？

**A**: 使用中国代理：
```bash
export GOPROXY=https://goproxy.cn,direct
```

### Q: 编译后如何运行？

**A**: 直接运行可执行文件：
```bash
./build/bin/res-downloader
```

---

## 下一步

1. 尝试编译项目
2. 解决编译错误（如果有）
3. 测试运行

---

**当前状态**: 前端依赖安装完成，准备编译 ✅
