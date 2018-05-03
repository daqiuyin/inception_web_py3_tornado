# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
from methods.connectmysql import mysqlconnect,dbtab
from methods.createsql import createsql,commentsql,createcolumnsql

class Mysqltooracle(BaseHandler):
    def get(self):
        iflogin = self.get_cookie('username')
        if iflogin:
            self.render('mysql_to_oracle.html', title='', sql_review='1', pagination='', macros='')
        else:
            self.render('index.html')

    def post(self):
        database = self.get_argument('database')
        tablename = self.get_argument('tablename')
        columnname = self.get_argument('columnname')
        if not (tablename and database) :
            self.write('请选择数据库或填写表名！')
            self.finish()
        else:
            dev = dbtab(database)
            mycon = mysqlconnect(host=dev.host, port=dev.port, user=dev.user, password=dev.password, db=dev.db,
                                 charset=dev.charset)
            tables = tablename.lower()
            tablist = tables.split(',')
            sqltext=''
            for m in tablist:
                i =  mycon.exsql(m, columnname)
                if i[1] == 1:
                    try:
                        b = createsql(i[0])
                        c = commentsql(i[0])
                        sqltext = sqltext + b + c
                    except:
                        sqltext = '请输入正确表名！'
                else:
                    try:
                        b = createcolumnsql(i[0])
                        c = commentsql(i[0])
                        sqltext = sqltext + b + c
                    except:
                        sqltext = '请输入正确表名！'
            self.write(sqltext)

# @Time    : 2018/4/26 11:05
# @Auth    : DAQIUYIN
# @File    : mysqltooracle.py
# @SoftWare: PyCharm Community Edition