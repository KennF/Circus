from functools import partial

def test_evens():
	for i in range(0, 5):
		f = partial(getattr(CheckEven(), 'check_even'), i , i*3)
		f.description = "test description - check_even({0}, {1})".format(i, i*3)
		test_evens.__name__ = "test evens - input is {0}".format(i)
		yield f,

class CheckEven(object):
	def check_even(self, n, nn):
		assert n%2 == 0  or nn%2 ==0
