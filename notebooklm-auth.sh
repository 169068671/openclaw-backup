#!/bin/bash
# NotebookLM 认证脚本 - 一键式认证

set -e

echo "🔑 NotebookLM 认证脚本"
echo "===================="
echo ""

# 检查 Chrome 是否运行
if ! pgrep -x chrome > /dev/null; then
    echo "❌ Chrome 未运行"
    echo "请先启动 Chrome 浏览器"
    exit 1
fi

echo "✅ Chrome 正在运行"
echo ""

# 步骤1：导出 Google cookies
echo "1️⃣  正在导出 Google cookies..."
echo "   请确保你已经在 Chrome 中登录 Google 账户"
echo ""

read -p "按 Enter 键继续（或 Ctrl+C 取消）..."

# 尝试导出 cookies
if browser-cookies-exporter .google.com /tmp/google-cookies.txt; then
    echo "✅ Cookies 导出成功"
else
    echo "❌ Cookies 导出失败"
    echo ""
    echo "可能的原因："
    echo "1. 你还没有在 Chrome 中登录 Google"
    echo "2. Cookies 格式发生变化"
    echo ""
    echo "解决方案："
    echo "1. 打开 Chrome"
    echo "2. 访问 https://accounts.google.com 并登录"
    echo "3. 访问 https://notebooklm.google.com 确保可以访问"
    echo "4. 重新运行此脚本"
    exit 1
fi

echo ""

# 步骤2：转换为 Playwright 格式
echo "2️⃣  正在转换为 Playwright 格式..."

SCRIPT_PATH="/home/admin/openclaw/workspace/notebooklm-auth-exporter/notebooklm-auth-exporter/scripts/convert_cookies.py"

if [ -f "$SCRIPT_PATH" ]; then
    python3 "$SCRIPT_PATH" /tmp/google-cookies.txt /tmp/storage_state.json
    echo "✅ 转换成功"
else
    echo "❌ 转换脚本不存在: $SCRIPT_PATH"
    exit 1
fi

echo ""

# 步骤3：部署到 VPS
echo "3️⃣  正在部署到 VPS..."

VPS_HOST="root@76.13.219.143"
VPS_PATH="/root/.config/notebooklm/session.json"

# 创建 VPS 目录
sshpass -p 'Whj001.Whj001' ssh -o StrictHostKeyChecking=no "$VPS_HOST" "mkdir -p /root/.config/notebooklm/"

# 上传文件
if sshpass -p 'Whj001.Whj001' scp -o StrictHostKeyChecking=no /tmp/storage_state.json "$VPS_HOST:$VPS_PATH"; then
    echo "✅ 部署成功"
else
    echo "❌ 部署失败"
    exit 1
fi

echo ""

# 步骤4：验证认证
echo "4️⃣  正在验证认证..."

VERIFICATION=$(sshpass -p 'Whj001.Whj001' ssh -o StrictHostKeyChecking=no "$VPS_HOST" "notebooklm list" 2>&1)

if echo "$VERIFICATION" | grep -q "Error"; then
    echo "⚠️  验证失败，但文件已部署"
    echo ""
    echo "错误信息："
    echo "$VERIFICATION" | head -5
    echo ""
    echo "可能的原因："
    echo "1. Cookies 已过期"
    echo "2. 需要额外的认证步骤"
    echo ""
    echo "你可以尝试："
    echo "1. 在 Chrome 中重新登录 Google"
    echo "2. 等待一段时间后重试"
    echo "3. 手动在 VPS 上运行: notebooklm login"
else
    echo "✅ 认证成功！"
    echo ""
    echo "笔记本列表："
    echo "$VERIFICATION" | head -10
fi

echo ""
echo "===================="
echo "✅ 认证流程完成！"
echo ""
echo "📖 使用指南："
echo "  ssh root@76.13.219.143"
echo "  notebooklm create \"我的笔记本\""
echo "  notebooklm source add \"URL\""
echo "  notebooklm generate audio --wait"
