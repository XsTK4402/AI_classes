age = int(input("輸入你的年紀："))
money = int(input("輸入你的資產："))

if age >= 18:
    print("歡迎光臨!")
elif age < 18 and money > 10000:
    print("歡迎光臨!")
else:
    print("謝謝惠顧。")
