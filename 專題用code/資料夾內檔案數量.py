import os

url = "C:\\Users\\Matthew\\Desktop\\[test]50classes_800x800arguments"
file = os.listdir(url)
os.chdir(url) # 改變程式的工作目錄至此

print(len(file))
# print(file)

for i in file:
    # os.rename(i, i.replace("scene", "Endgame"))
    print(f"{i}" + "：" +  f"{len(os.listdir(i))}")
