from pickle import FALSE
from flask import Flask, url_for, jsonify
from flask import render_template
from flask import request
from flask import redirect
from flask import session
import mysql.connector
import json

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
    session["user_status"] = "未登入"
    user_status = session["user_status"]
    print(user_status)
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
        return redirect(url_for("fail", message="帳號已被註冊"))
    elif sign_name=="" or sign_username=="" or sign_password=="":
        return redirect(url_for("fail", message="請輸入完整資訊"))
    else:
        cursor.execute("INSERT INTO `member`(`name`,`username`,`password`) VALUES (%s, %s, %s)", (sign_name, sign_username, sign_password))
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
        cursor.execute("SELECT `id`,`username`, `password` FROM `member` WHERE `username`=%s AND `password`=%s", (account, password))
        result = cursor.fetchall()
        if result != []:
            session["user_status"] = "已登入"
            session["username"] = account
            session["id"] = result[0][0]
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
    # Get the name of member
    cursor = cnx.cursor()
    cursor.execute("Select `name` FROM `member` WHERE `username` = %s", (username,))
    member_name = cursor.fetchall() 

    # Get message content
    cursor2 = cnx.cursor()
    cursor2.execute("SELECT `member`.`name`,`message`.`content` FROM `member` INNER JOIN `message` ON `member`.`id`=`message`.`member_id`")
    message_content = cursor2.fetchall()

    if status == "已登入":
        cursor.close()
        cnx.close()
        return render_template("success.html", name = member_name[0][0], comment = message_content)
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
    session.clear()
    #session["user_status"] == "未登入"
    return redirect("/")

@app.route("/message", methods=["POST"])
def Comment():
    message = request.form["message"]
    member_id = session["id"]
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO `message`(`member_id`,`content`) VALUES (%s,%s)", (member_id,message))
    cnx.commit()
    cursor.close()
    cnx.close()
    return redirect("/member")


@app.route("/api/member", methods=["GET", "PATCH"])
def MemberData():
    user_status = session["user_status"]
    username = session["username"]
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    if request.method == "GET":
        search_username = request.args.get("username")
        print(user_status)
        cursor.execute("SELECT `id`, `name`, `username` FROM `member` WHERE `username` = %s", (search_username,))
        result = cursor.fetchall()
        if result != [] and user_status == "已登入":
            return_value = {
                            "data": {
                                    "id" : result[0][0], 
                                    "name" : result[0][1],
                                    "username" : result[0][2]
                            }
            }
        else:
            return_value = {
                            "data": None
            }
        cursor.close()
        cnx.close()
        print(return_value)
        return json.dumps(return_value, ensure_ascii=False).encode("utf-8")
    elif request.method == "PATCH":
        new_name = request.get_json()
        if user_status == "已登入":
            cursor.execute("UPDATE `member` SET `name`=%s WHERE `username`=%s", (new_name["name"],username))
            cnx.commit()
            print(new_name["name"])
            return_value = { "ok" : True }
        else:
            return_value = { "error" : True}
        cursor.close()
        cnx.close()
        return json.dumps(return_value, ensure_ascii=False).encode("utf-8")


app.run(port=3000)
