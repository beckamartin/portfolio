import pytest
import random
from project import check_argv, select_type, random_pokemon


def main():
    test_check_argv()
    test_select_type()
    test_random_pokemon()


def test_check_argv():
    argv = ["project.py", "input.csv", "output.csv", "extra_arg"]
    with pytest.raises(SystemExit):
        check_argv()

    argv = ["project.py", "input.csv"]
    with pytest.raises(SystemExit):
        check_argv()

    argv = ["project.py", "input.txt", "output.csv"]
    with pytest.raises(SystemExit):
        check_argv()
    
    argv = ["project.py", "input.csv", "output.txt"]
    with pytest.raises(SystemExit):
        check_argv()


def test_select_type():
    assert select_type("normal") == ("Normal")

    assert select_type("rock") == ("Rock")

    assert select_type("Fire") == ("Fire")

    assert select_type("Water") == ("Water")

    assert select_type("12345") ==  None

    assert select_type("not a type") == None


def test_random_pokemon():
    data = [
        ["Linoone", "Normal"],
        ["Pidgey", "Normal"],
        ["Sentret", "Normal"],
        ["Emboar", "Fire"],
        ["Squirtle", "Water"],
        ["Skiddo", "Grass"]
    ]
    random_row = random.choice(data)

    assert random_pokemon([random_row]) == random_row

    
if __name__ == "__main__":
    main()