# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from methods.mysqldb import mysqldb
from handlers.base import BaseHandler
import time

class Findmycat(BaseHandler):
    def get(self, *args, **kwargs):
        iflogin = self.get_cookie('username')
        if iflogin:
            self.render('findmycat.html', title='', sql_review='1', pagination='', macros='')
        else:
            self.render('index.html')

    def post(self, *args, **kwargs):
        mycattableschema = self.get_argument('mycattableschema')
        mycattablename = self.get_argument('mycattablename')
        outinfo = ''
        if not (mycattableschema and mycattablename):
            self.write('请填写表名或选择相应数据库')
        else:
            for i in mycattablename.lower().split(','):
                # print(i)
                mycatgetsql = 'select table_name,table_schema,table_status from tab_schema where table_schema = \'{table_schema}\' and table_name = \'{table_name}\';'.format(
                    table_schema=mycattableschema.lower(), table_name=i)
                connet = mysqldb('130dev')
                # print(mycatgetsql)
                mycatinfo = connet.exsql(mycatgetsql)
                # print(mycatinfo)
                if not mycatinfo:
                    self.write('没有这个表！')
                else:
                    if mycatinfo[0]['table_status'] == 'global':
                        outinfo = outinfo + '全局表<br />' + '&#60;table name="{table_name}" dataNode="fas_dn$1-23" primaryKey="id" type="global" /&#62;<br />'.format(
                            table_name=mycatinfo[0]['table_name'])
                    elif mycatinfo[0]['table_status'] == 'sharding':
                        outinfo = outinfo + '分库表<br />' + '&#60;table name="{table_name}" dataNode="fas_dn$1-23" primaryKey="id" rule="sharding_by_organ_zone" /&#62;<br />'.format(
                            table_name=mycatinfo[0]['table_name'])
                    elif mycatinfo[0]['table_status'] == 'single':
                        outinfo = outinfo + '单表<br />' + '&#60;table name="{table_name}" dataNode="fas_dn1" primaryKey="id" /&#62;<br />'.format(
                            table_name=mycatinfo[0]['table_name'])
            self.write(outinfo)



# @Time    : 2018/4/26 14:32
# @Auth    : DAQIUYIN
# @File    : findmycat.py
# @SoftWare: PyCharm Community Edition