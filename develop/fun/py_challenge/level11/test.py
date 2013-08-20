import Image

image = Image.open('cave.jpg')
odd = Image.new('RGB', image.size)
even = Image.new('RGB', image.size)
print image.format, image.mode, image.size

print image.getbands()

for x in range(image.size[0], 2):
	for y in range(image.size[1], 2):
		even.putpixel((x, y),image.getpixel((x, y)))
		odd.putpixel((x+1, y+1), image.getpixel(x+1, y+1))

even.save("even.jpg")
odd.save("odd.jpg")