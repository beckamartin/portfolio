import unittest
from solution import is_pangram


class TestIsPangram(unittest.TestCase):
    def test_is_pangram_1(self):
        self.assertEqual(is_pangram("The quick brown fox jumps over the lazy dog"), True)

    def test_is_pangram_2(self):
        self.assertEqual(is_pangram("The quick brown fox jumps over the"), False)
    

if __name__ == '__main__':
    unittest.main()