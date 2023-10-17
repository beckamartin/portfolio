# Lines of Code


from sys import argv
from sys import exit


def main():

    print(check_file(argv))


def check_file(arg):

    if len(arg) == 1:
        exit("Too few command-line arguments")

    elif len(arg) > 2:
        exit("Too many command-line arguments")

    else:
        extension = arg[1]

        if extension.endswith(".py") == True:

            row = 0

            try:
                with open(arg[1], "r") as file:

                    for line in file:

                        line = line.lstrip()

                        if line == "" or line.startswith("#"):
                            pass
                        
                        else:
                            row += 1

                    return row

            except FileNotFoundError:
                exit("File does not exist")

        else:
            exit("Not a Python file")


if __name__ == "__main__":
    main()
