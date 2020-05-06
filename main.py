#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

'''
main.py

本文件用于调用其他 py 文件，无实际用处。

Author: _Wr_
AuthorURL: https://wrsblog.cn
'''
# 环境要求
requirementFile = open("requirement.txt", encoding='UTF-8')
requirement = requirementFile.read()
print(requirement)
input ("\n按下回车键以继续")
# 运行 all-wporg-plugins.py
print ("\n\nRunning all-wporg-plugins.py...")
os.system("python3 all-wporg-plugins.py")
# 运行 all-wporg-plugins-jsons.py
print ("Running all-wporg-plugins-jsons.py...")
os.system("python3 all-wporg-plugins-jsons.py")
# 运行 translate.py
print ("Running translate.py...")
os.system("python3 translate.py")
print ("Done")
input ("按下回车键以结束程序")
