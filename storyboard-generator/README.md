# 分镜生成器 - 快速开始指南

基于 MiniMax API 的轻量级分镜生成工具，一键生成 9 宫格/25 宫格分镜。

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install --user requests Pillow numpy
```

### 2. 配置 API Key

```bash
# 使用你的 MiniMax API Key
storyboard-generator config sk-cp-USkP97AOSiAG7SnxdGNFFbeOmBTYhYid2vwIkh4g0CWWcYFhrVwmvirCkw7NrclzFQbiOXUZdM0HJe2gAFiD8zft5RMgxSBY3-TyxsgSLESB21G35ydsa9s
```

### 3. 生成分镜

```bash
# 9 宫格分镜
storyboard-generator generate \
  --grid 3x3 \
  --prompts "镜头1：远景|镜头2：中景|镜头3：近景|镜头4：特写|镜头5：人物|镜头6：环境|镜头7：道具|镜头8：动作|镜头9：结尾"
```

## 📖 基础用法

### 生成分镜

```bash
# 3x3 网格（9 宫格）
storyboard-generator generate --grid 3x3 --prompts "镜头1|镜头2|镜头3|..."

# 5x5 网格（25 宫格）
storyboard-generator generate --grid 5x5 --prompts "镜头1|镜头2|镜头3|..."

# 指定风格
storyboard-generator generate --grid 3x3 --style anime --prompts "..."

# 使用参考图片
storyboard-generator generate --grid 3x3 --image ref.jpg --prompts "镜头1：@ref.jpg|..."
```

### 切割分镜

```bash
# 切割生成的图片
storyboard-generator cut output.jpg

# 指定输出目录
storyboard-generator cut output.jpg --output ./cuts
```

### 合并分镜

```bash
# 合并切割后的图片
storyboard-generator merge ./cuts --grid 3x3

# 指定输出文件
storyboard-generator merge ./cuts --grid 3x3 --output final.jpg
```

## 🎯 工作流程示例

### 完整流程

```bash
# 1. 生成分镜
storyboard-generator generate \
  --grid 3x3 \
  --prompts "镜头1：城市远景|镜头2：街道视角|镜头3：人物特写|..." \
  --output storyboard.jpg

# 2. 切割
storyboard-generator cut storyboard.jpg --output ./cuts

# 3. 编辑需要的分镜（手动或用 AI 工具）
# 编辑 ./cuts/cell_1_1.jpg

# 4. 重新合并
storyboard-generator merge ./cuts --grid 3x3 --output final.jpg
```

## 📝 提示词格式

### 基础格式

```
镜头序号：描述内容
```

### 参考图片

```
镜头1：@ref.jpg 调整角度
镜头2：@ref.jpg 变换场景
```

### 完整示例

```
镜头1：远景，城市天际线，夜晚，霓虹灯闪烁
镜头2：中景，街道视角，行人匆匆
镜头3：近景，人物面部，表情惊讶
镜头4：特写，手中物品，发光
镜头5：侧景，人物背影，走向远方
镜头6：全景，环境氛围，紧张感
镜头7：中景，多人场景，对话中
镜头8：特写，关键道具，神秘
镜头9：远景，夕阳西下，结束
```

## ⚙️ 配置文件

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

## 🎨 支持的风格

| 风格 | 说明 |
|------|------|
| `real` | 真实风格（默认） |
| `anime` | 动漫风格 |
| `3d` | 3D 风格 |
| `cartoon` | 卡通风格 |

## 📦 命令参考

| 命令 | 说明 |
|------|------|
| `config` | 配置 MiniMax API Key |
| `generate` | 生成分镜图片 |
| `cut` | 切割分镜图片 |
| `merge` | 合并分镜图片 |
| `edit` | 编辑单个分镜 |
| `regenerate` | 重新生成分镜 |
| `export-text` | 导出提示词文本 |

## ❓ 常见问题

### Q: API Key 在哪里获取？

A: 访问 [MiniMax 官网](https://platform.minimaxi.com/) 注册并获取 API Key。

### Q: 支持哪些网格大小？

A: 支持 3x3（9 宫格）和 5x5（25 宫格）。

### Q: 可以使用参考图片吗？

A: 可以，使用 `--image` 参数指定参考图片，在提示词中用 `@ref.jpg` 引用。

### Q: 如何编辑单个分镜？

A: 使用 `cut` 命令切割后，手动编辑或使用 AI 工具编辑单个图片，然后用 `merge` 重新合并。

## 🔗 相关链接

- [MiniMax 官网](https://platform.minimaxi.com/)
- [MiniMax API 文档](https://platform.minimaxi.com/document/guides/image-generation)
- [GitHub 原项目](https://github.com/henjicc/Storyboard-Copilot)
- [完整文档](SKILL.md)

## 💡 提示

- 提示词越详细，生成效果越好
- 使用参考图片可以保持风格一致
- 网格越大，生成时间越长
- 定期保存中间结果

---

**创建时间**: 2026-03-21
**版本**: 1.0.0
