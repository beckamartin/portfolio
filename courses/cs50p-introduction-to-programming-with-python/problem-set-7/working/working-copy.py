# Working 9 to 5


import re
import sys
from datetime import datetime


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([0-9]{1,2}(\:)?([0-9]{2})?\ (AM|PM))\ to\ ([0-9]{1,2}(\:)?([0-9]{2})?\ (AM|PM))$", s):
        time_str = matches.groups()
        print(time_str)

        if time_str[1] == ":":
            time_1 = datetime.strptime(time_str[0], "%I:%M %p")
            time_2 = datetime.strptime(time_str[4], "%I:%M %p")

            time_24h_1 = time_1.strftime("%H:%M")
            time_24h_2 = time_2.strftime("%H:%M")
        
            return (f"{time_24h_1} to {time_24h_2}")

        elif time_str[1] == None:
            time_1 = datetime.strptime(time_str[0], "%I %p")
            time_2 = datetime.strptime(time_str[4], "%I %p")

            time_24h_1 = time_1.strftime("%H:%M")
            time_24h_2 = time_2.strftime("%H:%M")
        
            return (f"{time_24h_1} to {time_24h_2}")
            
        else:
            raise ValueError

    else:
        raise ValueError


if __name__ == "__main__":
    main()
