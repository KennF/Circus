import unittest, myModule

class PrudctTestCase(unittest.TestCase):
	def testIntegers(self):
		for x in xrange(-10, 10):
			for y in xrange(-10, 10):
				p = myModule.product(x, y)
				self.failUnless(p == x*y, 'Integer multiplication failed')

	def testFloats(self):
		for x in range(-10, 10):
			for y in xrange(-10, 10):
				x = x/10.0
				y = y/10.0
				p = myModule.product(x, y)
				self.failUnless(p == x*y, 'Float multiplication failed')

if __name__ == '__main__':
	unittest.main()

