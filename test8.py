# -*- coding:utf-8 -*-
# __author__ = iris
# __date__ = 1028/10/29
# __desc__ = 字符串去重

from sys import argv

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def main(oldstr):
	if type(oldstr) == str:
		string = oldstr.decode('utf-8')
	else:
		string = oldstr
	coin = 0
	sub = 0
	newstr = ''
	for s in string:
		print s, newstr, sub, coin, string[sub:sub+sub]
		if len(newstr) < 2:
			newstr += s
			sub += 1
			continue
		if newstr == string[sub: sub+sub]:
			print sub, sub+sub, '-!!-', newstr, string[sub: sub+sub]
			coin = sub
		#else:
		#	print sub, sub+sub
		#	print '-***-', newstr, string[sub: sub+sub]
	
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

