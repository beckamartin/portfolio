import unittest
from solution import RomanNumerals


class TestRomanNumerals(unittest.TestCase):
    def test_to_roman_1(self):
        self.assertEqual(RomanNumerals.to_roman(1000), "M")

    def test_to_roman_2(self):
        self.assertEqual(RomanNumerals.to_roman(4), "IV")

    def test_to_roman_3(self):
        self.assertEqual(RomanNumerals.to_roman(1), "I")

    def test_to_roman_4(self):
        self.assertEqual(RomanNumerals.to_roman(1990), "MCMXC")

    def test_to_roman_5(self):
        self.assertEqual(RomanNumerals.to_roman(2008), "MMVIII")

    def test_from_roman_1(self):
        self.assertEqual(RomanNumerals.from_roman("XXI"), 21)

    def test_from_roman_2(self):
        self.assertEqual(RomanNumerals.from_roman("I"), 1)

    def test_from_roman_3(self):
        self.assertEqual(RomanNumerals.from_roman("IV"), 4)

    def test_from_roman_4(self):
        self.assertEqual(RomanNumerals.from_roman("MMVIII"), 2008)

    def test_from_roman_5(self):
        self.assertEqual(RomanNumerals.from_roman("MDCLXVI"), 1666)


if __name__ == "__main__":
    unittest.main()