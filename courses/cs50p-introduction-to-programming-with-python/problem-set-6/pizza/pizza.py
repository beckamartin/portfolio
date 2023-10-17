# Pizza Py


from sys import argv
from sys import exit
from tabulate import tabulate
import csv


def main():

    check_file(argv)


def check_file(arg):

    if len(arg) == 1:
        exit("Too few command-line arguments")

    elif len(arg) > 2:
        exit("Too many command-line arguments")

    else:
        check_extension = arg[1]

        if check_extension.endswith(".csv") == True:

            try:
                with open(arg[1], "r") as file:

                    pizza_maker(file)

            except FileNotFoundError:
                exit("File does not exist")

        else:
            exit("Not a Python file")


def pizza_maker(file):

    pizza_table = []

    reader = csv.reader(file)

    for row in reader:
        pizza_table.append(row)

    header = pizza_table.pop(0)

    table = pizza_table

    print(tabulate(table, header, tablefmt="grid"))


if __name__ == "__main__":
    main()
