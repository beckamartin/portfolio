import unittest
from solution import high_and_low


class TestHighAndLow(unittest.TestCase):
    def test_high_and_low_1(self):
        self.assertEqual(high_and_low("1 2 3 4 5"), "5 1")

    def test_high_and_low_2(self):
        self.assertEqual(high_and_low("1 2 -3 4 5"), "5 -3")
    
    def test_high_and_low_3(self):
        self.assertEqual(high_and_low("1 9 3 4 -5"), "9 -5")
        

if __name__ == '__main__':
    unittest.main()
