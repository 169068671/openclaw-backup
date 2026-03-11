# Whisper 安装记录

**日期：** 2026-03-02
**用户：** 王老师
**状态：** Docker 镜像拉取失败，切换到本地安装

---

## 📋 安装过程

### Docker 安装 ✅

| 步骤 | 状态 |
|------|------|
| 安装 Docker | ✅ 完成 |
| Docker 版本 | 29.2.1 |
| 用户组配置 | ✅ 完成 |
| 国内镜像源 | ✅ 已配置 |
| 测试 hello-world | ✅ 成功 |

### Docker 镜像拉取 ❌

**尝试的镜像：**

1. **guillaumekln/faster-whisper**
   - 镜像源 1：403 Forbidden
   - 镜像源 2：403 Forbidden
   - 官方源：网络超时

2. **openai/whisper**
   - 错误：仓库不存在或需要登录

3. **algarveu/whisper**
   - 错误：仓库不存在或需要登录

4. **homeassistant/amd64-whisper**
   - 错误：仓库不存在或需要登录

5. **python:3.10-slim**
   - 错误：EOF（网络问题）

6. **ultralytics/ultralytics**
   - 错误：TLS handshake timeout

**问题原因：**
- Docker Hub 网络不稳定
- SSH 隧道速度太慢（300 KB/s）
- 镜像文件太大（>1GB），容易超时

---

## 🚀 解决方案：本地安装 Whisper

由于 Docker 镜像拉取失败，采用本地安装方案。

### 安装步骤

```bash
# 更新系统
sudo apt update

# 安装 Python 依赖
sudo apt install -y python3-pip python3-venv

# 创建虚拟环境
python3 -m venv ~/whisper-env
source ~/whisper-env/bin/activate

# 升级 pip
pip install --upgrade pip

# 安装 Whisper（使用国内镜像源）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple openai-whisper

# 或者安装 faster-whisper（性能更好）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple faster-whisper

# 安装 ffmpeg（音频处理）
sudo apt install -y ffmpeg
```

---

## 📊 安装方案对比

| 方案 | 优势 | 劣势 | 推荐度 |
|------|------|------|--------|
| **本地安装** | 速度快、稳定 | 占用本地空间 | ⭐⭐⭐⭐⭐ |
| Docker | 隔离性好 | 镜像拉取慢/失败 | ⭐⭐ |

---

## ✅ 推荐方案：本地安装 faster-whisper

**原因：**
1. Docker 镜像拉取太慢（容易超时）
2. 本地安装使用国内 pip 镜像源，速度快
3. faster-whisper 性能更好（比原版快 4 倍）
4. 占用空间更小

---

## 🎯 快速开始

### 安装 faster-whisper

```bash
# 创建虚拟环境
python3 -m venv ~/whisper-env
source ~/whisper-env/bin/activate

# 安装 faster-whisper（清华镜像源）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple faster-whisper

# 安装 ffmpeg
sudo apt install -y ffmpeg
```

### 使用 faster-whisper

```bash
# 激活虚拟环境
source ~/whisper-env/bin/activate

# 转录音频
python3 -c "
from faster_whisper import WhisperModel
model = WhisperModel('small')
segments, info = model.transcribe('audio.mp3', language='zh')
for segment in segments:
    print(f'[{segment.start:.2f} -> {segment.end:.2f}] {segment.text}')
"
```

---

## 📝 下一步操作

### 选项 1：继续尝试 Docker

如果想继续尝试 Docker 镜像，可以：
1. 等待网络更稳定时重试
2. 手动下载镜像文件
3. 使用其他 VPS 拉取后导出镜像

### 选项 2：使用本地安装（推荐）

执行本地安装步骤：
```bash
python3 -m venv ~/whisper-env
source ~/whisper-env/bin/activate
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple faster-whisper
sudo apt install -y ffmpeg
```

---

## 🔍 日志记录

### Docker 镜像拉取失败记录

| 镜像 | 错误 | 时间 |
|------|------|------|
| guillaumekln/faster-whisper | 403 Forbidden | 19:25 |
| openai/whisper | 仓库不存在 | 19:25 |
| algarveu/whisper | 仓库不存在 | 19:25 |
| homeassistant/amd64-whisper | 仓库不存在 | 19:25 |
| python:3.10-slim | EOF | 19:25 |
| ultralytics/ultralytics | TLS timeout | 19:25 |

---

## 💡 建议

**推荐使用本地安装方案：**

1. ✅ 安装速度快（使用国内 pip 镜像源）
2. ✅ 性能好（faster-whisper 比原版快 4 倍）
3. ✅ 稳定可靠
4. ✅ 占用空间小

**如果必须使用 Docker：**
- 建议在网络更稳定时重试
- 或使用其他 VPS 拉取镜像后导入

---

**记录创建时间：** 2026-03-02 19:30 (GMT+8)
**创建人：** openclaw ⚡
