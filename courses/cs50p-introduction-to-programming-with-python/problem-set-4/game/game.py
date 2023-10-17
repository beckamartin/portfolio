# Guessing Game

def main():
    from random import randint
    import sys

    while True:
        try:
            intLevel = int(input("Level: "))
            if intLevel < 1:
                raise Exception

            elif intLevel >= 1:
                n = intLevel
                break

        except Exception:
            pass

    randomNumber = randint(1, n)

    while True:
        try:
            guess = int(input("Guess: "))

            if guess < randomNumber:
                print("Too small!")

            elif guess > randomNumber:
                print("Too large!")

            elif guess == randomNumber:
                print("Just right!")
                break
        except:
            pass

if __name__ == "__main__":
    main()