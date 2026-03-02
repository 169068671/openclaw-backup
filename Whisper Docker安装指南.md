# Whisper Docker 安装指南

**日期：** 2026-03-02
**模型：** Whisper Small
**目标：** 使用 Docker 安装 Whisper

---

## 📋 目录

1. [Docker 安装](#docker-安装)
2. [Whisper Docker 镜像选择](#whisper-docker-镜像选择)
3. [安装 Whisper Small 模型](#安装-whisper-small-模型)
4. [使用 Whisper](#使用-whisper)
5. [常见问题](#常见问题)

---

## Docker 安装

### Ubuntu 22.04 安装 Docker

```bash
# 更新包索引
sudo apt update

# 安装依赖
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release

# 添加 Docker 官方 GPG 密钥
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 添加 Docker 仓库
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 更新包索引
sudo apt update

# 安装 Docker
sudo apt install -y docker-ce docker-ce-cli containerd.io

# 将当前用户添加到 docker 组
sudo usermod -aG docker $USER

# 重新登录使组权限生效
```

**重新登录后验证：**
```bash
docker --version
docker run hello-world
```

---

## Whisper Docker 镜像选择

### 推荐镜像对比

| 镜像 | 大小 | 优势 | 劣势 | 推荐度 |
|------|------|------|------|--------|
| guillaumekln/faster-whisper | ~1GB | 性能好、速度快 | 需要 CTranslate2 | ⭐⭐⭐⭐⭐ |
| openai/whisper | 较大 | 官方支持 | 性能一般 | ⭐⭐⭐ |
| home-assistant/amd64-whisper | ~2GB | Home Assistant 集成 | 较大 | ⭐⭐⭐⭐ |

### 推荐方案：faster-whisper

**优势：**
- ✅ 性能更好（比原版快 4 倍以上）
- ✅ 支持 CPU 和 GPU
- ✅ 支持所有模型大小
- ✅ 内存占用更小
- ✅ 有 Docker 镜像

**Docker Hub：** https://hub.docker.com/r/guillaumekln/faster-whisper

---

## 安装 Whisper Small 模型

### 方法 1：使用 faster-whisper Docker（推荐）

```bash
# 拉取镜像
docker pull guillaumekln/faster-whisper

# 验证镜像
docker images | grep faster-whisper
```

### 方法 2：使用 openai/whisper Docker

```bash
# 拉取镜像（如果存在）
docker pull openai/whisper

# 或者使用社区镜像
docker pull niklasvh/whisper-gpu
```

---

## 使用 Whisper

### 1. 基本使用（faster-whisper）

**转录音频文件：**
```bash
docker run --rm -v $(pwd):/app guillaumekln/faster-whisper:latest --model small /app/audio.mp3
```

**参数说明：**
- `--rm`：容器运行后自动删除
- `-v $(pwd):/app`：挂载当前目录到容器
- `--model small`：使用 small 模型
- `/app/audio.mp3`：音频文件路径

### 2. 指定输出格式

**输出为文本：**
```bash
docker run --rm -v $(pwd):/app guillaumekln/faster-whisper:latest --model small --output_format txt /app/audio.mp3
```

**输出为 SRT 字幕：**
```bash
docker run --rm -v $(pwd):/app guillaumekln/faster-whisper:latest --model small --output_format srt /app/audio.mp3
```

**输出为 VTT 字幕：**
```bash
docker run --rm -v $(pwd):/app guillaumekln/faster-whisper:latest --model small --output_format vtt /app/audio.mp3
```

### 3. 中文音频转录

**指定中文：**
```bash
docker run --rm -v $(pwd):/app guillaumekln/faster-whisper:latest --model small --language zh /app/audio.mp3
```

**自动检测语言：**
```bash
docker run --rm -v $(pwd):/app guillaumekln/faster-whisper:latest --model small --task transcribe /app/audio.mp3
```

### 4. 使用 GPU（如果有）

**启用 GPU：**
```bash
docker run --rm --gpus all -v $(pwd):/app guillaumekln/faster-whisper:latest --model small --compute_type float16 /app/audio.mp3
```

### 5. 其他常用参数

```bash
docker run --rm -v $(pwd):/app guillaumekln/faster-whisper:latest \
  --model small \
  --language zh \
  --task transcribe \
  --output_format srt \
  --word_timestamps true \
  /app/audio.mp3
```

**参数说明：**
- `--model`：模型大小（tiny, base, small, medium, large）
- `--language`：语言代码（zh=中文, en=英文, auto=自动）
- `--task`：任务类型（transcribe=转录, translate=翻译）
- `--output_format`：输出格式（txt, srt, vtt, json）
- `--word_timestamps`：是否显示单词级别时间戳
- `--compute_type`：计算类型（int8, float16, float32）

---

## Whisper 模型对比

| 模型 | 参数量 | 大小 | 速度 | 准确率 | 内存 | 推荐场景 |
|------|--------|------|------|--------|------|----------|
| tiny | 39M | ~75MB | ⚡⚡⚡⚡ | ⭐⭐ | ~1GB | 快速测试 |
| base | 74M | ~140MB | ⚡⚡⚡ | ⭐⭐⭐ | ~1GB | 一般用途 |
| **small** | **244M** | **~461MB** | **⚡⚡⚡** | **⭐⭐⭐⭐** | **~2GB** | **推荐** |
| medium | 769M | ~1.5GB | ⚡⚡ | ⭐⭐⭐⭐⭐ | ~5GB | 高精度 |
| large | 1550M | ~3GB | ⚡ | ⭐⭐⭐⭐⭐ | ~10GB | 最高精度 |

**推荐：** small 模型在速度和准确率之间有很好的平衡。

---

## 实际使用示例

### 示例 1：转录中文音频

```bash
# 准备音频文件
ls -lh audio.mp3

# 转录为 SRT 字幕
docker run --rm -v $(pwd):/app guillaumekln/faster-whisper:latest \
  --model small \
  --language zh \
  --output_format srt \
  /app/audio.mp3

# 查看结果
cat audio.srt
```

### 示例 2：转录英文音频并翻译为中文

```bash
docker run --rm -v $(pwd):/app guillaumekln/faster-whisper:latest \
  --model small \
  --language en \
  --task translate \
  --output_format txt \
  /app/audio.mp3
```

### 示例 3：批量处理多个音频文件

```bash
# 使用脚本批量处理
for file in *.mp3; do
  echo "Processing $file..."
  docker run --rm -v $(pwd):/app guillaumekln/faster-whisper:latest \
    --model small \
    --language zh \
    --output_format srt \
    /app/$file
done
```

---

## 模型自动下载

**说明：**
- 模型会在首次使用时自动下载
- 下载位置：容器的 `/root/.cache/huggingface/hub/`
- 下载速度取决于网络

**手动下载模型（可选）：**

如果你想预下载模型：

```bash
# 创建下载容器
docker run -it --name whisper-download --rm \
  -v $(pwd):/app \
  guillaumekln/faster-whisper:latest \
  /bin/bash

# 在容器内下载模型
cd /root
python3 -c "from faster_whisper import WhisperModel; WhisperModel('small')"
```

---

## 常见问题

### 问题 1：模型下载慢

**解决方案：**
1. 使用国内镜像源
2. 手动下载模型文件
3. 使用代理

### 问题 2：GPU 不可用

**检查 GPU：**
```bash
nvidia-smi
```

**如果没有 GPU，使用 CPU 版本：**
```bash
docker run --rm -v $(pwd):/app guillaumekln/faster-whisper:latest --model small /app/audio.mp3
```

### 问题 3：内存不足

**解决方案：**
1. 使用更小的模型（base 或 tiny）
2. 降低线程数
3. 增加交换空间

### 问题 4：音频格式不支持

**支持的格式：**
- WAV
- MP3
- M4A
- FLAC
- OGG

**转换格式：**
```bash
# 使用 ffmpeg 转换
ffmpeg -i input.wav -ar 16000 output.wav
```

### 问题 5：中文识别不准确

**解决方案：**
1. 指定语言：`--language zh`
2. 使用更大的模型（medium）
3. 确保音频质量良好

---

## 性能优化

### CPU 优化

```bash
docker run --rm \
  -v $(pwd):/app \
  --cpus 4 \
  guillaumekln/faster-whisper:latest \
  --model small \
  --compute_type int8 \
  /app/audio.mp3
```

### GPU 优化

```bash
docker run --rm \
  --gpus all \
  -v $(pwd):/app \
  guillaumekln/faster-whisper:latest \
  --model small \
  --compute_type float16 \
  /app/audio.mp3
```

---

## 快速开始（3 步）

### 第 1 步：安装 Docker

```bash
sudo apt update && sudo apt install -y docker.io
sudo usermod -aG docker $USER
# 重新登录
```

### 第 2 步：拉取镜像

```bash
docker pull guillaumekln/faster-whisper
```

### 第 3 步：转录音频

```bash
# 准备测试音频
wget https://example.com/audio.mp3

# 转录
docker run --rm -v $(pwd):/app guillaumekln/faster-whisper:latest --model small /app/audio.mp3
```

---

## 📚 相关资源

**官方文档：**
- OpenAI Whisper: https://github.com/openai/whisper
- faster-whisper: https://github.com/SYSTRAN/faster-whisper

**Docker Hub：**
- faster-whisper: https://hub.docker.com/r/guillaumekln/faster-whisper

**模型下载：**
- Hugging Face: https://huggingface.co/guillaumekln/faster-whisper-large-v3

---

## ✅ 检查清单

- [ ] 安装 Docker
- [ ] 添加用户到 docker 组
- [ ] 重新登录
- [ ] 验证 Docker 安装
- [ ] 拉取 faster-whisper 镜像
- [ ] 准备测试音频文件
- [ ] 测试转录功能
- [ ] 根据需要调整参数

---

**文档创建时间：** 2026-03-02
**创建人：** openclaw ⚡
