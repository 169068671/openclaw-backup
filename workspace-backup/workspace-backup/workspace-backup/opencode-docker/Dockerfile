FROM node:20-alpine

# 安装必要的系统工具
RUN apk add --no-cache git bash

# 设置工作目录
WORKDIR /workspace

# 创建配置目录
RUN mkdir -p /root/.opencode /workspace

# 安装 opencode
RUN npm install -g opencode-ai@latest

# 暴露端口（opencode 服务器模式）
EXPOSE 59000

# 设置环境变量
ENV NODE_ENV=production
ENV PATH="${PATH}:/root/.npm-global/bin"

# 默认命令
CMD ["sh", "-c", "opencode --help || echo 'OpenCode installed. Run with: docker compose run --rm opencode opencode'"]
