# 字典(dictionay)中有很多鍵(key)與值(value)
dic = {
    "蘋果": "apple",
    "書本": "book",
    "貓": "cat",
    "狗": "dog",
}
#   { key  : value }
print(dic.keys())
print(dic.values())


print(dic["書本"])
# 印出""書本"的值
print(dic.get("蘋果"))
# 得到dic中""蘋果"的值

dic["大象"] = "elephants"
dic["大象"] = "elephant"
# 在字典中新增、修改一個值
print(dic)

del dic["大象"]
print(dic)


a = {"1": "apple", "2": "banana"}
b = {"3": "cat", "4": "dog"}

c = {
    **a,
    **b,
}

print(c)

