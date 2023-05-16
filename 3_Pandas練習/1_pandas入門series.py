import pandas as pd

# df = pd.read_excel("data/test.xlsx")
# # print(df)

pd.set_option('display.unicode.east_asian_width', True)

#series對象
index = ["郭元瑜","劉家齊","蔡至偉","林慧敏","許聖豪","潘彥伶","張建士"]
data = [72,88,63,72,92,81,78]
s = pd.Series(data = data, index = index)  
# print(s[1], type(s)) #從index找1個data
# print(s[[1,2]])  #從index找多個data
print(s["郭元瑜":"許聖豪"])  #從index找多個data，含頭不含尾，當index為字串時，含頭含尾

# 郭元瑜    72
# 劉家齊    88
# 蔡至偉    63
# 林慧敏    72
# 許聖豪    92

# print(s, type(s))
# print(s.index, type(s.index))
# print(list(s.index), type(list(s.index)))
# print(s.values, type(s.index))