# Just setting up my twttr

def main():

    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

    x = input("Input: ")

    while True:
        print("Output: ", end="")
        for i in x:
            if i in vowels:
                print("", end="")
            else:
                print(i, end="")
        break

if __name__ == "__main__":
    main()