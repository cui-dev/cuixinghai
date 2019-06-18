#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 10:20
# @Author  : cui
# @File    : tupian.py
import re
import requests

data={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
url="http://www.xiaohuar.com/2014.html"
# url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B5%CF%C0%F6%C8%C8%B0%CD&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
data_sess=requests.get(url,data).text
print(data_sess)
res=re.compile(r'src="(.+?.jpg)"')

reg=re.findall(res,data_sess)
for i in reg:
    if i.startswith('/d'):
        p = 'http://www.xiaohuar.com'+i
        b = requests.get(p)
        number=p[-8:]
        with open(r'D:\课文\%s' %number, 'bw') as f:
            f.write(b.content)
