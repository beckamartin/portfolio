import unittest
from solution import hotpot


class TestHotpot(unittest.TestCase):
    def test_hotpot(self):
        self.assertEqual(hotpot(1), 0)
        self.assertEqual(hotpot(5), 5)
        self.assertEqual(hotpot(6), 8)
        self.assertEqual(hotpot(23), 15)


if __name__ == '__main__':
    unittest.main()