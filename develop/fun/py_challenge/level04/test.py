#!/usr/bin/python

import requests
import re

init_num = '12345'
# init_num = '3875'
# init_num = '25357'
url_prefix = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
def FoundNext(iter_num):
	next_num = ''
	for i in range(iter_num):
		if next_num is '': 
			r = requests.get(url_prefix + init_num)
		else:
			r = requests.get(url_prefix + next_num)
		# print(r.text)
		result = re.search(r'\d+$', r.text)
		if result:
			if result.group(0) == '16044':
				next_num = str(int(result.group(0))/2)
			else:
				next_num = result.group(0)
			print(next_num)
		else:
			break
FoundNext(400)

#final is 66831
print 'the url of next level is http://www.pythonchallenge.com/pc/def/peak.html'