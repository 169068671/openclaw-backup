#!/bin/bash
# YouTube 工具测试脚本

echo "🔍 YouTube 工具测试"
echo "===================="
echo ""

# 测试 1: yt-dlp 版本
echo "1️⃣  测试 yt-dlp..."
if command -v yt-dlp &> /dev/null; then
    VERSION=$(yt-dlp --version)
    echo "   ✅ yt-dlp 已安装: v$VERSION"
else
    echo "   ❌ yt-dlp 未安装"
    exit 1
fi

# 测试 2: browser-cookies-exporter
echo ""
echo "2️⃣  测试 browser-cookies-exporter..."
if command -v browser-cookies-exporter &> /dev/null; then
    echo "   ✅ browser-cookies-exporter 已安装"
    echo "   📁 位置: $(which browser-cookies-exporter)"
else
    echo "   ❌ browser-cookies-exporter 未安装"
    exit 1
fi

# 测试 3: FFmpeg
echo ""
echo "3️⃣  测试 FFmpeg..."
if command -v ffmpeg &> /dev/null; then
    FFMPEG_VERSION=$(ffmpeg -version | head -1)
    echo "   ✅ FFmpeg 已安装"
    echo "   $FFMPEG_VERSION"
else
    echo "   ❌ FFmpeg 未安装"
fi

# 测试 4: SSH 隧道状态
echo ""
echo "4️⃣  测试 SSH 隧道..."
if netstat -tlnp 2>/dev/null | grep -q ":1080 "; then
    echo "   ✅ SSH 隧道正在运行 (端口 1080)"
else
    echo "   ⚠️  SSH 隧道未运行（可选）"
    echo "   启动命令: sshpass -p 'Whj001.Whj001' ssh -N -D 1080 -f root@76.13.219.143"
fi

# 测试 5: 技能文件
echo ""
echo "5️⃣  检查技能文件..."
SKILL_DIR="/home/admin/openclaw/workspace"

if [ -f "$SKILL_DIR/youtube-auth-exporter/SKILL.md" ]; then
    echo "   ✅ youtube-auth-exporter 技能已恢复"
else
    echo "   ⚠️  youtube-auth-exporter 技能未找到"
fi

if [ -f "$SKILL_DIR/yt-dlp-downloader/yt-dlp-downloader/SKILL.md" ]; then
    echo "   ✅ yt-dlp-downloader 技能已恢复"
else
    echo "   ⚠️  yt-dlp-downloader 技能未找到"
fi

if [ -f "$SKILL_DIR/YouTube技能使用指南.md" ]; then
    echo "   ✅ 使用指南已创建"
else
    echo "   ⚠️  使用指南未找到"
fi

# 总结
echo ""
echo "===================="
echo "✅ 测试完成！"
echo ""
echo "📖 使用指南: /home/admin/openclaw/workspace/YouTube技能使用指南.md"
echo ""
echo "🎯 快速开始："
echo "   下载视频: yt-dlp \"URL\""
echo "   导出cookies: browser-cookies-exporter .google.com /tmp/cookies.txt"
echo "   带cookies下载: yt-dlp --cookies /tmp/cookies.txt \"URL\""
