# Back to the Bank


def main():
    x = input("Greating: ")
    print("$", value(x))


def value(greeting):

    greeting = greeting.strip().lower()

    if greeting.startswith("hello"):
        return 0

    elif greeting.startswith("h", 0):
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
