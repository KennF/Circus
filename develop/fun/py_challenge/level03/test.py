out=[]
f=open("source.txt","r")
for l in f:
	out.append(l.strip())
f.close()
input = "".join(out)
# print input
import re
# reg = re.compile()
m = re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", input)
if m:
	print "".join(m)
else:
	print "no match"

print "the url is http://www.pythonchallenge.com/pc/def/linkedlist.php"
