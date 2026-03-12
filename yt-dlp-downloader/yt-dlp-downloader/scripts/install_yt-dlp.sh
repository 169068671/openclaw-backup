#!/bin/bash

# yt-dlp 安装脚本
# 支持多种安装方式：pip, 源码, 预编译二进制

set -e

echo "🎬 yt-dlp 安装脚本"
echo "================================"

# 检测操作系统
OS="$(uname -s)"
case "$OS" in
    Linux*)     MACHINE=Linux;;
    Darwin*)    MACHINE=Mac;;
    CYGWIN*)    MACHINE=Cygwin;;
    MINGW*)     MACHINE=MinGw;;
    *)          MACHINE="UNKNOWN:$OS"
esac

echo "检测到操作系统: $MACHINE"

# 安装选项
echo ""
echo "请选择安装方式："
echo "1) pip (推荐)"
echo "2) pip + FFmpeg (推荐)"
echo "3) 预编译二进制"
echo "4) 源码安装"
echo "5) 退出"

read -p "请输入选项 [1-5]: " choice

case $choice in
    1)
        echo ""
        echo "使用 pip 安装 yt-dlp..."
        pip3 install yt-dlp
        echo "✅ 安装完成！"
        echo ""
        echo "验证安装..."
        yt-dlp --version
        echo ""
        echo "注意：建议安装 FFmpeg 以获得最佳体验"
        ;;
    2)
        echo ""
        echo "使用 pip 安装 yt-dlp + FFmpeg..."

        # 安装 yt-dlp
        echo "安装 yt-dlp..."
        pip3 install yt-dlp

        # 安装 FFmpeg
        echo "安装 FFmpeg..."
        if [ "$MACHINE" = "Linux" ]; then
            sudo apt-get update
            sudo apt-get install -y ffmpeg
        elif [ "$MACHINE" = "Mac" ]; then
            brew install ffmpeg
        else
            echo "⚠️  请手动安装 FFmpeg"
            echo "   Ubuntu/Debian: sudo apt-get install ffmpeg"
            echo "   macOS: brew install ffmpeg"
            echo "   Windows: https://ffmpeg.org/"
        fi

        echo "✅ 安装完成！"
        echo ""
        echo "验证安装..."
        yt-dlp --version
        ffmpeg -version | head -1
        ;;
    3)
        echo ""
        echo "安装预编译二进制..."

        if [ "$MACHINE" = "Linux" ]; then
            echo "下载 Linux 二进制..."
            sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
            sudo chmod a+rx /usr/local/bin/yt-dlp
        elif [ "$MACHINE" = "Mac" ]; then
            echo "使用 Homebrew 安装..."
            brew install yt-dlp
        else
            echo "❌ 不支持的操作系统"
            exit 1
        fi

        echo "✅ 安装完成！"
        echo ""
        echo "验证安装..."
        yt-dlp --version
        ;;
    4)
        echo ""
        echo "从源码安装..."
        echo "需要 Git 和 Python 3.8+"

        # 检查依赖
        if ! command -v git &> /dev/null; then
            echo "❌ Git 未安装"
            exit 1
        fi

        if ! command -v python3 &> /dev/null; then
            echo "❌ Python3 未安装"
            exit 1
        fi

        # 克隆仓库
        echo "正在克隆 yt-dlp 仓库..."
        git clone https://github.com/yt-dlp/yt-dlp.git

        # 安装
        echo "正在安装..."
        cd yt-dlp
        pip3 install .

        echo "✅ 安装完成！"
        echo ""
        echo "验证安装..."
        yt-dlp --version

        # 返回上级目录
        cd ..
        ;;
    5)
        echo "退出安装"
        exit 0
        ;;
    *)
        echo "❌ 无效的选项"
        exit 1
        ;;
esac

echo ""
echo "================================"
echo "安装完成！"
echo ""
echo "快速开始："
echo "  yt-dlp URL"
echo ""
echo "查看支持的网站："
echo "  yt-dlp --list-extractors"
echo ""
echo "更多信息："
echo "  https://github.com/yt-dlp/yt-dlp"
