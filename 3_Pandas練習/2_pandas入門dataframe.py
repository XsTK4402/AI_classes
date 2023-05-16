import pandas as pd

df = pd.read_excel("data/test.xlsx")
# print(df)

# dataframe對象，列表方式建立
# data = [["郭元瑜",72,88],["劉家齊",88,82],["蔡至偉",63,49]]
# columns = ["姓名","國文","英文"]

# df = pd.DataFrame(data = data, columns = columns)  
# print(df, type(df))

# dataframe對象，字典方式建立
data = {
    "姓名":["郭元瑜","劉家齊","蔡至偉"],
    "國文":[72,88,63],
    "英文":[88,82,49],
    "班級名稱" : "三年甲班" #若元素相同不需列表
}
#array必須要有相同的長度

#    姓名  國文  英文  班級名稱
# 0  郭元瑜  72  88  三年甲班
# 1  劉家齊  88  82  三年甲班
# 2  蔡至偉  63  49  三年甲班 

df = pd.DataFrame(data = data)  
print(df, type(df))
