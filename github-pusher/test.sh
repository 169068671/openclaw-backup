#!/bin/bash
# test.sh - Test Git and GitHub connection

# Configuration
WORKSPACE="/home/admin/openclaw/workspace"
SSH_KEY="$HOME/.ssh/id_ed25519_github"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_header() {
    echo -e "${BLUE}=== $1 ===${NC}"
}

# Test counter
TOTAL_TESTS=0
PASSED_TESTS=0

# Function to run test
run_test() {
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    if eval "$1"; then
        PASSED_TESTS=$((PASSED_TESTS + 1))
        print_success "$2"
        return 0
    else
        print_error "$2"
        return 1
    fi
}

echo ""
print_header "GitHub Pusher 连接测试"
echo ""

# Test 1: Check if workspace exists
print_header "测试1：工作区检查"
if [ -d "$WORKSPACE" ]; then
    run_test "true" "工作区存在：$WORKSPACE"
else
    run_test "false" "工作区不存在：$WORKSPACE"
    exit 1
fi

echo ""

# Test 2: Check if it's a git repository
print_header "测试2：Git 仓库检查"
cd "$WORKSPACE" || exit 1
run_test "git rev-parse --git-dir > /dev/null 2>&1" "Git 仓库有效"

echo ""

# Test 3: Check Git configuration
print_header "测试3：Git 配置检查"
if run_test "git config user.name > /dev/null 2>&1" "Git 用户名已配置"; then
    USERNAME=$(git config user.name)
    print_info "用户名：$USERNAME"
fi

if run_test "git config user.email > /dev/null 2>&1" "Git 邮箱已配置"; then
    EMAIL=$(git config user.email)
    print_info "邮箱：$EMAIL"
fi

echo ""

# Test 4: Check SSH key
print_header "测试4：SSH 密钥检查"
if run_test "[ -f '$SSH_KEY' ]" "SSH 密钥文件存在：$SSH_KEY"; then
    PERMISSIONS=$(stat -c %a "$SSH_KEY" 2>/dev/null || stat -f %A "$SSH_KEY" 2>/dev/null)
    if run_test "[ '$PERMISSIONS' = '600' ]" "SSH 密钥权限正确：$PERMISSIONS"; then
        print_info "预期权限：600"
    else
        print_info "当前权限：$PERMISSIONS（应该为 600）"
    fi
fi

echo ""

# Test 5: Test SSH connection to GitHub
print_header "测试5：GitHub 连接测试"
if run_test "ssh -i '$SSH_KEY' -T git@github.com 2>&1 | grep -q 'successfully authenticated'" "GitHub SSH 连接成功"; then
    print_info "认证方式：SSH 密钥"
fi

echo ""

# Test 6: Check remote repository
print_header "测试6：远程仓库检查"
REMOTE_URL=$(git remote get-url origin 2>/dev/null)
print_info "远程地址：$REMOTE_URL"
# Check if remote URL contains expected elements
if [ -n "$REMOTE_URL" ] && echo "$REMOTE_URL" | grep -q "github.com" && echo "$REMOTE_URL" | grep -q "169068671"; then
    run_test "true" "远程仓库已配置"
else
    run_test "false" "远程仓库未正确配置"
fi

echo ""

# Test 7: Check Git command
print_header "测试7：Git 命令检查"
run_test "command -v git > /dev/null 2>&1" "Git 命令可用"
GIT_VERSION=$(git --version)
print_info "Git 版本：$GIT_VERSION"

echo ""

# Test 8: Check workspace permissions
print_header "测试8：工作区权限检查"
run_test "[ -w '$WORKSPACE' ]" "工作区可写"

echo ""

# Summary
print_header "测试总结"
print_info "总测试数：$TOTAL_TESTS"
print_info "通过测试：$PASSED_TESTS"

if [ $PASSED_TESTS -eq $TOTAL_TESTS ]; then
    print_success "🎉 所有测试通过！"
    echo ""
    print_info "你可以使用以下命令推送："
    echo "  ~/.openclaw/skills/github-pusher/push.sh \"your message\""
    exit 0
else
    FAILED_TESTS=$((TOTAL_TESTS - PASSED_TESTS))
    print_error "测试失败：$FAILED_TESTS 个"
    echo ""
    print_info "请检查失败的测试并修复问题"
    exit 1
fi
