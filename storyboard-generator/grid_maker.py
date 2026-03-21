#!/usr/bin/env python3
"""
网格图片生成器
创建分镜网格模板
"""

from PIL import Image, ImageDraw, ImageFont
import os


def create_grid_template(grid_size, output_file='storyboard.jpg'):
    """
    创建网格模板图片

    Args:
        grid_size: 网格大小 ('3x3' 或 '5x5')
        output_file: 输出文件名
    """
    rows, cols = map(int, grid_size.split('x'))

    # 每个单元格的大小
    cell_size = 512
    margin = 2

    # 图片总大小
    total_width = cols * cell_size + (cols - 1) * margin
    total_height = rows * cell_size + (rows - 1) * margin

    # 创建背景
    img = Image.new('RGB', (total_width, total_height), color='#1a1a1a')
    draw = ImageDraw.Draw(img)

    # 尝试加载字体
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        font = ImageFont.load_default()

    # 绘制网格
    for row in range(rows):
        for col in range(cols):
            # 计算位置
            x = col * (cell_size + margin)
            y = row * (cell_size + margin)

            # 绘制单元格边框
            draw.rectangle(
                [x, y, x + cell_size - margin, y + cell_size - margin],
                outline='#333333',
                width=2
            )

            # 绘制标签
            label = f"{row * cols + col + 1}"
            draw.text(
                (x + 10, y + 10),
                label,
                fill='#666666',
                font=font
            )

            # 绘制提示文本
            prompt_text = "镜头描述"
            draw.text(
                (x + 10, y + 50),
                prompt_text,
                fill='#888888',
                font=font
            )

    # 保存图片
    img.save(output_file, 'JPEG', quality=95)
    print(f"✅ 网格模板已创建: {output_file}")

    return output_file


def create_grid_from_images(images, grid_size, output_file='storyboard.jpg'):
    """
    从多张图片创建网格

    Args:
        images: 图片路径列表
        grid_size: 网格大小 ('3x3' 或 '5x5')
        output_file: 输出文件名
    """
    rows, cols = map(int, grid_size.split('x'))

    # 检查图片数量
    if len(images) != rows * cols:
        print(f"⚠️  警告: 图片数量 ({len(images)}) 与网格大小 ({grid_size}) 不匹配")
        return None

    # 读取第一张图片获取大小
    first_img = Image.open(images[0])
    cell_size = 512
    margin = 2

    # 调整图片大小
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
    print(f"✅ 网格图片已创建: {output_file}")

    return output_file


if __name__ == '__main__':
    # 测试创建 3x3 网格
    create_grid_template('3x3', 'test_3x3.jpg')

    # 测试创建 5x5 网格
    create_grid_template('5x5', 'test_5x5.jpg')
