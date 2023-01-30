# -*- coding: utf-8 -*-
# @Time   : 2023/1/29 17:09
# @Author : qiuzonghang
# @File   : conf.py


import os
import sys

from configparser import ConfigParser


class Config:
    # titles:
    TITLE_SQL_SERVER_DEV = 'sql_server_dev'

    VALUE_HOST = "host"
    VALUE_USERNAME = 'username'
    VALUE_PASSWORD = 'password'
    VALUE_DATABASE = 'database'

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conf.ini')

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='utf-8')

        self.sql_server_host_dev = self.get_conf(Config.TITLE_SQL_SERVER_DEV, Config.VALUE_HOST)
        self.sql_server_database_dev = self.get_conf(Config.TITLE_SQL_SERVER_DEV, Config.VALUE_DATABASE)
        self.sql_server_username_dev = self.get_conf(Config.TITLE_SQL_SERVER_DEV, Config.VALUE_USERNAME)
        self.sql_server_password_dev = self.get_conf(Config.TITLE_SQL_SERVER_DEV, Config.VALUE_PASSWORD)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)