import unittest
from main import clean_line

class TestMain(unittest.TestCase):

    def test_clean_line(self):

        self.assertEqual(clean_line('hello, world, '), 'hello world', msg='should not contain ","')
        self.assertEqual(clean_line('hello. world. '), 'hello world', msg='should not contain ","')
        self.assertEqual(clean_line('hello "world" '), 'hello world', msg='should not contain ","')
        self.assertEqual(clean_line(' , , , '), '', msg='should not contain ","')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
