# res-downloader 编译记录 - 2026-03-03 19:47

## ✅ 编译成功！

### 编译信息

| 项目 | 信息 |
|-----|------|
| **状态** | ✅ 编译成功 |
| **编译时间** | 1分28秒 |
| **可执行文件** | /home/admin/openclaw/workspace/res-downloader/build/bin/res-downloader |
| **文件大小** | 18M |

---

## 完成步骤

### 1. 克隆项目
```bash
cd /home/admin/openclaw/workspace
git -c http.proxy='socks5://127.0.0.1:1080' clone --depth 1 https://github.com/putyy/res-downloader.git
```
- ✅ 位置：/home/admin/openclaw/workspace/res-downloader
- ✅ 方法：SSH 隧道

### 2. 安装 Go
```bash
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf /tmp/go1.22.0.linux-amd64.tar.gz
```
- ✅ 版本：1.22.0
- ✅ 位置：/usr/local/go

### 3. 安装 Wails CLI
```bash
export GOPROXY=https://goproxy.cn,direct
go install github.com/wailsapp/wails/v2/cmd/wails@latest
```
- ✅ 版本：2.11.0
- ✅ 位置：$HOME/go/bin/wails

### 4. 安装前端依赖
```bash
cd frontend
npm install
```
- ✅ 包数：264 个
- ✅ 位置：frontend/

### 5. 安装编译依赖
```bash
sudo apt-get install -y pkg-config libwebkit2gtk-4.1-dev libgtk-3-dev libglib2.0-dev
```
- ✅ pkg-config：0.29.2
- ✅ libwebkit2gtk-4.1-dev：2.50.4

### 6. 解决版本问题
```bash
# 创建 webkit2gtk-4.0 符号链接
sudo ln -sf /usr/lib/x86_64-linux-gnu/pkgconfig/webkit2gtk-4.1.pc /usr/lib/x86_64-linux-gnu/pkgconfig/webkit2gtk-4.0.pc
```
- ✅ 符号链接创建成功

### 7. 编译项目
```bash
export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin
export GOPROXY=https://goproxy.cn,direct
wails build
```
- ✅ 编译时间：1分28秒
- ✅ 输出文件：build/bin/res-downloader
- ✅ 文件大小：18M

---

## 使用方法

### 运行程序

```bash
# 进入项目目录
cd /home/admin/openclaw/workspace/res-downloader

# 运行可执行文件
./build/bin/res-downloader
```

### 使用方法

1. **启动程序**
   ```bash
   ./build/bin/res-downloader
   ```

2. **启动代理**
   - 首页左上角点击"启动代理"
   - 选择要获取的资源类型（默认全部）

3. **获取资源**
   - 在外部打开资源页面（视频号、小程序、网页等）
   - 返回软件首页，即可看到资源列表

---

## 功能特性

| 特性 | 支持 |
|-----|------|
| 微信视频号 | ✅ |
| 小程序 | ✅ |
| 抖音 | ✅ |
| 快手 | ✅ |
| 小红书 | ✅ |
| m3u8 | ✅ |
| 直播流 | ✅ |
| 酷狗音乐 | ✅ |
| QQ音乐 | ✅ |
| 代理抓包 | ✅ |

---

## 遇到的问题和解决方案

### 问题1：网络问题

**错误**：
```
error: RPC failed; curl 16 Error in HTTP2 framing layer
fatal: expected flush after ref listing
```

**解决方案**：使用 SSH 隧道
```bash
git -c http.proxy='socks5://127.0.0.1:1080' clone https://github.com/putyy/res-downloader.git
```

### 问题2：Go toolchain 下载超时

**错误**：
```
dial tcp 142.250.69.177:443: i/o timeout
```

**解决方案**：使用中国代理
```bash
export GOPROXY=https://goproxy.cn,direct
```

### 问题3：pkg-config 未找到

**错误**：
```
pkg-config: executable file not found in $PATH
```

**解决方案**：安装 pkg-config
```bash
sudo apt-get install -y pkg-config libwebkit2gtk-4.1-dev libgtk-3-dev libglib2.0-dev
```

### 问题4：webkit2gtk-4.0 未找到

**错误**：
```
Package webkit2gtk-4.0 was not found in the pkg-config search path.
```

**解决方案**：创建符号链接
```bash
sudo ln -sf /usr/lib/x86_64-linux-gnu/pkgconfig/webkit2gtk-4.1.pc /usr/lib/x86_64-linux-gnu/pkgconfig/webkit2gtk-4.0.pc
```

---

## 环境要求

### 编译环境

| 依赖 | 版本 |
|-----|------|
| Go | 1.22.0 |
| Wails CLI | 2.11.0 |
| Node.js | v24.14.0 |
| npm | 11.9.0 |
| pkg-config | 0.29.2 |
| libwebkit2gtk-4.1-dev | 2.50.4 |
| libgtk-3-dev | - |
| libglib2.0-dev | - |

### 运行环境

- Linux (amd64)
- 需要图形界面支持

---

## 项目信息

| 项目 | 信息 |
|-----|------|
| **名称** | res-downloader |
| **作者** | putyy |
| **GitHub** | https://github.com/putyy/res-downloader |
| **Stars** | 15,543 ⭐⭐⭐⭐⭐ |
| **Forks** | 1,932 |
| **语言** | Go + Wails |
| **开源协议** | Apache-2.0 |

---

## 下一步

1. ✅ 测试运行程序
2. ✅ 验证功能正常
3. ⏳ （可选）创建快捷方式或系统服务

---

**编译完成！** ✅

res-downloader 已成功编译，可以使用了！
