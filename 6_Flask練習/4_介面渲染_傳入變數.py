from flask import Flask, render_template

app = Flask(__name__) 

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

@app.route("/")
def index():
    user = User(username = "台灣", email = "xxx@taiwan.com")
    return render_template("index.html", user = user)

@app.route("/user/<user_id>")
def user_id(user_id):
    person = {
        "username" : "中華民國",
        "phone" : "%s" % user_id,
        "address" : "台灣省"
    }
    return render_template("user_id.html", person = person, user_id = user_id)
#                                       
if __name__ == "__main__":
    app.run(debug=True)