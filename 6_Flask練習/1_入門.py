from flask import Flask

# 建立application物件
# __name__代表當前"1_入門.py"整個模組
app = Flask(__name__) 


# 建立網站首頁回復方式
# "/"為根目錄
@app.route("/")
def index():
    return "Hello 台灣啦"

# 1. debug模式
# app.run(debug = True)，檢測到內文變更即更動網頁

# 2. 修改host模式
# app.run(host = '0.0.0.0')
# 修改IP位置讓其他電腦能夠連接(cmd > ipconfig)
# 預設0.0.0.0 即為當前IP位置

# 3. 修改port號碼
# app.run(port = 8373)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 8000) #執行伺服器