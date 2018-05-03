# -*- coding: utf-8 -*-
import paramiko

def producecontent(gmsorfas,tablename,ttpye):
    global contents
    if gmsorfas=='retail_fas':
        if ttpye=='global':
            contents = r'        \<table name=\"{table_name}\" dataNode=\"fas_dn\$1-9\"  primaryKey=\"id\" type = \"global\"/\>'.format(table_name=tablename)
        elif ttpye=='single':
            contents = r'        \<table name=\"{table_name}\" dataNode=\"fas_dn1\"  primaryKey=\"id\" /\>'.format(table_name=tablename)
        elif ttpye=='partition':
            contents = r'        \<table name="{table_name}\" dataNode=\"fas_dn\$1-9\"  primaryKey=\"id\" rule=\"sharding_by_organ_zone\"/\>'.format(table_name=tablename)
    elif gmsorfas=='retail_gms':
        if ttpye=='global':
            contents = r'        \<table name=\"{table_name}\" dataNode=\"gms_dn\$1-6\"  primaryKey=\"id\" type = \"global\"/\>'.format(table_name=tablename)
        elif ttpye=='single':
            contents = r'        \<table name=\"{table_name}\" dataNode=\"gms_dn1\"  primaryKey=\"id\" /\>'.format(table_name=tablename)
        elif ttpye=='partition':
            contents = r'        \<table name="{table_name}\" dataNode=\"gms_dn\$1-6\"  primaryKey=\"id\" rule=\"sharding_by_organ_zone\"/\>'.format(table_name=tablename)
    return contents

def restmycat(gmsorfas,tablename,ttpye):
    if gmsorfas=='retail_fas':
        port = 22
        ip = '172.17.210.83'
        username = 'root'
        password = '172.17.210.83_Siji3&245)P1d'
        row_id = 5
    elif gmsorfas =='retail_gms':
        port = 22
        ip = '172.17.210.133'
        username = 'root'
        password = '172.17.210.133_Onx0i3&6)P7e'
        row_id = 5

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(ip, port, username, password)
    commends = "sed -i '{rowid}i\\".format(rowid=str(row_id)) + producecontent(gmsorfas,tablename,ttpye) + '\' /mycat/conf/schema.xml'
    # stdin, stdout, sterr = s.exec_command('cat -n /root/test/aaa/yinhang.sql|grep {table_name}'.format(table_name='yinhang'))
    try:
        stdin, stdout, sterr = s.exec_command(commends)
        err = sterr.read()
    except Exception as err:
        return err

    try:
        stdins, stdouts, sterrs = s.exec_command('/mycat/bin/mycat restart')
        errs = sterrs.read()
    except Exception as errs:
        return errs

    if not err and not errs:
        return 'OK'

    s.close()


# @Time    : 2018/4/11 16:41
# @Auth    : DAQIUYIN
# @File    : addmycat.py
# @SoftWare: PyCharm Community Edition