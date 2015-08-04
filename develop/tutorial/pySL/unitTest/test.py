import random
import unittest
import mock
import json

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    
    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        self.assertRaises(TypeError, random.shuffle,(1, 2, 3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


class TestIt(unittest.TestCase):
    def setUp(self):
        self.m = mock.Mock()
        self.m.get_user()
        self.m.get_user.return_value = '{"name": "John Snow"}'
        self.m.get_user_exception.side_effect = Exception('oops')

    def get_john_info(self):
        s = self.m.get_user()
        # print s 
        j = json.loads(s)
        return j['name']

    def test_get_user(self):
        name = self.get_john_info()
        self.assertEqual(name, 'John Snow')

    def test_get_user_excpetion(self):
        self.assertRaises(Exception, self.m.get_user_exception, ())


if __name__ == '__main__':
    unittest.main()