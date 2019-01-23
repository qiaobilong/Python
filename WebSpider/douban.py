#!user/bin/evn python
# -*- coding: utf-8 -*-

"""豆瓣电影"""

__author__ = 'Zerone龍'
__version__ = 4.0

import requests
import json
import random
import time
import urllib3
from bs4 import BeautifulSoup


def get_score(attrs):
    """处理未评星的评论数据"""
    if attrs is not None:
        if 'class' in attrs.keys():
            return attrs['class'][0].replace('allstar', '')
        else:
            return '0'
    else:
        return None


def get_response(url):
    time.sleep(random.randint(0, 20) / 10)
    header = headers[random.randint(0, 2)]
    # 不加这句会报错
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.get(url=url, headers=header, proxies=proxies, verify=False)
    return response


def is_none(var1, var2, parameter='func'):
    # 处理抓取空值问题，比较死板
    if var1 is not None:
        if parameter == 'func':
            if var2 == 'a':
                return var1.a
            elif var2 == 'text':
                return var1.text
            elif var2 == 'find_previous_sibling().attrs':
                return var1.find_previous_sibling().attrs
        elif parameter == 'attr':
            return var1[var2]
    else:
        return None


def get_data(url, movie_name):
    """获取一页评论数据"""
    response = get_response(url)
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # 获取每条评论数据
            for item in soup.select('.comment-item'):
                # 对generator（生成器）还不是很理解，用yield应该是不用再将数据写入列表了
                yield {
                    'movie_name': movie_name,
                    'user_id': is_none(item.input, 'value', 'attr'),
                    'username': is_none(is_none(item.find(class_='comment-info'), 'a'), 'text'),
                    'create_time': is_none(item.find(class_='comment-time'), 'title', 'attr'),
                    'score': get_score(is_none(item.find(class_='comment-time'), 'find_previous_sibling().attrs')),
                    'is_useful': is_none(item.find(class_='votes'), 'text'),
                    'comment': is_none(item.find(class_='short'), 'text')
                }
    except requests.ConnectionError:
        return None


def get_movie(start, stop):
    """获取电影名和ID"""
    for i in range(start, stop):
        url = f'https://movie.douban.com/subject/{i}/comments?start=0&limit=20&sort=new_score&status=P'
        res = get_response(url)
        try:
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                yield {
                    'movie_id': i,
                    'movie_name': soup.h1.text.replace(' 短评', '')
                }
        except requests.ConnectionError:
            return None


def main(movie_id, movie_name, pages):
    for i in pages:
        # 看过
        url = f'https://movie.douban.com/subject/{movie_id}/comments?start={i}&limit=20&sort=new_score&status=P'
        # 想看
        # url = f'https://movie.douban.com/subject/{movie_id}/comments?start={i}&limit=20&sort=new_score&status=F'
        data = get_data(url, movie_name)
        for j in data:
            with open('douban.json', 'a', encoding='utf-8') as file:
                # ensure_ascii参数为False时，以中文的形式记录
                file.write(json.dumps(j, ensure_ascii=False))


if __name__ == '__main__':
    headers = [{'User-Agent': 'Chrome/68.0.3440.106'},
               {'User-Agent': 'Safari/537.36'},
               {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}]
    proxies = {
        'http': 'http://218.85.22.156:9999'
    }
    begin = 26394100
    end = 26394100
    pages = [x * 20 for x in range(0, 50)]
    for i in get_movie(begin, end + 1):
        main(i['movie_id'], i['movie_name'], pages)
