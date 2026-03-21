#!/bin/bash
# 分镜生成器 - 安装脚本

echo "========================================="
echo "   分镜生成器 - 安装脚本"
echo "   版本: 1.0.0"
echo "========================================="
echo ""

# 检查 Python 版本
echo "📋 检查 Python 版本..."
python3 --version
if [ $? -ne 0 ]; then
    echo "❌ 错误: 需要安装 Python 3.8+"
    exit 1
fi

# 安装依赖
echo ""
echo "📦 安装 Python 依赖..."
pip3 install --user requests Pillow numpy

# 创建符号链接
echo ""
echo "🔗 创建命令行工具..."
ln -sf ~/.openclaw/skills/storyboard-generator/storyboard-generator.py ~/.local/bin/storyboard-generator

# 创建配置目录
echo ""
echo "📁 创建配置目录..."
mkdir -p ~/.storyboard-generator

echo ""
echo "✅ 安装完成！"
echo ""
echo "🚀 快速开始："
echo ""
echo "1. 配置 API Key："
echo "   storyboard-generator config <API Key>"
echo ""
echo "2. 生成分镜："
echo "   storyboard-generator generate --grid 3x3 --prompts \"镜头1|镜头2|...|镜头9\""
echo ""
echo "3. 切割分镜："
echo "   storyboard-generator cut <图片文件>"
echo ""
echo "4. 合并分镜："
echo "   storyboard-generator merge <目录> --grid 3x3"
echo ""
echo "📖 查看完整文档："
echo "   cat ~/.openclaw/skills/storyboard-generator/README.md"
echo ""
