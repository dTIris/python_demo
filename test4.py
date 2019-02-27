# -*-coding:utf-8 -*-
# __author__ = iris
# __date__ = 2018/10/19
# __desc__ = 生成随机时间函数

import time
import datetime
import random

a1=(2016,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
a2=(2018,10,1,23,59,59,0,0,0)    #设置结束日期时间元组

# 生成随机时间函数
def random_time(time_str1, time_str2, status):
	'''
	:param time_str1: 初始时间字符串
	:param time_str2: 结束时间字符串
	:param status: 1为日期+时刻，0只需要日期
	:returns: 随机时间字符串
	:raises error: None
	'''
	if not compare_time(time_str1, time_str2):
		time_str1, time_str2 = time_str2, time_str1

	#字符串转换为时间元组
	date1 = datetime.datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S")
	date2 = datetime.datetime.strptime(time_str2, "%Y-%m-%d %H:%M:%S")

	# 生成时间戳
	start=time.mktime(date1.timetuple())   
	end=time.mktime(date2.timetuple()) 

	# 随机取出一个,生成时间元组
	t=random.randint(start,end) 
	#date_touple=time.localtime(t) 
	date_touple = datetime.datetime.fromtimestamp(t)
	
	# 时间元组转成格式化字符串
	if status:
		date=datetime.datetime.strftime(date_touple, "%Y-%m-%d %H:%M:%S") 
	else:
		date=datetime.datetime.strftime(date_touple, "%Y-%m-%d")
    #print(date)
	
	return date

# 时间比较函数
def compare_time(time_str1, time_str2):
	'''
	:param time_str1: 时间字符串
	:param time_str2: 时间字符串
	:returns: time_str1 比 time_str2 小(早) 返回 true
	:raises error: None
	'''
	return time_str1 < time_str2

# 时间增加函数
def add_day(time_str, day):
	'''
	:param time_str: 待修改的字符串
	:param day: 变化的天数
	:returns: 时间字符串
	:raises error: None
	'''
	date_old = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
	day_bit = datetime.timedelta(days=day)
	date_new = date_old + day_bit

	date = date_new.strftime("%Y-%m-%d %H:%M:%S")
	return date

def main():
	#print random_time('2017-01-11 20:49:44', '2018-01-19 06:00:34', 1)
	#print compare_time('2018-05-24 19:26:36', '2018-05-14 19:26:36')
	#print add_day('2018-05-24 19:26:36', 1)


if __name__ == '__main__':
	main()


