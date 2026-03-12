#!/bin/bash
# NotebookLM 工具测试脚本

echo "📚 NotebookLM 工具测试"
echo "===================="
echo ""

# 测试 1: 本地 notebooklm
echo "1️⃣  测试本地 notebooklm..."
if command -v notebooklm &> /dev/null; then
    VERSION=$(notebooklm --version 2>&1)
    echo "   ✅ notebooklm 已安装: $VERSION"
else
    echo "   ❌ notebooklm 未安装（预期：主要在 VPS 上使用）"
fi

# 测试 2: VPS notebooklm
echo ""
echo "2️⃣  测试 VPS notebooklm..."
VPS_TEST=$(sshpass -p 'Whj001.Whj001' ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 root@76.13.219.143 "which notebooklm && notebooklm --version 2>&1" 2>/dev/null)
if [ $? -eq 0 ]; then
    echo "   ✅ VPS notebooklm 已安装: $VPS_TEST"
else
    echo "   ❌ VPS notebooklm 未安装或连接失败"
    exit 1
fi

# 测试 3: 技能文件
echo ""
echo "3️⃣  检查技能文件..."
SKILL_DIR="/home/admin/openclaw/workspace/skills"

if [ -f "$SKILL_DIR/notebooklm/SKILL.md" ]; then
    echo "   ✅ notebooklm 技能已恢复"
else
    echo "   ⚠️  notebooklm 技能未找到"
fi

if [ -f "$SKILL_DIR/notebooklm-youtube-importer/SKILL.md" ]; then
    echo "   ✅ notebooklm-youtube-importer 技能已恢复"
else
    echo "   ⚠️  notebooklm-youtube-importer 技能未找到"
fi

# 测试 4: 导入器脚本
echo ""
echo "4️⃣  检查导入器脚本..."
IMPORT_DIR="$SKILL_DIR/notebooklm-youtube-importer"

if [ -f "$IMPORT_DIR/youtube_importer_with_ytdlp.py" ]; then
    echo "   ✅ youtube_importer_with_ytdlp.py 已存在"
else
    echo "   ⚠️  youtube_importer_with_ytdlp.py 未找到"
fi

if [ -f "$IMPORT_DIR/notebooklm_youtube_importer_v2.py" ]; then
    echo "   ✅ notebooklm_youtube_importer_v2.py 已存在"
else
    echo "   ⚠️  notebooklm_youtube_importer_v2.py 未找到"
fi

# 测试 5: 使用指南
echo ""
echo "5️⃣  检查使用指南..."
if [ -f "/home/admin/openclaw/workspace/NotebookLM技能使用指南.md" ]; then
    echo "   ✅ 使用指南已创建"
else
    echo "   ⚠️  使用指南未找到"
fi

# 总结
echo ""
echo "===================="
echo "✅ 测试完成！"
echo ""
echo "📖 使用指南: /home/admin/openclaw/workspace/NotebookLM技能使用指南.md"
echo ""
echo "🖥️  VPS 使用（推荐）："
echo "   1. 连接到 VPS:"
echo "      sshpass -p 'Whj001.Whj001' ssh root@76.13.219.143"
echo ""
echo "   2. 创建笔记本:"
echo "      notebooklm create \"我的笔记本\""
echo ""
echo "   3. 添加源文件:"
echo "      notebooklm source add \"URL\""
echo ""
echo "   4. 生成内容:"
echo "      notebooklm generate audio --wait"
echo ""
echo "   5. 下载内容:"
echo "      notebooklm download audio ./podcast.mp3"
echo ""
echo "📹 批量导入 YouTube 播放列表："
echo "   cd $IMPORT_DIR"
echo "   python3 notebooklm_youtube_importer_v2.py \"PLAYLIST_URL\" \"笔记本名称\""
