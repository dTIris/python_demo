# -*-coding:utf-8 -*-
# __author__ = iris
# __date__ = 2018/10/23
# __desc__ = 字符串判断
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

yel = [u'稍等', u'那好', u'再见', u'滚蛋']

def find_yel(key):
	if type(key) == str:
		key = key.decode('utf-8')
	for y in yel:
		length = len(y) + 5
		if y in key and len(key) <= length:
				return True
	return False

key = '你好吗再见啦啦'

if find_yel(key):
	print key

