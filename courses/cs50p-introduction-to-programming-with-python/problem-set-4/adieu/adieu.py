# Adieu, Adieu

def main():
    nameList = []

    while True:
        try:
            nameInput = input("Name: ")
            nameList.append(nameInput)
        except EOFError:
            break

    print("\nAdieu, adieu, to ", end="")

    if len(nameList) == 1:
        print(nameList[0])

    elif len(nameList) == 2:
        print(f"{nameList[0]} and {nameList[1]}")

    else:
        for name in nameList[0:-1]:
            print(name, end=", ")
        print(f"and {nameList[-1]}")

if __name__ == "__main__":
    main()