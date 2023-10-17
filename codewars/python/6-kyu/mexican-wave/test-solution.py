import unittest
from solution import wave


class TestWave(unittest.TestCase):
    def test_wave_1(self):
        self.assertEqual(wave("hello"), ["Hello", "hEllo", "heLlo", "helLo", "hellO"])


if __name__ == '__main__':
    unittest.main()