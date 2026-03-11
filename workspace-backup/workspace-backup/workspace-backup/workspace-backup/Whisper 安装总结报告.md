# Whisper 安装总结报告

**日期：** 2026-03-02
**用户：** 王老师
**安装方式：** 本地安装（Python 虚拟环境）

---

## ✅ 已完成

| 项目 | 状态 | 版本 |
|------|------|------|
| Docker 安装 | ✅ 完成 | 29.2.1 |
| Python 虚拟环境 | ✅ 完成 | Python 3.10.12 |
| faster-whisper | ✅ 完成 | 1.2.1 |
| ffmpeg | ✅ 完成 | 4.4.2 |
| 转录脚本 | ✅ 完成 | transcribe.py |
| 测试脚本 | ✅ 完成 | test.sh |

---

## ❌ 未完成

| 项目 | 状态 | 原因 |
|------|------|------|
| Docker 镜像拉取 | ❌ 失败 | 网络超时/403错误 |
| Whisper 模型下载 | ❌ 失败 | 无法连接 Hugging Face |

---

## 📋 安装详情

### 本地安装（成功）

**位置：**
- 虚拟环境：`~/whisper-env/`
- Python 解释器：`~/whisper-env/bin/python3`
- 转录脚本：`~/whisper-env/transcribe.py`
- 测试脚本：`~/whisper-env/test.sh`

**已安装的包：**
- faster-whisper 1.2.1
- ctranslate2 4.7.1
- huggingface-hub 1.5.0
- 其他依赖包

### Docker 镜像拉取（失败）

**尝试的镜像：**
1. guillaumekln/faster-whisper → 403 Forbidden
2. openai/whisper → 仓库不存在
3. algarveu/whisper → 仓库不存在
4. homeassistant/amd64-whisper → 仓库不存在
5. python:3.10-slim → EOF
6. ultralytics/ultralytics → TLS timeout

**失败原因：**
- Docker Hub 网络不稳定
- SSH 隧道速度太慢（300 KB/s）
- 镜像文件太大（>1GB），容易超时

---

## 🎯 当前状态

### 可以使用的功能

**本地安装的 faster-whisper：**
- ✅ Python 虚拟环境已创建
- ✅ faster-whisper 已安装
- ✅ ffmpeg 已安装
- ✅ 转录脚本已创建
- ❌ 模型未下载（需要首次使用时自动下载）

### 需要解决的问题

**模型下载失败：**
- 首次使用需要从 Hugging Face 下载模型
- 网络连接问题导致下载失败
- 模型大小：~461MB (small 模型)

---

## 🚀 使用方法

### 激活虚拟环境

```bash
source ~/whisper-env/bin/activate
```

### 转录音频（模型首次使用会自动下载）

```bash
# 基本用法
python3 ~/whisper-env/transcribe.py audio.mp3

# 指定模型和语言
python3 ~/whisper-env/transcribe.py audio.mp3 small zh
```

**注意：**
- 首次使用时会自动下载模型（~461MB）
- 如果网络连接正常，下载需要几分钟
- 如果下载失败，可以手动下载模型

---

## 🔧 解决方案

### 方案 1：通过 SSH 隧道下载模型

如果 SSH 隧道正在运行，模型应该可以下载：

```bash
# 确保 SSH 隧道正在运行
ps aux | grep "ssh.*1080"

# 如果没有运行，启动隧道
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143

# 配置 Hugging Face 使用代理（如果需要）
export HF_ENDPOINT=https://hf-mirror.com

# 激活虚拟环境
source ~/whisper-env/bin/activate

# 测试模型加载（会自动下载）
python3 ~/whisper-env/test.sh
```

### 方案 2：手动下载模型

如果自动下载失败，可以手动下载：

1. 访问 Hugging Face：
   https://huggingface.co/guillaumekln/faster-whisper-small

2. 下载模型文件到：
   `~/.cache/huggingface/hub/`

3. 重启虚拟环境并测试

### 方案 3：使用更小的模型（网络更稳定）

使用 tiny 模型（~75MB），下载更快：

```bash
source ~/whisper-env/bin/activate
python3 ~/whisper-env/transcribe.py audio.mp3 tiny
```

---

## 📊 文件位置

### 虚拟环境

| 项目 | 路径 |
|------|------|
| 虚拟环境 | ~/whisper-env/ |
| Python | ~/whisper-env/bin/python3 |
| pip | ~/whisper-env/bin/pip |
| 转录脚本 | ~/whisper-env/transcribe.py |
| 测试脚本 | ~/whisper-env/test.sh |

### 模型缓存（首次下载后）

| 模型 | 缓存位置 | 大小 |
|------|---------|------|
| tiny | ~/.cache/huggingface/hub/ | ~75MB |
| base | ~/.cache/huggingface/hub/ | ~140MB |
| small | ~/.cache/huggingface/hub/ | ~461MB |
| medium | ~/.cache/huggingface/hub/ | ~1.5GB |
| large | ~/.cache/huggingface/hub/ | ~3GB |

---

## 🎉 总结

### 安装状态

| 项目 | 状态 |
|------|------|
| Docker | ✅ 已安装 |
| faster-whisper | ✅ 已安装 |
| 转录脚本 | ✅ 已创建 |
| 模型 | ❌ 未下载（需要网络） |

### 下一步

**选项 1：自动下载模型（推荐）**
```bash
# 确保 SSH 隧道正在运行
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143

# 激活虚拟环境
source ~/whisper-env/bin/activate

# 运行测试（会自动下载模型）
bash ~/whisper-env/test.sh
```

**选项 2：手动下载模型**
1. 访问 Hugging Face 下载模型
2. 放置到缓存目录
3. 测试转录功能

**选项 3：使用 tiny 模型（下载更快）**
```bash
source ~/whisper-env/bin/activate
python3 ~/whisper-env/transcribe.py audio.mp3 tiny
```

---

## 📞 技术支持

如果遇到问题：
1. 检查网络连接
2. 确认 SSH 隧道正在运行
3. 查看错误日志
4. 联系技术支持

---

**报告创建时间：** 2026-03-02 22:21 (GMT+8)
**创建人：** openclaw ⚡
