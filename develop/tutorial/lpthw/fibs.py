def fibs(num):
	'''
	return the fibs sequence 
	>>> fibs(3)
	[0, 1, 1]
	'''
	result = [0, 1]
	print range(num-2)
	for i in range(num-2):
		result.append(result[-2] + result[-1])
	return result

def square(x):
	'''
	>>> square(2)
	4
	>>> square(3)
	9
	'''
	return x*x


