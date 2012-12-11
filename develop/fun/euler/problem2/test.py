#!/usr/local/bin/python

def fib():
	a, b = 1, 2
	while True:
		yield a
		a, b = b, a + b

a = fib()
result = []
b = a.next()
print b
while(b < 4000000):
	if(b % 2 == 0):
		result.append(b)
	b = a.next()
	print b
print result
print sum(result)