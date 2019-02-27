# -*- coding:utf-8 -*-
# __author__ = iris
# __date__ = 2018/10/17
# __desc__ = 将字符串中连续重复的标点符号去除，只保留一个

from sys import argv

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def func(_str):
	'''
	:param _str:需要判断的字符串
	'''

	_str = _str.decode('utf-8')  
	_list = list(_str)  
	n = len(_list)  
	if n <= 1:
		return _str
 	list1 = []  

	for i in range(n-1):
		if _list[i] in u".!/_,$?=~%^*(  +\"'+——！，。？、~@#￥%……&*（）～":
			if _list[i] != _list[i+1]:
				list1.append(_list[i])
		else:
			list1.append(_list[i])  

	list1.append(_list[-1])  
	str1 = ''.join(list1)  
	return str1

if __name__ == '__main__':
	if len(argv) > 1:
		a = argv[1]
		string = func(a)
		print 'type', type(string), string
	else:
		print 'Please input your word'

