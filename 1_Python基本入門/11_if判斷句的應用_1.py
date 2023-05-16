rainy = True
if rainy:
    print("我就開車去上班")
else:
    print("我就走路去上班")

# rainy為一布林值(True or False)
# 上句為如果rainy是true，就印"我就開車去上班"
# 上句為如果rainy是False，就印"我就走路去上班"

scores = 70
if scores == 100:
    # ==判別左右數值是否相等，若是為True，否則為False。
    # !=判別左右數值是否不等，若是為True，否則為False。
    print("我給你1000元")
elif scores >= 80:
    print("我給你800元")
elif scores >= 60:
    print("我給你500元")
elif scores < 60:
    print("你給我300元")
# 判別分數落點，進入相對應程式碼

scores = 100
rainy = True
if scores == 100 and rainy:
    print("我給你1000元")
# and 左右兩側要皆為true，才會被判斷為True，若有一邊為False則判斷為False。
else:
    print("你給我300元")

scores = 60
rainy = False
if scores == 100 or not (rainy):
    # 將rainy這個布林值改為否定
    print("我給你500元")
else:
    print("你給我300元")