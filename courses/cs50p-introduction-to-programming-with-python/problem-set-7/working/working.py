# Working 9 to 5


import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([0-9][0-2]*):?([0-5][0-9])*\ (AM|PM)\ to\ ([0-9][0-2]*):?([0-5][0-9])*\ (AM|PM)$", s):
        time_str = matches.groups()
        
        if int(time_str[0]) > 12 or int(time_str[3]) > 12:
            raise ValueError

        time_1 = time(time_str[0], time_str[1], time_str[2])
        time_2 = time(time_str[3], time_str[4], time_str[5])

        return f"{time_1} to {time_2}"

    else:
        raise ValueError


def time(time_1, time_2, time_3):
    if int(time_1) == 12 and time_3 == "AM":
        hour = 0

    elif int(time_1) == 12 and time_3 == "PM":
        hour = 12

    elif int(time_1) != 12 and time_3 == "AM":
        hour = int(time_1)

    elif int(time_1) != 12 and time_3 == "PM":
        hour = int(time_1) + 12
    
    if time_2 == None:
        minute = 0
    
    else:
        minute = int(time_2)

    return f"{hour:02}:{minute:02}" 
    

if __name__ == "__main__":
    main()
