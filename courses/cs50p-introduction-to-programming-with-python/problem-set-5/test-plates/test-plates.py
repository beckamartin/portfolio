from plates import is_valid


def main():
    test_len()
    test_punctuation()
    test_end_is_alpha()
    test_numbers()
    test_starts_with_zero()

def test_len():
    assert is_valid("AA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False


def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI 14") == False


def test_end_is_alpha():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_numbers():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False


def test_starts_with_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


if __name__ == "__main__":
    main()
