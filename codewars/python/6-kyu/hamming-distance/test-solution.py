import unittest
from solution import hamming


class TestHamming(unittest.TestCase):
    def test_hamming_1(self):
        self.assertEqual(hamming("hello world","hello tokyo"), 4)

    def test_hamming_2(self):
        self.assertEqual(hamming("a man a plan a canal","a man a plan sobanal"), 3)

    def test_hamming_3(self):
        self.assertEqual(hamming("espresso","Expresso"),2)

    def test_hamming_4(self):
        self.assertEqual(hamming("old father, old artificer","of my soul the uncreated "),24)


if __name__ == "__main__":
    unittest.main()