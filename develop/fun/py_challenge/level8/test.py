import bz2

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
# im = Image.open('integrity.jpg')
# out = im.filter(ImageFilter.DETAIL) 
# out.save('integrity_detail.jpg')
# r,g,b = im.split()
# r.save('integrity_r.jpg')
# g.save('integrity_g.jpg')
# b.save('integrity_b.jpg')
# enh = ImageEnhance.Sharpness(im)  
# enh.enhance(5.0).save("integrity_5sharp.jpg")  

print 'username:', bz2.decompress(un)
print 'password:', bz2.decompress(pw)
print 'next url is http://www.pythonchallenge.com/pc/return/good.html'

