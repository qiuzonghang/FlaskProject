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
    # return "中国联通"
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
    if request.method == "GET":
        return render_template("login_input.html")
    else:
        return "登录成功！\n欢迎 %s" % request.form.get("username")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        print(request.form)
        return render_template("success_register.html")


@app.route('/report')
def report():
    return render_template("/html/index.html")


# @app.route('/do/login', methods=["GET"])
# def do_login():
#     print(request.args)
#     return "登录成功！"


if __name__ == '__main__':
    app.run()
