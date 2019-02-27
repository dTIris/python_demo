# -*- coding:utf-8 -*-
# __author__ = iris
# __date__ = 2018/10/29
# __ desc__ = 字符串遍历去重

from sys import argv

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def main(oldstr):
	if type(oldstr) == str:
		newstr = oldstr.decode('utf-8')
	else:
		newstr = oldstr
	string = ''
	coin = 0
	sub = 0
	while True:
		if newstr == string:
			print 'over', newstr, string
			break
		else:
			print 'start', newstr, '-', string
			string = newstr
			newstr = ''
			coin = 0
			sub = 0
		for s in string:
			#print s, newstr, sub, string[sub:sub+sub]
			if len(newstr) < 2:
				newstr += s
				sub += 1
				continue
			if newstr == string[sub: sub+sub]:
				#print sub, sub+sub, '-!!-', newstr, string[sub: sub+sub]
				coin = sub
	
			if coin:
				sub += 1
				coin -= 1
				continue
			else:
				newstr += s
				sub += 1
				
	return newstr

if __name__ == '__main__':
	if len(argv) > 1:
		a = argv[1]
		string = main(a)
		#print 'type', type(string),
		print  string
	else:
		print 'Please input your word'

