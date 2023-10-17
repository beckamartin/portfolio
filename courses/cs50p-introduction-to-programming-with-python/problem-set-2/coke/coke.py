def main():

    x = 50

    print("Amount due: ", x)

    while x <= 50 and x > 0:
        n = int(input("Insert coin: "))
        if n == 5 or n == 10 or n == 25:
            x = x - n
            if x > 0:
                print("Amount due: ", x)
            else:
                print("Change owed: ", x * -1)
        else:
            print("Amount due: ", x)


if __name__ == "__main__":
    main()