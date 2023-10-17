import unittest
from solution import domain_name


class TestDomainName(unittest.TestCase):
    def test_domain_name_1(self):
        self.assertEqual(domain_name("http://google.com"), "google")
    
    def test_domain_name_2(self):
        self.assertEqual(domain_name("http://google.co.jp"), "google")

    def test_domain_name_3(self):
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")

    def test_domain_name_4(self):
        self.assertEqual(domain_name("https://youtube.com"), "youtube")


if __name__ == "__main__":
    unittest.main()