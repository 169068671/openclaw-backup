# Whisper 本地安装完成报告

**日期：** 2026-03-02
**安装方式：** 本地安装（Python 虚拟环境）
**模型：** faster-whisper
**状态：** ✅ 安装完成

---

## ✅ 安装完成情况

| 项目 | 状态 | 版本 |
|------|------|------|
| Python 虚拟环境 | ✅ 完成 | - |
| faster-whisper | ✅ 完成 | 1.2.1 |
| ffmpeg | ✅ 完成 | 4.4.2 |
| 转录脚本 | ✅ 完成 | transcribe.py |

---

## 📂 安装位置

| 项目 | 路径 |
|------|------|
| 虚拟环境 | ~/whisper-env |
| Python 解释器 | ~/whisper-env/bin/python3 |
| 转录脚本 | ~/whisper-env/transcribe.py |

---

## 🚀 使用方法

### 1. 激活虚拟环境

```bash
source ~/whisper-env/bin/activate
```

### 2. 转录音频

**基本用法：**
```bash
python3 ~/whisper-env/transcribe.py audio.mp3
```

**指定模型和语言：**
```bash
python3 ~/whisper-env/transcribe.py audio.mp3 small zh
```

**使用不同模型：**
```bash
# 使用 tiny 模型（最快）
python3 ~/whisper-env/transcribe.py audio.mp3 tiny zh

# 使用 medium 模型（更准确）
python3 ~/whisper-env/transcribe.py audio.mp3 medium zh
```

### 3. 自动检测语言

```bash
python3 ~/whisper-env/transcribe.py audio.mp3 small
```

---

## 📋 参数说明

**命令格式：**
```bash
python3 transcribe.py <音频文件> [模型大小] [语言]
```

**参数：**
- `<音频文件>`: 要转录的音频文件（必填）
- `[模型大小]`: 模型大小（可选，默认：small）
  - tiny: 最快，精度最低
  - base: 快，精度一般
  - small: 推荐，平衡速度和精度
  - medium: 准确，速度较慢
  - large: 最准确，速度最慢
- `[语言]`: 语言代码（可选，默认：自动检测）
  - zh: 中文
  - en: 英文
  - 其他 ISO 639-1 语言代码

---

## 🎯 模型对比

| 模型 | 大小 | 速度 | 准确率 | 内存 | 推荐场景 |
|------|------|------|--------|------|----------|
| tiny | ~75MB | ⚡⚡⚡⚡ | ⭐⭐ | ~1GB | 快速测试 |
| base | ~140MB | ⚡⚡⚡ | ⭐⭐⭐ | ~1GB | 一般用途 |
| **small** | **~461MB** | **⚡⚡⚡** | **⭐⭐⭐⭐** | **~2GB** | **推荐** |
| medium | ~1.5GB | ⚡⚡ | ⭐⭐⭐⭐⭐ | ~5GB | 高精度 |
| large | ~3GB | ⚡ | ⭐⭐⭐⭐⭐ | ~10GB | 最高精度 |

---

## 📊 使用示例

### 示例 1：转录中文音频

```bash
source ~/whisper-env/bin/activate
python3 ~/whisper-env/transcribe.py lecture.mp3 small zh
```

### 示例 2：转录英文音频

```bash
source ~/whisper-env/bin/activate
python3 ~/whisper-env/transcribe.py speech.mp3 small en
```

### 示例 3：自动检测语言

```bash
source ~/whisper-env/bin/activate
python3 ~/whisper-env/transcribe.py recording.mp3
```

### 示例 4：快速测试（使用 tiny 模型）

```bash
source ~/whisper-env/bin/activate
python3 ~/whisper-env/transcribe.py test.mp3 tiny
```

---

## 💡 高级用法

### 在 Python 代码中使用

```python
from faster_whisper import WhisperModel

# 加载模型
model = WhisperModel('small', device="cpu", compute_type="int8")

# 转录音频
segments, info = model.transcribe('audio.mp3', language='zh')

# 输出结果
for segment in segments:
    print(f"[{segment.start:.2f} -> {segment.end:.2f}] {segment.text}")
```

### 获取单词级别时间戳

```python
from faster_whisper import WhisperModel

model = WhisperModel('small')
segments, info = model.transcribe('audio.mp3', word_timestamps=True)

for segment in segments:
    for word in segment.words:
        print(f"{word.word} [{word.start:.2f} -> {word.end:.2f}]")
```

---

## 🎵 支持的音频格式

- WAV
- MP3
- M4A
- FLAC
- OGG
- 其他 ffmpeg 支持的格式

---

## 🔧 性能优化

### 使用 GPU（如果有 NVIDIA GPU）

```python
model = WhisperModel('small', device="cuda", compute_type="float16")
```

### 降低 CPU 使用率

```python
model = WhisperModel('small', device="cpu", compute_type="int8", num_workers=1)
```

---

## ❓ 常见问题

### 问题 1：模型下载慢

**解决方案：**
- 模型会自动从 Hugging Face 下载
- 首次使用时可能需要几分钟
- 可以手动下载模型到缓存目录

### 问题 2：内存不足

**解决方案：**
- 使用更小的模型（tiny 或 base）
- 使用 compute_type="int8"
- 降低 num_workers 数量

### 问题 3：识别不准确

**解决方案：**
- 使用更大的模型（medium 或 large）
- 指定正确的语言
- 确保音频质量良好
- 清除背景噪音

### 问题 4：音频格式不支持

**解决方案：**
- 使用 ffmpeg 转换格式
- ```bash
  ffmpeg -i input.wav -ar 16000 output.wav
  ```

---

## 📝 快速开始（3 步）

### 第 1 步：激活虚拟环境

```bash
source ~/whisper-env/bin/activate
```

### 第 2 步：准备音频文件

```bash
# 将音频文件放到当前目录
ls *.mp3
```

### 第 3 步：转录音频

```bash
python3 ~/whisper-env/transcribe.py audio.mp3 small zh
```

---

## ✅ 检查清单

- [ ] Python 虚拟环境已创建
- [ ] faster-whisper 已安装
- [ ] ffmpeg 已安装
- [ ] 转录脚本已创建
- [ ] 已测试转录功能
- [ ] 已添加到 PATH（可选）

---

## 🎉 总结

**安装状态：** ✅ 完成

**可以开始使用：**
```bash
source ~/whisper-env/bin/activate
python3 ~/whisper-env/transcribe.py <音频文件> small zh
```

**推荐配置：**
- 模型：small
- 语言：zh（中文）或自动检测
- 音频格式：MP3/WAV

---

**文档创建时间：** 2026-03-02 19:35 (GMT+8)
**创建人：** openclaw ⚡
