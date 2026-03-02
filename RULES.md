# RULES.md - 全局规则

---

## 🌐 全局下载规则：优先使用 VPS

**规则：所有需要外网下载的内容，优先在 Hostinger VPS 上下载，然后传输到本地。**

### 适用场景

这条规则适用于所有需要从国外下载资源的情况：

1. **Docker 镜像** - docker pull
2. **Python 包** - pip install（尤其是大型包）
3. **机器学习模型** - Hugging Face、PyTorch、TensorFlow 模型
4. **软件安装包** - wget/curl 下载的大型文件
5. **Git 克隆** - GitHub 等国外仓库
6. **其他国外资源** - CDN、API 调用等

### 操作流程

**步骤 1：在 VPS 上下载**

```bash
# SSH 到 VPS
ssh root@76.13.219.143

# 在 VPS 上下载资源
# 例如：Docker 镜像
docker pull ubuntu:latest

# 例如：Python 包
pip install package-name

# 例如：模型文件
python3 -c "from transformers import AutoModel; AutoModel.from_pretrained('model-name')"
```

**步骤 2：打包/导出**

```bash
# Docker 镜像导出
docker save ubuntu:latest -o ubuntu-latest.tar

# Python 包/模型文件
tar -czf models.tar.gz ~/.cache/huggingface/hub/

# 其他文件
tar -czf data.tar.gz /path/to/data
```

**步骤 3：传输到本地**

```bash
# 使用 scp 传输
scp root@76.13.219.143:/root/ubuntu-latest.tar ~/
scp root@76.13.219.143:/root/models.tar.gz ~/

# 或使用 rsync（支持断点续传）
rsync -avz --progress root@76.13.219.143:/root/models.tar.gz ~/
```

**步骤 4：本地导入/解压**

```bash
# Docker 镜像导入
docker load -i ~/ubuntu-latest.tar

# Python 包/模型解压
tar -xzf ~/models.tar.gz -C ~/.cache/huggingface/hub/
```

### 为什么这样做？

| 方面 | 直接下载 | VPS 中转 | 优势 |
|------|---------|----------|------|
| **速度** | 慢（~300 KB/s） | 快（~20 MB/s） | ⚡⚡⚡ |
| **稳定性** | 经常超时/失败 | 稳定 | ✅ |
| **成功率** | 低 | 高 | ✅ |
| **时间成本** | 长（几小时） | 短（几分钟） | ⏰ |

### VPS 信息

| 项目 | 配置值 |
|------|--------|
| 地址 | 76.13.219.143 |
| 用户 | root |
| 密码 | Whj001.Whj001 |
| 连接命令 | `ssh root@76.13.219.143` |
| 传输命令 | `scp root@76.13.219.143:/path/file .` |

### 常用命令

**SSH 连接：**
```bash
ssh root@76.13.219.143
```

**文件传输（从 VPS 到本地）：**
```bash
scp root@76.13.219.143:/root/file.tar.gz ~/
```

**目录传输（从 VPS 到本地）：**
```bash
scp -r root@76.13.219.143:/root/directory ~/
```

**使用 rsync（断点续传）：**
```bash
rsync -avz --progress root@76.13.219.143:/root/largefile.tar.gz ~/
```

### 注意事项

1. **VPS 存储空间：** 下载大文件前检查 VPS 磁盘空间
   ```bash
   df -h
   ```

2. **传输后清理：** 传输完成后删除 VPS 上的临时文件
   ```bash
   ssh root@76.13.219.143 "rm -f /root/temp-file.tar.gz"
   ```

3. **压缩优化：** 大文件传输前先压缩以减少传输时间
   ```bash
   tar -czf archive.tar.gz /path/to/files
   ```

4. **断点续传：** 大文件使用 rsync 而不是 scp
   ```bash
   rsync -avz --progress --partial root@76.13.219.143:/root/largefile.tar.gz ~/
   ```

---

## 🚨 金科玉律：永不断开连接

**规则：不管做什么设置，一定要确保能再次打开。每次改变后，都要 ping 下自己，确保下次能打开。**

### 适用场景

这条规则适用于所有可能影响系统访问、服务运行、网络配置的操作：

1. **服务配置更改**（OpenClaw、Nginx、Apache 等）
2. **防火墙规则修改**（ufw、iptables）
3. **系统更新和升级**（apt upgrade、dist-upgrade）
4. **网络配置更改**（IP、端口、DNS）
5. **权限调整**（用户、文件权限）
6. **配置文件修改**（任何可能影响服务启动的配置）
7. **服务重启/停止操作**

### 自检清单

每次操作后，必须执行以下验证：

- [ ] 服务是否正常运行（systemctl status）
- [ ] 端口是否正常监听（netstat -tlnp）
- [ ] 能否正常访问（curl 本地/远程访问）
- [ ] 日志是否正常（journalctl / 服务日志）
- [ ] 配置是否已保存并持久化

### 🚨 如果发现问题 - 必须回滚

**规则：如果有问题，一定要回滚到设置前。**

1. **立即回滚更改** — 这是第一优先级
2. 检查错误日志，找出问题根源
3. 修复后再次验证
4. 确认恢复到稳定状态

### 回滚策略

- **配置文件：** 操作前先备份（.bak）
- **服务配置：** 使用版本控制或备份目录
- **系统级更改：** 记录所有修改，便于回滚
- **如果不确定能否成功，先在测试环境验证**

**不要"硬着头皮修复"，立即回滚是最安全的选择。**

---

记住：**生存第一，功能第二**。宁可少做一个功能，也不能让自己"死"掉。
