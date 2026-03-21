#!/usr/bin/env python3
"""
分镜生成器 - 主程序
基于 MiniMax API 生成分镜图片
"""

import argparse
import json
import os
import sys
from pathlib import Path

# 添加当前目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from grid_maker import create_grid_template
from cutter import cut_image
from merger import merge_images


class Config:
    """配置管理"""

    CONFIG_PATH = Path.home() / '.storyboard-generator' / 'config.json'

    @staticmethod
    def load():
        """加载配置"""
        if Config.CONFIG_PATH.exists():
            with open(Config.CONFIG_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        return Config.default_config()

    @staticmethod
    def default_config():
        """默认配置"""
        return {
            'apiKey': '',
            'model': 'minimax-image-01',
            'defaultGrid': '3x3',
            'defaultStyle': 'real',
            'outputDir': str(Path.home() / 'storyboard-output'),
            'maxRetries': 3
        }

    @staticmethod
    def save(config):
        """保存配置"""
        Config.CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(Config.CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

    @staticmethod
    def set_api_key(api_key):
        """设置 API Key"""
        config = Config.load()
        config['apiKey'] = api_key
        Config.save(config)
        print(f"✅ API Key 已保存到 {Config.CONFIG_PATH}")


def generate_storyboard(args):
    """生成分镜图片"""
    config = Config.load()

    if not config.get('apiKey'):
        print("❌ 错误: 请先配置 MiniMax API Key")
        print("运行: storyboard-generator config <API Key>")
        sys.exit(1)

    # 解析提示词
    prompts = args.prompts.split('|')
    grid = args.grid if args.grid else config.get('defaultGrid', '3x3')
    style = args.style if args.style else config.get('defaultStyle', 'real')

    print(f"🎬 开始生成分镜...")
    print(f"   网格: {grid}")
    print(f"   风格: {style}")
    print(f"   分镜数量: {len(prompts)}")

    # 检查网格大小与分镜数量匹配
    rows, cols = map(int, grid.split('x'))
    expected_cells = rows * cols

    if len(prompts) != expected_cells:
        print(f"⚠️  警告: 提示词数量 ({len(prompts)}) 与网格大小 ({grid}) 不匹配")
        print(f"   {grid} 网格需要 {expected_cells} 个提示词")
        response = input("是否继续? (y/n): ")
        if response.lower() != 'y':
            print("已取消")
            return

    # TODO: 调用 MiniMax API 生成图片
    # 这里先创建模板图片
    output_file = args.output if args.output else 'storyboard.jpg'
    create_grid_template(grid, output_file)

    print(f"✅ 分镜已生成: {output_file}")


def cut_storyboard(args):
    """切割分镜图片"""
    grid = args.grid if args.grid else '3x3'
    output_dir = args.output if args.output else './cuts'

    print(f"✂️  开始切割分镜...")
    print(f"   输入: {args.input}")
    print(f"   网格: {grid}")
    print(f"   输出目录: {output_dir}")

    result = cut_image(args.input, grid, output_dir)

    if result:
        print(f"✅ 切割完成，共 {result} 个分镜")
        print(f"   位置: {output_dir}")
    else:
        print("❌ 切割失败")


def merge_storyboard(args):
    """合并分镜图片"""
    grid = args.grid if args.grid else '3x3'
    output_file = args.output if args.output else 'merged.jpg'

    print(f"🔗 开始合并分镜...")
    print(f"   输入目录: {args.input}")
    print(f"   网格: {grid}")
    print(f"   输出文件: {output_file}")

    result = merge_images(args.input, grid, output_file)

    if result:
        print(f"✅ 合并完成: {output_file}")
    else:
        print("❌ 合并失败")


def export_text(args):
    """导出提示词文本"""
    output_file = args.output if args.output else 'prompts.txt'

    print(f"📝 导出提示词到: {output_file}")

    # TODO: 实现提示词导出
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 分镜提示词\n\n")
        f.write("# 请编辑以下提示词，然后重新生成\n")

    print(f"✅ 提示词已导出: {output_file}")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='分镜生成器 - 基于 MiniMax API 的轻量级分镜生成工具',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    # config 命令
    config_parser = subparsers.add_parser('config', help='配置 MiniMax API Key')
    config_parser.add_argument('apiKey', help='MiniMax API Key')

    # generate 命令
    generate_parser = subparsers.add_parser('generate', help='生成分镜图片')
    generate_parser.add_argument('--grid', choices=['3x3', '5x5'], help='网格大小 (3x3 或 5x5)')
    generate_parser.add_argument('--prompts', help='分镜提示词，用 | 分隔')
    generate_parser.add_argument('--style', choices=['real', 'anime', '3d', 'cartoon'], help='图片风格')
    generate_parser.add_argument('--image', help='参考图片路径')
    generate_parser.add_argument('--output', help='输出文件名')

    # cut 命令
    cut_parser = subparsers.add_parser('cut', help='切割分镜图片')
    cut_parser.add_argument('input', help='输入图片文件')
    cut_parser.add_argument('--output', help='输出目录')
    cut_parser.add_argument('--grid', choices=['3x3', '5x5'], help='网格大小')

    # merge 命令
    merge_parser = subparsers.add_parser('merge', help='合并分镜图片')
    merge_parser.add_argument('input', help='输入图片目录')
    merge_parser.add_argument('--grid', choices=['3x3', '5x5'], help='网格大小')
    merge_parser.add_argument('--output', help='输出文件名')

    # export-text 命令
    export_parser = subparsers.add_parser('export-text', help='导出提示词文本')
    export_parser.add_argument('--output', help='输出文件名')

    args = parser.parse_args()

    # 执行命令
    if args.command == 'config':
        Config.set_api_key(args.apiKey)
    elif args.command == 'generate':
        generate_storyboard(args)
    elif args.command == 'cut':
        cut_storyboard(args)
    elif args.command == 'merge':
        merge_storyboard(args)
    elif args.command == 'export-text':
        export_text(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
