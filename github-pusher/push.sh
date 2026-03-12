#!/bin/bash
# push.sh - Complete git push workflow for openclaw-backup

# Configuration
WORKSPACE="/home/admin/openclaw/workspace"
REMOTE_REPO="git@github.com:169068671/openclaw-backup.git"
BRANCH="master"

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

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Change to workspace directory
cd "$WORKSPACE" || exit 1

# Check if there are any changes
if [ -z "$(git status --porcelain)" ]; then
    print_info "没有需要提交的更改"
    exit 0
fi

# Get commit message
if [ -n "$1" ]; then
    MESSAGE="$1"
else
    # Generate default commit message
    MESSAGE="update $(date +%Y-%m-%d\ %H:%M:%S)"
fi

print_info "开始推送流程..."
echo ""

# Step 1: Add all changes
print_info "步骤1：添加文件..."
git add .
if [ $? -ne 0 ]; then
    print_error "添加文件失败"
    exit 1
fi
print_success "文件添加成功"
echo ""

# Step 2: Commit changes
print_info "步骤2：提交更改..."
print_info "提交消息：$MESSAGE"
git commit -m "$MESSAGE"
if [ $? -ne 0 ]; then
    print_error "提交失败"
    exit 1
fi
print_success "提交成功"
echo ""

# Step 3: Push to GitHub
print_info "步骤3：推送到 GitHub..."
git push origin "$BRANCH" 2>&1
if [ $? -ne 0 ]; then
    print_error "推送失败"
    print_info "请检查网络连接和 SSH 密钥配置"
    exit 1
fi
print_success "推送成功"
echo ""

# Step 4: Verify push
print_info "步骤4：验证推送..."
LOCAL_COUNT=$(git rev-list --count HEAD)
REMOTE_COUNT=$(git rev-list --count origin/"$BRANCH")
if [ "$LOCAL_COUNT" -eq "$REMOTE_COUNT" ]; then
    print_success "推送验证成功"
    print_info "本地提交：$LOCAL_COUNT 个"
    print_info "远程提交：$REMOTE_COUNT 个"
else
    print_warning "推送验证警告"
    print_info "本地提交：$LOCAL_COUNT 个"
    print_info "远程提交：$REMOTE_COUNT 个"
fi

echo ""
print_success "🎉 推送完成！"
echo ""
print_info "GitHub 仓库：https://github.com/169068671/openclaw-backup"
