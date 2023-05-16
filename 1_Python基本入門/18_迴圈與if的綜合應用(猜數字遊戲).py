import random
correct_num = random.randrange(1, 101)
guess = float(input("請輸入一個數字："))

while guess != correct_num:
    if guess < correct_num:
        guess = float(input("猜大一點！"))
    elif guess > correct_num:
        guess = float(input("猜小一點！"))

print("恭喜答對！")
