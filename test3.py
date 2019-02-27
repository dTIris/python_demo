# -*-coding:utf-8 -*-
# __author__ = iris
# __date__ = 2018/10/19
# __desc__ = 将rootdir的文件生成sitemap目录文件

import os
import sys
import time

endstring= """</sitemapindex>\n"""
sign = 0

# 修改文件名
rootdir = 'json1'
xmlname = 'jsonsite.xml'

url = 'https://www.169kang.com/'

i = 0
today = time.strftime('%Y-%m-%d',time.localtime(time.time()))

for name in os.listdir(rootdir):
        print "count=",i
        path = os.path.join(rootdir, name)
        file_name = url + path
        firststring =""
        firststring+="""<?xml version="1.0" encoding="UTF-8"?>\n"""
        firststring+="""<sitemapindex>\n"""
        mystring = ""
        mystring+="""    <sitemap>\n"""
        mystring+="""        <loc>"""
        mystring+=file_name
        mystring+="""</loc>\n"""
        mystring+="""        <lastmod>"""
		mystring+=str(today)
		mystring+="""</lastmod>\n"""
        mystring+="""    </sitemap>\n"""
        f = file(xmlname,'a+')
        if i == 0 :
                f.write(firststring)
                i += 1
        f.write(mystring)
		i += 1
f.write(endstring)

