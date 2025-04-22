import os
 
# 修改文件扩展名的函数
def rename_files(directory, old_ext, new_ext):
    for filename in os.listdir(directory):
        if filename.endswith(old_ext):
            old_name = os.path.join(directory, filename)
            new_name = os.path.join(directory, filename.replace(old_ext, new_ext))
            os.rename(old_name, new_name)
 
# 指定目录和要修改的扩展名
directory = r'D:\studyhard_lin\2025_research\code_program\comic_panels_analysis\dataset\test\BattleThroughtheHeavens_002'  # 当前目录
old_ext = '.jpeg'
new_ext = '.jpg'
 
# 执行文件重命名
rename_files(directory, old_ext, new_ext)
print("转换成功！")