num1 = input("請輸入第一個數字：")
sym = input("請選擇計算符號1(+)、2(-)、3(*)、4(/)：")
num2 = input("請入第二個數字：")

if float(sym) == 1:
    print(float(num1)+float(num2))
elif float(sym) == 2:
    print(float(num1)-float(num2))
elif float(sym) == 3:
    print(float(num1)*float(num2))
elif float(sym) == 4:
    print(float(num1)/float(num2))
else:
    print("輸入數值錯誤")
