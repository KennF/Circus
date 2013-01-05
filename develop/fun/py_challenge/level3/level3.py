import re

#prog = re.compile("""[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+""")
prog = re.compile("""[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]""")
f = open('equality.html')
content = f.readlines()
f.close()
#print content
all = "".join(content)
print prog.findall(all)

#http://www.pythonchallenge.com/pc/def/linkedlist.php

