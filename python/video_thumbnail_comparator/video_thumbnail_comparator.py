import os
import subprocess
from PIL import Image
from PIL import ImageChops
import math
import sys

def extract_thumbnail(video_path, output_path, timestamp="00:00:01"):
    """
    使用 ffmpeg 提取视频的缩略图。
    :param video_path: 视频文件路径
    :param output_path: 输出缩略图路径
    :param timestamp: 截图时间点 (默认 1 秒)
    """
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    command = [
        "ffmpeg", "-y", "-i", video_path, "-ss", timestamp, "-vframes", "1", output_path
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def calculate_image_similarity(image1_path, image2_path):
    """
    比较两张图片的相似性，返回相似度分数。
    :param image1_path: 第一张图片路径
    :param image2_path: 第二张图片路径
    :return: 相似度分数 (0 表示完全不同,1 表示完全相同)
    """
    # image1 = Image.open(image1_path).convert("RGB")
    image2 = Image.open(image2_path).convert("RGB")
    diff = ImageChops.difference(image1, image2)
    h = diff.histogram()
    sq = (value * ((idx % 256) ** 2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares / float(image1.size[0] * image1.size[1]))
    return 1 - rms / 255.0  # 归一化到 [0, 1]

def are_thumbnails_similar(video1, video2, threshold=0.9):
    """
    比较两个视频的缩略图是否相似。
    :param video1: 第一个视频文件路径
    :param video2: 第二个视频文件路径
    :param threshold: 相似度阈值 (默认 0.9)
    :return: 是否相似 (True/False)
    """
    thumbnail1 = "thumbnail1.jpg"
    thumbnail2 = "thumbnail2.jpg"
    try:
        extract_thumbnail(video1, thumbnail1)
        extract_thumbnail(video2, thumbnail2)
        similarity = calculate_image_similarity(thumbnail1, thumbnail2)
        return similarity >= threshold
    finally:
        if os.path.exists(thumbnail1):
            os.remove(thumbnail1)
        if os.path.exists(thumbnail2):
            os.remove(thumbnail2)

def are_thumbnails_similar_in_directory(video_dir1, video_dir2, threshold=0.9):
    """
    比较目录中的两个视频的缩略图是否相似。
    :param video_dir: 包含两个视频文件的目录路径
    :param threshold: 相似度阈值 (默认 0.9)
    :return: 是否相似 (True/False)
    """
    video1_files = [f for f in os.listdir(video_dir1) if f.endswith(('.mp4', '.avi', '.mkv'))]
    video2_files = [f for f in os.listdir(video_dir2) if f.endswith(('.mp4', '.avi', '.mkv'))]
    if not video1_files or not video2_files:
        raise FileNotFoundError("No video files found in one or both directories.")
    for video1_file in video1_files:
        for video2_file in video2_files:
                video1_path = os.path.join(video_dir1, video1_file)
                video2_path = os.path.join(video_dir2, video2_file)
                result = are_thumbnails_similar(video1_path, video2_path, threshold)
                if result:
                    print(f"Similar thumbnails found: {video1_file} and {video2_file}")
                    return True
 

if __name__ == "__main__":
    video_directory1 = "path/to/your/video/directory"  # 修改为实际视频目录路径
    video_directory2 = "path/to/your/video/directory2"  # 修改为实际视频目录路径
    try:
        if are_thumbnails_similar_in_directory(video_directory1, video_directory2):
            print("The videos have similar thumbnails.")
        else:
            print("The videos do not have similar thumbnails.")
    except Exception as e:
        print(f"Error: {e}")
