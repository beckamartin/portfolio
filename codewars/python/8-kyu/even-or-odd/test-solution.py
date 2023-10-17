import unittest
from solution import even_or_odd


class TestEvenOrOdd(unittest.TestCase):
    def test_even(self):
        self.assertEqual(even_or_odd(2), "Even")

    def test_odd(self):
        self.assertEqual(even_or_odd(3), "Odd")

        
if __name__ == '__main__':
    unittest.main()