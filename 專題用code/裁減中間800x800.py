import os
from os.path import join
from PIL import Image, ImageOps


oldpath = "C:\\Users\\Matthew\\Desktop\\新250張迷因"
newpath = "C:\\Users\\Matthew\\Desktop\\新增資料夾"

size = (800, 800) # 指定裁切的大小

def cropping(f, path, folder):
    destpath = join(newpath, folder)         # 新目標路徑
    img = Image.open(path).convert("RGB")       # 圖片統一轉成RGB
    newimg = ImageOps.fit(img, size, Image.LANCZOS) # 裁切 Image.LANCZOS優化器
    # 如果資料夾不存在，先建立再存圖
    if os.path.exists(destpath):
        newimg.save(join(destpath, f))
    else:
        os.mkdir(destpath)
        newimg.save(join(destpath, f))

# root 當前正在遍歷的目錄路徑
# dirs 當前目錄下的子目錄(資料夾)
# files 當前目錄下的所有檔案
for root, dirs, files in os.walk(oldpath): # 遍歷指定目錄下所有資料夾與檔案
    print("root：", root)
    if files:
        print("create cropping image")
        for f in files:
            path = join(root, f)     # 圖片檔路徑
            folder = root.split("/")[-1]
            cropping(f, path, folder)   # 裁切、建資料夾、存圖
            print(f, end=", ")
        print(f"\n{folder} {len(os.listdir(root))} images Done")
    else:
        print("no search files")
    print("--"*20)
