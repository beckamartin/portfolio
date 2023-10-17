# camelCase

def main():

    x = input("camelCase: ")

    for i in x:
        if i.islower():
            print(i, end="")
        else:
            print("_" + i.lower(), end="")

if __name__ == "__main__":
    main()