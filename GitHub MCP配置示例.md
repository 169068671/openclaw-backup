# GitHub MCP 配置示例

**配置日期：** 2026-03-12
**状态：** 配置示例（不包含敏感信息）

---

## 📦 安装 GitHub MCP

```bash
npm install -g github-mcp
```

---

## 🔧 配置步骤

### 步骤1：创建 GitHub Token

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 选择权限：
   - ✅ `repo` - 完整仓库访问权限（推荐）
   - ✅ `public_repo` - 仅公开仓库
4. 生成并复制 token

---

### 步骤2：创建配置文件

```bash
# 创建 GitHub MCP 配置文件
cat > ~/.github-mcp.env <<EOF
# GitHub MCP Configuration
GITHUB_ACCESS_TOKEN=your_github_token_here
EOF

# 设置权限（只有自己可读）
chmod 600 ~/.github-mcp.env
```

---

### 步骤3：启动 GitHub MCP

```bash
# 加载配置
source ~/.github-mcp.env

# 启动 GitHub MCP 服务器
github-mcp
```

---

## 🧪 测试配置

创建测试脚本：

```bash
cat > ~/test-github-mcp.sh <<'SCRIPT'
#!/bin/bash
# Test GitHub MCP server

# Load token from environment variable
if [ -z "$GITHUB_ACCESS_TOKEN" ]; then
    echo "❌ 错误：GITHUB_ACCESS_TOKEN 未设置"
    echo ""
    echo "请先设置环境变量："
    echo "  export GITHUB_ACCESS_TOKEN=your_github_token_here"
    exit 1
fi

echo "🧪 测试 GitHub MCP 服务器"
echo "====================="
echo ""

# Test 1: Check if token is set
echo "✅ 测试 1：环境变量"
if [ -n "$GITHUB_ACCESS_TOKEN" ]; then
    echo "✓ GITHUB_ACCESS_TOKEN 已设置"
    echo "  Token 前缀: ${GITHUB_ACCESS_TOKEN:0:20}..."
else
    echo "✗ GITHUB_ACCESS_TOKEN 未设置"
    exit 1
fi

echo ""

# Test 2: Check if github-mcp is installed
echo "✅ 测试 2：GitHub MCP 安装"
if command -v github-mcp &> /dev/null; then
    version=$(npm list -g github-mcp 2>/dev/null | grep github-mcp | awk '{print $2}')
    echo "✓ GitHub MCP 已安装 (版本: $version)"
else
    echo "✗ GitHub MCP 未安装"
    exit 1
fi

echo ""

# Test 3: Test GitHub API connection
echo "✅ 测试 3：GitHub API 连接"
response=$(curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: token $GITHUB_ACCESS_TOKEN" \
  https://api.github.com/user)

if [ "$response" = "200" ]; then
    echo "✓ GitHub API 连接成功"
    user=$(curl -s -H "Authorization: token $GITHUB_ACCESS_TOKEN" \
      https://api.github.com/user | grep -o '"login":"[^"]*' | cut -d'"' -f4)
    echo "  认证用户: $user"
else
    echo "✗ GitHub API 连接失败 (HTTP $response)"
    exit 1
fi

echo ""

# Test 4: Start GitHub MCP server
echo "✅ 测试 4：GitHub MCP 服务器启动"
echo "启动 GitHub MCP 服务器（5秒测试）..."
timeout 5 github-mcp 2>&1 | head -1
if [ $? -eq 0 ] || [ $? -eq 124 ]; then
    echo "✓ GitHub MCP 服务器可以启动"
else
    echo "✗ GitHub MCP 服务器启动失败"
fi

echo ""
echo "====================="
echo "🎉 所有测试完成！"
SCRIPT

chmod +x ~/test-github-mcp.sh
```

运行测试：

```bash
# 设置 token
export GITHUB_ACCESS_TOKEN="your_github_token_here"

# 运行测试
bash ~/test-github-mcp.sh
```

---

## 🔐 安全提示

### Token 管理
1. **不要分享** Token（这是你的密码）
2. **定期轮换** 每 3-6 个月更换一次
3. **最小权限** 只授予必要的权限
4. **安全存储** 使用受保护的文件

### 不要提交 Token
❌ **错误：**
```bash
GITHUB_ACCESS_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

✅ **正确：**
```bash
GITHUB_ACCESS_TOKEN=your_github_token_here
```

---

## 📚 详细文档

- **GitHub MCP 官方文档：** https://github.com/Seey215/github-mcp
- **GitHub API 文档：** https://docs.github.com/rest
- **Model Context Protocol：** https://modelcontextprotocol.io/

---

## ⚠️ 常见问题

### Q1：如何验证 Token？

```bash
# 测试 GitHub API 连接
curl -H "Authorization: Bearer YOUR_TOKEN" https://api.github.com/user
```

### Q2：Token 有效期多久？

可以设置过期时间：
- 不设置：永不过期（不推荐）
- 7/30/90/180/365 天：推荐设置

### Q3：如何撤销 Token？

1. 访问 https://github.com/settings/tokens
2. 找到 token
3. 点击 "Delete" 或 "Revoke"

---

## 🎯 下一步

1. ✅ 创建 GitHub Token
2. ✅ 创建配置文件 `~/.github-mcp.env`
3. ✅ 运行测试脚本
4. ✅ 启动 GitHub MCP 服务器

---

**配置完成！GitHub MCP 已准备就绪！** 🚀
