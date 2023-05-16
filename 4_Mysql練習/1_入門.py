import pymysql

link = pymysql.connect(
    host = "0.tcp.jp.ngrok.io", #雲端資料庫網址
    user = "root",  
    passwd = "",
    db = "2023-04-21", #連入的資料庫名稱
    charset = "utf8", #資料庫的編碼
    port = 10896
)

cur = link.cursor() #以上為連線指令，此行為對資料庫進行編輯指令

data = [                     ##INSERT資料1
    input("日期："),
    input("來源："),
    input("標題："),
    input("描述："),
    input("圖片："),
    input("網址：")
]

cur.execute("INSERT INTO `news`(`date`, `src`, `title`, `description`, `image`, `link`) VALUES (%s,%s,%s,%s,%s,%s)", data)

# data = {                      #INSERT資料2
#     "a" : input("日期："),
#     "b" : input("來源："),
#     "c" : input("標題："),
#     "d" : input("描述："),
#     "e" : input("圖片："),
#     "f" : input("網址：")
# }

# cur.execute("INSERT INTO `news`(`date`, `src`, `title`, `description`, `image`, `link`) VALUES (%(a)s,%(b)s,%(c)s,%(d)s,%(e)s,%(f)s)", data)

# data = {                       ##UPDATE資料
#     "a" : input("日期："),
#     "b" : input("來源："),
#     "c" : input("標題："),
#     "d" : input("描述："),
#     "e" : input("圖片："),
#     "f" : input("網址：")
# }

# cur.execute("UPDATE `news` SET `date`=%(a)s,`src`=%(b)s,`title`=%(c)s,`description`=%(d)s,`image`=%(e)s,`link`=%(f)s WHERE `id` = 5", data)

# cur.execute("SELECT * FROM `news`") #擷取資料
# print("資料數：", cur.rowcount)
# d = cur.fetchone()
# print(d[0:4])
# d = cur.fetchone()
# print(d[0:4])

# data = cur.fetchall()
# for d in data:
#     print(d[0], d[3], d[1])

print("剛剛新增的那筆資料為：",cur.lastrowid)


link.close()