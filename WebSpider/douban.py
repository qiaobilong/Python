#!user/bin/evn python
# -*- coding: utf-8 -*-

"""豆瓣电影"""


__author__ = 'Zerone龍'
__version__ = 0.1


import time
import requests
from bs4 import BeautifulSoup


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
                yield{
                    'movie_name': movie_name,
                    'user_id': item.input['value'],
                    'username': item.find(class_='comment-info').a.text,
                    'create_time': item.find(class_='comment-time')['title'],
                    # 评分获取的时候经常会报错，暂时还不知道如何处理2019-1-18 22:29:52
                    'score': item.find(class_='comment-time').find_previous_sibling()['class'][0].replace('allstar', ''),
                    'is_useful': item.find(class_='votes').text,
                    'comment': item.find(class_='short').text
                }
    except requests.ConnectionError:
        return None


def main(movie, offset):
    url = f'https://movie.douban.com/subject/{movie}/comments?start={offset}&limit=20&sort=new_score&status=P'
    for item in get_data(url, offset):
        lst.append(item)


headers = {
    'User-Agent': 'Chrome/68.0.3440.106 Mobile Safari/537.36'
}
# 电影的唯一标识，可以通过浏览器查看url获取
movie_id = 26394152
movie_name = ''
start = 0
stop = 6
lst = []

if __name__ == '__main__':
    pages = [x * 20 for x in range(start, stop+1)]
    for i in pages:
        main(movie_id, i)
        time.sleep(0.3)
    for i in lst:
        print(i)
