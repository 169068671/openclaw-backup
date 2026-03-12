#!/bin/bash
# commit.sh - Commit changes without pushing

# Configuration
WORKSPACE="/home/admin/openclaw/workspace"

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

print_info "开始提交流程..."
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

# Step 2: Show changes
print_info "步骤2：查看更改..."
git diff --cached --stat
echo ""

# Step 3: Commit changes
print_info "步骤3：提交更改..."
print_info "提交消息：$MESSAGE"
git commit -m "$MESSAGE"
if [ $? -ne 0 ]; then
    print_error "提交失败"
    exit 1
fi
print_success "提交成功"
echo ""

# Step 4: Show status
print_info "步骤4：查看状态..."
git status
echo ""

# Step 5: Show unpushed commits
print_info "步骤5：查看待推送的提交..."
UNPUSHED=$(git log origin/master..HEAD --oneline | wc -l)
if [ "$UNPUSHED" -eq 0 ]; then
    print_success "所有提交已推送"
else
    print_info "待推送的提交：$UNPUSHED 个"
    echo ""
    git log origin/master..HEAD --oneline
fi

echo ""
print_success "🎉 提交完成！"
echo ""
print_info "提示：运行以下命令推送到 GitHub"
echo "  ~/.openclaw/skills/github-pusher/push.sh"
