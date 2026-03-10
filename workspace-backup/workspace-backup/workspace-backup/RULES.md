# RULES.md - 最高优先级规则

> 这是绝对不能违反的铁律，高于所有其他规则
> 最后更新：2026-03-03

---

## 🚨 第一规则：永不断开连接

**核心理念**：不管做什么设置，一定要确保能再次打开。每次改变后，都要测试连接，确保下次能启动。

### 适用范围

**每次执行以下操作后，必须执行连接测试**：
- ✅ 修改系统配置文件
- ✅ 更新 OpenClaw 配置
- ✅ 修改网络/代理设置
- ✅ 更改 SSH 配置
- ✅ 安装/卸载软件
- ✅ 修改防火墙规则
- ✅ 重启服务
- ✅ 任何可能影响系统稳定性的操作

### 测试清单

#### 1. OpenClaw 服务测试
```bash
# 检查服务状态
systemctl status openclaw-gateway

# 检查进程
ps aux | grep openclaw

# 检查端口
netstat -tuln | grep gateway
```

**预期结果**：
- ✅ 服务状态为 `active (running)`
- ✅ 进程正在运行
- ✅ 端口正常监听

#### 2. 网络连接测试
```bash
# 测试本地网络
ping -c 3 127.0.0.1

# 测试互联网连接
ping -c 3 8.8.8.8

# 测试 GitHub 连接
curl -I https://github.com

# 测试 SSH 连接
ssh -T git@github.com
```

**预期结果**：
- ✅ 本地网络：100% 成功
- ✅ 互联网：低延迟（<100ms）
- ✅ GitHub：HTTP 200
- ✅ SSH：成功认证

#### 3. Git 仓库测试
```bash
# 测试 VPS 备份仓库
ssh root@76.13.219.143 "cd /vps-backup && git status"

# 测试本地仓库
cd /home/admin/openclaw/workspace && git status
```

**预期结果**：
- ✅ VPS：能正常访问仓库
- ✅ 本地：能正常访问仓库

#### 4. SSH 隧道测试（如使用）
```bash
# 检查端口
netstat -tuln | grep 1080

# 测试代理
curl -x socks5://127.0.0.1:1080 -I https://www.google.com
```

**预期结果**：
- ✅ 端口 1080 正常监听
- ✅ 代理能正常访问

#### 5. 文件系统测试
```bash
# 检查磁盘空间
df -h

# 检查重要文件
ls -lh ~/.openclaw/openclaw.json
ls -lh /home/admin/openclaw/workspace/

# 测试读写
echo "test" > /tmp/test && cat /tmp/test && rm /tmp/test
```

**预期结果**：
- ✅ 磁盘空间充足（>10%）
- ✅ 配置文件存在
- ✅ 读写功能正常

### 测试失败处理

**如果任何测试失败**：
1. ❌ 立即停止当前操作
2. 📝 记录失败的测试项
3. 🔧 尝试恢复到之前的状态
4. 📢 向用户报告问题
5. 🚫 不得继续执行其他操作

### 测试通过标志

**所有测试通过后**：
- ✅ 在日志中记录测试通过
- ✅ 继续执行后续操作
- ✅ 更新相关文档

---

## 📋 第二规则：操作前备份

**核心理念**：重要操作前，必须创建备份，以便出错时可以快速恢复。

### 需要备份的操作

- 🔄 修改系统配置文件（`/etc/*`, `~/.config/*`）
- 🔄 修改 OpenClaw 配置（`~/.openclaw/*`）
- 🔄 修改 Git 配置
- 🔄 删除重要文件或目录
- 🔄 重装软件

### 备份方法

```bash
# 方法1：Git提交（推荐）
git add .
git commit -m "备份：$(date +%Y-%m-%d_%H-%M-%S)"

# 方法2：文件复制
cp file file.backup.$(date +%Y%m%d)

# 方法3：完整备份
tar -czf backup-$(date +%Y%m%d-%H%M%S).tar.gz /path/to/important
```

---

## 🎯 第三规则：全局优先级

**规则优先级**：
1. 🔴 **第一优先级**：永不断开连接（本文件）
2. 🔴 **第一优先级**：操作前备份（本文件）
3. 🟡 **第二优先级**：GitHub备份全局配置
4. 🟢 **第三优先级**：代理规则
5. 🔵 **第四优先级**：其他配置规则

**冲突处理**：
- 当第一优先级规则与其他规则冲突时，**必须遵守第一优先级**
- 例如：即使全局规则要求更新配置，如果可能导致断开连接，必须停止

---

## 📝 测试记录模板

每次执行连接测试时，使用以下模板记录：

```markdown
## 连接测试记录 - YYYY-MM-DD HH:MM:SS

### 执行的操作
- [操作描述]

### 测试结果

#### 1. OpenClaw 服务
- [x] 服务状态：active (running)
- [x] 进程运行：正常
- [x] 端口监听：正常

#### 2. 网络连接
- [x] 本地网络：100%
- [x] 互联网：延迟 20ms
- [x] GitHub：HTTP 200
- [x] SSH：成功认证

#### 3. Git 仓库
- [x] VPS备份：正常
- [x] 本地仓库：正常

#### 4. 文件系统
- [x] 磁盘空间：45%
- [x] 配置文件：存在
- [x] 读写功能：正常

### 结论
✅ 所有测试通过，系统状态正常
```

---

## ⚠️ 紧急恢复程序

### 如果 OpenClaw 无法启动

**步骤1：检查服务**
```bash
systemctl status openclaw-gateway
journalctl -u openclaw-gateway -n 50
```

**步骤2：检查配置**
```bash
~/.openclaw/openclaw.json
```

**步骤3：重启服务**
```bash
systemctl restart openclaw-gateway
```

**步骤4：从备份恢复**
```bash
cd /home/admin/openclaw/workspace
git log --oneline -10
git reset --hard <commit-id>
```

### 如果网络无法连接

**步骤1：检查网络配置**
```bash
ping -c 3 8.8.8.8
ip addr
ip route
```

**步骤2：检查代理设置**
```bash
env | grep -i proxy
```

**步骤3：恢复直连**
```bash
unset http_proxy
unset https_proxy
unset HTTP_PROXY
unset HTTPS_PROXY
```

---

## 📌 关键文件位置

| 文件 | 用途 |
|-----|------|
| `RULES.md` | 本文件（最高优先级规则） |
| `SOUL.md` | 个性与行为准则 |
| `TOOLS.md` | 配置与工具信息 |
| `GitHub备份全局配置.md` | 备份系统规则 |

---

## ✅ 检查清单

**每次执行重要操作前，确认**：
- [ ] 已阅读 RULES.md
- [ ] 已理解操作风险
- [ ] 已创建备份
- [ ] 已准备测试方案

**每次执行重要操作后，确认**：
- [ ] 已执行连接测试
- [ ] 所有测试通过
- [ ] 已记录测试结果
- [ ] 已更新相关文档

---

**违反本规则的后果**：
- ❌ 可能导致系统无法启动
- ❌ 可能导致数据丢失
- ❌ 可能导致无法恢复
- ❌ 严重时需要完全重装系统

**遵守本规则的好处**：
- ✅ 系统稳定性提高
- ✅ 问题可快速恢复
- ✅ 用户体验更好
- ✅ 避免重大损失

---

**牢记：第一规则是铁律，永不违反！** 🚨
