import re
def gen(num_seq):
	print "input" + str(num_seq)
	str_seq = str(num_seq)
	ret = ""
	while len(str_seq) !=0:
		m = re.match(r"(\d)\1*", str_seq)
		ret = ret + str(len(m.group())) + str(m.group()[0])
		str_seq = str_seq.lstrip(m.group(0))
		print "After:" + str_seq
	print "return========>" + ret
	return int(ret)
	

if __name__ == '__main__':
	a = [1, 11, 21, 1211, 111221]
	print 'Ask len(a[30]) = ?'

	print "11 - one 1"
	print "21 - two 1"
	print "1211 - one 2 and two 1"
	print "111221 - one 1, one 2 and two 1"

	print "so..."

	init = 1
	gen(init)
	for i in range(30):
		init = gen(init)

	print init
	print len(str(init))

	print "next url is http://www.pythonchallenge.com/pc/return/5808.html"



