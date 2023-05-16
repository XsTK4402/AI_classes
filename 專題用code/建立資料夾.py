import os

a = 2457
b = 2507
for i in range(a,b):
    path = f'C:\\Users\\Matthew\\Desktop\\新增資料夾\\Endgame_{i}'

    if not os.path.isdir(path):
        os.mkdir(path)