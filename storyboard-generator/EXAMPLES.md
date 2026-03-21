# 分镜生成器 - 使用示例

## 🚀 快速开始（3 步）

```bash
# 1. 配置 API Key
storyboard-generator config sk-cp-USkP97AOSiAG7SnxdGNFFbeOmBTYhYid2vwIkh4g0CWWcYFhrVwmvirCkw7NrclzFQbiOXUZdM0HJe2gAFiD8zft5RMgxSBY3-TyxsgSLESB21G35ydsa9s

# 2. 生成分镜
storyboard-generator generate \
  --grid 3x3 \
  --prompts "镜头1：城市天际线|镜头2：街道视角|镜头3：人物特写|镜头4：手中物品|镜头5：人物背影|镜头6：环境氛围|镜头7：多人场景|镜头8：关键道具|镜头9：夕阳西下" \
  --output my_storyboard.jpg

# 3. 切割分镜
storyboard-generator cut my_storyboard.jpg
```

---

## 📖 常用场景

### 场景 1：快速生成 9 宫格分镜

```bash
storyboard-generator generate \
  --grid 3x3 \
  --prompts "镜头1：开场|镜头2：人物|镜头3：动作|镜头4：近景|镜头5：细节|镜头6：反应|镜头7：对话|镜头8：高潮|镜头9：结束" \
  --output quick_3x3.jpg
```

### 场景 2：生成动漫风格分镜

```bash
storyboard-generator generate \
  --grid 3x3 \
  --style anime \
  --prompts "镜头1：城市|镜头2：校园|镜头3：教室|镜头4：走廊|镜头5：天台|镜头6：夕阳|镜头7：公园|镜头8：海边|镜头9：星空" \
  --output anime_style.jpg
```

### 场景 3：生成 25 宫格分镜

```bash
storyboard-generator generate \
  --grid 5x5 \
  --prompts "镜头1|镜头2|镜头3|镜头4|镜头5|镜头6|镜头7|镜头8|镜头9|镜头10|镜头11|镜头12|镜头13|镜头14|镜头15|镜头16|镜头17|镜头18|镜头19|镜头20|镜头21|镜头22|镜头23|镜头24|镜头25" \
  --output detailed_5x5.jpg
```

### 场景 4：使用参考图片

```bash
# 准备参考图片
ref_image="/path/to/reference.jpg"

# 生成带参考的分镜
storyboard-generator generate \
  --grid 3x3 \
  --image $ref_image \
  --prompts "镜头1：@$ref_image 调整角度|镜头2：@$ref_image 变换场景|镜头3：@$ref_image 改变光照|镜头4：@$ref_image 更换视角|镜头5：@$ref_image 优化构图|镜头6：@$ref_image 调整色调|镜头7：@$ref_image 增加细节|镜头8：@$ref_image 优化人物|镜头9：@$ref_image 最终效果" \
  --output with_reference.jpg
```

### 场景 5：完整工作流

```bash
# 第 1 步：生成分镜
storyboard-generator generate \
  --grid 3x3 \
  --prompts "镜头1：远景|镜头2：中景|镜头3：近景|镜头4：特写|镜头5：人物|镜头6：环境|镜头7：道具|镜头8：动作|镜头9：结尾" \
  --output workflow_step1.jpg

# 第 2 步：切割分镜
storyboard-generator cut workflow_step1.jpg --output ./workflow_cuts

# 第 3 步：编辑单个分镜（手动或用其他工具）
# 这里可以手动编辑 ./workflow_cuts/cell_1_1.jpg

# 第 4 步：重新合并
storyboard-generator merge ./workflow_cuts --grid 3x3 --output workflow_final.jpg
```

---

## 🎯 专业提示词示例

### 1. 城市夜景

```bash
storyboard-generator generate \
  --grid 3x3 \
  --style real \
  --prompts "镜头1：远景，城市天际线，夜晚，霓虹灯闪烁，高楼大厦|镜头2：中景，街道视角，行人匆匆，车流不息|镜头3：近景，人物面部，表情惊讶，瞳孔放大|镜头4：特写，手中物品，发光，蓝光闪烁|镜头5：侧景，人物背影，走向远方，消失在夜色中|镜头6：全景，环境氛围，紧张感，黑暗角落|镜头7：中景，多人场景，对话中，表情严肃|镜头8：特写，关键道具，神秘，金属质感|镜头9：远景，夕阳西下，城市剪影，结束定格"
```

### 2. 动漫校园

```bash
storyboard-generator generate \
  --grid 3x3 \
  --style anime \
  --prompts "镜头1：远景，樱花飞舞，校园入口，樱花树|镜头2：中景，教学楼走廊，阳光透过窗户|镜头3：近景，少女侧脸，发丝微动，微笑|镜头4：特写，手中课本，写着名字|镜头5：侧景，少年背影，奔跑，操场|镜头6：全景，教室全景，同学们，认真听讲|镜头7：中景，讲台，老师粉笔，板书|镜头8：特写，黑板擦，粉笔灰，阳光照射|镜头9：远景，放学铃声，夕阳，校门口"
```

### 3. 3D 游戏场景

```bash
storyboard-generator generate \
  --grid 3x3 \
  --style 3d \
  --prompts "镜头1：远景，神秘森林，古树参天，雾气缭绕|镜头2：中景，主角视角，手持武器，警戒姿态|镜头3：近景，敌人出现，盔甲反光，武器发光|镜头4：特写，护身符，魔法光效，符文闪现|镜头5：侧景，战斗开始，快速移动，残影|镜头6：全景，战场全景，法术特效，爆炸|镜头7：中景，队友支援，治疗光效，生命恢复|镜头8：特写，宝箱，黄金光芒，传说物品|镜头9：远景，BOSS现身，巨龙咆哮，压迫感"
```

---

## 🔧 批量操作

### 批量生成多个分镜

```bash
# 创建脚本 generate_multiple.sh
cat > generate_multiple.sh << 'EOF'
#!/bin/bash
for style in real anime 3d; do
  echo "生成 $style 风格..."
  storyboard-generator generate \
    --grid 3x3 \
    --style $style \
    --prompts "镜头1|镜头2|镜头3|镜头4|镜头5|镜头6|镜头7|镜头8|镜头9" \
    --output "storyboard_${style}.jpg"
done
EOF

chmod +x generate_multiple.sh
./generate_multiple.sh
```

### 批量处理多个分镜

```bash
# 创建脚本 process_all.sh
cat > process_all.sh << 'EOF'
#!/bin/bash
for file in *.jpg; do
  echo "处理 $file..."
  base_name="${file%.jpg}"

  # 切割
  storyboard-generator cut "$file" --output "./${base_name}_cuts"

  # 合并
  storyboard-generator merge "./${base_name}_cuts" --grid 3x3 --output "${base_name}_merged.jpg"
done
EOF

chmod +x process_all.sh
./process_all.sh
```

---

## 📋 提示词格式参考

### 基础格式

```
镜头序号：描述内容
```

### 完整格式

```
镜头1：景别，主体，动作，环境，氛围，细节
```

### 景别参考

| 景别 | 说明 | 示例 |
|------|------|------|
| **远景** | 展现环境、场景 | "远景，城市天际线，夜晚" |
| **全景** | 展现人物和场景关系 | "全景，教室，同学们听讲" |
| **中景** | 展现人物上半身 | "中景，对话场景，表情严肃" |
| **近景** | 展现人物面部表情 | "近景，少女侧脸，发丝微动" |
| **特写** | 展现细节或关键物品 | "特写，手中物品，发光" |

### 风格参考

| 风格 | 关键词 | 示例 |
|------|---------|------|
| **真实** | 摄影、光影、细节 | "真实，摄影级，光影，4K" |
| **动漫** | 赛璐璐、线条、色彩 | "动漫，赛璐璐，鲜艳色彩" |
| **3D** | 建模、渲染、材质 | "3D，高模，PBR材质，光线追踪" |
| **卡通** | 简约、可爱、色彩明亮 | "卡通，扁平化，可爱风格" |

---

## 💡 最佳实践

### 1. 提示词编写

- ✅ **详细描述**: 镜头序号：景别，主体，动作，环境，氛围，细节
- ✅ **保持一致**: 同一场景的分镜，风格保持一致
- ✅ **使用参考**: 重要场景使用参考图片，确保风格统一
- ❌ **避免模糊**: 不要只写"镜头1"，要详细描述

### 2. 工作流程

- ✅ **先草稿**: 先用简单提示词生成草稿，再细化
- ✅ **及时保存**: 每个步骤都保存，避免丢失进度
- ✅ **逐步优化**: 不要指望一次完美，逐步调整
- ✅ **版本管理**: 保存不同版本，方便对比

### 3. 图片处理

- ✅ **高质量**: 使用高分辨率图片（1024x1024）
- ✅ **格式统一**: 统一使用 JPEG 格式，质量 95
- ✅ **命名规范**: 使用清晰的文件名（cell_0_0.jpg）

---

## ❓ 故障排查

### 问题 1：API Key 无效

**错误信息**: `❌ 错误: 请先配置 MiniMax API Key`

**解决方法**:
```bash
storyboard-generator config <你的 API Key>
```

### 问题 2：提示词数量不匹配

**错误信息**: `⚠️  警告: 提示词数量 (7) 与网格大小 (3x3) 不匹配`

**解决方法**:
- 3x3 网格需要 9 个提示词
- 5x5 网格需要 25 个提示词
- 检查提示词是否用 `|` 正确分隔

### 问题 3：切割失败

**错误信息**: `❌ 切割失败: 图片尺寸不匹配`

**解决方法**:
- 确保生成的图片是网格格式
- 检查网格大小是否正确（3x3 或 5x5）
- 确保图片文件完整

### 问题 4：合并失败

**错误信息**: `❌ 错误: 找不到图片 cell_0_0.jpg`

**解决方法**:
- 确保切割步骤成功完成
- 检查切割目录中的文件数量
- 确保文件命名格式正确（cell_0_0.jpg）

---

## 📚 更多资源

- [完整文档](SKILL.md)
- [快速开始](README.md)
- [测试报告](TEST_REPORT.md)
- [MiniMax API 文档](https://platform.minimaxi.com/document/guides/image-generation)
- [GitHub 原项目](https://github.com/henjicc/Storyboard-Copilot)

---

**创建时间**: 2026-03-21
**版本**: 1.0.0
**作者**: openclaw ⚡
