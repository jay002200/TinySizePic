import tkinter
import os
from tkinter import filedialog
from PIL import Image


def read_directory(path):
    array_img = [] 
    for filename in os.listdir(r"{0}".format(path)):
        if filename.endswith(r".jpg") or filename.endswith(r".png"): 
            array_img.append(filename)  
    return array_img

def compress_image(input_file_path, output_file_path, max_size, quality=80):
    # 打開圖像文件
    with Image.open(input_file_path) as im:
        # 檢查圖像大小是否超過指定大小
        if im.size[0] > max_size or im.size[1] > max_size:
            # 計算縮小比例
            ratio = max_size / max(im.size)
            # 計算縮小後的大小
            size = tuple([int(x * ratio) for x in im.size])
            # 縮小圖像
            im = im.resize(size, Image.ANTIALIAS)
        # 保存圖像文件
        im.save(output_file_path, format='JPEG', quality=quality, optimize=True)

try:
    print("選擇要壓縮圖片的資料夾")
  
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()  
    all_pic = read_directory(file_path)
    for file in all_pic:
        pic_path = file_path + "/" + file
        compress_image(pic_path,pic_path,4096,quality=50)
        
    print("壓縮成功")
except:
    print("未選擇資料夾或意外錯誤")
    exit()





