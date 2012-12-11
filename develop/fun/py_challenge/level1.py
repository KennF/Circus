import string

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
output = []

# for ch in input:
# 	if (ch.isalpha()):
# 		asiic = ord(ch) + 2
# 		if asiic > 122:
# 			asiic = 97 + asiic % 122 - 1
# 		output.append(chr(asiic))
# 	else:
# 		output.append(ch)
# print ''.join(output)

url = "pc/def/map.html"

trans_table = string.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
print input.translate(trans_table)
print url.translate(trans_table)
print "url is www.pythonchallenge.com/pc/def/ocr.html"
