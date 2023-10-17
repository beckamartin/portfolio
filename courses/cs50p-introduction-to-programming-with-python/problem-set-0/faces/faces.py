#Making Faces

def convert(n):
    n = n.replace(":)", "🙂").replace(":(", "🙁")
    print(n)

def main():
    x = input("User input: ")

    x = convert(x)

if __name__ == "__main__":
    main()