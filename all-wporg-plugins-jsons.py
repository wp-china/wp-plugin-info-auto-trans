#!/usr/bin/python
# -*- coding: UTF-8 -*-
from urllib.request import urlretrieve
import os
# 解决，导入ssl模块，再加一行代码
import ssl

'''
all-wporg-plugins.py

本文件用于从 all_plugins_urls.txt下载json。

Author: _Wr_
AuthorURL: https://wrsblog.cn
'''
ssl._create_default_https_context = ssl._create_unverified_context

'''
通过txt网址文件，现在图片到本地
'''
def download():    
    categories = ['json']
    for category in categories:
        # 新建存储hello文件夹存储图片
        # 新建文件夹地址为./data/hello
        os.makedirs('data/%s' % category, exist_ok=True)
        # 读取txt文件
        # txt文件地址为./hello.txt
        with open('%s.txt' % category, 'r') as file:
            urls = file.readlines()
            # 计算URL地址条数
            n_urls = len(urls)
            # 遍历链接地址下载图片
            for i, url in enumerate(urls):
                try:
                     # 请求下载图片，并截取最后链接第一最后一节字段命名图片
                     # 文件命名为./data/hello/000pwF9.jpg
                     urlretrieve(url.strip(), 'data/%s/%s' % (category, url.strip().split('/')[-1]))
                     # hello 1/16
                     print('%s %i/%i' % (category, i, n_urls))
                except:
                	#hello 8/16 no image
                     print('%s %i/%i' % (category, i, n_urls), 'No Such File')

if __name__ == '__main__':
    download();
