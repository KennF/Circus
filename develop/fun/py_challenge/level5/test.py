import pickle, urllib

handle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(handle)
handle.close()
print data
for elt in data:
    print "".join([e[1] * e[0] for e in elt])


print "the answer is 'channel'"
print "http://www.pythonchallenge.com/pc/def/channel.html"