# Hostinger VPS 使用指南

**日期：** 2026-03-02
**用途：** 直接在 VPS 上访问国外网站

---

## 🌐 快速访问国外网站

### SSH 连接

```bash
ssh root@76.13.219.143
```

### 使用 lynx（文本浏览器）

```bash
# 安装 lynx（如果没有）
apt install -y lynx

# 访问网站
lynx https://www.google.com
lynx https://www.github.com
```

### 使用 curl 下载文件

```bash
# 下载文件
wget https://example.com/file.zip

# 或使用 curl
curl -O https://example.com/file.zip
```

### 使用文本模式浏览器（w3m）

```bash
# 安装 w3m
apt install -y w3m

# 访问网站
w3m https://www.google.com
```

---

## 📥 常用场景

### 1. 下载大型文件

```bash
# 下载文件到 VPS
wget https://example.com/large-file.tar.gz

# 使用断点续传
wget -c https://example.com/large-file.tar.gz
```

### 2. 克隆 Git 仓库

```bash
# 克隆 GitHub 仓库
git clone https://github.com/user/repo.git

# 克隆 GitLab 仓库
git clone https://gitlab.com/user/repo.git
```

### 3. 安装软件包

```bash
# 从国外源下载
pip install package-name
npm install package-name
```

### 4. 下载 Docker 镜像

```bash
# 拉取镜像
docker pull ubuntu:latest
docker pull nginx:latest
```

### 5. 下载机器学习模型

```python
# Python 脚本
from transformers import AutoModel
model = AutoModel.from_pretrained('model-name')
```

---

## 📊 传输文件到本地

### 使用 scp

```bash
# 从 VPS 下载文件
scp root@76.13.219.143:/root/file.tar.gz ~/

# 下载目录
scp -r root@76.13.219.143:/root/directory ~/

# 下载文件并重命名
scp root@76.13.219.143:/root/file.tar.gz ~/new-name.tar.gz
```

### 使用 rsync（支持断点续传）

```bash
# 同步文件
rsync -avz --progress root@76.13.219.143:/root/file.tar.gz ~/

# 同步目录
rsync -avz --progress root@76.13.219.143:/root/directory ~/

# 断点续传
rsync -avz --progress --partial root@76.13.219.143:/root/large-file.tar.gz ~/
```

---

## 🎯 常用命令

### SSH 连接

```bash
# 基本连接
ssh root@76.13.219.143

# 使用 sshpass（不输入密码）
sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143

# 使用密钥（如果配置了）
ssh -i ~/.ssh/id_rsa root@76.13.219.143
```

### 文件传输

```bash
# scp - 上传到 VPS
scp local-file root@76.13.219.143:/root/

# scp - 从 VPS 下载
scp root@76.13.219.143:/root/remote-file ~/

# rsync - 从 VPS 下载
rsync -avz --progress root@76.13.219.143:/root/remote-file ~/
```

### VPS 信息

| 项目 | 配置值 |
|------|--------|
| 地址 | 76.13.219.143 |
| 用户 | root |
| 密码 | Whj001.Whj001 |
| 系统 | Ubuntu 22.04.5 LTS |
| Python | 3.10.12 |
| Docker | 29.2.1 |

---

## 💡 使用建议

### 场景 1：下载大型文件

```bash
# 1. SSH 到 VPS
ssh root@76.13.219.143

# 2. 下载文件
wget https://example.com/large-file.zip

# 3. 传输到本地
# 在本地执行
scp root@76.13.219.143:/root/large-file.zip ~/
```

### 场景 2：克隆 Git 仓库

```bash
# 1. SSH 到 VPS
ssh root@76.13.219.143

# 2. 克隆仓库
git clone https://github.com/user/repo.git

# 3. 传输到本地
scp -r root@76.13.219.143:/root/repo ~/
```

### 场景 3：下载 Docker 镜像

```bash
# 1. SSH 到 VPS
ssh root@76.13.219.143

# 2. 拉取镜像
docker pull ubuntu:latest

# 3. 导出镜像
docker save ubuntu:latest -o ubuntu-latest.tar

# 4. 传输到本地
# 在本地执行
scp root@76.13.219.143:/root/ubuntu-latest.tar ~/

# 5. 本地导入
docker load -i ~/ubuntu-latest.tar
```

### 场景 4：下载机器学习模型

```bash
# 1. SSH 到 VPS
ssh root@76.13.219.143

# 2. Python 下载模型
python3 << 'EOF'
from transformers import AutoModel
model = AutoModel.from_pretrained('bert-base-uncased')
print("模型下载完成！")
EOF

# 3. 打包模型
tar -czf models.tar.gz ~/.cache/huggingface/hub/

# 4. 传输到本地
# 在本地执行
scp root@76.13.219.143:/root/models.tar.gz ~/

# 5. 本地解压
tar -xzf ~/models.tar.gz -C ~/.cache/huggingface/hub/
```

---

## 📝 常用快捷方式

### 创建快捷命令

在本地 `~/.bashrc` 中添加：

```bash
# VPS 快捷命令
alias vps='ssh root@76.13.219.143'

# VPS 下载文件快捷命令
vps-download() {
    ssh root@76.13.219.143 "cd ~ && wget $1"
    scp root@76.13.219.143:~/$(basename $1) ~/
}

# VPS 克隆仓库快捷命令
vps-clone() {
    ssh root@76.13.219.143 "cd ~ && git clone $1"
    scp -r root@76.13.219.143:~/$(basename $1 .git) ~/
}
```

**使用示例：**
```bash
# 重新加载配置
source ~/.bashrc

# 连接 VPS
vps

# 下载文件
vps-download https://example.com/file.zip

# 克隆仓库
vps-clone https://github.com/user/repo.git
```

---

## 🔧 工具安装

### 文本浏览器

```bash
# lynx（推荐）
apt install -y lynx

# w3m（支持表格和颜色）
apt install -y w3m
```

### 下载工具

```bash
# wget（已安装）
apt install -y wget

# curl（已安装）
apt install -y curl
```

### 版本控制

```bash
# git（已安装）
apt install -y git
```

---

## ✅ 优势总结

| 优势 | 说明 |
|------|------|
| 速度快 | VPS 直接访问国外网站，速度快 |
| 稳定性好 | VPS 网络稳定，不容易断开 |
| 无需本地代理 | 不需要配置本地浏览器代理 |
| 批量下载 | 可以批量下载多个文件 |
| 后台下载 | 可以在 VPS 后台下载，不影响本地工作 |

---

## 🎉 总结

**推荐使用场景：**
- ✅ 下载大型文件
- ✅ 克隆 Git 仓库
- ✅ 下载 Docker 镜像
- ✅ 下载机器学习模型
- ✅ 访问国外网站

**VPS 信息：**
- 地址：76.13.219.143
- 用户：root
- 密码：Whj001.Whj001

**常用命令：**
```bash
# SSH 连接
ssh root@76.13.219.143

# 下载文件后传输
# VPS 上：wget https://example.com/file.zip
# 本地：scp root@76.13.219.143:~/file.zip ~/
```

---

**文档创建时间：** 2026-03-02 22:45 (GMT+8)
**创建人：** openclaw ⚡
