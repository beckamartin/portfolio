from fuel import convert
from fuel import gauge
import pytest


def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("0/4") == 0
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")    

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(33) == "33%"

if __name__ == "__main__":
    main()