import pandas as pd

# pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

data = {
    "姓名": ["郭元瑜", "劉家齊", "蔡至偉", "林慧敏", "許聖豪", "潘彥伶", "張建士"],
    "國文": [72, 88, 63, 72 ,92, 81, 78],
    "英文": [88, 82, 49, 64, 79, 72, 77],
    "數學": [88, 77, 55, 82, 93, 62, 51],
    "理化": [84, 80, 68, 74, 89, 70, 72]
}

df = pd.DataFrame(data=data)

print(df.describe())

