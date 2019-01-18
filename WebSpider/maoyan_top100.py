#!user/bin/env python
#-*- coding: utf-8 -*-

'''maoyan TOP100'''

__author__ = 'Zerone龍'
__version__ = 2.0


import requests
import re
from bs4 import BeautifulSoup
#如何输出后期版本更新，现在还不会2018-12-8
import xlwt
import pandas


lst = []


def get_one_page(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)',
                   'Host':'maoyan.com'}
        res = requests.get(url = url, headers = headers)
        if res.status_code == 200:
            return res.text
        return None
    except Exception as e:
        print(e)
        
 
def parse_one_page(html):
    #解析每一页的内容
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)<.*?name"><a.*?>(.*?)</a>.*?'
                        +'star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>'
                        +'.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for i in items:
        #yield将返回一个可迭代的对象
        yield {'index' : i[0],
               'name' : i[1],
               'star' : i[2].strip()[3:],
               'releasetime' : i[3].strip()[5:],
               'score' : i[4] + i[5]}
        

            
def main(offset):
    url = f'http://maoyan.com/board/4?offset={offset}'
    html = get_one_page(url)
    for i in parse_one_page(html):
        lst.append(i)
    return lst
#         #index = [0]暂不理解，不加就报错
#         df = pandas.DataFrame(i, index = [0])
                

if __name__ == '__main__':
    for i in range(10):
        main(offset = i * 10)
    df = pandas.DataFrame(lst)
    df.to_excel('maoyan.xlsx', 'Top100')

