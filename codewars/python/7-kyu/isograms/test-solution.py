import unittest
from solution import is_isogram


class TestIsIsogram(unittest.TestCase):
    def test_is_isogram_1(self):
        self.assertEqual(is_isogram("Dermatoglyphics"), True)

    def test_is_isogram_2(self):
        self.assertEqual(is_isogram("moOse"), False)
    
    def test_is_isogram_3(self):
        self.assertEqual(is_isogram("aba"), False)
        

if __name__ == '__main__':
    unittest.main()