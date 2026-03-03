# Apache Guacamole 部署完成报告

**日期：** 2026-03-02
**时间：** 22:48 - 22:54 (GMT+8)
**用户：** 王老师
**状态：** ✅ 部署完成

---

## 🎯 部署结果

| 项目 | 状态 | 详情 |
|------|------|------|
| Docker Compose | ✅ 完成 | 3 个容器运行中 |
| Guacamole Web | ✅ 运行中 | 端口 8081 |
| MySQL 数据库 | ✅ 运行中 | 端口 3306 |
| Guacamole Daemon | ✅ 运行中 | 端口 4822 |

---

## 📋 部署的组件

### 1. MySQL 数据库

| 配置项 | 值 |
|--------|-----|
| 镜像 | mysql:8.0 |
| 容器名 | guacamole-mysql |
| 数据库名 | guacamole_db |
| 用户名 | guacamole_user |
| 密码 | guacamole_password |
| 数据卷 | mysql-data |

### 2. Guacamole Daemon (guacd)

| 配置项 | 值 |
|--------|-----|
| 镜像 | guacamole/guacd:latest |
| 容器名 | guacamole-guacd |
| 网络 | guacamole-net |

### 3. Guacamole Web 应用

| 配置项 | 值 |
|--------|-----|
| 镜像 | guacamole/guacamole:latest |
| 容器名 | guacamole-web |
| Web 端口 | 8081:8080 |
| 网络 | guacamole-net |
| 数据库连接 | ✅ 正常 |
| guacd 连接 | ✅ 正常 |

---

## 🚀 访问 Guacamole

### 1. 访问 Web 界面

**访问地址：**
```
http://76.13.219.143:8081/guacamole
```

### 2. 登录信息

**默认登录：**
- 用户名：`guacadmin`
- 密码：`guacadmin`

**首次登录后：** 建议立即修改密码

---

## 📊 容器状态

```bash
$ docker ps
CONTAINER ID   IMAGE                       COMMAND             CREATED         STATUS         PORTS                            NAMES
6b4e1c3a5519   guacamole/guacamole:latest  "/opt/guacamole/bin/…"   2 minutes ago   Up 2 minutes   0.0.0.0:8081->8080/tcp   guacamole-web
078ee0354a22   mysql:8.0                  "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   3306/tcp, 33060/tcp        guacamole-mysql
694a3c772560   guacamole/guacd:latest      "/opt/guacamole/entr…"   2 minutes ago   Up 2 minutes   4822/tcp                        guacamole-guacd
```

---

## 🔧 Docker Compose 配置

**配置文件：** `/root/guacamole-docker-compose.yml`

**内容：**
```yaml
version: '3'

services:
  # MySQL 数据库
  mysql:
    image: mysql:8.0
    container_name: guacamole-mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: guacamole_db
      MYSQL_USER: guacamole_user
      MYSQL_PASSWORD: guacamole_password
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - guacamole-net

  # Guacamole Daemon (guacd)
  guacd:
    image: guacamole/guacd:latest
    container_name: guacamole-guacd
    restart: always
    networks:
      - guacamole-net

  # Guacamole Web 应用
  guacamole:
    image: guacamole/guacamole:latest
    container_name: guacamole-web
    restart: always
    depends_on:
      - guacd
      - mysql
    environment:
      GUACD_HOSTNAME: guacd
      MYSQL_HOSTNAME: mysql
      MYSQL_PORT: 3306
      MYSQL_DATABASE: guacamole_db
      MYSQL_USER: guacamole_user
      MYSQL_PASSWORD: guacamole_password
    ports:
      - "8081:8080"
    networks:
      - guacamole-net

volumes:
  mysql-data:
    driver: local

networks:
  guacamole-net:
    driver: bridge
```

---

## 🎯 Guacamole 功能

### 支持的协议

| 协议 | 说明 |
|------|------|
| SSH | 远程连接 Linux/Unix 系统 |
| RDP | 远程连接 Windows 系统 |
| VNC | 远程桌面控制 |
| Telnet | 远程登录 |

### 主要功能

- ✅ **Web 界面访问** - 无需安装客户端
- ✅ **多用户管理** - 支持多用户登录
- ✅ **连接保存** - 保存多个连接配置
- ✅ **文件传输** - 支持 SFTP 文件传输
- ✅ **会话管理** - 管理多个远程会话
- ✅ **权限控制** - 用户和组权限管理

---

## 📝 使用指南

### 1. 首次登录

1. 打开浏览器，访问：`http://76.13.219.143:8081/guacamole`
2. 输入默认登录：
   - 用户名：`guacadmin`
   - 密码：`guacadmin`
3. 点击"Login"

### 2. 添加 SSH 连接

**步骤：**
1. 登录后，点击"Connections" → "New Connection"
2. 配置连接：
   - **名称：** VPS（或其他名称）
   - **协议：** SSH
   - **主机名：** 76.13.219.143（或其他 IP）
   - **端口：** 22
   - **用户名：** root（或其他用户）
   - **密码：** Whj001.Whj001（或其他密码）
3. 点击"Save"

**连接：** 点击连接名称，打开远程终端

### 3. 管理连接

**查看所有连接：**
- Connections → 所有连接

**编辑连接：**
- Connections → 选择连接 → Settings

**删除连接：**
- Connections → 选择连接 → Delete

### 4. 用户管理

**添加用户：**
1. Users → New User
2. 配置用户信息
3. 设置权限

**修改密码：**
1. Users → 选择用户 → Settings
2. 修改密码

---

## 🔧 管理命令

### 查看 Guacamole 日志

```bash
# SSH 到 VPS
ssh root@76.13.219.143

# 查看 Web 容器日志
docker logs guacamole-web

# 查看 guacd 日志
docker logs guacamole-guacd

# 查看 MySQL 日志
docker logs guacamole-mysql
```

### 停止 Guacamole

```bash
# SSH 到 VPS
ssh root@76.13.219.143

# 停止所有容器
cd /root
docker-compose -f guacamole-docker-compose.yml down
```

### 启动 Guacamole

```bash
# SSH 到 VPS
ssh root@76.13.219.143

# 启动所有容器
cd /root
docker-compose -f guacamole-docker-compose.yml up -d
```

### 重启 Guacamole

```bash
# SSH 到 VPS
ssh root@76.13.219.143

# 重启所有容器
cd /root
docker-compose -f guacamole-docker-compose.yml restart
```

### 更新 Guacamole

```bash
# SSH 到 VPS
ssh root@76.13.219.143

# 拉取最新镜像
docker pull guacamole/guacamole:latest
docker pull guacamole/guacd:latest

# 重启容器
cd /root
docker-compose -f guacamole-docker-compose.yml up -d
```

---

## 💡 使用建议

### 推荐使用场景

1. **远程服务器管理**
   - 通过 Web 界面 SSH 到 VPS
   - 无需安装 SSH 客户端

2. **远程桌面访问**
   - 通过 RDP 连接 Windows 机器
   - 通过 VNC 连接 Linux 桌面

3. **文件传输**
   - 使用 SFTP 功能传输文件
   - 无需额外的 FTP 客户端

4. **多服务器管理**
   - 保存多个连接配置
   - 快速切换不同服务器

### 安全建议

1. **修改默认密码**
   - 首次登录后立即修改 `guacadmin` 密码

2. **配置防火墙**
   - 只开放必要的端口（8081）
   - 限制访问来源 IP（如果可能）

3. **使用 HTTPS**
   - 配置反向代理（Nginx）
   - 使用 SSL 证书

4. **定期备份**
   - 备份 Guacamole 配置
   - 备份 MySQL 数据库

---

## 📊 性能说明

### 资源占用

| 容器 | CPU | 内存 | 磁盘 |
|------|-----|------|------|
| guacamole-web | 低 | ~200MB | ~500MB |
| guacamole-mysql | 低 | ~200MB | ~1GB |
| guacamole-guacd | 低 | ~50MB | ~100MB |

### 并发连接

- **推荐：** 5-10 个并发连接
- **最大：** 取决于 VPS 资源

---

## 📝 故障排查

### 问题 1：无法访问 Web 界面

**检查：**
```bash
# SSH 到 VPS
ssh root@76.13.219.143

# 检查容器状态
docker ps -a | grep guacamole

# 检查端口
netstat -tlnp | grep 8081
```

**解决：**
- 重启容器：`docker restart guacamole-web`
- 检查防火墙规则

### 问题 2：连接失败

**检查：**
- 目标服务器是否可访问
- SSH 服务是否运行
- 用户名和密码是否正确
- 网络是否通畅

**解决：**
- 检查服务器状态
- 验证凭据
- 查看 guacd 日志

### 问题 3：数据库连接失败

**检查：**
```bash
# 检查 MySQL 容器
docker ps | grep guacamole-mysql

# 查看 MySQL 日志
docker logs guacamole-mysql
```

**解决：**
- 重启 MySQL 容器
- 检查数据库配置
- 查看网络连接

---

## 🎉 总结

**部署状态：** ✅ 完成

**访问地址：** http://76.13.219.143:8081/guacamole

**默认登录：**
- 用户名：guacadmin
- 密码：guacadmin

**主要功能：**
- ✅ SSH 远程连接
- ✅ RDP 远程桌面
- ✅ VNC 远程控制
- ✅ Web 界面访问
- ✅ 多用户管理
- ✅ 连接保存

---

**部署完成时间：** 2026-03-02 22:54 (GMT+8)
**部署人：** openclaw ⚡
