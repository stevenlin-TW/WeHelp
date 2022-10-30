from crypt import methods
from pickle import TRUE
from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import session
import mysql.connector


config = {
    'user' : 'root',
    'password' : '12345678',
    'host' : 'localhost',
    'database' : 'website',
    'raise_on_warnings' : True
}

app = Flask(__name__, static_folder="static", static_url_path=None)

app.secret_key="1234"

@app.route("/")
def login_page():
    return render_template("main_page.html")

@app.route("/signup", methods=["POST"])
def SignUp():
    sign_name = request.form["name"]
    sign_username = request.form["username"]
    sign_password = request.form["password"]

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("SELECT `username` FROM `member` WHERE `username` = %s", (sign_username,))
    username = cursor.fetchall()
    # Check if the entered username has been exist
    if username != []:
        return redirect("/error?message=帳號已被註冊")
    else:
        cursor.execute("INSERT INTO `member`(`name`,`username`,`password`) VALUES (%s, %s, %s)", (sign_name, sign_username, sign_password))
        print(cursor.lastrowid)
        cnx.commit()
        cursor.close()
        cnx.close()
        return redirect("/")

@app.route("/signin", methods=["GET", "POST"])
def SignIn():
    if request.method == "GET":
        return redirect("/")
    else:
        account = request.form["username"]
        password = request.form["password"]
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute("SELECT `username`, `password` FROM `member` WHERE `username`=%s AND `password`=%s", (account, password))
        result = cursor.fetchall()
        if result != []:
            session["user_status"] = "已登入"
            session["username"] = account
            return redirect("/member")
        elif account == "" or password== "":
            return redirect(url_for("fail", message="請輸入帳號、密碼"))
        else:
            return redirect(url_for("fail", message="帳號、密碼輸入錯誤"))

@app.route("/member")
def success():
    status = session["user_status"]
    username = session["username"]
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    # Get the name of member
    cursor.execute("Select `name` FROM `member` WHERE `username` = %s", (username,))
    member_name = cursor.fetchall() 
    if status == "已登入":
        cursor.close()
        cnx.close()
        return render_template("success.html", name = member_name[0][0])
    else:
        cursor.close()
        cnx.close()
        return redirect("/")

@app.route("/error")
def fail():
    error_message = request.args.get("message")
    session["user_status"] = "未登入"
    return render_template("fail.html", message_text = error_message)

@app.route("/signout")
def SignOut():
    session["user_status"] = ""
    session["username"] = ""
    return redirect("/")

app.run(port=3000)
