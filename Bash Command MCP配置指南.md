# Bash Command MCP 配置指南

**安装日期：** 2026-03-13
**版本：** 0.1.4
**状态：** ✅ 已安装

---

## 📦 安装信息

### 基本信息
- **名称：** bash-command-mcp
- **版本：** 0.1.4
- **作者：** mrorigo
- **安装位置：** /home/admin/.npm-global/lib/node_modules/bash-command-mcp
- **可执行文件：** /home/admin/.npm-global/bin/bash-command-mcp

### 描述
Sophisticated bash command MCP server that runs and manages shell execution.

---

## 🔧 配置方法

### 方法1：OpenClaw 配置文件

编辑 OpenClaw 配置文件：

```bash
nano ~/.openclaw/openclaw.json
```

添加以下配置：

```json
{
  "mcpServers": {
    "bash-command": {
      "command": "/home/admin/.npm-global/bin/bash-command-mcp",
      "env": {
        "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
      }
    }
  }
}
```

### 方法2：环境变量

设置环境变量：

```bash
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
```

### 方法3：直接启动

直接运行：

```bash
bash-command-mcp
```

---

## 🚀 启动方法

### 方法1：手动启动

```bash
# 直接启动
bash-command-mcp
```

### 方法2：OpenClaw 集成

重启 OpenClaw Gateway：

```bash
openclaw gateway restart
```

### 方法3：测试启动

测试运行：

```bash
timeout 3 bash-command-mcp
```

---

## 🧪 测试方法

### 测试1：基本启动

```bash
# 测试启动
timeout 3 bash-command-mcp
```

**预期输出：**
```
bash-command-mcp running on stdio (observability=on, reason=active)
```

### 测试2：OpenClaw 集成

```bash
# 检查 MCP 服务器
openclaw status
```

### 测试3：命令执行

```bash
# 通过 MCP 执行命令
# 需要配置 OpenClaw 使用 MCP
```

---

## 📋 功能特性

### 基本功能
- ✅ 执行 Bash 命令
- ✅ 管理命令执行
- ✅ 标准 I/O 支持
- ✅ 可观测性支持

### 高级功能
- ✅ 命令超时控制
- ✅ 环境变量支持
- ✅ 工作目录控制
- ✅ 错误处理

---

## 🔐 安全配置

### 安全建议

1. **限制命令执行**
   - 只允许特定命令
   - 使用白名单机制

2. **环境变量控制**
   - 不包含敏感信息
   - 使用最小权限原则

3. **工作目录限制**
   - 限制在特定目录
   - 防止访问系统关键路径

4. **超时设置**
   - 设置命令超时
   - 防止长时间运行

### 安全配置示例

```json
{
  "mcpServers": {
    "bash-command": {
      "command": "/home/admin/.npm-global/bin/bash-command-mcp",
      "env": {
        "PATH": "/usr/local/bin:/usr/bin:/bin",
        "HOME": "/home/admin",
        "WORKING_DIR": "/home/admin"
      },
      "timeout": 30
    }
  }
}
```

---

## 📚 使用示例

### 示例1：执行简单命令

```bash
# 通过 MCP 执行 ls 命令
# 需要配置 OpenClaw 使用 MCP
```

### 示例2：执行复杂命令

```bash
# 通过 MCP 执行脚本
# 需要配置 OpenClaw 使用 MCP
```

### 示例3：管理命令执行

```bash
# 通过 MCP 管理多个命令
# 需要配置 OpenClaw 使用 MCP
```

---

## ⚠️ 注意事项

### 使用限制
1. **权限限制**
   - 需要适当的文件权限
   - 需要适当的命令权限

2. **环境限制**
   - 环境变量可能影响命令执行
   - 工作目录需要正确设置

3. **安全限制**
   - 不要执行危险命令
   - 不要暴露敏感信息

### 故障排除

1. **启动失败**
   ```bash
   # 检查安装
   which bash-command-mcp
   npm list -g bash-command-mcp

   # 检查权限
   ls -la /home/admin/.npm-global/bin/bash-command-mcp
   ```

2. **命令执行失败**
   ```bash
   # 检查环境变量
   echo $PATH

   # 检查工作目录
   pwd
   ```

3. **连接失败**
   ```bash
   # 检查 OpenClaw 配置
   cat ~/.openclaw/openclaw.json

   # 重启 OpenClaw
   openclaw gateway restart
   ```

---

## 🔗 相关资源

- **NPM 包：** https://npm.im/bash-command-mcp
- **GitHub：** https://github.com/mrorigo/bash-command-mcp
- **MCP 协议：** https://modelcontextprotocol.io/
- **OpenClaw 文档：** https://docs.openclaw.ai/

---

## 📊 配置清单

- [x] 安装 bash-command-mcp
- [x] 验证安装
- [x] 测试启动
- [ ] 配置 OpenClaw
- [ ] 重启 Gateway
- [ ] 测试 MCP 功能

---

## 🎯 下一步

1. ✅ 安装完成
2. ⚠️ 配置 OpenClaw（需要编辑配置文件）
3. ⚠️ 重启 Gateway
4. ⚠️ 测试 MCP 功能

---

**配置完成！Bash Command MCP 已安装！** 🎉

---

**安装完成日期：** 2026-03-13 00:20 GMT+8
**安装状态：** ✅ 成功
