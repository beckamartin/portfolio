from seasons import get_date
from sys import exit
import pytest


def main():
    test_get_date_valid_input()
    test_get_date_invalid_input()


def test_get_date_valid_input():
    assert get_date("1997-01-20") == "1997-01-20"


def test_get_date_invalid_input():
    with pytest.raises(SystemExit):
        get_date("")

    with pytest.raises(SystemExit):
        get_date("cat")

    with pytest.raises(SystemExit):
        get_date("1997.01.20")           


if __name__ == "__main__":
    main()
