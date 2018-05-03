# -*- coding: utf-8 -*-

import pymysql
import configparser
import application
import os



class mysqldb:
    def __init__(self,tabname):

        configfile = os.path.join(application.settings['static_path'], 'conf/mysqlconfig.txt')
        config = configparser.ConfigParser()
        config.read(configfile)
        self.host = config.get(tabname, 'host')
        self.port = config.get(tabname, 'port')
        self.user = config.get(tabname, 'user')
        self.password = config.get(tabname, 'password')
        self.db = config.get(tabname, 'db')
        self.charset = config.get(tabname, 'charset')

    def exsql(self,sqltext):
        connection = pymysql.connect( host = self.host,
                                      port = int(self.port),
                                      user = self.user,
                                      password= self.password,
                                      db= self.db,
                                      charset = self.charset,
                                      cursorclass = pymysql.cursors.DictCursor)

        try:
         with connection.cursor() as cursor:
            cursor.execute(sqltext)
            results = cursor.fetchall()
            return results

        finally:
         connection.commit()
         connection.close()

if __name__ == '__main__':
    # getinfsql = 'select infor from user_tab where user_name =\'{username}\';'.format(username=username)
    getinfsql = 'insert into tab_schema(table_name,table_schema,table_status) values(\'{table_name}\',\'retail_fas\',\'{table_status}\');'.format(table_name = 'yinhangtest'.lower(),table_status = 'global')
    connet = mysqldb('130dev')
    usernames = connet.exsql(getinfsql)
    print(usernames)

# @Time    : 2018/3/10 15:57
# @Auth    : DAQIUYIN
# @File    : mysqldb.py
# @SoftWare: PyCharm Community Edition