import unittest
from solution import sum_strings


class TestSumStrings:
    def test_sum_strings_1(self):
        self.assertEqual(sum_strings("1", "1"), "2")

    def test_sum_strings_2(self):
        self.assertEqual(sum_strings("123", "456"), "579")


if __name__ == "__main__":
    unittest.main()