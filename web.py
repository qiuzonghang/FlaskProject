# -*- coding: utf-8 -*-
# @Time   : 2022/11/1 10:04
# @Author : qiuzonghang
# @File   : web.py

from flask import Flask, render_template, request
from common import function as func

app = Flask(__name__)


# 创建网址/show/info和方法index的对应关系，访问/show/info执行index方法
@app.route("/index")
def index():
    # 读取文件内容并返回,默认取templates目录找
    return render_template('index.html')


@app.route("/get/news")
def news():
    return "跳转成功"


@app.route("/goods/list")
def get_goods_list():
    return render_template("goods_list.html")


@app.route('/user/list')
def user_list():
    return render_template("user_list.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    sql = func.ConnectSql()
    if request.method == "GET":
        return render_template("login_input.html")
    else:
        login_info = request.form
        select_message = sql.select_sql("select * from flask_db.user_info where username = '%s' or phone = '%s'" % (login_info.get('username'), login_info.get('phone')))
        sql.close_sql()
        if select_message is not False:
            if len(select_message) == 1:
                if select_message[0][2] == login_info.get("pw"):
                    return "登录成功！\n欢迎 %s！" % login_info.get("username")
                else:
                    return render_template("login_no.html")
            elif len(select_message) != 1:
                return "检测到多个账号，请重新注册。"
            else:
                return render_template("login_no.html")
        else:
            return "登录失败，未知错误。"


@app.route('/register', methods=["GET", "POST"])
def register():
    sql = func.ConnectSql()
    if request.method == "GET":
        return render_template("register.html")
    else:
        register_info = request.form
        select_repeat = sql.select_sql("select * from flask_db.user_info where username = '%s' or phone = '%s'" % (register_info.get('username'), register_info.get('phone')))
        if select_repeat is not False:
            if len(select_repeat) == 0:
                insert_message = sql.insert_sql("INSERT INTO flask_db.user_info (id, username, password, gender, hobby, city, sign, creation_time, phone) VALUES ((select count(id) from flask_db.user_info) + 1, '%s', '%s', '%s', '%s', '%s','%s', getdate(), '%s')" % (str(register_info.get('username')), str(register_info.get('pw')), str(register_info.get('gender')), str(register_info.get('hobby')), str(register_info.get('city')), str(register_info.get('sign')), str(register_info.get('phone'))))
                sql.close_sql()
                if insert_message is True:
                    return render_template("success_register.html")
                else:
                    return "注册失败：%s" % insert_message
            else:
                return render_template("register_repeat.html")
        else:
            return "注册失败，未知错误。"


@app.route('/report')
def report():
    return render_template("/html/index.html")


# @app.route('/do/login', methods=["GET"])
# def do_login():
#     print(request.args)
#     return "登录成功！"


if __name__ == '__main__':
    app.run()
