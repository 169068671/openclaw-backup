# CoPaw 完整配置与故障排查指南

**创建时间**: 2026-03-05
**最后更新**: 2026-03-05
**维护人**: openclaw ⚡

---

## 📋 目录

1. [CoPaw 完整配置信息](#1-copaw-完整配置信息)
2. [记忆问题及修复方案](#2-记忆问题及修复方案)
3. [解决问题策略](#3-解决问题策略)
4. [常见问题与解决方法](#4-常见问题与解决方法)
5. [故障排查流程](#5-故障排查流程)
6. [快速修复命令](#6-快速修复命令)

---

## 1. CoPaw 完整配置信息

### 1.1 本地 CoPaw

**基本信息**
- **部署方式**: 直接运行（非 systemd）
- **Web UI**: http://127.0.0.1:8089
- **工作目录**: /home/admin/.copaw/
- **配置文件**: ~/.copaw/config.json

**钉钉机器人**
- **机器人名称**: 本地的 CoPaw 的机器人
- **Client ID**: ding4zn6bwph8ugrgei1
- **Client Secret**: GAtSSvW1UzLsO4PED0q5UWdR5YVLHXsn-h3e30tmwJlcz4CCsjTGZlpawxsZjQek
- **Agent ID**: 4291316103
- **App ID**: 17e303c3-954a-4e86-b095-8088f2492d30
- **Bot Prefix**: [BOT]
- **连接状态**: ✅ 已连接

**LLM 配置**
- **Provider**: aliyun-codingplan
- **API Key**: sk-sp-b8cc74984e064982850e9cd85ed89477
- **Base URL**: https://coding.dashscope.aliyuncs.com/v1
- **模型**: qwen-plus

**服务管理**
```bash
# 启动服务
nohup copaw app --host 0.0.0.0 --port 8089 > /tmp/copaw_local.log 2>&1 &

# 查看进程
ps aux | grep 'copaw app' | grep -v grep

# 停止服务
pkill -f 'copaw app'

# 查看日志
tail -f /tmp/copaw_local.log

# 查看配置
cat ~/.copaw/config.json
```

**配置文件位置**
- `~/.copaw/config.json` - 主配置
- `~/.copaw/AGENTS.md` - 工作区规则（含系统初始化）
- `~/.copaw/PROFILE.md` - 用户资料和重要提醒
- `~/.copaw/MEMORY.md` - 长期记忆

---

### 1.2 VPS CoPaw (Hostinger VPS)

**基本信息**
- **VPS 地址**: 76.13.219.143
- **主机名**: srv1437164
- **SSH 用户**: root
- **SSH 密码**: Whj001.Whj001
- **SSH 连接**: `sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143`

**部署信息**
- **部署方式**: systemd 服务
- **服务名称**: copaw.service
- **Web UI**: http://76.13.219.143:8088
- **工作目录**: /root/.copaw/
- **配置文件**: /root/.copaw/config.json

**钉钉机器人**
- **机器人名称**: HostingerVPS-CoPaw
- **Client ID**: dingcvagqvwxfx5w6kbf
- **Client Secret**: GyCFe_GpNjZWR4cp5NmkRVyaisPkEBvm8anVU9lLFfVZ4yqM_l3i5buKjWnWnbGA
- **Agent ID**: 4312319425
- **App ID**: 3c1268c1-c584-4c10-bc0a-2b382af2aa51
- **Bot Prefix**: [BOT]
- **连接状态**: ✅ 已连接

**LLM 配置**
- **Provider**: aliyun-codingplan
- **API Key**: sk-sp-b8cc74984e064982850e9cd85ed89477
- **Base URL**: https://coding.dashscope.aliyuncs.com/v1
- **模型**: qwen3-max-2026-01-23

**服务管理**
```bash
# SSH 连接
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143

# 查看状态
systemctl status copaw.service

# 启动服务
systemctl start copaw.service

# 停止服务
systemctl stop copaw.service

# 重启服务
systemctl restart copaw.service

# 查看日志
journalctl -u copaw.service -f

# 查看配置
cat /root/.copaw/config.json

# 查看当前 LLM
curl -s http://127.0.0.1:8088/api/models/active
```

**配置文件位置**
- `/root/.copaw/config.json` - 主配置
- `/root/.copaw/AGENTS.md` - 工作区规则（含系统初始化）
- `/root/.copaw/PROFILE.md` - 用户资料和重要提醒
- `/root/.copaw/MEMORY.md` - 长期记忆
- `/etc/systemd/system/copaw.service` - systemd 服务配置

---

### 1.3 钉钉企业信息

**企业信息**
- **企业名称**: 睿墨眼镜
- **Corp ID**: ding4ef6bd48ee3dd8e4a1320dcb25e91351
- **企业 API Token**: e651c00ecdf03464825c2a008524d797

**用户信息**
- **姓名**: 王华军
- **钉钉手机号**: 13851300141
- **钉钉号**: iu7mu8u
- **用户 ID**: 193200103629107416
- **身份**: 睿墨眼镜企业成员

---

### 1.4 钉钉应用列表（三个）

| # | 机器人名称 | Client ID | Agent ID | 部署位置 | 状态 |
|---|-----------|-----------|----------|---------|------|
| 1 | HostingerVPS-CoPaw | dingcvagqvwxfx5w6kbf | 4312319425 | VPS (8088) | ✅ 使用中 |
| 2 | 本地的 CoPaw 的机器人 | ding4zn6bwph8ugrgei1 | 4291316103 | 本地 (8089) | ✅ 使用中 |
| 3 | 王华军 openclaw | dingyscopnptfxm4hg8q | 4291443459 | 本地 (openclaw) | ✅ 使用中 |

---

### 1.5 钉钉开发者后台

**网址**: https://open-dev.dingtalk.com/

**重要操作流程**:

1. **修改应用名称**:
   - 进入应用 → 开发管理 → 应用信息
   - 修改应用名称
   - 应用发布 → 版本管理与发布 → 创建新版本 → 发布

2. **获取 Access Token**:
   ```
   https://oapi.dingtalk.com/gettoken?appkey=CLIENT_ID&appsecret=CLIENT_SECRET
   ```
   - 有效期: 7200 秒（2 小时）

3. **发送消息 API**:
   - URL: https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2
   - 方法: POST
   - Content-Type: application/json

---

## 2. 记忆问题及修复方案

### 2.1 问题描述

**症状**: 每次新会话或重启后，Agent 认为钉钉未配置，需要重新配置。

**影响**:
- 用户反复被要求提供钉钉凭证
- 配置信息不一致
- 用户体验差

---

### 2.2 根本原因

**旧流程（有问题）**:
```
会话开始 → 检查记忆文件 → 发现"未配置" → 重复配置
```

**问题**:
1. 记忆文件是静态的，不会自动更新
2. 实际配置存在但未被读取
3. 记忆与实际配置不同步

---

### 2.3 修复方案（已实施）

**新流程（修复后）**:
```
会话开始 → 读取 config.json → 检查实际配置 → 更新记忆 → 正常工作
```

**核心原则**: **以实际配置为准，记忆文件为辅助**

---

### 2.4 系统初始化流程（AGENTS.md）

每次会话开始时，Agent 必须执行以下步骤：

#### 步骤 1: 读取钉钉配置状态

**读取 config.json**:
```bash
# 本地
cat ~/.copaw/config.json | grep -A 5 'dingtalk'

# VPS
cat /root/.copaw/config.json | grep -A 5 'dingtalk'
```

**检查配置项**:
- `channels.dingtalk.enabled` 是否为 `true`
- `channels.dingtalk.client_id` 是否存在
- `channels.dingtalk.client_secret` 是否存在

**判断标准**:
- 以上三项都存在且 `enabled=true` → **钉钉已配置**
- 否则 → 钉钉未配置

#### 步骤 2: 更新钉钉状态记忆

**如果钉钉已配置**:
- 在 AGENTS.md 或 PROFILE.md 中记录：钉钉已配置并正常运行
- **不要记录** Client Secret（敏感信息）
- 记录 Client ID 和配置文件路径
- 更新 PROFILE.md 的「重要提醒」section

**如果钉钉未配置**:
- 记录：钉钉尚未配置
- 等待用户提供凭证

#### 步骤 3: 检查 LLM 配置

**读取当前 LLM 配置**:
```bash
# 本地
curl -s http://127.0.0.1:8089/api/models/active

# VPS
curl -s http://127.0.0.1:8088/api/models/active
```

**记录**:
- Provider ID
- Model 名称

#### 步骤 4: 总结初始化状态

在会话开始时，输出类似这样的总结：
```
=== 系统初始化 ===
✓ 钉钉通道：已配置 (dingcvagqvwxfx5w6kbf)
✓ LLM：aliyun-codingplan / qwen3-max-2026-01-23
✓ 服务状态：正常运行
===
```

---

### 2.5 配置持久化说明

**配置文件（持久化）**:
- ✅ `~/.copaw/config.json` - 主要配置，重启自动加载
- ✅ 配置不会丢失
- ✅ Agent 每次会话开始时读取此文件

**记忆文件（同步状态）**:
- ✅ AGENTS.md 的初始化流程会在每次会话开始时同步配置
- ✅ 记忆会与实际配置保持一致
- ✅ 每次会话自动更新

---

## 3. 解决问题策略

### 3.1 核心原则

1. **实际配置 > 记忆文件**
   - 优先读取 config.json
   - 记忆文件仅作为状态记录
   - 每次会话开始时同步

2. **预防为主**
   - 初始化流程自动同步
   - 关键信息记录在多个文件
   - 定期备份配置

3. **快速定位**
   - 按照故障排查流程逐步检查
   - 使用快速修复命令
   - 查看日志和配置文件

---

### 3.2 AGENTS.md 的系统初始化流程

**必须包含的初始化步骤**:
1. 读取钉钉配置状态（config.json）
2. 更新钉钉状态记忆（PROFILE.md）
3. 检查 LLM 配置
4. 总结初始化状态

**关键配置**:
```
## 系统初始化（会话开始时必须执行）

每次新会话开始时，必须按以下顺序执行初始化步骤：

### 1. 读取钉钉配置状态
### 2. 更新钉钉状态记忆
### 3. 检查 LLM 配置
### 4. 总结初始化状态
```

---

### 3.3 PROFILE.md 的重要提醒

**必须记录的内容**:
- 用户资料（姓名、称呼、时区）
- 重要提醒 - 钉钉已配置
- 钉钉机器人信息（Client ID、状态）
- 配置文件路径

**示例**:
```
### 重要提醒 - 钉钉已配置

**钉钉机器人（HostingerVPS-CoPaw）：**
- **状态：** ✅ 已配置并正常运行
- **机器人名称：** HostingerVPS-CoPaw
- **Client ID：** dingcvagqvwxfx5w6kbf
- **配置文件：** `~/.copaw/config.json`
- **部署位置：** Hostinger VPS (76.13.219.143:8088)

**重要：**
1. 钉钉机器人**已经配置完成**，不需要重新配置或绑定
2. 配置保存在 `~/.copaw/config.json` 中
3. 重启后会自动加载，配置不会丢失
4. 如果用户询问是否配置钉钉，直接回复"已配置并正常运行"
5. 以 `~/.copaw/config.json` 的实际配置为准
```

---

### 3.4 记忆管理策略

**防止重复写入**:
1. 读取现有内容
2. 检查是否已存在
3. 检查文件大小（>100KB 警告）
4. 只写入新内容
5. 验证写入结果

**记忆文件大小限制**:
- `MEMORY.md`: 建议不超过 100KB
- `memory/YYYY-MM-DD.md`: 建议不超过 50KB

**定期维护**:
- 利用 heartbeat 定期清理
- 归档旧内容
- 去重优化

---

## 4. 常见问题与解决方法

### 4.1 记忆文件重复写入问题

**症状**:
- 记忆文件快速增长（>1MB）
- 同一内容重复多次出现
- 文件中有大量相似但不完全相同的行

**根本原因**:
- 某个工具或脚本逐字符拆解文本并重复写入
- 循环读取同一文件并追加写入
- 没有检查内容是否已存在

**修复步骤**:
1. 立即停止所有文件写入操作
2. 备份问题文件
3. 使用 `sort -u` 去重
4. 手动清理垃圾内容
5. 添加防重复规则

**命令**:
```bash
# 备份
cp MEMORY.md MEMORY.md.backup

# 去重
sort -u MEMORY.md > MEMORY.md.tmp
mv MEMORY.md.tmp MEMORY.md

# 手动清理
```

**预防措施**:
- 写入前检查文件大小
- 使用 grep 检查内容是否已存在
- 不要逐字符或逐行重复文本

---

### 4.2 钉钉配置状态不同步

**症状**:
- 每次会话都认为钉钉未配置
- 需要重复提供凭证
- 记忆与实际配置不一致

**根本原因**:
- 记忆文件是静态的，不会自动更新
- 没有读取实际配置文件
- 初始化流程缺失

**修复步骤**:
1. 检查 config.json 是否存在配置
2. 更新 AGENTS.md 添加系统初始化流程
3. 更新 PROFILE.md 记录重要提醒
4. 每次会话开始时执行初始化

**验证修复**:
```bash
# 重启会话后，检查是否输出
=== 系统初始化 ===
✓ 钉钉通道：已配置 (dingcvagqvwxfx5w6kbf)
✓ LLM：aliyun-codingplan / qwen3-max-2026-01-23
✓ 服务状态：正常运行
===
```

---

### 4.3 CoPaw 服务无法启动

**症状**:
- Web UI 无法访问
- 服务状态显示失败
- 日志显示错误

**排查步骤**:
1. 检查服务状态
2. 查看日志
3. 检查配置文件
4. 检查端口占用

**修复命令**:
```bash
# 检查服务状态
systemctl status copaw.service

# 查看日志
journalctl -u copaw.service -n 50

# 检查端口占用
netstat -tlnp | grep 8088

# 重启服务
systemctl restart copaw.service

# 本地手动启动
nohup copaw app --host 0.0.0.0 --port 8089 > /tmp/copaw_local.log 2>&1 &
```

---

### 4.4 钉钉消息无法发送或接收

**症状**:
- Agent 无法收到钉钉消息
- Agent 无法发送钉钉消息
- 连接状态显示断开

**排查步骤**:
1. 检查钉钉配置是否正确
2. 检查 Client ID 和 Secret 是否正确
3. 检查钉钉应用是否发布
4. 检查网络连接
5. 查看日志

**修复命令**:
```bash
# 检查钉钉配置
cat ~/.copaw/config.json | grep -A 8 'dingtalk'

# 查看日志
tail -f /tmp/copaw_local.log  # 本地
journalctl -u copaw.service -f  # VPS

# 重启服务
pkill -f 'copaw app'  # 本地
systemctl restart copaw.service  # VPS
```

**钉钉开发者后台检查**:
- 应用是否已发布
- 权限是否正确（Card.Streaming.Write、Card.Instance.Write、qyapi_robot_sendmsg）
- Client ID 和 Secret 是否匹配

---

### 4.5 LLM 响应失败

**症状**:
- Agent 无法生成回复
- 错误提示 API 调用失败
- 响应超时

**排查步骤**:
1. 检查 API Key 是否正确
2. 检查网络连接
3. 检查 API 额度
4. 查看日志

**修复命令**:
```bash
# 检查当前 LLM
curl -s http://127.0.0.1:8089/api/models/active  # 本地
curl -s http://127.0.0.1:8088/api/models/active  # VPS

# 测试 API 连接
curl -X POST https://coding.dashscope.aliyuncs.com/v1/chat/completions \
  -H "Authorization: Bearer sk-sp-b8cc74984e064982850e9cd85ed89477" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-plus",
    "messages": [{"role": "user", "content": "test"}]
  }'
```

---

### 4.6 SSH 连接 VPS 失败

**症状**:
- 无法连接到 VPS
- 连接超时
- 密码错误

**排查步骤**:
1. 检查网络连接
2. 检查 VPS 是否在线
3. 检查密码是否正确
4. 检查 SSH 服务是否运行

**修复命令**:
```bash
# 测试网络连接
ping 76.13.219.143

# 测试 SSH 连接
ssh root@76.13.219.143

# 使用 sshpass 自动输入密码
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143

# 查看本地 SSH 隧道状态
netstat -tlnp | grep 1080
```

---

## 5. 故障排查流程

### 5.1 通用的故障排查步骤

1. **确认问题**
   - 明确问题是什么
   - 什么时候发生的
   - 有什么错误信息

2. **检查配置文件**
   - 检查 config.json 是否正确
   - 检查 AGENTS.md 是否有初始化流程
   - 检查 PROFILE.md 是否有重要提醒

3. **查看日志**
   - 本地: `tail -f /tmp/copaw_local.log`
   - VPS: `journalctl -u copaw.service -f`

4. **检查服务状态**
   - 本地: `ps aux | grep 'copaw app'`
   - VPS: `systemctl status copaw.service`

5. **检查网络连接**
   - 检查网络是否正常
   - 检查 VPS 是否可连接
   - 检查端口是否开放

6. **重启服务**
   - 尝试重启服务
   - 观察启动日志
   - 验证问题是否解决

---

### 5.2 钉钉问题排查流程

```
钉钉问题
  ↓
检查 config.json 钉钉配置
  ↓
检查 Client ID 和 Secret
  ↓
检查钉钉开发者后台
  ↓
检查网络连接
  ↓
查看日志
  ↓
重启服务
```

---

### 5.3 LLM 问题排查流程

```
LLM 问题
  ↓
检查当前 LLM 配置
  ↓
检查 API Key
  ↓
测试 API 连接
  ↓
检查网络连接
  ↓
检查 API 额度
  ↓
查看日志
  ↓
重启服务
```

---

### 5.4 记忆问题排查流程

```
记忆问题
  ↓
检查 config.json 实际配置
  ↓
检查 AGENTS.md 初始化流程
  ↓
检查 PROFILE.md 重要提醒
  ↓
检查记忆文件大小
  ↓
检查是否有重复内容
  ↓
去重和清理
  ↓
添加防重复规则
```

---

## 6. 快速修复命令

### 6.1 本地 CoPaw

```bash
# 查看钉钉配置
cat ~/.copaw/config.json | grep -A 8 'dingtalk'

# 查看当前 LLM
curl -s http://127.0.0.1:8089/api/models/active

# 查看服务状态
ps aux | grep 'copaw app' | grep -v grep

# 查看日志
tail -f /tmp/copaw_local.log

# 重启服务
pkill -f 'copaw app'
nohup copaw app --host 0.0.0.0 --port 8089 > /tmp/copaw_local.log 2>&1 &

# 检查配置文件
ls -la ~/.copaw/
cat ~/.copaw/AGENTS.md | grep -A 20 "系统初始化"
cat ~/.copaw/PROFILE.md | grep -A 15 "重要提醒"
```

---

### 6.2 VPS CoPaw

```bash
# SSH 连接
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143

# 查看钉钉配置
cat /root/.copaw/config.json | grep -A 8 'dingtalk'

# 查看当前 LLM
curl -s http://127.0.0.1:8088/api/models/active

# 查看服务状态
systemctl status copaw.service

# 查看日志
journalctl -u copaw.service -f

# 重启服务
systemctl restart copaw.service

# 检查配置文件
ls -la /root/.copaw/
cat /root/.copaw/AGENTS.md | grep -A 20 "系统初始化"
cat /root/.copaw/PROFILE.md | grep -A 15 "重要提醒"
```

---

### 6.3 钉钉配置验证

```bash
# 验证配置完整性
cat ~/.copaw/config.json | jq '.channels.dingtalk'

# 检查必需字段
cat ~/.copaw/config.json | grep -E '"enabled"|"client_id"|"client_secret"' | grep -A 2 dingtalk

# 获取 Access Token（测试）
curl "https://oapi.dingtalk.com/gettoken?appkey=dingcvagqvwxfx5w6kbf&appsecret=GyCFe_GpNjZWR4cp5NmkRVyaisPkEBvm8anVU9lLFfVZ4yqM_l3i5buKjWnWnbGA"
```

---

### 6.4 记忆文件修复

```bash
# 检查文件大小
ls -lh ~/.copaw/MEMORY.md
wc -c ~/.copaw/MEMORY.md

# 查找重复内容
grep -c "钉钉企业完整信息" ~/.copaw/MEMORY.md

# 备份
cp ~/.copaw/MEMORY.md ~/.copaw/MEMORY.md.backup

# 去重
sort -u ~/.copaw/MEMORY.md > ~/.copaw/MEMORY.md.tmp
mv ~/.copaw/MEMORY.md.tmp ~/.copaw/MEMORY.md
```

---

### 6.5 网络测试

```bash
# 测试网络连接
ping 8.8.8.8
ping 76.13.219.143

# 测试 SSH 连接
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143 "echo 'Connection OK'"

# 测试 Web UI
curl -I http://127.0.0.1:8089  # 本地
curl -I http://76.13.219.143:8088  # VPS

# 测试 LLM API
curl -X POST https://coding.dashscope.aliyuncs.com/v1/chat/completions \
  -H "Authorization: Bearer sk-sp-b8cc74984e064982850e9cd85ed89477" \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen-plus", "messages": [{"role": "user", "content": "test"}]}'
```

---

## 7. 配置文件模板

### 7.1 AGENTS.md 系统初始化部分

```markdown
## 系统初始化（会话开始时必须执行）

每次新会话开始时，必须按以下顺序执行初始化步骤：

### 1. 读取钉钉配置状态

**读取 `~/.copaw/config.json` 中的钉钉配置：**
```bash
execute_shell_command(command="cat ~/.copaw/config.json | grep -A 5 'dingtalk'")
```

**检查配置项：**
- `channels.dingtalk.enabled` 是否为 `true`
- `channels.dingtalk.client_id` 是否存在
- `channels.dingtalk.client_secret` 是否存在

**判断标准：**
- 如果以上三项都存在且 enabled=true，则**钉钉已配置**
- 否则，钉钉未配置

### 2. 更新钉钉状态记忆

**如果钉钉已配置：**
- 在 AGENTS.md 或 PROFILE.md 中记录：钉钉已配置并正常运行
- 不要记录 Client Secret（敏感信息）
- 记录 Client ID 和配置文件路径

**如果钉钉未配置：**
- 记录：钉钉尚未配置
- 等待用户提供凭证

### 3. 检查 LLM 配置

**读取当前 LLM 配置：**
```bash
execute_shell_command(command="curl -s http://127.0.0.1:8088/api/models/active")
```

**记录当前使用的：**
- Provider ID
- Model 名称

### 4. 总结初始化状态

在会话开始时，输出类似这样的总结：
```
=== 系统初始化 ===
✓ 钉钉通道：已配置 (dingcvagqvwxfx5w6kbf)
✓ LLM：aliyun-codingplan / qwen3-max-2026-01-23
✓ 服务状态：正常运行
===
```
```

---

### 7.2 PROFILE.md 重要提醒部分

```markdown
### 重要提醒 - 钉钉已配置

**钉钉机器人（HostingerVPS-CoPaw）：**
- **状态：** ✅ 已配置并正常运行
- **机器人名称：** HostingerVPS-CoPaw
- **Client ID：** dingcvagqvwxfx5w6kbf
- **Agent ID：** 4312319425
- **App ID：** 3c1268c1-c584-4c10-bc0a-2b382af2aa51
- **配置文件：** `~/.copaw/config.json`
- **部署位置：** Hostinger VPS (76.13.219.143:8088)
- **连接状态：** Stream 模式已连接
- **消息功能：** 发送和接收正常

**重要：**
1. 钉钉机器人**已经配置完成**，不需要重新配置或绑定
2. 配置保存在 `~/.copaw/config.json` 中
3. 重启后会自动加载，配置不会丢失
4. 如果用户询问是否配置钉钉，直接回复"已配置并正常运行"
5. 以 `~/.copaw/config.json` 的实际配置为准
```

---

## 8. 经验教训与最佳实践

### 8.1 经验教训

1. **SSH隧道 > Tinyproxy**: SSH隧道更稳定可靠
2. **直连 > 代理**: 能直连就不要用代理（快3倍）
3. **流行工具更可靠**: yt-dlp（100k+ stars）比实验工具更稳定
4. **测试再承诺**: 新工具必须先测试性能和用户体验
5. **及时清理**: 失败的实验要彻底清理，不留垃圾文件
6. **实际配置 > 记忆文件**: 以 config.json 为准，记忆文件为辅助
7. **预防重复写入**: 写入前检查内容是否已存在

---

### 8.2 工作方法

1. **文档先行**: 每次配置都记录详细文档
2. **版本控制**: Git保存所有重要配置和历史版本
3. **问题诊断**: 逐步测试、隔离问题、及时记录
4. **用户体验**: 简化配置步骤、提供详细文档、及时沟通

---

### 8.3 安全意识

1. **永不断开**: 每次改变后测试连接
2. **操作前备份**: 重要操作前必须创建备份
3. **私密不外泄**: 私密信息绝对不外泄
4. **Client Secret 保护**: 不要在记忆文件中记录敏感信息

---

## 9. 联系人和服务

### 9.1 VPS 服务商
- **Hostinger**: https://hostinger.com
- **VPS地址**: 76.13.219.143

### 9.2 AI 服务商
- **智谱AI**: https://open.bigmodel.cn/ (GLM-4.7)
- **阿里云百炼**: https://bailian.console.aliyun.com/

### 9.3 钉钉开放平台
- **开发者后台**: https://open-dev.dingtalk.com/

### 9.4 GitHub
- **VPS备份仓库**: git@github.com:169068671/vps-backup
- **OpenClaw备份仓库**: git@github.com:169068671/openclaw-backup

---

## 10. 附录

### 10.1 重要日期

- **2026-03-02**: 工作空间初始化，HTTP代理配置，钉钉通道配置
- **2026-03-03**: OpenClaw升级（2026.2.1→2026.3.2），yutto-downloader技能创建，SSH隧道配置
- **2026-03-04**: MEMORY.md 创建
- **2026-03-05**: CoPaw 记忆问题修复，系统初始化流程实施

---

### 10.2 文件清单

**本地文件**:
- `~/.copaw/config.json` - 主配置
- `~/.copaw/AGENTS.md` - 工作区规则
- `~/.copaw/PROFILE.md` - 用户资料和重要提醒
- `~/.copaw/MEMORY.md` - 长期记忆
- `~/.copaw/memory/YYYY-MM-DD.md` - 日常日志
- `/tmp/copaw_local.log` - 本地服务日志

**VPS 文件**:
- `/root/.copaw/config.json` - 主配置
- `/root/.copaw/AGENTS.md` - 工作区规则
- `/root/.copaw/PROFILE.md` - 用户资料和重要提醒
- `/root/.copaw/MEMORY.md` - 长期记忆
- `/root/.copaw/memory/YYYY-MM-DD.md` - 日常日志
- `/etc/systemd/system/copaw.service` - systemd 服务配置

**OpenClaw 工作空间**:
- `/home/admin/openclaw/workspace/COPAW_完整配置与故障排查.md` - 本文档
- `/home/admin/openclaw/workspace/SOUL.md` - 我的"灵魂"和个性
- `/home/admin/openclaw/workspace/IDENTITY.md` - 我的身份信息
- `/home/admin/openclaw/workspace/USER.md` - 王老师信息
- `/home/admin/openclaw/workspace/RULES.md` - 全局规则（铁律）
- `/home/admin/openclaw/workspace/TOOLS.md` - 工具和配置笔记
- `/home/admin/openclaw/workspace/AGENTS.md` - 工作空间规则
- `/home/admin/openclaw/workspace/MEMORY.md` - 长期记忆

---

## 11. 快速参考

### 11.1 钉钉机器人信息速查

| 机器人名称 | Client ID | 部署位置 | 端口 |
|-----------|-----------|---------|------|
| HostingerVPS-CoPaw | dingcvagqvwxfx5w6kbf | VPS (76.13.219.143) | 8088 |
| 本地的 CoPaw 的机器人 | ding4zn6bwph8ugrgei1 | 本地 | 8089 |
| 王华军 openclaw | dingyscopnptfxm4hg8q | 本地 (openclaw) | - |

### 11.2 常用命令速查

| 操作 | 本地 | VPS |
|------|------|-----|
| 查看配置 | `cat ~/.copaw/config.json` | `cat /root/.copaw/config.json` |
| 查看状态 | `ps aux \| grep 'copaw app'` | `systemctl status copaw.service` |
| 查看日志 | `tail -f /tmp/copaw_local.log` | `journalctl -u copaw.service -f` |
| 重启服务 | `pkill -f 'copaw app' && nohup copaw app --host 0.0.0.0 --port 8089 > /tmp/copaw_local.log 2>&1 &` | `systemctl restart copaw.service` |
| 查看 LLM | `curl -s http://127.0.0.1:8089/api/models/active` | `curl -s http://127.0.0.1:8088/api/models/active` |

---

**文档维护人**: openclaw ⚡
**最后更新**: 2026-03-05 20:40 (GMT+8)
**版本**: 1.0
