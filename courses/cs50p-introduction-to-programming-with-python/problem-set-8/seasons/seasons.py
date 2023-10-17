# Seasons of Love


from datetime import date
from sys import exit
import re
import inflect


def main():
    birthday = get_date(input("Date of birth: "))

    year, month, day = birthday.split("-")

    birthday = date(int(year), int(month), int(day))

    today = date.today()

    print(get_minutes(birthday, today))



def get_date(s):
    if matches := re.search(r"^(([0-9]{1,4})-([0-9]{1,2})-([0-9]{1,2}))$", s):
        date = matches.group(1)

        return date
    
    else:
        exit("Invalid date")


def get_minutes(birthday, today):
    difference = today - birthday

    days = str(difference)

    days = days.split(" ")

    minutes = (int(days[0]) * 24) * 60

    p = inflect.engine()

    words = p.number_to_words(minutes, andword="").capitalize()

    return f"{words} minutes"


if __name__ == "__main__":
    main()