#!/bin/bash
#
# YouTube Cookies Validator - 验证 YouTube cookies 是否有效
#

set -e

# 默认值
COOKIES_FILE="/tmp/youtube_cookies.txt"
PROXY="socks5h://127.0.0.1:1080"
VERBOSE=false

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 打印帮助信息
print_help() {
    cat << EOF
YouTube Cookies Validator - 验证 YouTube cookies 是否有效

用法: $0 [OPTIONS]

选项:
  -c, --cookies FILE      Cookies 文件路径（默认: $COOKIES_FILE）
  -p, --proxy PROXY       代理地址（默认: $PROXY，使用 'none' 禁用代理）
  -v, --verbose           详细输出
  -h, --help              显示帮助信息

示例:
  # 基本验证
  $0

  # 使用自定义 cookies 文件
  $0 -c ~/Downloads/cookies.txt

  # 不使用代理
  $0 -p none

EOF
}

# 解析命令行参数
while [[ $# -gt 0 ]]; do
    case $1 in
        -c|--cookies)
            COOKIES_FILE="$2"
            shift 2
            ;;
        -p|--proxy)
            PROXY="$2"
            shift 2
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -h|--help)
            print_help
            exit 0
            ;;
        *)
            echo -e "${RED}❌ 错误: 未知选项: $1${NC}"
            echo "使用 -h 或 --help 查看帮助信息"
            exit 1
            ;;
    esac
done

# 检查 cookies 文件是否存在
if [ ! -f "$COOKIES_FILE" ]; then
    echo -e "${RED}❌ 错误: Cookies 文件不存在: $COOKIES_FILE${NC}"
    exit 1
fi

# 检查 yt-dlp 是否已安装
if ! command -v yt-dlp &> /dev/null; then
    echo -e "${RED}❌ 错误: yt-dlp 未安装${NC}"
    echo "安装方法: pip install yt-dlp"
    exit 1
fi

# 打印验证信息
echo -e "${GREEN}🔍 开始验证 YouTube cookies${NC}"
echo -e "${YELLOW}Cookies 文件:${NC} $COOKIES_FILE"
echo -e "${YELLOW}代理:${NC} $PROXY"
echo ""

# 测试视频（YouTube 第一个视频）
TEST_VIDEO="https://www.youtube.com/watch?v=jNQXAC9IVRw"

# 构建 yt-dlp 命令
YTDLP_CMD="yt-dlp"

# 添加代理
if [ "$PROXY" != "none" ]; then
    YTDLP_CMD="$YTDLP_CMD --proxy $PROXY"
fi

# 添加 cookies
YTDLP_CMD="$YTDLP_CMD --cookies $COOKIES_FILE"

# 添加 JS runtime 和 EJS 组件
YTDLP_CMD="$YTDLP_CMD --js-runtimes node --remote-components ejs:github"

# 添加模拟模式（不下载）
YTDLP_CMD="$YTDLP_CMD --simulate"

# 添加详细输出
if [ "$VERBOSE" = true ]; then
    YTDLP_CMD="$YTDLP_CMD --verbose"
fi

# 打印视频信息
YTDLP_CMD="$YTDLP_CMD --print \"✅ 登录成功！\\n标题: %(title)s\\n作者: %(uploader)s\\n时长: %(duration)s\\n\""

# 添加视频 URL
YTDLP_CMD="$YTDLP_CMD '$TEST_VIDEO'"

# 执行验证
echo -e "${YELLOW}正在测试视频...${NC}"
echo -e "${YELLOW}视频: Me at the zoo（YouTube 第一个视频）${NC}"
echo ""

if eval $YTDLP_CMD 2>&1 | grep -q "✅ 登录成功"; then
    echo ""
    echo -e "${GREEN}✅ Cookies 验证通过！${NC}"
    echo -e "${GREEN}可以正常访问 YouTube${NC}"
    exit 0
else
    echo ""
    echo -e "${RED}❌ Cookies 验证失败${NC}"
    echo -e "${RED}无法访问 YouTube${NC}"
    exit 1
fi
