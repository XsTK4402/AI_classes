def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3


print(max_num(-1, -10, -100))

# 定義max_num有三個數字num1,num2.num3
# 判斷num1是否>=num2和num3，若是則回傳num1值
# 否則判斷num2是否>=num1和num1，若是則回傳num2值
# 否則判斷num3是否>=num1和num2，若是則回傳num3值
# 列印max_num(-1,-10,-100)

number = 0
if number > 0:
    print("正數")
elif number < 0:
    print("負數")
else:
    print("0")


number = int(input("請輸入一個數字: "))
if number % 2 == 1:
    print("這是一個奇數")
else:
    print("這是一個偶數")
