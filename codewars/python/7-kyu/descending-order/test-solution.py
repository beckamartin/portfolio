import unittest
from solution import descending_order


class TestDescendingOrder(unittest.TestCase):
    def test_descending_order_1(self):
        self.assertEqual(descending_order(0), 0)

    def test_descending_order_2(self):
        self.assertEqual(descending_order(15), 51)

    def test_descending_order_3(self):
        self.assertEqual(descending_order(123456789), 987654321)


if __name__ == "__main__":
    unittest.main()