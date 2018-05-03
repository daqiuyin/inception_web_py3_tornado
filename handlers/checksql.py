# -*- coding: utf-8 -*-


from handlers.base import BaseHandler
import pymysql

class CheckHandler(BaseHandler):
     def get(self):
         iflogin = self.get_cookie('username')
         if iflogin:
             self.render('checksql.html', title='', sql_review='1', pagination='', macros='')
         else:
             self.render('index.html')

     def post(self, *args, **kwargs):
         out = ''
         checkcontent = self.get_argument('checkcontent')
         sql1 = '/*--user=mycat;--password=mycat@123;--host=172.17.210.39;--execute=1;--port=3306;*/\
                     inception_magic_start;\
                     use retail_fas_db1;'
         sql2 = 'inception_magic_commit;'
         sql = sql1 + checkcontent + sql2
         try:
             conn = pymysql.connect(host='172.17.209.221', user='yinghua', passwd='123456', port=6669, use_unicode=True,
                                    charset="utf8")
             with conn.cursor() as cur:
                 ret = cur.execute(sql)
                 result = cur.fetchall()
                 for i in range(1, len(result)):
                       print(out)
                       out=out+result[i][4].replace('.','<br />')+'<br />'
                 self.write(out)
             conn.close()
         except Exception as e:
             self.write("Mysql Error %d: %s" % (e.args[0], e.args[1]))



# @Time    : 2018/4/26 15:03
# @Auth    : DAQIUYIN
# @File    : checksql.py
# @SoftWare: PyCharm Community Edition