from um import count


def main():
    test_1()
    test_2()
    test_3()


def test_1():
    assert count("") == 0
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1

def test_2():
    assert count("Um, um...") == 2
    assert count("Hi, um.. myum is...") == 1


def test_3():
    assert count("Um. My name is.. um... Um!") == 3
    assert count("Hello Um, um... um.") == 3


if __name__ == "__main__":
    main()