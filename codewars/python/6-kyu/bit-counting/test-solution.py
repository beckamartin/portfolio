import unittest
from solution import count_bits


class TestCountBits(unittest.TestCase):
    def test_count_bits_1(self):
        self.assertEqual(count_bits(1234), 5)

        
if __name__ == '__main__':
    unittest.main()