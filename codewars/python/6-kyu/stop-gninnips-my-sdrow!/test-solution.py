import unittest
from solution import spin_words


class TestSpinWords(unittest.TestCase):
    def test_spin_words_1(self):
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")

    def test_spin_words_2(self):
        self.assertEqual(spin_words("This is a test"), "This is a test")
    
    def test_spin_words_3(self):
        self.assertEqual(spin_words("This is another test"), "This is rehtona test")


if __name__ == '__main__':
    unittest.main()