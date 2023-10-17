from twttr import shorten


def main():
    test_AEIOU()
    test_aeiou()
    test_number()
    test_punctuation()

def test_aeiou():
    assert shorten("Hello World") == "Hll Wrld"

def test_AEIOU():
     assert shorten("hEllO wOrld") == "hll wrld"

def test_number():
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten("?!,.") == "?!,."


if __name__ == "__main__":
    main()