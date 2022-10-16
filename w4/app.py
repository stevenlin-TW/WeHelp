from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import session

app = Flask(__name__, static_folder="static", static_url_path=None)

app.secret_key="1234"

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/signin", methods=["GET", "POST"])
def SignIn():
    if request.method == "GET":
        return redirect("/")
    else:
        account = request.form["account"]
        password = request.form["password"]
        if account=="test" and password=="test":
            session["user_status"] = "已登入"
            flash("Login Success!")
            return redirect("/member")
        elif account == "" or password=="":
            return redirect("/error?message=請輸入帳號、密碼")
        else:
            return redirect("/error?message=帳號、密碼輸入錯誤")

@app.route("/member")
def success():
    status = session["user_status"]
    if status == "已登入":
        return render_template("success.html")
    else:
        return redirect("/")
@app.route("/error")
def fail():
    error_message = request.args.get("message", "請輸入帳號、密碼")
    session["user_status"] = "未登入"
    return render_template("fail.html", message_text = error_message)

@app.route("/signout")
def SignOut():
    session["user_status"] = "未登入"
    return redirect("/")

@app.route("/square/<num>")
def square(num):
    num = int(num)
    sqr = num**2
    return render_template("square.html", result = sqr)

app.run(port=3000)
