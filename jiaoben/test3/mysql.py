#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pymysql
#链接数据库
def link():
    coon=pymysql.connect("cuishao","root2","123456","agileone")
    return coon

#查找
def seek (sql):
    coon = link()
    cur=coon.cursor()
    cur.execute(sql)
    dates=cur.fetchall()
    coon.commit()
    coon.close()
    return dates

#增删改
def alter(sql):
    coon=link()
    cur = coon.cursor()
    cur.execute(sql)
    coon.commit()
    coon.close()