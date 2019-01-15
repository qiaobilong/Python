#!user/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
from urllib.parse import urlencode
from hashlib import md5


def get_page(offset):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
    }
    parameters = {
        'offset': offset,
        'format': 'json',
        'keyword': '汽车',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    # 构造完整url
    url = 'http://www.toutiao.com/search_content/?' + urlencode(parameters)
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for i in json.get('data'):
            if i.get('cell_type') is not None:
                continue
            title = i.get('title')
            images = i.get('image_list')
            for i in images:
                yield{
                    'image': 'https:' + i.get('url'),
                    'title': title
                }


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        # 获取图片
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    json = get_page(offset)
    for i in get_images(json):
        print(i)
        save_image(i)


GROUP_START = 0
GROUP_END = 1

if __name__ == '__main__':
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    for i in groups:
        main(i)
