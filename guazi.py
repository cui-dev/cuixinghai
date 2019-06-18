#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 20:27
# @Author  : cui
# @File    : guazi.py


import requests
from lxml import etree

hade = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Cookie':'f798aea0-a526-44de-ed84-dc8329988105; ganji_uuid=4256107207182718553276; lg=1; user_city_id=155; antipas=33j9965G288871U57111h1zTFkM8; clueSourceCode=%2A%2300; sessionid=51eee386-dc44-4cea-ff1c-a5397480c900; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22ca_i%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22f798aea0-a526-44de-ed84-dc8329988105%22%2C%22sessionid%22%3A%2251eee386-dc44-4cea-ff1c-a5397480c900%22%7D; preTime=%7B%22last%22%3A1558315344%2C%22this%22%3A1558153502%2C%22pre%22%3A1558153502%7D; cityDomain=zz; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A33756838548%7D'
        }
def get_url(url):
    req = requests.get(url, headers=hade)
    reqs = req.content.decode("utf-8")
    resp = etree.HTML(reqs)
    ul = resp.xpath('//ul[@class="carlist clearfix js-top"]')[0]
    lis = ul.xpath('./li')
    list1=[]
    for li in lis:
        datail_urls = li.xpath('./a/@href')
        datail_url = 'https://www.guazi.com' + datail_urls[0]
        list1.append(datail_url)
    return list1

def parse_dataila_url(url):
    resp=requests.get(url,headers=hade)
    resp_te=resp.content.decode("utf-8")
    html=etree.HTML(resp_te)
    title=html.xpath('//div[@class="product-textbox"]/h2/text()')[0]
    title1=title.replace(r'\r\n','').strip()   #去除空格跟换行  .strip去除首尾的空格
    infos={}  #空的字典,存放数据
    info=html.xpath('//div[@class="product-textbox"]/ul/li/span/text()')
    cardtime = info[0]  #上牌时间
    km=info[1]  #里程
    displacement = info[2]  #排量
    speedbox= info[3]   #变速箱
    infos['车型']=title1
    infos['上牌时间'] = cardtime
    infos['里程'] = km
    infos['排量'] = displacement
    infos['变速箱'] = speedbox
    return infos

def main():
    old_url = "https://www.guazi.com/ty/buy/o{}/"
    with open('guizi.csv', 'a', encoding='utf-8') as f:
        for i in range(0,51):
            url=old_url.format(i)
            list1=get_url(url)
            for data_url in list1:
                infos=parse_dataila_url(data_url)
                f.write('{},{},{},{},{}\n'.format(infos['车型'],infos['上牌时间'],infos['里程'], infos['排量'],infos['变速箱']))


if __name__ == '__main__':
    main()


