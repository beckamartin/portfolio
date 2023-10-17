# Grocery List

def main():

    groceryList = {}

    while True:
        try:
            x = input().upper()

            groceryList[x] = groceryList.get(x, 0) + 1

        except EOFError:
            for item in sorted(groceryList):
                print(groceryList[item], item)
            break

        except KeyError:
            pass

if __name__ == "__main__":
    main()