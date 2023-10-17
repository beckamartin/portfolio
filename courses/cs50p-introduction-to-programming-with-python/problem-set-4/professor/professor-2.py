from random import randint
import sys

def main():

    level = get_level()

    score = run_game(level)

    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x, y = randint(0,9), randint(0, 9)
    elif level == 2:
        x, y = randint(10,99), randint(10, 99)
    elif level == 3:
        x, y = randint(100,999), randint(100, 999)
    return x, y

def run_round(x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries += 1
            print("EEE")
            pass
    print(f"{x} + {y} = {x + y}")
    return False

def run_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x, y = generate_integer(level)
        response = run_round(x, y)
        if response == True:
            score += 1
        count_round += 1
    return score

if __name__ == "__main__":
    main()