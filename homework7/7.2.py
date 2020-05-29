#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 给定100个企业网站首页链接地址（用1中给出的URL地址）；
# 请爬取每个页面上，企业介绍的链接地址；
#     说明，满足企业介绍网址的条件是，
#     标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
#     提示：要用到requests库，BeautifulSoup库

import requests
import re
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get(url):
    try:
        bup = requests.get(url)
        bup.encoding = bup.apparent_encoding
    except HTTPError:
        print('网页错误')
    except requests.exceptions.ConnectionError:   #Requests请求时有时会请求不到页面，或是请求到空白的页面，超时要重试几次，使用try…except语句
        pass
    else:
        bs = BeautifulSoup(bup.text, 'html.parser') #指定Beautiful的解析器为html.parser
        tt = bs.find_all("a")
        for t in tt:
            ht = t.get('href')
            if ht and 'html' in ht:
                try:
                    bup1 = requests.get('http://www.chrtc.cn')
                    bup1.encoding = bup1.apparent_encoding
                except HTTPError:
                    print('网页错误')
                except requests.exceptions.ConnectionError:
                    pass
                else:
                    bs1 = BeautifulSoup(bup1.text, 'html.parser')
                    label = bs1.findAll("a",text=re.compile(r"企业[介绍,历史,概况,发展]|关于[我们]|发展[历史]"),limit=1)
                    if label:
                        if 'http' not in ht:
                            print(url + ht)
                        else:
                            print(ht)
                    break


with open('totalurl.txt', 'r') as f:
    n = 1
    while n < 100:
        line = f.readline()
        while line:
            line = line.strip()
            get(line)
            line = f.readline()
            n += 1

