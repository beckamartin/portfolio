import unittest
from solution import pig_it


class TestPigIt(unittest.TestCase):
    def test_pig_it_1(self):
        self.assertEqual(pig_it("Pig latin is cool"), "igPay atinlay siay oolcay")
    
    def test_pig_it_2(self):
        self.assertEqual(pig_it("This is my string"), "hisTay siay ymay tringsay")

    def test_pig_it_3(self):
        self.assertEqual(pig_it("Hello world !"), "elloHay orldway !")


if __name__ == "__main__":
    unittest.main()