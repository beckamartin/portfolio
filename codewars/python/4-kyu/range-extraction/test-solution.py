import unittest
from solution import solution as range_extractor


class TestRangeExtractor(unittest.TestCase):
    def test_range_extractor_1(self):
        """Testing list of zero elements.
        """
        self.assertEqual(range_extractor([]), "")

    def test_range_extractor_2(self):
        """Testing list of one element.
        """
        self.assertEqual(range_extractor([0]), "0")

    def test_range_extractor_3(self):
        """Testing list of two following elements.
        """
        self.assertEqual(range_extractor([0, 1]), "0,1")

    def test_range_extractor_4(self):
        """Testing list of two non-following elements.
        """
        self.assertEqual(range_extractor([0, 2]), "0,2")

    def test_range_extractor_5(self):
        """Testing list of three following elements.
        """
        self.assertEqual(range_extractor([0, 1, 2]), "0-2")

    def test_range_extractor_6(self):
        """Testing list of three non-following elements.
        """
        self.assertEqual(range_extractor([0, 2, 4,]), "0,2,4")

    def test_range_extractor_7(self):
        """Testing list of more then three following elements.
        """
        self.assertEqual(range_extractor([0, 1, 2, 3]), "0-3")

    def test_range_extractor_8(self):
        """Testing list of more then three non-following elements.
        """
        self.assertEqual(range_extractor([0, 2, 4, 6]), "0,2,4,6")

    def test_range_extractor_9(self):
        """Testing list of more then three following elements and one non-following.
        """
        self.assertEqual(range_extractor([0, 1, 2, 3, 5]), "0-3,5")

    def test_range_extractor_10(self):
        """Testing list of one non-following and more then three following elements.
        """
        self.assertEqual(range_extractor([0, 2, 3, 4, 5]), "0,2-5")

    def test_range_extractor_example_1(self):
        """Testing list example 1.
        """
        self.assertEqual(range_extractor([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]), "-10--8,-6,-3-1,3-5,7-11,14,15,17-20")
        
    def test_range_extractor_example_2(self):
        """Testing list example 2.
        """
        self.assertEqual(range_extractor([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')
        

if __name__ == "__main__":
    unittest.main()