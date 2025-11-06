#!/usr/bin/env python3
"""
从vlm文件夹中的每个子文件夹的visual文件夹中随机抽取一张图片，
然后使用OpenCV将这些图片拼接成一张大图
"""

import os
import random
import cv2
import numpy as np
import math
from pathlib import Path

def get_vlm_subdirs(vlm_path):
    """获取vlm文件夹中所有数字编号的子文件夹"""
    subdirs = []
    if not os.path.exists(vlm_path):
        print(f"错误：vlm路径不存在: {vlm_path}")
        return subdirs

    for item in os.listdir(vlm_path):
        item_path = os.path.join(vlm_path, item)
        if os.path.isdir(item_path) and item.isdigit():
            visual_path = os.path.join(item_path, 'visual')
            if os.path.exists(visual_path):
                subdirs.append(item_path)

    # 按数字大小排序
    subdirs.sort(key=lambda x: int(os.path.basename(x)))
    return subdirs

def get_random_image_from_visual(visual_path):
    """从visual文件夹中随机选择一张图片"""
    if not os.path.exists(visual_path):
        return None

    # 获取所有图片文件
    image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
    images = []
    for file in os.listdir(visual_path):
        if any(file.lower().endswith(ext) for ext in image_extensions):
            images.append(os.path.join(visual_path, file))

    if not images:
        return None

    # 随机选择一张图片
    return random.choice(images)

def resize_image_to_target(image, target_width, target_height):
    """将图片调整到目标尺寸，保持宽高比"""
    h, w = image.shape[:2]

    # 计算缩放比例
    scale_w = target_width / w
    scale_h = target_height / h
    scale = min(scale_w, scale_h)

    # 计算新尺寸
    new_w = int(w * scale)
    new_h = int(h * scale)

    # 调整图片大小
    resized = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # 创建目标尺寸的画布（黑色背景）
    canvas = np.zeros((target_height, target_width, 3), dtype=np.uint8)

    # 计算居中位置
    y_offset = (target_height - new_h) // 2
    x_offset = (target_width - new_w) // 2

    # 将调整后的图片放到画布中央
    canvas[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized

    return canvas

def create_image_collage(vlm_path, vln_path, output_path, max_images=None, grid_cols=None):
    """
    创建图片拼接
    
    Args:
        vlm_path: vlm文件夹路径
        output_path: 输出图片路径
        max_images: 最大图片数量限制
        grid_cols: 网格列数，如果为None则自动计算
    """
    print(f"开始处理vlm文件夹: {vlm_path}")

    # 获取所有子文件夹
    subdirs = get_vlm_subdirs(vlm_path)
    if not subdirs:
        print("未找到任何包含visual文件夹的子文件夹")
        return

    print(f"找到 {len(subdirs)} 个子文件夹")

    # 限制处理的图片数量
    if max_images and len(subdirs) > max_images:
        subdirs = subdirs[:max_images]
        print(f"限制处理前 {max_images} 个文件夹")

    # 收集所有图片
    images = []
    image_paths = []

    for subdir in subdirs:
        visual_path = os.path.join(subdir, 'visual')
        image_path = get_random_image_from_visual(visual_path)

        if image_path:
            image = cv2.imread(image_path)
            if image is not None:
                images.append(image)
                image_paths.append(image_path)
                print(f"已加载: {image_path}")
            else:
                print(f"无法加载图片: {image_path}")
        else:
            print(f"在 {visual_path} 中未找到图片")

    if not images:
        print("未找到任何可用的图片")
        return

    print(f"总共加载了 {len(images)} 张图片")

    # 计算网格布局
    num_images = len(images)
    if grid_cols is None:
        # 自动计算最接近正方形的网格
        grid_cols = int(math.ceil(math.sqrt(num_images)))

    grid_rows = int(math.ceil(num_images / grid_cols))

    print(f"网格布局: {grid_rows} 行 x {grid_cols} 列")

    # 获取单张图片的尺寸（使用第一张图片作为参考）
    sample_image = images[0]
    img_height, img_width = sample_image.shape[:2]

    # 计算每个网格单元的目标尺寸
    cell_width = 300  # 可以调整这个值
    cell_height = int(cell_width * img_height / img_width)  # 保持原始宽高比

    # 创建拼接画布
    canvas_width = grid_cols * cell_width
    canvas_height = grid_rows * cell_height
    canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

    print(f"画布尺寸: {canvas_width} x {canvas_height}")
    print(f"单元格尺寸: {cell_width} x {cell_height}")

    # 将图片放置到网格中
    for i, image in enumerate(images):
        row = i // grid_cols
        col = i % grid_cols

        # 调整图片尺寸
        resized_image = resize_image_to_target(image, cell_width, cell_height)

        # 计算在画布上的位置
        y_start = row * cell_height
        y_end = y_start + cell_height
        x_start = col * cell_width
        x_end = x_start + cell_width

        # 放置图片
        canvas[y_start:y_end, x_start:x_end] = resized_image

        print(f"已放置图片 {i+1}/{len(images)} 到位置 ({row}, {col})")

    # 保存拼接后的图片
    success = cv2.imwrite(output_path, canvas)
    if success:
        print(f"拼接完成！输出文件: {output_path}")
        print(f"最终图片尺寸: {canvas_width} x {canvas_height}")
    else:
        print(f"保存失败: {output_path}")

def get_random_images_from_folder(folder_path, num_images):
    """从指定文件夹下所有子文件夹/visual中随机选取num_images张图片"""
    subdirs = get_vlm_subdirs(folder_path)
    all_images = []
    for subdir in subdirs:
        visual_path = os.path.join(subdir, 'visual')
        if os.path.exists(visual_path):
            image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
            for file in os.listdir(visual_path):
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    all_images.append(os.path.join(visual_path, file))
    if len(all_images) < num_images:
        print(f"警告: {folder_path} 可用图片不足 {num_images} 张, 实际: {len(all_images)}")
        num_images = len(all_images)
    return random.sample(all_images, num_images)

def create_image_collage_from_two_folders(vlm_path, vln_path, output_path, num_each=72, grid_cols=16, grid_rows=9):
    """
    从vlm和vln各取num_each张图片, 随机拼接成grid_cols*grid_rows拼图
    """
    print(f"从 {vlm_path} 和 {vln_path} 各取 {num_each} 张图片, 拼接成 {grid_cols}x{grid_rows}")
    images_vlm = get_random_images_from_folder(vlm_path, num_each)
    images_vln = get_random_images_from_folder(vln_path, num_each)
    all_images = images_vlm + images_vln
    if len(all_images) < grid_cols * grid_rows:
        print("图片总数不足, 无法拼接")
        return
    random.shuffle(all_images)
    selected_images = all_images[:grid_cols * grid_rows]
    # 读取图片
    loaded_images = []
    for img_path in selected_images:
        img = cv2.imread(img_path)
        if img is not None:
            loaded_images.append(img)
        else:
            print(f"无法加载图片: {img_path}")
    if len(loaded_images) < grid_cols * grid_rows:
        print("有效图片不足, 无法拼接")
        return
    # 统一尺寸
    cell_width = 300
    h, w = loaded_images[0].shape[:2]
    cell_height = int(cell_width * h / w)
    canvas_width = grid_cols * cell_width
    canvas_height = grid_rows * cell_height
    canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)
    for idx, image in enumerate(loaded_images):
        row = idx // grid_cols
        col = idx % grid_cols
        resized_image = resize_image_to_target(image, cell_width, cell_height)
        y_start = row * cell_height
        y_end = y_start + cell_height
        x_start = col * cell_width
        x_end = x_start + cell_width
        canvas[y_start:y_end, x_start:x_end] = resized_image
    success = cv2.imwrite(output_path, canvas)
    if success:
        print(f"拼接完成！输出文件: {output_path}")
        print(f"最终图片尺寸: {canvas_width} x {canvas_height}")
    else:
        print(f"保存失败: {output_path}")


def main():
    """主函数"""
    vlm_path = "/shared5/vlm"
    vln_path = "/shared5/vln"
    output_path = "./vlm_vln_collage.jpg"
    num_each = 72
    grid_cols = 16
    grid_rows = 9
    print("=== 图片拼接工具 (vlm+vln) ===")
    print(f"VLM路径: {vlm_path}")
    print(f"VLN路径: {vln_path}")
    print(f"输出路径: {output_path}")
    print(f"每个文件夹取: {num_each} 张")
    print(f"拼接网格: {grid_cols} x {grid_rows}")
    print("=" * 30)
    try:
        create_image_collage_from_two_folders(vlm_path, vln_path, output_path, num_each, grid_cols, grid_rows)
    except Exception as e:
        print(f"发生错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
