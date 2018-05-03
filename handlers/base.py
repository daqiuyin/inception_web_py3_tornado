# -*- coding: utf-8 -*-
import tornado.web
import tornado.options

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
         return self.get_secure_cookie("username")

# @Time    : 2018/3/12 20:16
# @Auth    : DAQIUYIN
# @File    : base.py
# @SoftWare: PyCharm Community Edition