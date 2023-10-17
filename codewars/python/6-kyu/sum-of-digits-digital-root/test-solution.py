import unittest
from solution import digital_root


class TestDigitalRoot(unittest.TestCase):
    def test_digital_root_1(self):
        self.assertEqual(digital_root(16), 7)

    def test_digital_root_2(self):
        self.assertEqual(digital_root(942), 6)
    
    def test_digital_root_3(self):
        self.assertEqual(digital_root(132189), 6)


if __name__ == '__main__':
    unittest.main()