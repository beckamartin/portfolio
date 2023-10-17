# Scourgify


from sys import exit
from sys import argv
from os.path import exists
import csv


def main():
    check_file(argv)
    
    students = read_csv(argv)

    write_csv(students, argv)


def write_csv(students, argv):
    with open(argv[2], "w", newline="") as file:
        
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

        writer.writeheader()

        for row in students:
            writer.writerow({"first": row[0], "last": row[1], "house": row[2]})


def read_csv(argv):
        with open(argv[1], "r") as file:

            reader = csv.DictReader(file)

            students = []

            for row in reader:
                split_name = row['name'].split(",")

                students.append([split_name[1].replace(" ", ""), split_name[0], row['house']])
            
            return students


def check_file(argv):
    if len(argv) <= 2:
        exit("Too few command-line arguments")

    elif len(argv) > 3:
        exit("Too many command-line arguments")

    elif len(argv) == 3:
        if argv[1].endswith(".csv") == False or argv[2].endswith(".csv") == False:
            exit("Not a python file")

        elif exists(argv[1]) == False:
            exit(f"Could not read {argv[1]}")


if __name__ == "__main__":
    main()