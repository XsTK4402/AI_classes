import os


url = "C:\\Users\\Matthew\\Desktop\\python\\dataset\\50classes_meme"
file = os.listdir(url)
os.chdir(url) # 改變程式的工作目錄至此

print(file)

for i in range(len(file)):
    os.rename(file[i], file[i].replace("G", "g"))
