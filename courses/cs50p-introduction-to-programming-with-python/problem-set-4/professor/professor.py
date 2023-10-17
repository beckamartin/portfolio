# Little Professor

from random import randint

def main():
    generate_integer(get_level())

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
    score = 0

    for i in range(10):
        trials = 0

        if level == 1:
            x, y = randint(0,9), randint(0, 9)
        elif level == 2:
            x, y = randint(10,99), randint(10, 99)
        elif level == 3:
            x, y = randint(100,999), randint(100, 999)

        while True:
            if trials < 3:
                print(f"{x} + {y} = ", end="")
                try:
                    answer = int(input())
                    if answer == x + y:
                        if trials == 0:
                            score += 1
                            break
                        elif trials != 0:
                            break
                    else:
                        trials += 1
                        print("EEE")
                        continue
                except:
                    trials += 1
                    print("EEE")
                    continue
            elif trials == 3:
                print(f"{x} + {y} = {x + y}")
                break
    print(f"Score: {score}")

if __name__ == "__main__":
    main()
