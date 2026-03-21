# 分镜生成器 Skill

基于 MiniMax API 的轻量级分镜生成工具，支持 9 宫格/25 宫格分镜生成、图片切割、编辑与合并导出。

## 功能特性

✅ **生成分镜图片** - 支持 3x3 (9 宫格) 和 5x5 (25 宫格)
✅ **参考图片支持** - 上传参考图片，@ 引用
✅ **自动切割** - 一键切割分镜图片
✅ **单独编辑** - 分离单个分镜进行编辑
✅ **合并导出** - 重新组合并导出
✅ **多风格支持** - 真实、动漫、3D、卡通风格
✅ **轻量级设计** - 无需桌面应用，命令行操作

## 安装

### 依赖安装

```bash
pip install --user requests Pillow numpy
```

### 配置 API Key

```bash
# 方法 1：命令行配置
storyboard-generator config sk-cp-USkP97AOSiAG7SnxdGNFFbeOmBTYhYid2vwIkh4g0CWWcYFhrVwmvirCkw7NrclzFQbiOXUZdM0HJe2gAFiD8zft5RMgxSBY3-TyxsgSLESB21G35ydsa9s

# 方法 2：手动编辑配置文件
~/.storyboard-generator/config.json
```

## 使用方法

### 1. 生成分镜

```bash
# 基础使用 - 9 宫格
storyboard-generator generate \
  --grid 3x3 \
  --prompts "镜头1：远景|镜头2：中景|镜头3：近景|镜头4：特写|镜头5：人物侧面|镜头6：人物正面|镜头7：环境全景|镜头8：道具细节|镜头9：结尾定格"

# 指定风格
storyboard-generator generate \
  --grid 5x5 \
  --style anime \
  --prompts "镜头1|镜头2|镜头3|镜头4|镜头5|..."

# 使用参考图片
storyboard-generator generate \
  --grid 3x3 \
  --image ref.jpg \
  --prompts "镜头1：@ref.jpg 调整角度|镜头2：@ref.jpg 变换场景|..."
```

### 2. 切割分镜

```bash
# 切割生成的分镜图
storyboard-generator cut output.jpg

# 指定输出目录
storyboard-generator cut output.jpg --output ./cuts
```

### 3. 编辑单个分镜

```bash
# 分离某个分镜进行编辑
storyboard-generator edit ./cuts/cell_0_0.jpg --prompt "优化光影效果"

# 使用 MiniMax 重新生成
storyboard-generator regenerate ./cuts/cell_0_0.jpg --prompt "更明亮"
```

### 4. 合并导出

```bash
# 合并所有切割后的图片
storyboard-generator merge ./cuts --grid 3x3

# 合并并导出
storyboard-generator merge ./cuts --grid 3x3 --output merged.jpg

# 复制描述文本
storyboard-generator export-text --output prompts.txt
```

## 参数说明

### generate 命令

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--grid` | 网格大小 (3x3, 5x5) | 3x3 |
| `--prompts` | 分镜提示词，用 \| 分隔 | 必填 |
| `--style` | 图片风格 (real, anime, 3d, cartoon) | real |
| `--image` | 参考图片路径 | 无 |
| `--output` | 输出文件名 | storyboard.jpg |

### cut 命令

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `input` | 输入图片文件 | 必填 |
| `--output` | 输出目录 | ./cuts |
| `--grid` | 网格大小 | 3x3 |

### merge 命令

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `input` | 输入图片目录 | 必填 |
| `--grid` | 网格大小 | 3x3 |
| `--output` | 输出文件名 | merged.jpg |

## 提示词格式

### 基础格式

```
镜头序号：描述内容
```

### 使用参考图片

```
镜头1：@ref.jpg 调整角度
镜头2：@ref.jpg 变换场景
镜头3：@ref.jpg 改变光照
```

### 复杂描述

```
镜头1：远景，城市天际线，夜晚，霓虹灯闪烁
镜头2：中景，街道视角，行人匆匆
镜头3：近景，人物面部，表情惊讶
镜头4：特写，手中物品，发光
镜头5：侧景，人物背影，走向远方
```

## 工作流程

### 完整工作流

```bash
# 1. 生成分镜
storyboard-generator generate \
  --grid 3x3 \
  --prompts "镜头1|镜头2|镜头3|..." \
  --output storyboard.jpg

# 2. 切割分镜
storyboard-generator cut storyboard.jpg --output ./cuts

# 3. 编辑需要的分镜
storyboard-generator edit ./cuts/cell_2_1.jpg --prompt "优化光影"

# 4. 重新合并
storyboard-generator merge ./cuts --grid 3x3 --output final.jpg

# 5. 导出文本
storyboard-generator export-text --output prompts.txt
```

## 配置文件

配置文件位置：`~/.storyboard-generator/config.json`

```json
{
  "apiKey": "sk-cp-...",
  "model": "minimax-image-01",
  "defaultGrid": "3x3",
  "defaultStyle": "real",
  "outputDir": "~/storyboard-output",
  "maxRetries": 3
}
```

## API 说明

本项目使用 MiniMax 图片生成 API：

- **接口**: POST /v1/text/image_generation_v2
- **文档**: https://platform.minimaxi.com/document/guides/image-generation
- **费用**: 按 Token 计费

## 故障排查

### API Key 无效

检查配置文件中的 API Key 是否正确。

### 网络连接失败

检查网络连接，确保能访问 MiniMax API。

### 图片切割失败

确保生成的图片尺寸正确，且网格设置匹配。

### 合并失败

检查切割后的图片数量是否匹配网格大小（3x3 需要 9 张，5x5 需要 25 张）。

## 高级功能

### 批量生成

```bash
# 从文件读取提示词
storyboard-generator generate --prompts-file prompts.txt

# 批量生成多个分镜
for grid in 3x3 5x5; do
  storyboard-generator generate --grid $grid --prompts "..."
done
```

### 自定义风格

```json
{
  "style": {
    "real": {
      "style_setting": "photorealistic",
      "resolution": "1024*1024"
    },
    "anime": {
      "style_setting": "anime",
      "resolution": "1024*1024"
    }
  }
}
```

## 更新日志

### v1.0.0 (2026-03-21)
- ✅ 初始版本发布
- ✅ 支持分镜生成（3x3, 5x5）
- ✅ 支持图片切割和合并
- ✅ 支持参考图片
- ✅ 支持多种风格

## 相关资源

- [MiniMax 官网](https://platform.minimaxi.com/)
- [GitHub 原项目](https://github.com/henjicc/Storyboard-Copilot)
- [分镜师 Skill](storyboard-artist)

---

**创建时间**: 2026-03-21
**作者**: openclaw
**版本**: 1.0.0
