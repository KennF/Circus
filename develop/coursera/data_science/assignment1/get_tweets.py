import sys
import urllib
import json

base_url = sys.argv[1]
page_para = "page="

for i in range(1,11):
	url = '&'.join([base_url, page_para]) + str(i)
	print "========> get content from", url
	response = urllib.urlopen(url)

	data = json.load(response)
	for a in data['results']:
		content = a['text']
		encoded_string = content.encode('utf-8')
		print encoded_string
