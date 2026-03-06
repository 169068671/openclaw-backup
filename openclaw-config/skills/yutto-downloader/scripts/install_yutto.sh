#!/bin/bash

# Yutto 安装脚本
# 支持多种安装方式：pip, Homebrew, 源码安装

set -e

echo "🧊 Yutto 安装脚本"
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
echo "2) Homebrew (仅 macOS)"
echo "3) 源码安装"
echo "4) 退出"

read -p "请输入选项 [1-4]: " choice

case $choice in
    1)
        echo ""
        echo "使用 pip 安装..."
        pip3 install yutto
        echo "✅ 安装完成！"
        echo ""
        echo "验证安装..."
        yutto --version
        ;;
    2)
        if [ "$MACHINE" != "Mac" ]; then
            echo "❌ 错误：Homebrew 仅支持 macOS"
            exit 1
        fi
        echo ""
        echo "使用 Homebrew 安装..."
        brew tap siguremo/tap
        brew install yutto
        echo "✅ 安装完成！"
        echo ""
        echo "验证安装..."
        yutto --version
        ;;
    3)
        echo ""
        echo "从源码安装..."
        echo "需要 Git 和 Python 3.8+"

        # 检查 Git
        if ! command -v git &> /dev/null; then
            echo "❌ Git 未安装"
            exit 1
        fi

        # 检查 Python
        if ! command -v python3 &> /dev/null; then
            echo "❌ Python3 未安装"
            exit 1
        fi

        # 克隆仓库
        echo "正在克隆 yutto 仓库..."
        git clone https://github.com/yutto-dev/yutto.git

        # 安装
        echo "正在安装..."
        cd yutto
        pip3 install -e .

        echo "✅ 安装完成！"
        echo ""
        echo "验证安装..."
        yutto --version

        # 返回上级目录
        cd ..
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
echo "  yutto https://www.bilibili.com/video/BV1xxxxx/"
echo ""
echo "配置文件："
echo "  在家目录创建 yutto.toml 配置文件"
echo ""
echo "更多信息："
echo "  https://yutto.nyakku.moe/"
