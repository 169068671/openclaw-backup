#!/bin/bash

set -e

# 颜色输出
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== OpenCode Docker 部署脚本 ===${NC}"

# 检查 .env 文件
if [ ! -f .env ]; then
    echo -e "${RED}错误: .env 文件不存在${NC}"
    echo "请复制 .env.example 到 .env 并配置 API Key"
    exit 1
fi

# 检查 API Key
if grep -q "your_anthropic_api_key_here\|your_openai_api_key_here" .env; then
    echo -e "${YELLOW}警告: .env 文件中的 API Key 还是示例值${NC}"
    echo "请编辑 .env 文件，填入实际的 API Key"
    read -p "是否继续？(y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# 创建必要目录
echo -e "${GREEN}创建目录...${NC}"
mkdir -p workspace config

# 构建镜像
echo -e "${GREEN}构建 Docker 镜像...${NC}"
docker-compose build

# 完成
echo -e "${GREEN}=== 部署完成！===${NC}"
echo ""
echo "使用方法："
echo "  1. 交互式运行: docker-compose run --rm opencode"
echo "  2. 后台运行:    docker-compose up -d"
echo "  3. 查看日志:    docker-compose logs -f"
echo "  4. 停止容器:    docker-compose down"
echo ""
echo -e "${YELLOW}提示: 首次运行前请确保已配置 .env 文件中的 API Key${NC}"
