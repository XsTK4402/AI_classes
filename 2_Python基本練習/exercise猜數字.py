import random
com_num = random.randint(1,100)
guess = int(input())

while guess != com_num:
    if guess > com_num:
        print("請猜小一點")
        guess = int(input())
    elif guess < com_num:
        print("請猜大一點")
        guess = int(input())
print("恭喜答對！")