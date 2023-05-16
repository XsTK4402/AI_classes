from flask import Flask, render_template

app = Flask(__name__) 

# 回傳值變為"render_template"html模板
@app.route("/")
def index():
    return render_template("index.html")

# 回傳值為不固定標籤
@app.route("/user/<user_id>")
def user_id(user_id):
    return render_template("user_id.html", user_id = user_id)
#                                        回傳一份"user_id"給html檔案
if __name__ == "__main__":
    app.run(debug=True)