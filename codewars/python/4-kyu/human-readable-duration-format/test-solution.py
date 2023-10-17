import unittest
from solution import format_duration


class TestFormatDuration(unittest.TestCase):
    def test_format_duration_1(self):
        self.assertEqual(format_duration(0), "now")

    def test_format_duration_2(self):
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")

    def test_format_duration_3(self):
        self.assertEqual(format_duration(3662), "1 hour, 1 minute and 2 seconds")
        
    
if __name__ == '__main__':
    unittest.main()