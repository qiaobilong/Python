#!/user/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年11月1日
@author: Administrator
v1.0 Completed on 2018-11-2 12:43:11
    主要结构
v1.1 Completed on 2018-11-2 21:31:11
    加入请求伪装，用户指定文档存放路径
v1.2 Completed on 2018-11-3 22:43:39
    增加提取来源和分类的方法，并简化提取链接的写法，同时增加更多的人机交互
'''
 
import urllib.request
import pandas
from bs4 import BeautifulSoup


def get_soup(url):
    '''
    解析页面内容
    '''
    headers = {'User-Agent':'Chrome/67.0.3396.99',
               'Host':'db.ouryao.com'}
    request = urllib.request.Request(url = url,headers = headers)
    response = urllib.request.urlopen(request)
    html_sample = response.read().decode('utf-8')
    # 解析html文件，剖析器用html.parser
    soup = BeautifulSoup(html_sample, 'html.parser')
    return soup


def get_content(url, goodscontent):
    '''
    提取每位药的内容
    '''
    soup = get_soup(url)
    if soup.select('#content_text'):
        goodscontent.append(soup.select('#content_text')[0].text)
    else:
        goodscontent.append('空')
    

def get_table(url):
    '''
    获取表格前三列
    '''
    table = get_soup(url).select('.cms_list table tr td')
    for i in range(len(table)):
        if i % 5 == 0 and i <= len(table):
            goodsname.append(table[i].text)
        elif i % 5 == 1 and i <= len(table):
            goodssource.append(table[i].text)
        elif i % 5 == 2 and i <= len(table):
            goodsclass.append(table[i].text)


def get_a_link(url, pageurl, goodsname_url):
    '''
    获取药品名称链接，生成列表
    '''
    get_table(pageurl)
    content = get_soup(pageurl).select('.cms_list table tr td a')
    for i in range(len(content)):
        if i % 3 == 0 :
            goodsname_url.append(f"{url}{content[i]['href']}")
    return goodsname_url   


def get_all_link(url):
    '''
    提取每个页面的链接
    '''
    goodsname_url = []
    start = int(input('>>>请输入要提取的起始页：'))
    stop = int(input('>>>请输入要提取的终止页：')) + 1
    print('开始获取页面链接：')
    for i in range(start, stop):
        get_a_link(url, f'{url}index.php?k=&cid=0&cid2=0&page={i}', goodsname_url)
        if i + 1 == stop:
            print(f'完成第{i}页','---------已获取所有页面链接---------',sep = '\n')
        else:
            print(f'完成第{i}页')
    return goodsname_url


print('---------欢迎使用药典提取器---------')
print('此工具仅用于提取http://db.ouryao.com/yd2015/中的内容')
url = 'http://db.ouryao.com/yd2015/'
goodsname = []
goodssource = []
goodsclass = []
goodscontent = []

all_link = get_all_link(url)

for i in all_link:
    get_content(i, goodscontent)
    print(f'药典内容已获取：{all_link.index(i)+1}条')

yaodian_dict = {'goodsname':goodsname,
                'goodssource':goodssource,
                'goodsclass':goodsclass,
                'goodscontent':goodscontent}
  
df = pandas.DataFrame(yaodian_dict)
path = input('>>>请输入文件的存储路径，以“\”结束：')
df.to_excel(f'{path}药典2015版.xlsx', sheet_name='药典2015版', index_label='goodsid')
print(f"药典文件已生成完毕，请到'{path}'下查看")