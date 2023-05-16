scores = [50, 50, 90, 88, 48]
friends = ["小黃", "小綠", "小白"] #有內容的list

mix = ["小黃", 22, True]
# 列表的用法為中括號[]，裡面可以有數字集合、字串集合、布林值集合或混和

print(mix[2])
# 印出mix列表中順序為2的值(True)。

print(50 in scores)
# scores列表中是否有50這個值(True)。

print(scores[-1])
# 印出scores列表中順序為-1的值(48)。

print(friends[::-1])
# 印出friends這個list中，倒過來

print(scores.index(48))
# 印出scores列表中48為第幾序位(4)。

print(scores[0:2])
# 印出scores列表中從第0位取到第2位(不包含第2位)(50,50)。

print(scores[1:4])
# 印出scores列表中從第1位取到第4位(不包含第4位)(50,90,88)。

print(scores[1:])
# 印出scores列表中從第1位取到列表結束(50,90,88,48)。

scores[0] = 30
print(scores)
# scores列表中從第0位等於30，
# 印出scores列表(30,50,90,88,48)。

print(len(scores))
# 印出scores列表中有幾個數值(5)。
