# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.options
import tornado.httpserver

from application import application

from tornado.options import define,options
define('port',default=8000,help='run on the given port',type = int)



def main():
    tornado.options.parse_command_line()
    # 增加日志
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print ("Development server is running at http://127.0.0.1:%s" % options.port)
    print ("Quit the server with Control-C")
    tornado.ioloop.IOLoop.instance().start()

    # http_server.bind(options.port)
    # http_server.start(num_processes=0)  # tornado将按照cpu核数来fork进程
    # tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()




# @Time    : 2018/3/10 14:42
# @Auth    : DAQIUYIN
# @File    : server.py.py
# @SoftWare: PyCharm Community Edition