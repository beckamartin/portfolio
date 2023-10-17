import unittest
from solution import multiplication_table


class TestMultiplicationTable(unittest.TestCase):
    def test_multiplication_table_1(self):
        self.assertEqual(multiplication_table(3), [[1,2,3],[2,4,6],[3,6,9]])


if __name__ == '__main__':
    unittest.main()