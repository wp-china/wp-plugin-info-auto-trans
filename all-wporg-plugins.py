#!/usr/bin/python
# -*- coding: UTF-8 -*-
from requests_html import HTMLSession

'''
all-wporg-plugins.py

本文件用于从 http://plugins.svn.wordpress.org 获取插件 slug，生成 json.txt 文件。

Author: _Wr_
AuthorURL: https://wrsblog.cn
'''
session = HTMLSession()
print ("Fetching from http://plugins.svn.wordpress.org/...")
r = session.get('http://plugins.svn.wordpress.org/')
links = r.html.links  
print ("Replacing slugs...")
slugs=[ link.replace('/','') for link in links ]
plugins_urls=[ "https://api.wordpress.org/plugins/info/1.0/{}.json".format(slug) for slug in slugs ]
print ("Writing to json.txt...")
with open('json.txt','a') as out:
    out.write("\n".join(plugins_urls))
