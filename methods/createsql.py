# -*- coding: utf-8 -*-
import re

def createsql(columns):
    wholsql='/*createsql*/<br />create table {tablename} ( <br />'.format(tablename = columns[0]['table_name'])
    for evecolumn in columns:
        if evecolumn['column_type'][0:4] == 'char'or evecolumn['column_type'][0:7] == 'varchar':
            charlen=re.findall('\d',evecolumn['column_type'])
            numlen=''.join(charlen)
            columnssql=' '+evecolumn['column_name']+' varchar2('+numlen+' char),<br />'
            wholsql = wholsql+columnssql

        elif evecolumn['column_type'][0:6] == 'bigint' or evecolumn['column_type'][0:7] == 'decimal' or evecolumn['column_type'][0:5] == 'float' or evecolumn['column_type'][0:3] == 'int' or evecolumn['column_type'][0:8] == 'smallint' or evecolumn['column_type'][0:7] == 'tinyint':
            columnssql = ' ' + evecolumn['column_name'] + ' number,<br />'
            wholsql = wholsql + columnssql
        elif evecolumn['column_type'][0:4] == 'date' or evecolumn['column_type'][0:8] == 'datetime' or evecolumn['column_type'][0:4] == 'time' or evecolumn['column_type'][0:9] == 'timestamp' :
            columnssql = ' ' + evecolumn['column_name'] + ' date,<br />'
            wholsql = wholsql + columnssql
    wholsql=wholsql+'PRIMARY KEY (id) <br />);'
    return wholsql

def commentsql(columns):
    whocomsql = '/*commentsql*/<br />'
    for evecom in columns:
     if  evecom['COLUMN_COMMENT']:
      comsql = 'comment on column {table_name}.{column_name} is \'{comment}\';<br />'.format(table_name =evecom['table_name'],column_name=evecom['column_name'],comment=evecom['COLUMN_COMMENT'])
      whocomsql = whocomsql+comsql
    return whocomsql

def createcolumnsql(columns):
    wholsql='/*createcolumnsql*/<br />'
    for evecolumn in columns:
        wholsql = wholsql+'alter table {tablename} add '.format(tablename=columns[0]['table_name'])
        if evecolumn['column_type'][0:4] == 'char'or evecolumn['column_type'][0:7] == 'varchar':
            charlen=re.findall('\d',evecolumn['column_type'])
            numlen=''.join(charlen)
            columnssql=' '+evecolumn['column_name']+' varchar2('+numlen+' char);<br />'
            wholsql = wholsql+columnssql

        elif evecolumn['column_type'][0:6] == 'bigint' or evecolumn['column_type'][0:7] == 'decimal' or evecolumn['column_type'][0:5] == 'float' or evecolumn['column_type'][0:3] == 'int' or evecolumn['column_type'][0:8] == 'smallint':
            columnssql = ' ' + evecolumn['column_name'] + ' number;<br />'
            wholsql = wholsql + columnssql

        elif evecolumn['column_type'][0:4] == 'date' or evecolumn['column_type'][0:8] == 'datetime' or evecolumn['column_type'][0:4] == 'time' or evecolumn['column_type'][0:9] == 'timestamp' or evecolumn['column_type'][0:7] == 'tinyint':
            columnssql = ' ' + evecolumn['column_name'] + ' date;<br />'
            wholsql = wholsql + columnssql

    return wholsql

if __name__ == '__main__':
    k=[{'table_name': 'test_tb', 'column_name': 'id', 'column_type': 'date', 'COLUMN_COMMENT': ''}, {'table_name': 'test_tb', 'column_name': 'name', 'column_type': 'varchar(32)', 'COLUMN_COMMENT': ''}]
    a = createsql(k)
    b = commentsql(k)
    c = createcolumnsql(k)
    print(a)
    print(b)
    print(c)


# @Time    : 2018/3/5 14:25
# @Auth    : DAQIUYIN
# @File    : createsql.py
# @SoftWare: PyCharm Community Edition