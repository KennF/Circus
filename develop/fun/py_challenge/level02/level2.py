out = []
f = open('ocr.html')
for line in f:
	for ch in line:
		if ch.isalpha():
			out.append(ch)
f.close()
print ''.join(out)