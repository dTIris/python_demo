# -*- coding:utf-8 -*-
# __author__ = iris
# __date__ = 2018/10/29
# __desc__ = 遍历文件下的xml文件并用dom解析


from pymongo import MongoClient
from xml.dom import minidom
import os
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

client = MongoClient('10.5.0.10', 38000)
db = client['iris_xml']
keyword = db['new_keyword']

def insertdata(rootfile):
	with open(rootfile,'r') as f:
		dom=minidom.parse(f)

	root=dom.documentElement
	print root.nodeName
	items = root.getElementsByTagName("item")
	i = 0
	length = len(items)
	for item in items:
		key = item.getElementsByTagName("key")[0]
		#print key.nodeName, key.nodeType
		key_text = key.childNodes[0]
		if key_text.nodeType == 4:
			id_ = key_text.data.strip()
			#print key.nodeName, id_
		else:
			print key_text.data.strip()
			#continue
		question = item.getElementsByTagName("question")[0]
		que_key = question.childNodes[0]
		if que_key.nodeType == 4:
			data = que_key.data.strip()
			d_list = data.split(';')
		else:
			print que_key.data.strip()
			#continue
			#print question.nodeName, d_list 
		
		try:
			keyword.insert({'_id': id_, 'other':d_list})
			i += 1
		except Exception, e:
			print id_, 'error:\n', e
	if i == length:
		print '已成功输入', i, '个文件'
	else:
		print '此文件出现错误， 有',length-i,'个错误文件'

def main():
	cwd=os.getcwd()
	file_ = 'jk_wap'
	rootdir = cwd + '/' + file_
	print 'rootdir:', rootdir
	for f_name in os.listdir(rootdir):
		rootfile = file_ + '/' + f_name
		print 'file_name:', f_name
		insertdata(rootfile)
		print '------------------------------------------------------'
		#break

if __name__ == '__main__':
	main()

