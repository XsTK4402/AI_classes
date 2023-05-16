import os
import datetime

# 指定欲更改名稱的目錄路徑
file_path = "C:\\Users\\Matthew\\Desktop\\python\\Avenger_Endgame_24FPS"

#注意这里使用lambda表达式将文件按照最后修改时间顺序升序排列
# os.path.getmtime() 函数是获取文件最后修改时间
# os.path.getctime() 函数是获取文件最后创建时间
def get_file_list(file_path):
    dir_list = os.listdir(file_path)
    if not dir_list:
        return
    else:
        dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        print(dir_list)
        return dir_list
    
a = get_file_list(file_path)
# print(a)

for i in range(len(a)):
    os.rename(os.path.join(file_path, a[i]), os.path.join(file_path, f"scene{i+1}"))