#!/usr/bin/env python3
"""
YouTube 播放列表导入器（完整版）- 使用 yt-dlp 获取播放列表
"""

import asyncio
import os
import sys
import subprocess
from notebooklm import NotebookLMClient

# 配置代理
os.environ['HTTP_PROXY'] = 'socks5://127.0.0.1:1080'
os.environ['HTTPS_PROXY'] = 'socks5://127.0.0.1:1080'
os.environ['ALL_PROXY'] = 'socks5://127.0.0.1:1080'


def extract_videos_with_ytdlp(playlist_url: str) -> list:
    """使用 yt-dlp 提取 YouTube 播放列表中的所有视频链接"""
    
    print(f"使用 yt-dlp 提取播放列表...\n")
    print(f"播放列表 URL: {playlist_url}\n")
    
    try:
        # 运行 yt-dlp 提取视频链接
        result = subprocess.run(
            [
                'yt-dlp',
                '--flat-playlist',
                '--get-url',
                '--skip-download',
                '--proxy', 'socks5://127.0.0.1:1080',
                playlist_url
            ],
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if result.returncode != 0:
            print(f"✗ yt-dlp 执行失败: {result.stderr}")
            return []
        
        # 解析输出
        video_urls = [line.strip() for line in result.stdout.strip().split('\n') if line.strip()]
        
        # 去重
        unique_urls = list(dict.fromkeys(video_urls))
        
        print(f"✓ 提取到 {len(unique_urls)} 个视频链接\n")
        
        return unique_urls
        
    except subprocess.TimeoutExpired:
        print("✗ yt-dlp 执行超时（300秒）")
        return []
    except Exception as e:
        print(f"✗ 提取失败: {e}")
        return []


async def import_videos_from_ytdlp(playlist_url: str, notebook_name: str):
    """使用 yt-dlp 提取并导入视频"""
    
    print(f"使用 yt-dlp 方式导入...\n")
    
    # 1. 提取视频链接
    video_urls = extract_videos_with_ytdlp(playlist_url)
    
    if not video_urls:
        print("✗ 未能提取到任何视频链接")
        return None
    
    # 2. 创建笔记本
    async with await NotebookLMClient.from_storage() as client:
        notebook = await client.notebooks.create(notebook_name)
        notebook_id = notebook.id
        
        print(f"\n✓ 笔记本创建成功！")
        print(f"  ID: {notebook_id}")
        print(f"  名称: {notebook_name}\n")
        
        # 3. 导入视频
        print(f"开始导入 {len(video_urls)} 个视频...\n")
        
        added_count = 0
        skipped_count = 0
        error_count = 0
        
        for i, url in enumerate(video_urls, 1):
            try:
                # 不等待，提高速度
                await client.sources.add_url(notebook_id, url, wait=False)
                added_count += 1
                print(f"[{i}/{len(video_urls)}] ✓ 添加成功")
            except Exception as e:
                error_msg = str(e).lower()
                if "already" in error_msg or "duplicate" in error_msg:
                    skipped_count += 1
                    print(f"[{i}/{len(video_urls)}] - 已存在，跳过")
                else:
                    error_count += 1
                    print(f"[{i}/{len(video_urls)}] ✗ 失败: {e}")
            
            # 每3个视频后暂停
            if i % 3 == 0:
                await asyncio.sleep(2)
        
        print(f"\n{'='*60}")
        print(f"导入完成！")
        print(f"{'='*60}")
        print(f"✓ 成功添加: {added_count}")
        print(f"- 已存在跳过: {skipped_count}")
        print(f"✗ 失败: {error_count}")
        print(f"总计: {len(video_urls)}")
        print(f"\n笔记本 ID: {notebook_id}")
        print(f"\n⏳ NoteBookLM 正在后台处理视频，这可能需要几分钟...")
        
        return notebook_id


def main():
    """主函数"""
    
    if len(sys.argv) < 2:
        print("用法:")
        print(f"  {sys.argv[0]} ytdlp <YouTube_URL> [笔记本名称]")
        print()
        print("示例:")
        print(f"  {sys.argv[0]} ytdlp 'https://www.youtube.com/playlist?list=PLAYLIST_ID' '我的笔记本'")
        print(f"  {sys.argv[0]} ytdlp 'https://www.youtube.com/watch?v=XXX&list=YYY' '教程'")
        print()
        print("说明:")
        print("  - 使用 yt-dlp 提取播放列表中的所有视频")
        print("  - 自动创建笔记本并导入所有视频")
        print("  - 自动去重，避免重复导入")
        print("  - 后台处理，不等待每个视频完成")
        print()
        return
    
    command = sys.argv[1].lower()
    
    if command == "ytdlp":
        if len(sys.argv) < 3:
            print("用法: python3 script.py ytdlp <YouTube_URL> [笔记本名称]")
            return
        
        playlist_url = sys.argv[2]
        notebook_name = sys.argv[3] if len(sys.argv) > 3 else "YouTube 播放列表"
        
        # 使用 yt-dlp 提取并导入
        asyncio.run(import_videos_from_ytdlp(playlist_url, notebook_name))
    
    else:
        print(f"未知命令: {command}")
        print("使用: ytdlp")


if __name__ == "__main__":
    main()
