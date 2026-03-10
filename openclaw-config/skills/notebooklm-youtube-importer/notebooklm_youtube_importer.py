#!/usr/bin/env python3
"""
NotebookLM YouTube 播放列表导入器
用于将 YouTube 播放列表中的所有视频导入到 NotebookLM 笔记本
"""

import asyncio
import os
import sys
from notebooklm import NotebookLMClient

# 配置代理（根据需要修改）
os.environ['HTTP_PROXY'] = 'socks5://127.0.0.1:1080'
os.environ['HTTPS_PROXY'] = 'socks5://127.0.0.1:1080'
os.environ['ALL_PROXY'] = 'socks5://127.0.0.1:1080'

# FreeCAD: Learn Python (Beginners Guide) 播放列表 - 37个视频
FREECAD_PYTHON_VIDEOS = [
    ("01 Setup", "https://www.youtube.com/watch?v=KujiAIHNRKQ"),
    ("02 Simple input", "https://www.youtube.com/watch?v=2dhtUh-O0zI"),
    ("03 Data types", "https://www.youtube.com/watch?v=9CfOJdIs0rA"),
    ("04 Operators", "https://www.youtube.com/watch?v=jtl0XEPtsgA"),
    ("05 Conditions", "https://www.youtube.com/watch?v=H8K8c5HCBII"),
    ("06 For Loop", "https://www.youtube.com/watch?v=M_V6QYEa56c"),
    ("07 Refactoring", "https://www.youtube.com/watch?v=v6ANLO5aDN4"),
    ("08 Dictionary", "https://www.youtube.com/watch?v=wZwimBd2K08"),
    ("09 Colour faces", "https://www.youtube.com/watch?v=mckkPGAso2c"),
    ("10 Try except", "https://www.youtube.com/watch?v=YV3Tpdi67eM"),
    ("11 Timer Loops", "https://www.youtube.com/watch?v=Y7Oi51_TP8I"),
    ("12 Collections 1", "https://www.youtube.com/watch?v=2PO_fvE2NQM"),
    ("13 Collections 2", "https://www.youtube.com/watch?v=iADzJkIU_tU"),
    ("14 Coordinates list", "https://www.youtube.com/watch?v=9_0IU1Ah1Yw"),
    ("15 Image mask 1", "https://www.youtube.com/watch?v=qFL5v6CNPK0"),
    ("16 Image mask 2", "https://www.youtube.com/watch?v=332oZ83yRug"),
    ("17 C64 Braille", "https://www.youtube.com/watch?v=W3BRhcL-3zM"),
    ("18 Gear animation", "https://www.youtube.com/watch?v=i9jFzZ-VKVw"),
    ("19 Buttons GUI 1", "https://www.youtube.com/watch?v=juk-jEj4NJg"),
    ("20 Slider GUI 2", "https://www.youtube.com/watch?v=QwTN884trnk"),
    ("21 Digger Arm", "https://www.youtube.com/watch?v=tkfJ8cLGS90"),
    ("22 Text file", "https://www.youtube.com/watch?v=asLTXzkFjLY"),
    ("23 Face select 1", "https://www.youtube.com/watch?v=hP4j22ELbIM"),
    ("24 Face select 2", "https://www.youtube.com/watch?v=euK-dcmbPh0"),
    ("25 Path Workbench", "https://www.youtube.com/watch?v=wlPx93pjKJo"),
    ("26 Randomness 1", "https://www.youtube.com/watch?v=2ZgL6cejQ40"),
    ("27 Randomness 2 Long", "https://www.youtube.com/watch?v=Jo5bQ9kzZR8"),
    ("28 Randomness 2 Short", "https://www.youtube.com/watch?v=moS0WBmiHK4"),
    ("29 Move tools", "https://www.youtube.com/watch?v=ZdAtdch3EKE"),
    ("30 3D Collision", "https://www.youtube.com/watch?v=6CIorZvubtc"),
    ("31 Console tips", "https://www.youtube.com/watch?v=_shYQMpTAk4"),
    ("32 Spring anim", "https://www.youtube.com/watch?v=1T8znLnUBYM"),
    ("33 Custom widgets", "https://www.youtube.com/watch?v=_tFZRfQNGtA"),
    ("34 Move to target", "https://www.youtube.com/watch?v=7TrmrAAKLT0"),
    ("35 Animation tricks", "https://www.youtube.com/watch?v=j7jMgVpY9Fc"),
    ("36 Follow path", "https://www.youtube.com/watch?v=sIQnX6L1Kys"),
    ("37 Viewport layout", "https://www.youtube.com/watch?v=msxwZymg8ys"),
]


async def import_videos(notebook_id: str, videos: list):
    """导入视频到笔记本"""
    
    async with await NotebookLMClient.from_storage() as client:
        print(f"笔记本 ID: {notebook_id}")
        print(f"开始导入 {len(videos)} 个视频...\n")
        
        added_count = 0
        skipped_count = 0
        error_count = 0
        
        for i, (title, url) in enumerate(videos, 1):
            try:
                # 尝试添加视频
                await client.sources.add_url(notebook_id, url, wait=True)
                added_count += 1
                print(f"[{i}/{len(videos)}] ✓ [{title}] 添加成功")
            except Exception as e:
                error_msg = str(e).lower()
                # 检查是否是重复错误
                if "already" in error_msg or "duplicate" in error_msg:
                    skipped_count += 1
                    print(f"[{i}/{len(videos)}] - [{title}] 已存在，跳过")
                else:
                    error_count += 1
                    print(f"[{i}/{len(videos)}] ✗ [{title}] 失败: {e}")
            
            # 每5个视频后暂停一下，避免过载
            if i % 5 == 0:
                await asyncio.sleep(2)
        
        print(f"\n{'='*60}")
        print(f"导入完成！")
        print(f"{'='*60}")
        print(f"✓ 成功添加: {added_count}")
        print(f"- 已存在跳过: {skipped_count}")
        print(f"✗ 失败: {error_count}")
        print(f"总计: {len(videos)}")


async def create_and_import(notebook_name: str, videos: list):
    """创建笔记本并导入视频"""
    
    async with await NotebookLMClient.from_storage() as client:
        # 创建笔记本
        notebook = await client.notebooks.create(notebook_name)
        notebook_id = notebook.id
        
        print(f"✓ 笔记本创建成功！")
        print(f"  名称: {notebook_name}")
        print(f"  ID: {notebook_id}")
        print(f"\n开始导入视频...\n")
        
        # 导入视频
        await import_videos(notebook_id, videos)
        
        print(f"\n笔记本 ID: {notebook_id}")
        print(f"可以使用此 ID 进行后续操作")


async def check_notebook(notebook_id: str):
    """检查笔记本状态"""
    
    async with await NotebookLMClient.from_storage() as client:
        try:
            notebook = await client.notebooks.get(notebook_id)
            print(f"\n笔记本状态：")
            print(f"  名称: {notebook.title}")
            print(f"  ID: {notebook.id}")
            print(f"  源文件数: {notebook.sources_count}")
            print(f"  所有者: {'Owner' if notebook.is_owner else 'Shared'}")
        except Exception as e:
            print(f"检查失败: {e}")


def main():
    """主函数"""
    
    if len(sys.argv) < 2:
        print("用法:")
        print("  1. 创建新笔记本并导入:")
        print(f"     {sys.argv[0]} create <笔记本名称>")
        print()
        print("  2. 导入到现有笔记本:")
        print(f"     {sys.argv[0]} import <笔记本ID>")
        print()
        print("  3. 检查笔记本状态:")
        print(f"     {sys.argv[0]} check <笔记本ID>")
        print()
        print("  4. 使用 FreeCAD 教程播放列表:")
        print(f"     {sys.argv[0]} freecad <create|import|check> [笔记本ID]")
        print()
        return
    
    command = sys.argv[1].lower()
    
    if command == "create":
        # 创建新笔记本
        notebook_name = sys.argv[2] if len(sys.argv) > 2 else "YouTube Videos"
        asyncio.run(create_and_import(notebook_name, FREECAD_PYTHON_VIDEOS))
    
    elif command == "import":
        # 导入到现有笔记本
        notebook_id = sys.argv[2]
        asyncio.run(import_videos(notebook_id, FREECAD_PYTHON_VIDEOS))
    
    elif command == "check":
        # 检查笔记本
        notebook_id = sys.argv[2]
        asyncio.run(check_notebook(notebook_id))
    
    elif command == "freecad":
        # FreeCAD 教程快捷方式
        if len(sys.argv) < 3:
            print("用法: python3 script.py freecad <create|import|check> [笔记本ID]")
            return
        
        subcommand = sys.argv[2].lower()
        
        if subcommand == "create":
            name = sys.argv[3] if len(sys.argv) > 3 else "FreeCAD Python 教程"
            asyncio.run(create_and_import(name, FREECAD_PYTHON_VIDEOS))
        
        elif subcommand == "import":
            if len(sys.argv) < 4:
                print("用法: python3 script.py freecad import <笔记本ID>")
                return
            notebook_id = sys.argv[3]
            asyncio.run(import_videos(notebook_id, FREECAD_PYTHON_VIDEOS))
        
        elif subcommand == "check":
            if len(sys.argv) < 4:
                print("用法: python3 script.py freecad check <笔记本ID>")
                return
            notebook_id = sys.argv[3]
            asyncio.run(check_notebook(notebook_id))
    
    else:
        print(f"未知命令: {command}")
        print("使用: create | import | check | freecad")


if __name__ == "__main__":
    main()
