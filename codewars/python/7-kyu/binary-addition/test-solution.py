import unittest
from solution import add_binary


class TestAddBinary(unittest.TestCase):
    def test_add_binary_1(self):
        self.assertEqual(add_binary(1, 1), "10")

    def test_add_binary_2(self):
        self.assertEqual(add_binary(5, 9), "1110")

        
if __name__ == '__main__':
    unittest.main()