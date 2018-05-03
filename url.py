# -*- coding: utf-8 -*-

"""
the url structure of website
"""

import sys     #utf-8，兼容汉字
from handlers.index import IndexHandler
from handlers.welcome import WelcomeHandle
from handlers.checksql import CheckHandler
from handlers.mysqltooracle import Mysqltooracle
from handlers.findmycat import Findmycat
from handlers.setmycat import Setmycat
url = [
    (r'/',IndexHandler),
    (r'/welcomehandle', WelcomeHandle),
    (r'/checksql',CheckHandler),
    (r'/mysqltooracle',Mysqltooracle),
    (r'/findmycat',Findmycat),
    (r'/setmycat',Setmycat)
]


# @Time    : 2018/3/10 14:42
# @Auth    : DAQIUYIN
# @File    : url.py.py
# @SoftWare: PyCharm Community Edition