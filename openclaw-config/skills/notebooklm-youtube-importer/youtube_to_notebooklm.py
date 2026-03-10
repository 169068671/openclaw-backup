#!/usr/bin/env python3
"""
YouTube 播放列表导入到 NotebookLM
从单个 YouTube 视频链接提取播放列表并导入所有视频
"""

import asyncio
import os
import sys
import re
from notebooklm import NotebookLMClient

# 配置代理
os.environ['HTTP_PROXY'] = 'socks5://127.0.0.1:1080'
os.environ['HTTPS_PROXY'] = 'socks5://127.0.0.1:1080'
os.environ['ALL_PROXY'] = 'socks5://127.0.0.1:1080'


def extract_playlist_id(youtube_url: str) -> str:
    """从 YouTube URL 中提取播放列表 ID"""
    
    # 支持的 URL 格式：
    # https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID
    # https://www.youtube.com/playlist?list=PLAYLIST_ID
    # https://youtu.be/VIDEO_ID?list=PLAYLIST_ID
    
    # 方法1: 从 watch URL 提取
    if '&list=' in youtube_url:
        parts = youtube_url.split('&list=')
        if len(parts) > 1:
            playlist_id = parts[1].split('&')[0]
            return playlist_id
    
    # 方法2: 从 playlist URL 提取
    elif '/playlist?list=' in youtube_url:
        parts = youtube_url.split('/playlist?list=')
        if len(parts) > 1:
            playlist_id = parts[1].split('&')[0]
            return playlist_id
    
    return None


def get_playlist_videos_from_text(text: str) -> list:
    """从页面文本中提取视频链接"""
    
    # 查找所有 watch?v= 后跟视频 ID 的链接
    pattern = r'/watch\?v=([a-zA-Z0-9_-]{11})'
    matches = re.findall(pattern, text)
    
    # 去重
    unique_videos = list(dict.fromkeys(matches))
    
    return [f"https://www.youtube.com/watch?v={vid}" for vid in unique_videos]


async def import_from_playlist_url(playlist_url: str, notebook_name: str):
    """从播放列表 URL 导入"""
    
    print(f"处理播放列表: {playlist_url}")
    print(f"笔记本名称: {notebook_name}\n")
    
    async with await NotebookLMClient.from_storage() as client:
        # 创建笔记本
        notebook = await client.notebooks.create(notebook_name)
        notebook_id = notebook.id
        
        print(f"✓ 笔记本创建成功！")
        print(f"  ID: {notebook_id}")
        print(f"  名称: {notebook_name}\n")
        
        # 尝试直接添加播放列表 URL
        try:
            result = await client.sources.add_url(notebook_id, playlist_url, wait=False)
            print(f"✓ 已添加播放列表 URL")
            print(f"  NoteBookLM 可能需要一些时间处理所有视频")
            print(f"\n笔记本 ID: {notebook_id}")
            return notebook_id
        except Exception as e:
            print(f"✗ 直接添加失败: {e}")
            print(f"  这可能需要手动导入每个视频")
            return notebook_id


async def import_from_video_urls(video_urls: list, notebook_name: str):
    """从视频 URL 列表导入"""
    
    print(f"导入 {len(video_urls)} 个视频到: {notebook_name}\n")
    
    async with await NotebookLMClient.from_storage() as client:
        # 创建笔记本
        notebook = await client.notebooks.create(notebook_name)
        notebook_id = notebook.id
        
        print(f"✓ 笔记本创建成功！")
        print(f"  ID: {notebook_id}")
        print(f"  名称: {notebook_name}\n")
        
        added_count = 0
        skipped_count = 0
        error_count = 0
        
        for i, url in enumerate(video_urls, 1):
            try:
                await client.sources.add_url(notebook_id, url, wait=True)
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
            
            # 每5个视频后暂停
            if i % 5 == 0:
                await asyncio.sleep(2)
        
        print(f"\n{'='*60}")
        print(f"导入完成！")
        print(f"{'='*60}")
        print(f"✓ 成功添加: {added_count}")
        print(f"- 已存在跳过: {skipped_count}")
        print(f"✗ 失败: {error_count}")
        print(f"总计: {len(video_urls)}")
        print(f"\n笔记本 ID: {notebook_id}")
        
        return notebook_id


def main():
    """主函数"""
    
    if len(sys.argv) < 2:
        print("用法:")
        print(f"  {sys.argv[0]} <YouTube_URL> [笔记本名称]")
        print()
        print("示例:")
        print(f"  {sys.argv[0]} 'https://www.youtube.com/watch?v=KujiAIHNRKQ&list=PLAYLIST_ID'")
        print(f"  {sys.argv[0]} 'https://www.youtube.com/playlist?list=PLAYLIST_ID' '我的笔记本'")
        print()
        print("说明:")
        print("  - 第一个参数：YouTube 视频链接或播放列表链接")
        print("  - 第二个参数（可选）：笔记本名称，默认为 'YouTube 播放列表'")
        print()
        return
    
    youtube_url = sys.argv[1]
    notebook_name = sys.argv[2] if len(sys.argv) > 2 else "YouTube 播放列表"
    
    # 提取播放列表 ID
    playlist_id = extract_playlist_id(youtube_url)
    
    if playlist_id:
        print(f"✓ 检测到播放列表 ID: {playlist_id}")
        playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
        
        # 使用 asyncio 运行导入
        notebook_id = asyncio.run(import_from_playlist_url(playlist_url, notebook_name))
        
        print(f"\n{'='*60}")
        print(f"完成！")
        print(f"{'='*60}")
        print(f"笔记本名称: {notebook_name}")
        print(f"笔记本 ID: {notebook_id}")
        print(f"\n您可以使用此 ID 继续操作：")
        print(f"  notebooklm use {notebook_id}")
        print(f"  notebooklm ask \"您的问题\"")
        
    else:
        print(f"✗ 无法从 URL 中提取播放列表 ID")
        print(f"  请确认 URL 格式正确：")
        print(f"  - https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID")
        print(f"  - https://www.youtube.com/playlist?list=PLAYLIST_ID")
        sys.exit(1)


if __name__ == "__main__":
    main()
