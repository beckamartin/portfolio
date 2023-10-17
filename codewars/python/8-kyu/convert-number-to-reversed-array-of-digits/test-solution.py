import unittest
from solution import digitize


class TestDigitalize(unittest.TestCase):
    def test_digitalize_1(self):
        self.assertEqual(digitize(35231), [1,3,2,5,3])

    def test_digitalize_2(self):
        self.assertEqual(digitize(0), [0])

    def test_digitalize_3(self):
        self.assertEqual(digitize(23582357), [7,5,3,2,8,5,3,2])

    def test_digitalize_4(self):
        self.assertEqual(digitize(984764738), [8,3,7,4,6,7,4,8,9])

    def test_digitalize_5(self):
        self.assertEqual(digitize(45762893920), [0,2,9,3,9,8,2,6,7,5,4])

    def test_digitalize_6(self):
        self.assertEqual(digitize(548702838394), [4,9,3,8,3,8,2,0,7,8,4,5])


if __name__ == "__main__":
    unittest.main()