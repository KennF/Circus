from PIL import Image

img = Image.open('wire.png')
print img.size, img.mode

result_img = Image.new('RGB', (100, 100))

index = 0

x_limit = (0, 99)
y_limit = (0, 99)
x = 0
y = 0

# for x in range(100):
# 	for y in range(100):
# 		result_img.putpixel((x,y), img.getpixel((i,0)))
# 		i = i +  1

# result_img.save('result.png')

direction=[(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_index = 0

while index <=9999 :
	print '({0},{1})'.format(x, y)
	print 'index: ' + str(index)
	result_img.putpixel((x, y), img.getpixel((index,0)))
	x, y = x + direction[direction_index][0], y + direction[direction_index][1]

	if y > y_limit[1]:
		direction_index = (direction_index + 1) % 4
		x_limit = (x_limit[0] + 1 , x_limit[1])
		y = y - 1
		x, y = x + direction[direction_index][0], y + direction[direction_index][1]
		# print '(x_limit: {0},{1})'.format(x_limit[0], x_limit[1])
		# print '(y_limit: {0},{1})'.format(y_limit[0], y_limit[1])
		print '================================================'

	elif x > x_limit[1]:
		direction_index = (direction_index + 1) % 4
		y_limit = (y_limit[0], y_limit[1] - 1)
		x = x - 1
		x, y = x + direction[direction_index][0], y + direction[direction_index][1]
		# print '(x_limit: {0},{1})'.format(x_limit[0], x_limit[1])
		# print '(y_limit: {0},{1})'.format(y_limit[0], y_limit[1])
		print '================================================'

	elif y < y_limit[0]:
		direction_index = (direction_index + 1) % 4
		x_limit = (x_limit[0], x_limit[1] - 1)
		y = y + 1
		x, y = x + direction[direction_index][0], y + direction[direction_index][1]
		# print '(x_limit: {0},{1})'.format(x_limit[0], x_limit[1])
		# print '(y_limit: {0},{1})'.format(y_limit[0], y_limit[1])
		print '================================================'
		

	elif x < x_limit[0]:
		direction_index = (direction_index + 1) % 4
		y_limit = (y_limit[0] + 1, y_limit[1])
		x = x + 1
		x, y = x + direction[direction_index][0], y + direction[direction_index][1]
		# print '(x_limit: {0},{1})'.format(x_limit[0], x_limit[1])
		# print '(y_limit: {0},{1})'.format(y_limit[0], y_limit[1])
		print '================================================'
	index = index +  1

result_img.save('result.png')

print "the next level url is http://www.pythonchallenge.com/pc/return/cat.html"