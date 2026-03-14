#!/bin/bash
#
# YouTube Access Skill - 测试脚本
#

set -e

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  YouTube Access Skill - 功能测试${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# 测试 1: Cookies 转换
echo -e "${YELLOW}测试 1: Cookies 转换${NC}"
echo "----------------------------------------"
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py \
  /home/admin/Downloads/BestCookier20260314-185155-youtube.com.json \
  --playwright /tmp/test_storage_state.json \
  --netscape /tmp/test_cookies.txt
echo ""

# 测试 2: Cookies 验证
echo -e "${YELLOW}测试 2: Cookies 验证${NC}"
echo "----------------------------------------"
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py \
  /home/admin/Downloads/BestCookier20260314-185155-youtube.com.json \
  --validate
echo ""

# 测试 3: Cookies 信息
echo -e "${YELLOW}测试 3: Cookies 信息${NC}"
echo "----------------------------------------"
python3 ~/.openclaw/skills/youtube-access/yt-cookies-manager.py \
  /home/admin/Downloads/BestCookier20260314-185155-youtube.com.json \
  --info
echo ""

# 测试 4: 验证脚本
echo -e "${YELLOW}测试 4: Cookies 有效性验证${NC}"
echo "----------------------------------------"
~/.openclaw/skills/youtube-access/yt-validate.sh -c /tmp/test_cookies.txt
echo ""

# 测试 5: 下载帮助信息
echo -e "${YELLOW}测试 5: 下载脚本帮助信息${NC}"
echo "----------------------------------------"
~/.openclaw/skills/youtube-access/yt-download.sh --help
echo ""

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  ✅ 所有测试通过！${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${YELLOW}已生成的测试文件:${NC}"
echo -e "  - Playwright 格式: /tmp/test_storage_state.json"
echo -e "  - Netscape 格式: /tmp/test_cookies.txt"
echo ""
echo -e "${YELLOW}使用示例:${NC}"
echo -e "  # 验证 cookies"
echo -e "  ~/.openclaw/skills/youtube-access/yt-validate.sh"
echo ""
echo -e "  # 下载视频"
echo -e "  ~/.openclaw/skills/youtube-access/yt-download.sh \"https://www.youtube.com/watch?v=VIDEO_ID\""
echo ""
