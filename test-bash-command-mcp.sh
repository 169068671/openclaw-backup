#!/bin/bash
# Test Bash Command MCP server

echo "🧪 测试 Bash Command MCP 服务器"
echo "====================="
echo ""

# Test 1: Check if bash-command-mcp is installed
echo "✅ 测试 1：安装检查"
if command -v bash-command-mcp &> /dev/null; then
    version=$(npm list -g bash-command-mcp 2>/dev/null | grep bash-command-mcp | awk '{print $2}')
    echo "✓ Bash Command MCP 已安装"
    echo "  版本: $version"
    echo "  位置: $(which bash-command-mcp)"
else
    echo "✗ Bash Command MCP 未安装"
    exit 1
fi

echo ""

# Test 2: Check if executable
echo "✅ 测试 2：可执行检查"
if [ -x "$(which bash-command-mcp)" ]; then
    echo "✓ Bash Command MCP 可执行"
else
    echo "✗ Bash Command MCP 不可执行"
    exit 1
fi

echo ""

# Test 3: Test startup
echo "✅ 测试 3：启动测试"
echo "启动 Bash Command MCP（3秒测试）..."
timeout 3 bash-command-mcp 2>&1 | head -1
if [ $? -eq 0 ] || [ $? -eq 124 ]; then
    echo "✓ Bash Command MCP 可以启动"
else
    echo "✗ Bash Command MCP 启动失败"
    exit 1
fi

echo ""

# Test 4: Check OpenClaw configuration
echo "✅ 测试 4：OpenClaw 配置检查"
config_file="$HOME/.openclaw/openclaw.json"
if [ -f "$config_file" ]; then
    if grep -q "bash-command-mcp" "$config_file" 2>/dev/null; then
        echo "✓ Bash Command MCP 已在 OpenClaw 中配置"
    else
        echo "⚠️  Bash Command MCP 未在 OpenClaw 中配置"
        echo "   请编辑配置文件：$config_file"
    fi
else
    echo "⚠️  OpenClaw 配置文件未找到：$config_file"
fi

echo ""

# Test 5: Check OpenClaw Gateway status
echo "✅ 测试 5：OpenClaw Gateway 状态"
if command -v openclaw &> /dev/null; then
    echo "✓ OpenClaw 已安装"
    echo "  版本: $(openclaw --version | head -1)"
    echo "  Gateway: $(ps aux | grep openclaw-gateway | grep -v grep | wc -l) 个进程"
else
    echo "⚠️  OpenClaw 未安装"
fi

echo ""
echo "====================="
echo "🎉 所有测试完成！"
echo ""
echo "📝 配置信息："
echo "  - 位置: $(which bash-command-mcp)"
echo "  - 版本: $version"
echo ""
echo "💡 下一步："
echo "  1. 编辑 OpenClaw 配置文件：$config_file"
echo "  2. 添加 bash-command-mcp 配置"
echo "  3. 重启 OpenClaw Gateway: openclaw gateway restart"
echo ""
echo "✅ Bash Command MCP 已准备就绪！"
