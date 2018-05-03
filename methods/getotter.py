# -*- coding: utf-8 -*-
from methods.mysqldb import mysqldb

def getotter(sour_schema,sour_table,tag_schema,tag_table):
    if not sour_table:
        sqltext = 'select source_name,source_schema,target_name,target_schema from table_otter where source_name = \'{}\' and source_schema = \'\''



# @Time    : 2018/3/15 17:38
# @Auth    : DAQIUYIN
# @File    : getotter.py
# @SoftWare: PyCharm Community Edition