from sys import exit, argv
import csv
import re
import random


def main():
    check_argv()

    team = list()

    while True:
        try:
            team_range = input("How many pokemones you want? ")

            team_range = int(team_range)

            break

        except:
                pass
       
    for _ in range(0,team_range): 
        while True:
            try:
                type = select_type(input("Select type: "))

                types = ["Normal", "Rock", "Fire", "Water", "Grass"]

                if type in types:
                    break

            except:
                pass

        with open(argv[1], "r") as file:
            reader = csv.DictReader(file)

            data = []

            for row in reader:
                if row["Type 1"] == type:
                    data.append([row["Name"], row["Type 1"]])
        
        new_pokemon = random_pokemon(data)
        team.append(new_pokemon)

    with open(argv[2], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["#", "Name", "Type"])

        writer.writeheader()

        for i, row in enumerate(team):
            writer.writerow({"#": i+1, "Name": row[0], "Type": row[1]})

    print("Here is your random pokemon team, also you can find it in CSV file!\n")

    for row in team:
        print(f"Name: {row[0]}, Type: {row[1]}")


def check_argv():
    if len(argv) > 3:
        exit("Too many arguments")

    elif len(argv) < 3:
        exit("Too few arguments")
    
    elif ".csv" not in argv[1] or ".csv" not in argv[2]:
        exit("Invalid suffix")


def select_type(type):
    if matches := re.search(r"^(([A-Z]|[a-z]){1}[a-z]+)$", type):
        type = matches.group(1).capitalize()
        
        return type


def random_pokemon(data):
        random_index = random.randint(0, len(data)-1)
        random_row = data[random_index]

        return random_row


if __name__ == "__main__":
    main()