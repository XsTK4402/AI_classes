C = float(input("輸入攝氏溫度："))

if C is not None:
    F = (9/5) * C + 32
    print("華氏溫度為：" + str(F))
else:
    print("無效的溫度")
