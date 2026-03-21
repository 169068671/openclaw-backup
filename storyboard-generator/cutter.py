#!/usr/bin/env python3
"""
图片切割工具
将网格图片切割为单个分镜
"""

from PIL import Image
import os


def cut_image(input_file, grid_size='3x3', output_dir='./cuts'):
    """
    切割网格图片

    Args:
        input_file: 输入图片路径
        grid_size: 网格大小 ('3x3' 或 '5x5')
        output_dir: 输出目录

    Returns:
        切割后的图片数量，失败返回 None
    """
    try:
        # 打开图片
        img = Image.open(input_file)
        width, height = img.size

        rows, cols = map(int, grid_size.split('x'))

        # 计算单元格大小
        cell_width = width // cols
        cell_height = height // rows

        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)

        # 切割图片
        count = 0
        for row in range(rows):
            for col in range(cols):
                # 计算切割位置
                left = col * cell_width
                top = row * cell_height
                right = left + cell_width
                bottom = top + cell_height

                # 切割
                cell = img.crop((left, top, right, bottom))

                # 保存
                output_file = os.path.join(output_dir, f'cell_{row}_{col}.jpg')
                cell.save(output_file, 'JPEG', quality=95)

                count += 1
                print(f"   切割: cell_{row}_{col}.jpg")

        return count

    except Exception as e:
        print(f"❌ 切割失败: {e}")
        return None


def cut_image_with_margin(input_file, grid_size='3x3', output_dir='./cuts', margin=2):
    """
    切割网格图片（带边距）

    Args:
        input_file: 输入图片路径
        grid_size: 网格大小 ('3x3' 或 '5x5')
        output_dir: 输出目录
        margin: 边距（像素）

    Returns:
        切割后的图片数量，失败返回 None
    """
    try:
        # 打开图片
        img = Image.open(input_file)
        width, height = img.size

        rows, cols = map(int, grid_size.split('x'))

        # 计算单元格大小（包含边距）
        cell_width_with_margin = width // cols
        cell_height_with_margin = height // rows

        # 计算实际单元格大小（去除边距）
        cell_width = cell_width_with_margin - margin
        cell_height = cell_height_with_margin - margin

        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)

        # 切割图片
        count = 0
        for row in range(rows):
            for col in range(cols):
                # 计算切割位置（跳过边距）
                left = col * cell_width_with_margin + margin
                top = row * cell_height_with_margin + margin
                right = left + cell_width
                bottom = top + cell_height

                # 切割
                cell = img.crop((left, top, right, bottom))

                # 保存
                output_file = os.path.join(output_dir, f'cell_{row}_{col}.jpg')
                cell.save(output_file, 'JPEG', quality=95)

                count += 1
                print(f"   切割: cell_{row}_{col}.jpg")

        return count

    except Exception as e:
        print(f"❌ 切割失败: {e}")
        return None


if __name__ == '__main__':
    # 测试切割
    print("测试切割 3x3 网格...")
    cut_image('test_3x3.jpg', '3x3', './test_cuts')

    print("\n测试切割 5x5 网格...")
    cut_image('test_5x5.jpg', '5x5', './test_cuts')
