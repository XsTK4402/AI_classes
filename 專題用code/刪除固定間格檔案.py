import os

for i in range(2457, 2467):
    url = f"C:\\Users\\Matthew\\Desktop\\800800halfhalf\\Endgame_{i}"

    file = os.listdir(url)
    os.chdir(url) # 改變程式的工作目錄至此

    print(len(file))

    for i in range(len(file))[::2]:
        os.remove(file[i])




# url = f"C:\\Users\\Matthew\\Desktop\\[test]50classes\\Endgame_2499"

# file = os.listdir(url)
# os.chdir(url) # 改變程式的工作目錄至此

# print(len(file))

# if len(file) >= 25:
#     for i in range(len(file))[::2]:
#         os.remove(file[i])
