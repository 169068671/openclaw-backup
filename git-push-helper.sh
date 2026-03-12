#!/bin/bash
# GitHub Push Helper - 推送代码到 GitHub

echo "🚀 GitHub Push Helper"
echo "===================="
echo ""

# 进入工作目录
cd /home/admin/openclaw/workspace

# 检查 Git 状态
echo "📋 Git 状态："
git status --short
echo ""

# 显示远程仓库
echo "📦 远程仓库："
git remote -v
echo ""

# 显示当前分支
echo "🌿 当前分支："
git branch --show-current
echo ""

# 显示最后提交
echo "📝 最后提交："
git log -1 --oneline
echo ""

# 询问推送方式
echo "请选择推送方式："
echo "1. 使用 Personal Access Token（推荐）"
echo "2. 使用 SSH 密钥（长期使用）"
echo "3. 手动输入用户名和密码"
echo ""
read -p "请选择 (1/2/3): " choice

case $choice in
    1)
        echo ""
        echo "🔑 使用 Personal Access Token"
        echo "====================="
        echo ""
        echo "步骤1：创建 GitHub Token"
        echo "  1. 访问: https://github.com/settings/tokens"
        echo "  2. 点击 'Generate new token (classic)'"
        echo "  3. 选择权限: repo (完整仓库访问权限)"
        echo "  4. 生成并复制 token (格式: ghp_xxxxxxxxxx)"
        echo ""
        read -p "请输入你的 GitHub Token: " token

        if [ -z "$token" ]; then
            echo "❌ Token 不能为空"
            exit 1
        fi

        echo ""
        echo "步骤2：配置 Git Credential Helper"
        git config credential.helper store
        echo "https://169068671:$token@github.com" > ~/.git-credentials
        echo "✅ Credential 已配置"
        echo ""

        echo "步骤3：推送到 GitHub"
        if git push -u origin master; then
            echo ""
            echo "✅ 推送成功！"
            echo "📦 仓库地址: https://github.com/169068671/openclaw-backup"
        else
            echo ""
            echo "❌ 推送失败"
            echo ""
            echo "可能的原因："
            echo "1. Token 权限不足（需要 repo 权限）"
            echo "2. Token 已过期"
            echo "3. 仓库不存在"
            echo ""
            echo "请检查后重试"
        fi
        ;;
    2)
        echo ""
        echo "🔑 使用 SSH 密钥"
        echo "====================="
        echo ""

        # 检查是否已有 SSH 密钥
        if [ -f ~/.ssh/id_ed25519.pub ] || [ -f ~/.ssh/id_rsa.pub ]; then
            echo "✅ 检测到现有 SSH 密钥："
            if [ -f ~/.ssh/id_ed25519.pub ]; then
                echo "  - ~/.ssh/id_ed25519.pub (ed25519)"
                echo ""
                echo "公钥内容："
                cat ~/.ssh/id_ed25519.pub
            fi
            if [ -f ~/.ssh/id_rsa.pub ]; then
                echo "  - ~/.ssh/id_rsa.pub (RSA)"
                echo ""
                echo "公钥内容："
                cat ~/.ssh/id_rsa.pub
            fi
            echo ""
            read -p "是否使用现有密钥？(y/n): " use_existing

            if [ "$use_existing" = "y" ] || [ "$use_existing" = "Y" ]; then
                echo "✅ 使用现有密钥"
                key_file="id_ed25519"
            else
                echo "步骤1：生成新的 SSH 密钥"
                read -p "请输入注释（可选）: " comment
                comment=${comment:-"169068671@qq.com"}

                echo "正在生成 SSH 密钥..."
                ssh-keygen -t ed25519 -C "$comment" -f ~/.ssh/id_ed25519_github -N
                echo "✅ SSH 密钥已生成"
                echo ""
                echo "公钥内容："
                cat ~/.ssh/id_ed25519_github.pub
                echo ""
                key_file="id_ed25519_github"

                # 配置 SSH
                cat >> ~/.ssh/config <<EOF

Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/$key_file
    IdentitiesOnly yes
EOF
                echo "✅ SSH 配置已添加到 ~/.ssh/config"
            fi
        else
            echo "步骤1：生成 SSH 密钥"
            read -p "请输入注释（可选）: " comment
            comment=${comment:-"169068671@qq.com"}

            echo "正在生成 SSH 密钥..."
            ssh-keygen -t ed25519 -C "$comment" -f ~/.ssh/id_ed25519_github -N
            echo "✅ SSH 密钥已生成"
            echo ""
            echo "公钥内容："
            cat ~/.ssh/id_ed25519_github.pub
            echo ""
            key_file="id_ed25519_github"

            # 配置 SSH
            cat >> ~/.ssh/config <<EOF

Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/$key_file
    IdentitiesOnly yes
EOF
            echo "✅ SSH 配置已添加到 ~/.ssh/config"
        fi

        echo ""
        echo "步骤2：添加公钥到 GitHub"
        echo "  1. 复制上面的公钥内容"
        echo "  2. 访问: https://github.com/settings/keys"
        echo "  3. 点击 'New SSH key'"
        echo "  4. 粘贴公钥内容"
        echo "  5. 添加密钥"
        echo ""
        read -p "按 Enter 继续（确认已添加公钥到 GitHub）..."

        echo ""
        echo "步骤3：测试 SSH 连接"
        echo "正在测试 SSH 连接到 GitHub..."
        if ssh -T git@github.com 2>&1 | grep -q "successfully authenticated"; then
            echo "✅ SSH 连接成功"
        else
            echo "⚠️  SSH 连接失败（但可能仍然可以推送）"
        fi
        echo ""

        echo "步骤4：更改远程仓库为 SSH"
        git remote set-url origin git@github.com:169068671/openclaw-backup.git
        echo "✅ 远程仓库已更改为 SSH"
        echo ""

        echo "步骤5：推送到 GitHub"
        if git push -u origin master; then
            echo ""
            echo "✅ 推送成功！"
            echo "📦 仓库地址: https://github.com/169068671/openclaw-backup"
        else
            echo ""
            echo "❌ 推送失败"
            echo ""
            echo "可能的原因："
            echo "1. SSH 密钥未正确添加到 GitHub"
            echo "2. SSH 配置错误"
            echo "3. 仓库不存在"
            echo ""
            echo "请检查后重试"
        fi
        ;;
    3)
        echo ""
        echo "🔐 手动输入用户名和密码"
        echo "====================="
        echo ""

        read -p "请输入 GitHub 用户名: " username
        read -sp "请输入 GitHub 密码或 Token: " password
        echo ""

        # 配置 credential helper
        git config credential.helper store
        echo "https://$username:$password@github.com" > ~/.git-credentials
        echo "✅ Credential 已配置"
        echo ""

        echo "推送到 GitHub..."
        if git push -u origin master; then
            echo ""
            echo "✅ 推送成功！"
            echo "📦 仓库地址: https://github.com/169068671/openclaw-backup"
        else
            echo ""
            echo "❌ 推送失败"
            echo ""
            echo "可能的原因："
            echo "1. 用户名或密码错误"
            echo "2. 需要使用 Personal Access Token 而不是密码"
            echo "3. 仓库不存在"
            echo ""
            echo "请检查后重试"
        fi
        ;;
    *)
        echo "❌ 无效的选择"
        exit 1
        ;;
esac

echo ""
echo "===================="
echo "✅ 完成！"
