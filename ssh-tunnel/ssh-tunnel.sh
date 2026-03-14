#!/bin/bash
# SSH Tunnel Manager
# 通过 SSH 隧道建立 SOCKS5 代理

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 配置
VPS_HOST="76.13.219.143"
VPS_USER="root"
VPS_PASSWORD="Whj001.Whj001"
VPS_NAME="srv1437164"
LOCAL_PORT="1080"
SSH_KEY="$HOME/.ssh/id_rsa"

# Google 测试
GOOGLE_URL="https://www.google.com"
CHECK_TIMEOUT=10

# 获取进程信息
get_ssh_tunnel_pid() {
    ps aux | grep "ssh.*-D.*${LOCAL_PORT}" | grep -v grep | awk '{print $2}' | head -n 1
}

# 获取进程运行时间
get_process_uptime() {
    local pid=$1
    if [ -z "$pid" ]; then
        echo "N/A"
        return
    fi

    # 直接使用 ps 的 etime 参数（已用时间）
    local uptime=$(ps -p "$pid" -o etime= 2>/dev/null | tr -d ' ')
    if [ -z "$uptime" ]; then
        echo "N/A"
    else
        echo "$uptime"
    fi
}

# 测试 Google 连通性
test_google_connectivity() {
    echo ""
    echo "🔍 ${BLUE}测试 Google 连通性...${NC}"

    local result
    result=$(curl --proxy socks5h://127.0.0.1:${LOCAL_PORT} -I -s -o /dev/null -w "%{http_code}" --connect-timeout ${CHECK_TIMEOUT} "${GOOGLE_URL}" 2>&1)
    local exit_code=$?

    if [ $exit_code -eq 0 ]; then
        if [ "$result" = "200" ] || [ "$result" = "301" ] || [ "$result" = "302" ]; then
            echo "   ✅ ${GREEN}测试成功: HTTP ${result}${NC}"
            echo "   说明: VPS 可以访问 Google"
            return 0
        else
            echo "   ⚠️  ${YELLOW}测试异常: HTTP ${result}${NC}"
            echo "   说明: VPS 可以连接 Google，但返回状态异常"
            return 1
        fi
    else
        echo "   ❌ ${RED}测试失败: Connection timed out${NC}"
        echo "   说明: VPS 无法访问 Google（网络限制）"
        echo "   提示: 这是 VPS 网络质量问题，不是隧道配置问题"
        return 1
    fi
}

# 启动隧道
start_tunnel() {
    echo "🚀 ${BLUE}启动 SSH 隧道...${NC}"

    # 检查隧道是否已运行
    local pid=$(get_ssh_tunnel_pid)
    if [ -n "$pid" ]; then
        echo "   ⚠️  ${YELLOW}隧道已在运行 (PID: $pid)${NC}"
        show_status
        return 0
    fi

    # 启动隧道（使用 sshpass 密码认证）
    sshpass -p "${VPS_PASSWORD}" ssh -N -D ${LOCAL_PORT} -f ${VPS_USER}@${VPS_HOST}
    local start_result=$?

    # 等待启动
    sleep 2

    # 检查是否成功
    pid=$(get_ssh_tunnel_pid)
    if [ -n "$pid" ]; then
        echo "   ✅ ${GREEN}隧道启动成功${NC}"
        echo "   PID: $pid"
        echo "   代理: 127.0.0.1:${LOCAL_PORT} (SOCKS5)"

        # 测试 Google 连通性（除非指定 --no-check）
        if [ "$1" != "--no-check" ]; then
            test_google_connectivity
        fi

        show_status
        return 0
    else
        echo "   ❌ ${RED}隧道启动失败${NC}"
        echo "   退出码: $start_result"
        return 1
    fi
}

# 停止隧道
stop_tunnel() {
    echo "🛑 ${BLUE}停止 SSH 隧道...${NC}"

    local pid=$(get_ssh_tunnel_pid)
    if [ -z "$pid" ]; then
        echo "   ℹ️  ${YELLOW}隧道未运行${NC}"
        return 0
    fi

    kill "$pid"
    local kill_result=$?

    # 等待停止
    sleep 1

    # 验证是否停止
    pid=$(get_ssh_tunnel_pid)
    if [ -z "$pid" ]; then
        echo "   ✅ ${GREEN}隧道已停止${NC}"
    else
        echo "   ⚠️  ${YELLOW}停止失败，尝试强制终止...${NC}"
        kill -9 "$pid"
        sleep 1
        pid=$(get_ssh_tunnel_pid)
        if [ -z "$pid" ]; then
            echo "   ✅ ${GREEN}隧道已强制停止${NC}"
        else
            echo "   ❌ ${RED}无法停止隧道 (PID: $pid)${NC}"
            return 1
        fi
    fi
}

# 显示状态
show_status() {
    local pid=$(get_ssh_tunnel_pid)

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    if [ -n "$pid" ]; then
        # 隧道运行中
        echo "🟢 ${GREEN}SSH 隧道状态：运行中${NC}"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "🌐 服务器: ${VPS_HOST} (${VPS_NAME})"
        echo "🔌 本地端口: 127.0.0.1:${LOCAL_PORT} (SOCKS5)"
        echo "👤 用户: ${VPS_USER}"
        echo "🔑 认证: 密码"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

        # 进程信息
        local cpu=$(ps -p "$pid" -o %cpu= 2>/dev/null | tr -d ' ')
        local mem=$(ps -p "$pid" -o %mem= 2>/dev/null | tr -d ' ')
        local uptime=$(get_process_uptime "$pid")

        echo "📊 进程信息:"
        echo "  PID: $pid"
        echo "  CPU: ${cpu}%"
        echo "  MEM: ${mem}%"
        echo "  运行时间: $uptime"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

        # 网络监听
        local ipv4_status="❌"
        local ipv6_status="❌"

        if netstat -tlnp 2>/dev/null | grep -q "127.0.0.1:${LOCAL_PORT}"; then
            ipv4_status="✅"
        fi

        if netstat -tlnp 2>/dev/null | grep -q "\[::1\]:${LOCAL_PORT}"; then
            ipv6_status="✅"
        fi

        echo "🌐 网络监听:"
        echo "  IPv4: 127.0.0.1:${LOCAL_PORT} ${ipv4_status}"
        echo "  IPv6: [::1]:${LOCAL_PORT} ${ipv6_status}"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

        # Google 连通性
        test_google_connectivity
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    else
        # 隧道未运行
        echo "🔴 ${RED}SSH 隧道状态：未运行${NC}"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "提示: 使用以下命令启动隧道"
        echo "  $0 start"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    fi
}

# 重启隧道
restart_tunnel() {
    echo "🔄 ${BLUE}重启 SSH 隧道...${NC}"
    stop_tunnel
    sleep 1
    start_tunnel "$1"
}

# 主函数
main() {
    case "$1" in
        start)
            start_tunnel "$2"
            ;;
        stop)
            stop_tunnel
            ;;
        status)
            show_status
            ;;
        restart)
            restart_tunnel "$2"
            ;;
        *)
            echo "📖 SSH Tunnel Manager - 使用方法"
            echo ""
            echo "用法: $0 {start|stop|status|restart} [--no-check]"
            echo ""
            echo "命令:"
            echo "  start      启动 SSH 隧道（自动测试 Google）"
            echo "  stop       停止 SSH 隧道"
            echo "  status     查看隧道状态"
            echo "  restart    重启 SSH 隧道"
            echo ""
            echo "选项:"
            echo "  --no-check 启动时不测试 Google（加快启动速度）"
            echo ""
            echo "示例:"
            echo "  $0 start              # 启动隧道并测试 Google"
            echo "  $0 start --no-check    # 启动隧道但不测试 Google"
            echo "  $0 stop               # 停止隧道"
            echo "  $0 status             # 查看状态"
            echo "  $0 restart            # 重启隧道"
            echo ""
            echo "配置:"
            echo "  服务器: ${VPS_HOST} (${VPS_NAME})"
            echo "  用户: ${VPS_USER}"
            echo "  本地端口: ${LOCAL_PORT} (SOCKS5)"
            exit 1
            ;;
    esac
}

main "$@"
