#!/usr/bin/env python3
"""
图片合并工具
将单个分镜合并为网格图片
"""

from PIL import Image, ImageDraw
import os


def merge_images(input_dir, grid_size='3x3', output_file='merged.jpg'):
    """
    合并多个图片为网格

    Args:
        input_dir: 输入图片目录
        grid_size: 网格大小 ('3x3' 或 '5x5')
        output_file: 输出文件名

    Returns:
        成功返回 True，失败返回 False
    """
    try:
        rows, cols = map(int, grid_size.split('x'))
        expected_count = rows * cols

        # 收集图片文件
        images = []
        for row in range(rows):
            for col in range(cols):
                image_path = os.path.join(input_dir, f'cell_{row}_{col}.jpg')

                if os.path.exists(image_path):
                    images.append(image_path)
                else:
                    print(f"❌ 错误: 找不到图片 {image_path}")
                    return False

        # 检查图片数量
        if len(images) != expected_count:
            print(f"❌ 错误: 图片数量 ({len(images)}) 与网格大小 ({grid_size}) 不匹配")
            print(f"   需要 {expected_count} 张图片，找到 {len(images)} 张")
            return False

        # 读取第一张图片获取大小
        first_img = Image.open(images[0])
        cell_size = 512
        margin = 2

        # 调整所有图片到统一大小
        resized_images = []
        for img_path in images:
            img = Image.open(img_path)
            img_resized = img.resize((cell_size, cell_size), Image.Resampling.LANCZOS)
            resized_images.append(img_resized)

        # 创建背景
        total_width = cols * cell_size + (cols - 1) * margin
        total_height = rows * cell_size + (rows - 1) * margin

        result = Image.new('RGB', (total_width, total_height), color='#1a1a1a')

        # 组合图片
        for row in range(rows):
            for col in range(cols):
                index = row * cols + col
                x = col * (cell_size + margin)
                y = row * (cell_size + margin)

                # 粘贴图片
                result.paste(resized_images[index], (x, y))

                # 绘制边框
                draw = ImageDraw.Draw(result)
                draw.rectangle(
                    [x, y, x + cell_size - margin, y + cell_size - margin],
                    outline='#333333',
                    width=2
                )

        # 保存结果
        result.save(output_file, 'JPEG', quality=95)
        return True

    except Exception as e:
        print(f"❌ 合并失败: {e}")
        return False


def merge_images_with_margin(input_dir, grid_size='3x3', output_file='merged.jpg', margin=2):
    """
    合并多个图片为网格（带边距）

    Args:
        input_dir: 输入图片目录
        grid_size: 网格大小 ('3x3' 或 '5x5')
        output_file: 输出文件名
        margin: 边距（像素）

    Returns:
        成功返回 True，失败返回 False
    """
    try:
        rows, cols = map(int, grid_size.split('x'))
        expected_count = rows * cols

        # 收集图片文件
        images = []
        for row in range(rows):
            for col in range(cols):
                image_path = os.path.join(input_dir, f'cell_{row}_{col}.jpg')

                if os.path.exists(image_path):
                    images.append(image_path)
                else:
                    print(f"❌ 错误: 找不到图片 {image_path}")
                    return False

        # 检查图片数量
        if len(images) != expected_count:
            print(f"❌ 错误: 图片数量 ({len(images)}) 与网格大小 ({grid_size}) 不匹配")
            return False

        # 读取第一张图片获取大小
        first_img = Image.open(images[0])
        cell_size = 512

        # 调整所有图片到统一大小
        resized_images = []
        for img_path in images:
            img = Image.open(img_path)
            img_resized = img.resize((cell_size, cell_size), Image.Resampling.LANCZOS)
            resized_images.append(img_resized)

        # 创建背景
        total_width = cols * cell_size + (cols - 1) * margin
        total_height = rows * cell_size + (rows - 1) * margin

        result = Image.new('RGB', (total_width, total_height), color='#1a1a1a')

        # 组合图片
        for row in range(rows):
            for col in range(cols):
                index = row * cols + col
                x = col * (cell_size + margin)
                y = row * (cell_size + margin)

                # 粘贴图片
                result.paste(resized_images[index], (x, y))

                # 绘制边框
                draw = ImageDraw.Draw(result)
                draw.rectangle(
                    [x, y, x + cell_size - margin, y + cell_size - margin],
                    outline='#333333',
                    width=2
                )

        # 保存结果
        result.save(output_file, 'JPEG', quality=95)
        return True

    except Exception as e:
        print(f"❌ 合并失败: {e}")
        return False


if __name__ == '__main__':
    # 测试合并
    print("测试合并 3x3 网格...")
    merge_images('./test_cuts', '3x3', 'test_merged_3x3.jpg')

    print("\n测试合并 5x5 网格...")
    merge_images('./test_cuts', '5x5', 'test_merged_5x5.jpg')
