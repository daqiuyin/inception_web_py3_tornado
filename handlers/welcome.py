# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from methods.mysqldb import mysqldb
from handlers.base import BaseHandler
import time


class WelcomeHandle(BaseHandler):

     def get(self):
        iflogin=self.get_cookie('username')
        if  iflogin:
            self.render('welcome.html',title='',sql_review='1',pagination='',macros='')
        else:
            self.render('index.html')

     # def post(self):
     #    username = self.get_argument('username')
     #    password = self.get_argument('password')
     #
     #    getinfsql = 'select user_name,password,infor from user_tab where user_name = \'{username}\''.format(username = username)
     #    connet=mysqldb('130dev')
     #    getinf =connet.exsql(getinfsql)
     #    if getinf:
     #        if getinf[0]['password'] == password:
     #            self.set_secure_cookie('username',getinf[0]['password'], expires_days=None)
     #            self.write('1')
     #        else:
     #            self.write('0')
     #    else:
     #        self.write('0')


# @Time    : 2018/3/10 15:39
# @Auth    : DAQIUYIN
# @File    : welcome.py.py
# @SoftWare: PyCharm Community Edition