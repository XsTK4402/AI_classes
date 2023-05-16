import pandas as pd


data = {
    "姓名": ["郭元瑜", "劉家齊", "蔡至偉"],
    "國文": [72, 88, 63],
    "英文": [88, 82, 49],
    "班級名稱": "三年甲班"  # 若元素相同不需列表
}

df = pd.DataFrame(data=data)

# print(df)
# print("查看所有元素的值：\n", df.values)        # 扣除index與columns
# print("查看所有元素的類型：\n", df.dtypes)      # 印出columns中元素類型(object, int64)
# print("查看所有行名、重命名行名：\n", df.index)  # 印出index值(RangeIndex(start=0, stop=3, step=1))
# print("查看所有列名、重命名列名：\n", df.columns)# 印出columns值(Index(['姓名', '國文', '英文', '班級名稱'], dtype='object'))
# print("行列數據轉換：\n", df.T)                 # 行列數據轉換
# print("前n條數據：\n", df.head(1))              # 查看前N條數據,默認5條
# print("後n條數據：\n", df.tail(1))              # 查看後N條數據,默認5條
# print("查看行數和列數shape：\n", df.shape)      # 查看行數和列數shape[0]]表示行,shape[1]表示列
# print("查看行數和列數shape：\n", df.info)       # 查看索引、數據類型和內存信息，跟print(df)功能相同



