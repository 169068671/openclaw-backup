#!/bin/bash
# status.sh - Check Git status and sync status

# Configuration
WORKSPACE="/home/admin/openclaw/workspace"
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

print_header() {
    echo -e "${BLUE}=== $1 ===${NC}"
}

# Change to workspace directory
cd "$WORKSPACE" || exit 1

echo ""
print_header "Git 状态"
echo ""

# Show git status
git status --short

echo ""
print_header "提交历史"
echo ""

# Show local commits
print_info "本地提交（最近 5 个）："
git log --oneline -5

echo ""

# Show remote commits
print_info "远程提交（最近 5 个）："
git log --oneline origin/"$BRANCH" -5

echo ""
print_header "同步状态"
echo ""

# Check sync status
LOCAL_COUNT=$(git rev-list --count HEAD)
REMOTE_COUNT=$(git rev-list --count origin/"$BRANCH")
UNPUSHED=$(git log origin/"$BRANCH"..HEAD --oneline | wc -l)

print_info "本地提交：$LOCAL_COUNT 个"
print_info "远程提交：$REMOTE_COUNT 个"

if [ "$UNPUSHED" -eq 0 ]; then
    print_success "完全同步：没有待推送的提交"
else
    print_info "待推送的提交：$UNPUSHED 个"
    echo ""
    git log origin/"$BRANCH"..HEAD --oneline
fi

echo ""
print_header "远程仓库"
echo ""

git remote -v

echo ""
print_header "GitHub 仓库"
echo ""

print_info "https://github.com/169068671/openclaw-backup"

echo ""
