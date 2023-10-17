from bank import value


def main():
    test_hello()
    test_h()
    test_any()


def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0


def test_h():
    assert value("Hi") == 20
    assert value("hi") == 20


def test_any():
    assert value("Any") == 100
    assert value("123") == 100


if __name__ == "__main__":
    main()
