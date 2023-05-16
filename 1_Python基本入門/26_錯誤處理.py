# try:
#     print(1/0)
# except:
#     print("除數不可以為0")



try:
    pwd = input("請輸入您的密碼: ")
    if len(pwd)<8:
        raise Exception("密碼長度不足")
    if len(pwd)>16:
        raise Exception("密碼長度太長")
except Exception as e:
    print("密碼長度檢查異常: " + str(e))  