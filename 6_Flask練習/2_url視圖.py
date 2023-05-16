from flask import Flask, request
app = Flask(__name__) 

# url: http[80]/https[443]://127.0.0.1/path
# url視圖 : path視圖

@app.route("/")
def index():
    return "到台灣啦"

# 定義多層視圖，未帶參數url
# http://127.0.0.1:5000/user
@app.route("/user")
def user():
    return "你好啊!"

# 將參數固定至url
# http://127.0.0.1:5000/user/1223
@app.route("/user/<int:userid>")
def user_detail(userid):
    return "你訪問的使用者編號為： %s" % userid

# 查詢參數傳遞至url
@app.route("/book/list")
def book_list():
    # arguments : 參數
    # request.args : 類字典類型
    # http://127.0.0.1:5000/book/list?page=5
    page = request.args.get("page", default = 1, type = int)
    return f"你獲取的是第{page}的列表"

if __name__ == "__main__":
    app.run(debug = True) 