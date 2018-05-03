# -*- coding: utf-8 -*-
import pymysql
#from confctr import dbtab
import configparser
import application
import os

class dbtab:
    def __init__(self,tabname):
        configfile = os.path.join(application.settings['static_path'], 'conf', 'mysqlconfig.txt')
        config = configparser.ConfigParser()
        config.read(configfile)
        self.host =config.get(tabname, 'host')
        self.port =config.get(tabname, 'port')
        self.user =config.get(tabname, 'user')
        self.password=config.get(tabname, 'password')
        self.db=config.get(tabname, 'db')
        self.charset = config.get(tabname,'charset')

class mysqlconnect:
    def __init__(self,host,port,user,password,db,charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.errmes=''
        self.execmes=''
        if charset :
            self.charset = charset
        else:
            self.charset = 'utf8'

    def exsql(self,tab_name,column=''):
        flag=99
        if not column:
            self.sql = "select table_name,column_name,column_type,COLUMN_COMMENT from information_schema.COLUMNS where TABLE_SCHEMA = '{tableschema}' and table_name = '{tablename}';".format(tableschema =self.db ,tablename=tab_name)
            flag=1
        else:
            column_name = column.lower().replace(',','\',\'').replace('，','\',\'')
            standcolname='\''+column_name+'\''
            self.sql = "select table_name,column_name,column_type,COLUMN_COMMENT from information_schema.COLUMNS where TABLE_SCHEMA = '{tableschema}' and table_name = '{tablename}' and column_name in( {columnname});".format(
                tableschema=self.db, tablename=tab_name,columnname = standcolname)
            flag=2

        connection =  pymysql.connect(host=self.host,
                                     user=self.user,
                                     password=self.password,
                                     db=self.db,
                                     charset=self.charset,
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                cursor.execute(self.sql)
                results =  cursor.fetchall()
                return results,flag

        except Exception as exceptmes:
            raise exceptmes
        finally:
            connection.close()





if __name__ == '__main__':
    def run_sql():
        dev = dbtab('221dev')
        mycon = mysqlconnect(host=dev.host, port=dev.port, user=dev.user, password=dev.password, db=dev.db,
                             charset=dev.charset)
        # mycon.exsql("insert into test_tb values ('1','kk');",1)
        a = mycon.exsql('test_tb','name')
        print(a)
    run_sql()



# @Time    : 2018/3/5 14:13
# @Auth    : DAQIUYIN
# @File    : connectmysql.py
# @SoftWare: PyCharm Community Edition