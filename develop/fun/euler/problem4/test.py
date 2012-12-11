#!/usr/local/bin/python

def isPalidromic(a):
	strA = str(a)
	return strA[0:] == strA[-1::-1]
result = []
for x in range(100,999):
	for y in range(100,999):
		z = x*y
		if (isPalidromic(z)):
			result.append(z)
print max(result)
print sorted(set(result))