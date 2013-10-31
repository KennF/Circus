from PIL import Image
from StringIO import StringIO
import requests

# r = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png')
# print r.text
# print r.encoding
# print r.content
# im = Image.open(StringIO(r.content))

# im.save('oxygen.png')

im = Image.open('oxygen.png')
print im.format, im.size, im.mode
# width, height = 629, 95
# xs = []
# ys = []
# for x in range(width):
# 	for y in range(height):
# 		r,g,b,z = im.getpixel((x,y))
# 		if r == g and g == b:
# 			print x, ',', y
# 			xs.append(x)
# 			ys.append(y)
# print min(xs), ',', max(xs)
# print min(ys), ',', max(ys)

xmin, xmax = 0 , 609
ymin, ymin = 43 , 51
result = [chr(im.getpixel((i,51))[0]) for i in range(0,609,7)]
print result
print "".join(result)
next = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print "".join(chr(ch) for ch in next)
print 'next url is http://www.pythonchallenge.com/pc/def/integrity.html'

# result = []
# for pixel in im.getdata():
# 	if pixel[0] == pixel[1] and pixel[1]==pixel[2]:
# 		print pixel