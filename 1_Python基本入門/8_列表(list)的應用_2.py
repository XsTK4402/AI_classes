scores = [50, 50, 90, 88, 48]
friends = ["小黃", "小綠", "小白"]
mix = ["小黃", 22, True]

print(scores + friends)
# 印出scores列表加上friends列表
# (50, 50, 90, 88, 48, '小黃', '小綠', '小白')

scores.extend(friends)
# 將score列表延伸至friends列表
# (50, 50, 90, 88, 48, '小黃', '小綠', '小白')
print(scores)

scores.append(30)
# 將score列表延伸至friends列表的基礎下，加上30這個值
# (50, 50, 90, 88, 48, '小黃', '小綠', '小白',30)
print(scores)

scores.insert(7, 66)
# 將score列表延伸至friends列表加上30這個值的基礎下，將第七序位插入66這個值。
# (50, 50, 90, 88, 48, '小黃', '小綠', 66, '小白', 30)
print(scores)

scores.remove("小綠")
# 將score列表延伸至friends列表加上30這個值，
# 將第七序位插入66這個值的基礎下，移除"小綠這個值"。
# (50, 50, 90, 88, 48, '小黃', 66, '小白', 30)
print(scores)

scores.pop()
# 將列表最後一位移除
# (50, 50, 90, 88, 48, '小黃', 66, '小白')
print(scores)

scores = [50, 50, 90, 88, 48]
scores.sort()
# 將scores列表從小到大做排列(回傳None)
# (48, 50, 50, 88, 90)
print(scores)

print(sorted(scores))
# 將scores列表從小到大做排列(回傳整理過的scores)

scores.reverse()
# 將已經sort過的scores列表反轉
# (90, 88, 50, 50, 48)
print(scores)

print(scores.count(50))
# 將已經sort過的scores列表反轉後，計算裡面有幾個50。

scores.clear()
# 將列表清空
print(scores)
