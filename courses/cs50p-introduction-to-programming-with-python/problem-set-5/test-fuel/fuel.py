# Refueling

def main():
    fraction = input("Fraction: ")

    x = convert(fraction)

    print(gauge(x))

def convert(fraction):
    try:
        x, y = fraction.split("/")

        x, y = int(x), int(y)

        if y == 0:
            raise ZeroDivisionError

        elif x > y:
            raise ValueError

    except (ValueError, ZeroDivisionError):
        raise

    else:
        x = int(round((x / y) * 100))
   
        return x            

def gauge(percentage):
    if percentage <= 1:
        return f"E"
    elif percentage >= 99:
        return f"F"
    else:
        return f"{int(percentage)}%"

if __name__ == "__main__":
    main()
