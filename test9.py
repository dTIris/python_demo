# -*- coding:utf-8 -*-
# __author__ = iris
# __date__ = 2018/10/29
# __desc__ = 判断字符串是否含中文

import re
from sys import argv

def main(_str):
	if type(_str) == str:
		_str = _str.decode('utf-8')

	re_str = re.compile(u"[\u4e00-\u9fa5]+")
	str_group = re_str.search(_str, 0)
	if not str_group:
		print _str, 'no group'
		return ''
	strs = str_group.group()
	return strs

if __name__ == '__main__':
	if len(argv) > 1:
		a = argv[1]
		string = main(a)
		print a , '的中文是：', string
	else:
		print 'Please input your word'

	
