# Home Federal Savings Bank

def main():
    x = input("Greating: ").strip().lower()

    if x.startswith("hello"):
        print("$0")

    elif x.startswith("h", 0):
        print("$20")

    else:
        print("$100")

if __name__ == "__main__":
    main()