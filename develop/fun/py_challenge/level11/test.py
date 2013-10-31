from PIL import Image
import os

EVEN_JPG = "even.jpg"
ODD_JPG = "odd.jpg"

image = Image.open('cave.jpg')
print image.format, image.mode, image.size

if os.path.exists(EVEN_JPG):
	os.remove(EVEN_JPG)
if os.path.exists(ODD_JPG):
	os.remove(ODD_JPG)

img = Image.open('cave.jpg')
even = Image.new('RGB',img.size)
odd = Image.new('RGB',img.size)

for x in range(0,img.size[0],2):
    for y in range(0,img.size[1],2):
        even.putpixel((x,y),img.getpixel((x,y)))
        odd.putpixel((x+1,y+1),img.getpixel((x+1,y+1)))

even = even.resize((img.size[0]/2,img.size[1]/2))
odd = odd.resize((img.size[0]/2,img.size[1]/2))

even.save(EVEN_JPG)
odd.save(ODD_JPG)

print "next url is http://www.pythonchallenge.com/pc/return/evil.html"