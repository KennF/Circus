numbers=[2, 7, 11, 15]
target=9

# complexity - o(n**2)
# def two_sum(numbers, target):
# 	length = len(numbers)
# 	for i in range(length - 1):
# 		for j in range(i + 1, length):
# 			# print "%d, %d" % (i, j)
# 			if numbers[i] + numbers[j] == target:
# 				return (i+1, j+1)
# 	return None

def two_sum(numbers, target):
	map = {}
	for i in range(len(numbers)):
		if target - numbers[i] in map.keys():
			return (map[target - numbers[i]]+1, i+1)
		else:
			map[numbers[i]] = i
	

if __name__ == '__main__':
	print two_sum(numbers, target)
			