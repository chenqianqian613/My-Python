#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#
#参考文档：https://blog.csdn.net/weixin_43687366/article/details/88877996
# 爬取这个网址上https://www.programcreek.com/python/，
# 搜索request的范例代码；保存到txt文件中（只保留文字）；
#     文本文件类似（注意是类似的效果，不是说一定要做的一模一样）的效果如下：
from bs4 import BeautifulSoup
import requests

url = 'https://www.programcreek.com/python/index/221/requests'
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                     AppleWebKit/537.36 (KHTML, like Gecko) \
                     Chrome/78.0.3904.108 Safari/537.36'}
hmtl = requests.get(url,headers=head).content.decode('utf-8')

soup = BeautifulSoup(hmtl,'html.parser')
ls = soup.find(id='api-list').find_all('a')
list = []
for i in ls:
	list.append(i.attrs['href'])
for k in list:
    d1 = {}
    exe = requests.get(k, headers=head).content.decode('utf-8')
    bs = BeautifulSoup(exe, 'html.parser')
    d1['example'] = bs.find(id='main').h1.text
    l1 = []
    for i in bs.find_all('pre', class_='prettyprint'):
        l1.append(i.text)
    d1['ans'] = l1

    with open('requestexe.txt','a+',encoding='utf-8') as f:
        f.write(d1['example']+'\n')
        for i in d1['ans']:
            f.write("--------------------------------------------")
            f.write('\n')
            f.write(i+'\n')
            f.write("--------------------------------------------")
            f.write('\n')
