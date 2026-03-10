#!/usr/bin/env python3
"""
NotebookLM YouTube 播放列表导入器（改进版）
使用 agent-browser 提取播放列表中的所有视频链接并导入到 NotebookLM
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


async def import_videos_with_browser(youtube_url: str, notebook_name: str):
    """使用浏览器提取并导入视频"""
    
    print(f"YouTube URL: {youtube_url}")
    print(f"笔记本名称: {notebook_name}\n")
    
    # 1. 先创建笔记本
    async with await NotebookLMClient.from_storage() as client:
        notebook = await client.notebooks.create(notebook_name)
        notebook_id = notebook.id
        
        print(f"✓ 笔记本创建成功！")
        print(f"  ID: {notebook_id}")
        print(f"  名称: {notebook_name}\n")
    
    # 2. 使用 agent-browser 提取视频链接
    print(f"正在使用 agent-browser 提取播放列表...")
    print(f"这可能需要 1-2 分钟，请耐心等待...\n")
    
    # 运行 agent-browser 命令
    import subprocess
    try:
        # 打开浏览器
        subprocess.run(
            ['agent-browser', '--proxy', 'socks5://127.0.0.1:1080', 'open', youtube_url],
            check=True,
            timeout=60
        )
        print("✓ 浏览器已打开")
        
        # 等待页面加载
        print("⏳ 等待页面加载...")
        import time
        time.sleep(15)
        
        # 获取快照
        print("📸 获取页面快照...")
        result = subprocess.run(
            ['agent-browser', 'snapshot'],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        snapshot_text = result.stdout
        
        # 关闭浏览器
        subprocess.run(['agent-browser', 'close'], timeout=10)
        print("✓ 浏览器已关闭\n")
        
        # 提取视频链接
        pattern = r'/watch\?v=([a-zA-Z0-9_-]{11})'
        matches = re.findall(pattern, snapshot_text)
        
        # 去重
        unique_videos = list(dict.fromkeys(matches))
        video_urls = [f"https://www.youtube.com/watch?v={vid}" for vid in unique_videos]
        
        print(f"✓ 提取到 {len(video_urls)} 个视频链接\n")
        
    except subprocess.TimeoutExpired:
        print("✗ 浏览器操作超时")
        return None
    except Exception as e:
        print(f"✗ 提取失败: {e}")
        return None
    
    # 3. 导入视频
    async with await NotebookLMClient.from_storage() as client:
        print(f"开始导入 {len(video_urls)} 个视频...\n")
        
        added_count = 0
        skipped_count = 0
        error_count = 0
        
        for i, url in enumerate(video_urls, 1):
            try:
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
        print(f"\n⏳ NoteBookLM 正在处理视频，这可能需要几分钟...")
        
        return notebook_id


async def check_notebook(notebook_id: str):
    """检查笔记本状态"""
    
    async with await NotebookLMClient.from_storage() as client:
        try:
            notebook = await client.notebooks.get(notebook_id)
            sources = await client.sources.list(notebook_id)
            
            print(f"\n笔记本状态：")
            print(f"  名称: {notebook.title}")
            print(f"  ID: {notebook.id}")
            print(f"  源文件数: {len(sources)}")
            print(f"  所有者: {'Owner' if notebook.is_owner else 'Shared'}")
            
            if sources:
                print(f"\n源文件列表（前5个）：")
                for i, source in enumerate(sources[:5], 1):
                    print(f"  {i}. {source.title[:60]}...")
                if len(sources) > 5:
                    print(f"  ... 还有 {len(sources) - 5} 个")
        except Exception as e:
            print(f"检查失败: {e}")


def main():
    """主函数"""
    
    if len(sys.argv) < 2:
        print("用法:")
        print(f"  {sys.argv[0]} browser <YouTube_URL> [笔记本名称]")
        print(f"  {sys.argv[0]} check <笔记本ID>")
        print()
        print("示例:")
        print(f"  {sys.argv[0]} browser 'https://www.youtube.com/watch?v=XXX&list=YYY' '我的笔记本'")
        print(f"  {sys.argv[0]} check <笔记本ID>")
        print()
        print("说明:")
        print("  - 使用 agent-browser 提取播放列表中的所有视频")
        print("  - 自动创建笔记本并导入所有视频")
        print("  - 自动去重，避免重复导入")
        print()
        return
    
    command = sys.argv[1].lower()
    
    if command == "browser":
        if len(sys.argv) < 3:
            print("用法: python3 script.py browser <YouTube_URL> [笔记本名称]")
            return
        
        youtube_url = sys.argv[2]
        notebook_name = sys.argv[3] if len(sys.argv) > 3 else "YouTube 播放列表"
        
        # 使用浏览器提取并导入
        asyncio.run(import_videos_with_browser(youtube_url, notebook_name))
    
    elif command == "check":
        if len(sys.argv) < 3:
            print("用法: python3 script.py check <笔记本ID>")
            return
        
        notebook_id = sys.argv[2]
        asyncio.run(check_notebook(notebook_id))
    
    else:
        print(f"未知命令: {command}")
        print("使用: browser | check")


if __name__ == "__main__":
    main()
