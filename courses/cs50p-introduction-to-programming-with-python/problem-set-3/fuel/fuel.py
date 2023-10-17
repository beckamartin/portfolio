# Fuel Gauge

def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")

            x, y = int(x), int(y)

            if x > y or y == 0:
                raise Exception()

            x = int(round((x / y) * 100))

        except ValueError:
            pass

        except ZeroDivisionError:
            pass

        except Exception:
            pass

        else:
            if x <= 1:
                print("E")
            elif x >= 99:
                print("F")
            else:
                print(f"{int(x)}%")
            break

if __name__ == "__main__":
    main()
