# Felipe’s Taqueria

def main():

    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    sum = 0.00

    while True:
        try:
            x = input("Item: ").title()

            sum = sum + menu[x]

            print(f"Total: ${sum:.2f}")

        except EOFError:
            break

        except KeyError:
            pass

if __name__ == "__main__":
    main()