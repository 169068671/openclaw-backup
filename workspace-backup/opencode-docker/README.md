# OpenCode Docker 部署

OpenCode - 开源的 AI 编码代理

## 快速开始

### 1. 配置 API Key

编辑 `.env` 文件，填入你的 API Key：

```bash
nano .env
```

支持以下 AI 提供商：
- **Anthropic** (推荐): `ANTHROPIC_API_KEY`
- **OpenAI**: `OPENAI_API_KEY`
- **Google**: `GOOGLE_API_KEY`

### 2. 构建镜像

```bash
docker-compose build
```

### 3. 运行容器

#### 交互式运行（推荐）

```bash
docker-compose run --rm opencode
```

#### 后台运行

```bash
docker-compose up -d
```

#### 查看日志

```bash
docker-compose logs -f
```

## 目录结构

```
.
├── Dockerfile              # Docker 镜像定义
├── docker-compose.yml      # Docker Compose 配置
├── .env                   # 环境变量配置（包含 API Key）
├── .env.example           # 环境变量模板
├── workspace/             # 工作目录（自动创建）
├── config/                # 配置持久化（自动创建）
└── README.md             # 本文件
```

## 使用方法

### 在容器内使用 opencode

```bash
# 进入容器
docker-compose exec opencode sh

# 使用 opencode
opencode
```

### 直接运行 opencode 命令

```bash
# 交互式运行
docker-compose run --rm opencode opencode

# 查看帮助
docker-compose run --rm opencode opencode --help
```

## 高级配置

### 修改工作目录挂载

编辑 `docker-compose.yml` 中的 `volumes` 部分：

```yaml
volumes:
  - /path/to/your/project:/workspace
```

### 使用不同的 AI 模型

编辑 `.env` 文件：

```bash
OPENCODE_MODEL=claude-3-opus-20240229
# 或
OPENCODE_MODEL=gpt-4-turbo
```

### 网络配置

如果需要从外部访问 opencode 的服务器模式，修改端口映射：

```yaml
ports:
  - "59000:59000"
```

## OpenCode 命令参考

```bash
# 启动 opencode
opencode

# 查看帮助
opencode --help

# 指定工作目录
opencode --path /workspace

# 使用 plan 模式（只读）
opencode --agent plan
```

## 常见问题

### Q: 如何在本地使用 opencode？

A: 直接使用 npm 安装更方便：

```bash
npm install -g opencode-ai
opencode
```

### Q: Docker 方式有什么优势？

A:
- 环境隔离
- 易于部署
- 可在任何支持 Docker 的系统运行
- 配置持久化

### Q: 如何更新 opencode？

A: 重新构建镜像：

```bash
docker-compose build --no-cache
```

## 相关链接

- [OpenCode 官网](https://opencode.ai)
- [GitHub 仓库](https://github.com/anomalyco/opencode)
- [官方文档](https://opencode.ai/docs)
- [Discord 社区](https://opencode.ai/discord)

## 许可证

OpenCode 是开源项目，详见其官方仓库。
