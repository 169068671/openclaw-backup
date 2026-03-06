#!/bin/bash

# musicdl 安装脚本
# 支持多种安装方式：pip, 源码

set -e

echo "🎵 musicdl 安装脚本"
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

# 检查 Python 版本
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo "Python 版本: $PYTHON_VERSION"

# 安装选项
echo ""
echo "请选择安装方式："
echo "1) pip (推荐)"
echo "2) 源码安装"
echo "3) 最新版本（pip）"
echo "4) 退出"

read -p "请输入选项 [1-4]: " choice

case $choice in
    1)
        echo ""
        echo "使用 pip 安装 musicdl..."
        pip3 install musicdl
        echo "✅ 安装完成！"
        echo ""
        echo "验证安装..."
        musicdl --version
        ;;
    2)
        echo ""
        echo "从源码安装..."
        echo "需要 Git 和 Python 3.7+"

        # 检查 Git
        if ! command -v git &> /dev/null; then
            echo "❌ Git 未安装"
            echo "   安装命令：sudo apt-get install git"
            exit 1
        fi

        # 检查 Python 版本
        PYTHON_VERSION=$(python3 --version | awk '{print $2}')
        PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
        if [ "$PYTHON_MAJOR" -lt "3" ] || [ "$PYTHON_MAJOR" -eq "3" ] && [ "$(echo $PYTHON_VERSION | cut -d. -f2)" -lt "7" ]; then
            echo "❌ Python 版本过低（需要 3.7+）"
            exit 1
        fi

        # 克隆仓库
        echo "正在克隆 musicdl 仓库..."
        git clone https://github.com/CharlesPikachu/musicdl.git

        # 安装
        echo "正在安装..."
        cd musicdl
        pip3 install .

        echo "✅ 安装完成！"
        echo ""
        echo "验证安装..."
        musicdl --version

        # 返回上级目录
        cd ..
        ;;
    3)
        echo ""
        echo "安装最新版本..."
        pip3 install --upgrade musicdl
        echo "✅ 安装完成！"
        echo ""
        echo "验证安装..."
        musicdl --version
        ;;
    4)
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
echo "  musicdl 歌曲名称"
echo "  musicdl -p 歌单名称"
echo "  musicdl -a 专辑名称"
echo ""
echo "查看支持的平台："
echo "  musicdl --help"
echo ""
echo "更多信息："
echo "  https://musicdl.readthedocs.io/"
echo "  https://github.com/CharlesPikachu/musicdl"
