import unittest
from solution import to_jaden_case


class TestToJadenCase(unittest.TestCase):
    def test_to_jaden_case(self):
        self.assertEqual(to_jaden_case("How can mirrors be real if our eyes aren't real"), "How Can Mirrors Be Real If Our Eyes Aren't Real")


if __name__ == "__main__":
    unittest.main()