import pymysql
import sys
import prettytable

host_data = "tcp://0.tcp.jp.ngrok.io"      #input("請輸入主機位置：")
user_data = "root"                         #input("請輸入資料庫帳號：")
passwd_data = input("請輸入資料庫密碼：")
port_data = "10896"                        #input("請輸入資料庫的Port：")
db_data = "homework2"                      #input("請輸入資料庫的名稱：")

link = pymysql.connect(
    host = host_data,
    user = user_data,
    passwd = passwd_data,
    db = db_data,
    charset = "utf8",
    port = int(port_data)
)

menu = (
    '(0) 離開程式\n'
    '(1) 顯示會員列表\n'
    '(2) 新增會員資料\n'
    '(3) 更新會員資料\n'
    '(4) 刪除會員資料'
)
print(menu)
user_choose = input("指令：")
cur = link.cursor()

while True:
# ---------------------------------------------------------------------------------------------------------------------
    if int(user_choose) == 0:
        link.close()
        sys.exit()
# ---------------------------------------------------------------------------------------------------------------------
    if int(user_choose) == 1:
        cur.execute("SELECT * FROM `member`")
        x = prettytable.PrettyTable()
        data = cur.fetchall()
        for d in data:
            x.field_names = ["編號", "姓名", "生日", "地址"]
            x.add_row(d)

        print(x)
        print(menu)
        user_choose = input("指令：")
# ---------------------------------------------------------------------------------------------------------------------
    if int(user_choose) == 2:

        data = {
            "a": input("請輸入會員姓名："),
            "b": input("請輸入會員生日："),
            "c": input("請輸入會員地址：")
        }

        cur.execute(
            "INSERT INTO `member`(`name`, `birthday`, `address`) VALUES (%(a)s, %(b)s, %(c)s)", data)
        link.commit()

        print(menu)
        user_choose = input("指令：")
# ---------------------------------------------------------------------------------------------------------------------
    if int(user_choose) == 3:

        cur.execute("SELECT * FROM `member`")
        x = prettytable.PrettyTable()
        data = cur.fetchall()
        for d in data:
            x.field_names = ["編號", "姓名", "生日", "地址"]
            x.add_row(d)

        print(x)
        id = int(input("請選擇你要修改的資料編號："))

        data = {
            "a": input("請輸入會員姓名："),
            "b": input("請輸入會員生日："),
            "c": input("請輸入會員地址："),
            "d": id
        }

        cur.execute(
            "UPDATE `member` SET `name`=%(a)s,`birthday`=%(b)s,`address`=%(c)s WHERE `id` = %(d)s", data)
        link.commit()

        print(menu)
        user_choose = input("指令：")
# ---------------------------------------------------------------------------------------------------------------------
    if int(user_choose) == 4:

        cur.execute("SELECT * FROM `member`")
        x = prettytable.PrettyTable()
        data = cur.fetchall()
        for d in data:
            x.field_names = ["編號", "姓名", "生日", "地址"]
            x.add_row(d)

        print(x)
        id = int(input("請選擇你要刪除的資料編號："))

        data = {"a": id}

        cur.execute("DELETE FROM `member` WHERE `id` = %(a)s", data)
        link.commit()

        print(menu)
        user_choose = input("指令：")
