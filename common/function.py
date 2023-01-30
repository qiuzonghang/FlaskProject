# -*- coding: utf-8 -*-
# @Time   : 2022/11/7 10:58
# @Author : qiuzonghang
# @File   : function.py


import pymssql
from conf.conf import Config


def process_params(param):
    print(param["username"])


cf = Config()


def connect_sql(sql):
    conn = pymssql.connect(cf.sql_server_host_dev, cf.sql_server_username_dev, cf.sql_server_password_dev, cf.sql_server_database_dev, charset='cp936')
    cur = conn.cursor()
    # sql = "select * from flask_db.user_info"
    print(sql)
    cur.execute(sql)
    # result = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    # return result


class ConnectSql:

    def __init__(self):
        self.conn = pymssql.connect(cf.sql_server_host_dev, cf.sql_server_username_dev, cf.sql_server_password_dev,
                               cf.sql_server_database_dev, charset='cp936')
        self.cur = self.conn.cursor()

    def select_sql(self, sql):
        print(sql)
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()
        except:
            return False
        # self.cur.execute(sql)
        # return self.cur.fetchall()

    def insert_sql(self, sql):
        try:
            self.cur.execute(sql)
            return True
        except pymssql._pymssql.OperationalError as e:
            return e

    def close_sql(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


# test = ConnectSql()
# print(test.select_sql("select * from flask_db.user_info where username = '4321' or phone = '4321'"))

