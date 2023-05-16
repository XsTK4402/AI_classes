import pandas as pd
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

df = pd.read_excel("data/前瞻計畫「改善山區行動通訊品質計畫」之改善站點.xlsx", sheet_name = "109年", header = 84)
# pd.read(io, sheet_name, header)

print(df)

# io表示文件名或文件路徑
# sheet_name表示工作表，sheet_name = 0 為第一頁。
#                      sheet_name = "abc123" 為開啟名為abc123的dataframe。
#                      sheet_name = [0, 1, "abc123"] 讀取第一頁、第二頁、abc123。
#                      sheet_name = None 為讀取所有工作表。
# header為讀取列，全部讀取為header = None。
                   