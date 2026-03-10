#!/bin/bash
# SSH 隧道手动启动脚本

echo "========================================="
echo "SSH 隧道手动启动"
echo "========================================="
echo ""

# 检查是否已有 SSH 隧道在运行
PID=$(pgrep -f "ssh.*1080")
if [ ! -z "$PID" ]; then
    echo "[警告] SSH 隧道已在运行（PID: $PID）"
    echo "正在停止..."
    kill $PID
    sleep 2
fi

# 启动 SSH 隧道
echo "[1/2] 启动 SSH 隧道..."
sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143

# 等待 2 秒
sleep 2

# 检查隧道状态
PID=$(pgrep -f "ssh.*1080")
if [ ! -z "$PID" ]; then
    echo "[2/2] ✅ SSH 隧道已启动（PID: $PID）"
    echo ""
    echo "隧道信息："
    echo "  协议：SOCKS5"
    echo "  地址：127.0.0.1:1080"
    echo "  目标：VPS (76.13.219.143)"
    echo ""
    echo "使用方法："
    echo "  浏览器配置：127.0.0.1:1080 (SOCKS v5)"
    echo "  测试命令：curl --socks5 127.0.0.1:1080 https://www.google.com"
else
    echo "[2/2] ❌ SSH 隧道启动失败"
    echo "请检查："
    echo "  1. VPS 是否在线"
    echo "  2. SSH 密码是否正确"
    echo "  3. 网络连接是否正常"
fi

echo ""
echo "========================================="
echo "完成"
echo "========================================="
