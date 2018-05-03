# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
from methods.mysqldb import mysqldb

class IndexHandler(BaseHandler):
     def get(self):
        self.render('index.html')

     def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')

        getinfsql = 'select user_name,password,infor from user_tab where user_name = \'{username}\''.format(
            username=username)
        connet = mysqldb('130dev')
        getinf = connet.exsql(getinfsql)
        if getinf:
            if getinf[0]['password'] == password:
                self.set_secure_cookie('username', getinf[0]['password'], expires_days=None)
                self.write('1')
            else:
                self.write('0')
        else:
            self.write('0')



# @Time    : 2018/4/28 13:41
# @Auth    : DAQIUYIN
# @File    : index.py
# @SoftWare: PyCharm Community Edition