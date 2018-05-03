# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from methods.mysqldb import mysqldb
from handlers.base import BaseHandler
from methods.addmycat import restmycat

class Setmycat(BaseHandler):
    def get(self, *args, **kwargs):
        iflogin = self.get_cookie('username')
        if iflogin:
            self.render('setmycat.html', title='', sql_review='1', pagination='', macros='')
        else:
            self.render('index.html')

    def post(self, *args, **kwargs):
        addmycattablename = self.get_argument('addmycattablename')
        addmycatschema = self.get_argument('addmycatschema')
        addmycattableschema = self.get_argument('addmycattableschema')
        outinfo = ''
        if  addmycattablename.strip() and addmycatschema.strip() and addmycattableschema.strip():
            for i in addmycattablename.lower().split(','):
                if not i:
                    self.write('请填写表名！')
                elif i.replace('_', '').isalpha():
                    try:
                        ifaddmycatgetsql = 'select table_name from tab_schema where  table_name = \'{table_name}\' and table_schema = \'{table_schema}\';'.format(
                            table_name=i.lower(), table_schema=addmycattableschema)
                        ifaddconnet = mysqldb('130dev')
                        ifaddinfor = ifaddconnet.exsql(ifaddmycatgetsql)
                    except Exception as erro:
                        self.write('表校验出现问题，检查130数据库')
                    if len(ifaddinfor) == 0:
                        try:
                            a = restmycat(addmycattableschema, i.lower(), addmycatschema)
                        except:
                            self.write('增加配置出现问题，检查对应系统的mycat服务器')
                        if a == 'OK':
                            try:
                                addmycatgetsql = 'insert into tab_schema(table_name,table_schema,table_status) values(\'{table_name}\',\'{table_schema}\',\'{table_status}\');'.format(
                                    table_name=i.lower(), table_schema=addmycattableschema, table_status=addmycatschema)
                                addconnet = mysqldb('130dev')
                                addconnet.exsql(addmycatgetsql)
                            except:
                                self.write('表回写出现问题，检查130数据库')
                            outinfo = outinfo + addmycattableschema.upper() + '的表 ' + i.upper() + ' mycat 配置添加完成！\n'
                    else:
                        self.write(i+' 表已经在mycat存在！\n')
                else:
                    self.write('输入错误！')
            self.write(outinfo)
        else:
            self.write('请将信息填写完整')


# @Time    : 2018/4/26 14:32
# @Auth    : DAQIUYIN
# @File    : setmycat.py
# @SoftWare: PyCharm Community Edition