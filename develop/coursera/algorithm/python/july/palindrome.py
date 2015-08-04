import unittest


def is_palindrom(s):
	if s is None or len(s) == 0:
		return False
	front = 0
	back = len(s) - 1

	while(front < back):
		if s[front] != s[back]:
			return False
		else:
			front = front + 1
			back = back -1

		return True

class PalindromTest(unittest.TestCase):
	def test_is_palindrom(self):
		self.assertFalse(is_palindrom(None))
		self.assertFalse(is_palindrom(''))
		self.assertTrue(is_palindrom('abcdefggfedbca'))
		self.assertFalse(is_palindrom('abcdefggfe'))


if __name__ == '__main__':
	unittest.main()