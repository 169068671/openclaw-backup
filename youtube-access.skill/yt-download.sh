#!/bin/bash
#
# YouTube Video Downloader - 使用 cookies 下载 YouTube 视频
#

set -e

# 默认值
COOKIES_FILE="/tmp/youtube_cookies.txt"
PROXY="socks5h://127.0.0.1:1080"
OUTPUT_DIR="/tmp"
FORMAT="bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
SUBTITLES=false
VERBOSE=false

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 打印帮助信息
print_help() {
    cat << EOF
YouTube Video Downloader - 使用 cookies 下载 YouTube 视频

用法: $0 [OPTIONS] <VIDEO_URL>

选项:
  -c, --cookies FILE      Cookies 文件路径（默认: $COOKIES_FILE）
  -p, --proxy PROXY       代理地址（默认: $PROXY，使用 'none' 禁用代理）
  -o, --output DIR        输出目录（默认: $OUTPUT_DIR）
  -f, --format FORMAT     视频格式（默认: $FORMAT）
  -s, --subtitles         下载字幕
  -v, --verbose           详细输出
  -h, --help              显示帮助信息

示例:
  # 基本下载
  $0 "https://www.youtube.com/watch?v=VIDEO_ID"

  # 使用自定义 cookies 文件
  $0 -c ~/Downloads/cookies.txt "https://www.youtube.com/watch?v=VIDEO_ID"

  # 不使用代理
  $0 -p none "https://www.youtube.com/watch?v=VIDEO_ID"

  # 下载字幕
  $0 -s "https://www.youtube.com/watch?v=VIDEO_ID"

  # 指定输出目录
  $0 -o ~/Videos "https://www.youtube.com/watch?v=VIDEO_ID"

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
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -f|--format)
            FORMAT="$2"
            shift 2
            ;;
        -s|--subtitles)
            SUBTITLES=true
            shift
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
            VIDEO_URL="$1"
            shift
            ;;
    esac
done

# 检查是否提供了视频 URL
if [ -z "$VIDEO_URL" ]; then
    echo -e "${RED}❌ 错误: 未提供视频 URL${NC}"
    echo "使用 -h 或 --help 查看帮助信息"
    exit 1
fi

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

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

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

# 添加输出目录
YTDLP_CMD="$YTDLP_CMD -o '$OUTPUT_DIR/%(title)s.%(ext)s'"

# 添加格式
YTDLP_CMD="$YTDLP_CMD -f '$FORMAT'"

# 添加字幕
if [ "$SUBTITLES" = true ]; then
    YTDLP_CMD="$YTDLP_CMD --write-subs --sub-langs zh-Hans,zh-Hant,en"
fi

# 添加详细输出
if [ "$VERBOSE" = true ]; then
    YTDLP_CMD="$YTDLP_CMD --verbose"
fi

# 添加视频 URL
YTDLP_CMD="$YTDLP_CMD '$VIDEO_URL'"

# 打印下载信息
echo -e "${GREEN}🎬 开始下载 YouTube 视频${NC}"
echo -e "${YELLOW}视频 URL:${NC} $VIDEO_URL"
echo -e "${YELLOW}Cookies:${NC} $COOKIES_FILE"
echo -e "${YELLOW}代理:${NC} $PROXY"
echo -e "${YELLOW}输出目录:${NC} $OUTPUT_DIR"
echo ""

# 执行下载
eval $YTDLP_CMD

# 检查退出状态
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ 下载完成！${NC}"
    echo -e "${GREEN}文件保存在: $OUTPUT_DIR${NC}"
else
    echo ""
    echo -e "${RED}❌ 下载失败${NC}"
    exit 1
fi
