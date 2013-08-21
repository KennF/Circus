import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print proxy.system.listMethods()
print proxy.system.getCapabilities()
print proxy.system.methodHelp('phone')
print proxy.system.methodSignature('phone')
print proxy.phone('test')
print proxy.phone("Bert")

multicall = xmlrpclib.MultiCall(proxy)
multicall.phone("Test")
multicall.phone("Bert")
result = multicall()
print result.results

print "the next level url is http://www.pythonchallenge.com/pc/return/italy.html"