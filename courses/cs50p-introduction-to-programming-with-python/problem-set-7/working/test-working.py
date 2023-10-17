from working import convert
import pytest


def main():
    test_ok()
    test_ok_2()
    test_convert()
    test_wrong_hour()
    test_wrong_minute()


def test_ok():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:30 AM to 08:50 AM") == "00:30 to 08:50"

def test_ok_2():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_convert():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM5 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("9:72 to 6:30")
    with pytest.raises(ValueError):
        convert("13:20 to 6:30")

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")

def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")


if __name__ == "__main__":
    main()