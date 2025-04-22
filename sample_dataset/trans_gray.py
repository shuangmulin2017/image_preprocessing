import os
from PIL import Image
 
def convert_to_grayscale(input_folder, output_folder):
    """
    将指定文件夹内所有彩色图片转换为灰度图并保存到输出文件夹。
    :param input_folder: 彩色图片所在的文件夹路径。
    :param output_folder: 灰度图片将要保存的文件夹路径。
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
 
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            color_image = Image.open(os.path.join(input_folder, filename))
            gray_image = color_image.convert('L')
            gray_image.save(os.path.join(output_folder, filename))
 

input_folder = '.\BattleThroughtheHeavens_001'
output_folder = '.\BattleThroughtheHeavens_001_gray'
convert_to_grayscale(input_folder, output_folder)