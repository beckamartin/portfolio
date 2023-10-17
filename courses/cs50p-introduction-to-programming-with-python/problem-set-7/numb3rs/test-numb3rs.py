from numb3rs import validate


def main():
    test_validate()


def test_validate():
    assert validate("300.168.10.1") == True
    assert validate("275.3.6.28") == False
    assert validate("192.300.6.28") == False
    assert validate("192.3.600.28") == False
    assert validate("192.3.6.800") == False
    assert validate("275,3,6,28") == False
    assert validate("-275.3.6.28") == False


if __name__ == "__main__":
    main()
