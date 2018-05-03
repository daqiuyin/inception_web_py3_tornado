# -*- coding: utf-8 -*-

from url import url
import tornado.web
import os

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__),'templates'),
    static_path = os.path.join(os.path.dirname(__file__),'statics'),
    cookie_secret = "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    login_url='/',
    debug='True'
)

application = tornado.web.Application(
    handlers=url,
    **settings
)

# @Time    : 2018/3/10 14:41
# @Auth    : DAQIUYIN
# @File    : application.py.py
# @SoftWare: PyCharm Community Edition