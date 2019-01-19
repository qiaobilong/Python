#!user/bin/evn python
# -*- coding: utf-8 -*-

"""豆瓣电影"""

__author__ = 'Zerone龍'
__version__ = 1.0


import requests
import json
from bs4 import BeautifulSoup


def get_score(attrs):
    """处理未评星的评论数据"""
    if 'class' in attrs.keys():
        return attrs['class'][0].replace('allstar', '')
    else:
        return '0'


def get_data(url, offset):
    response = requests.get(url=url, headers=headers)
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # 获取评论第一页的标题作为电影名
            if offset == 0:
                global movie_name
                movie_name = soup.h1.text.replace(' 短评', '')

            # 获取每条评论数据
            for item in soup.select('.comment-item'):
                # 对generator（生成器）还不是很理解，用yield应该是不用再将数据写入列表了
                yield {
                    'movie_name': movie_name,
                    'user_id': item.input['value'],
                    'username': item.find(class_='comment-info').a.text,
                    'create_time': item.find(class_='comment-time')['title'],
                    'score': get_score(item.find(class_='comment-time').find_previous_sibling().attrs),
                    'is_useful': item.find(class_='votes').text,
                    'comment': item.find(class_='short').text
                }
    except requests.ConnectionError:
        return None


def main(movie, offset):
    url = f'https://movie.douban.com/subject/{movie}/comments?start={offset}&limit=20&sort=new_score&status=P'
    for item in get_data(url, offset):
        with open('douban.json', 'a', encoding='utf-8') as file:
            file.write(json.dumps(item, ensure_ascii=False))


headers = {
    'User-Agent': 'Chrome/68.0.3440.106 Mobile Safari/537.36'
}
# 电影的唯一标识，可以通过浏览器查看url获取
movie_id = 26394152
# 电影名
movie_name = ''
# 开始抓取的页码，0为第一页
start = 0
# 抓取的截止页码
stop = 2500

if __name__ == '__main__':
    pages = [x * 20 for x in range(start, stop + 1)]
    for i in pages:
        main(movie_id, i)
