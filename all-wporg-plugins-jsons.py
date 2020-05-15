#!/usr/bin/python
# -*- coding: UTF-8 -*-

from urllib.request import urlretrieve
import os
import ssl

'''
all-wporg-plugins.py

本文件用于从 json.txt下载 json。

Author: _Wr_
AuthorURL: https://wrsblog.cn
'''
ssl._create_default_https_context = ssl._create_unverified_context

def download():    
    categories = ['json']
    for category in categories:
        # 新建存储json文件夹存储文件
        # 新建文件夹地址为./data/json
        os.makedirs('data/%s' % category, exist_ok=True)
        # 读取txt文件
        # txt文件地址为./json.txt
        with open('%s.txt' % category, 'r') as file:
            urls = file.readlines()
            # 计算URL地址条数
            n_urls = len(urls)
            # 遍历链接地址下载json
            for i, url in enumerate(urls):
                try:
                     # 请求下载json，并截取最后链接第一最后一节字段命名文件
                     urlretrieve(url.strip(), 'data/%s/%s' % (category, url.strip().split('/')[-1]))
                     print('%s %i/%i' % (category, i, n_urls))
                except:
                     print('%s %i/%i' % (category, i, n_urls), 'No Such File')

if __name__ == '__main__':
    download();
