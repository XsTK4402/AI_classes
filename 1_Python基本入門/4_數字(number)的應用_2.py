from math import *
import math
number = -8
print(str(number))
# str的用法為將 數值 轉變為 字串。

print("會印出數字"+str(number))
# 印出"會印出數字" 加上 被轉變為字串的number(8)

print(abs(number))
# abs的用法為數字運算中的取絕對值

number1 = "22"
print(int(number1))
# int的用法為將字串轉換為整數數字(小數點會出現錯誤)。

number2 = "22.5"
print(float(number2))
# float的用法為將字串轉換為小數點數字。

print(pow(2, 5))
# pow的用法為數字運算中次方的運算，前者為基數，後者為幾次方

print(max(1, 22, abs(-100), 54, 66))
# max的用法為在一串數字中找最大值

print(min(1, 22, abs(-100), 54, 66))
# min的用法為在一串數字中找最小值

print(round(6/10))
# round的用法為數字運算中五捨六入。

# 會導入整個 math 模組，需要在使用模組內函數時加上前綴 "math."
# 容易造成命名空間污染

print(floor(29/10))
# python中原先無floor無條件退位的用法，須從模組中引入。

print(ceil(21/10))
# python中原先無ceil無條件進位的用法，須從模組中引入。

print(sqrt(10000))
print(100**0.5)
# python中原先無sqrt開根號的用法，須從模組中引入。
