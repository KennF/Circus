#!/usr/local/bin/python


primes = [2, 3, 5, 7, 11, 13, 17,19]

def getDividable(n):
	# print n
	factors = []
	while(n!= 1):
		for p in primes:
			if n % p == 0:
				factors.append(p)
				n = n/p
	print "factors", str(factors)
	return factors

def getStatistic(numList):
	dic = {}
	for i in numList:
		if dic.has_key(i):
			dic[i] = dic[i] + 1
		else:
			dic[i] = 1


	print "dict", str(dic)
	return dic


resultDic = {}
print getStatistic(getDividable(8))
for i in range(2, 21):
	for key, value in getStatistic(getDividable(i)).iteritems():
		if resultDic.has_key(key):
			if resultDic[key] < value:
				resultDic[key] = value;
		else:
			resultDic[key] = value;
	print resultDic

result = 1
for key, value in resultDic.iteritems():
	result = result * (key**value)
print result
	



