# -*-coding:utf-8 -*-
# __author__ = iris
# __date__ = 2018/10/23
# __desc__ = 读表格文件并最后按首字母输出
import xlrd

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def readxls(name, sheet_):
	'''
	:param name: 待读取文件名
	:param sheet_: 工作表名
	:returns: None
	:raises error: None
	'''
	data = xlrd.open_workbook(name)
	table = data.sheets()[sheet_]
	
	nrows = table.nrows
	
	words = {}
	
	for i in range(nrows):
		word = table.row_values(i)[1]
	    print word.replace(' ', '').strip()
	
	    first = word[0]
	    other = word[1:]
	    if first in words:
	        words[first] += (other+',')
	    else:
	        words[first] = (other+',')
	
	    for word in words:
	    print word+':'+words[word]
	
	    #print first, other

