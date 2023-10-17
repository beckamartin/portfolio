import unittest
from solution import summation


class TestSummation(unittest.TestCase):
    def test_summation(self):
        self.assertEqual(summation(2), 3)
        self.assertEqual(summation(8), 36)


if __name__ == "__main__":
    unittest.main()
