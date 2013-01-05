import zipfile, re

history = []

def FoundNext(zipped_file, file_name):
	f = zipped_file.open(file_name, 'r')
	content = f.read()
	print content
	result = re.search(r'\d+$', content)
	print zipped_file.getinfo(file_name).comment
	history.append(zipped_file.getinfo(file_name).comment)
	f.close()
	next_file = ''
	if result:
		next_file= result.group(0)
	print next_file
	return next_file

f = zipfile.ZipFile('channel.zip', 'r')
init = '90052'
# print f.namelist()
while True:
	init = FoundNext(f, init + '.txt')
	if init is '':
		break
print f.comment
f.close()
print "".join(history)


