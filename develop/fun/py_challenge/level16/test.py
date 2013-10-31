from PIL import Image

def straighten(line):
    idx=0
    while line[idx]!=195:
        idx+=1
    return line[idx:]+line[:idx] # good skill

im = Image.open('mozart.gif')
for y in range(im.size[1]):
    line=[im.getpixel((x, y)) for x in range(im.size[0])]
    line=straighten(line)
    [im.putpixel((x, y),line[x]) for x in range(len(line))]
im.save('result.gif')

print "the next level url is http://www.pythonchallenge.com/pc/return/romance.html"