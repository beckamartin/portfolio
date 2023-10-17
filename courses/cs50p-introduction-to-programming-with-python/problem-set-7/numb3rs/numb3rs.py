# NUMB3RS


import re
from sys import exit


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
        numbers = matches.groups()
        
        for n in numbers:
            if int(n) > 255 or int(n) < 0:
                return False
    
        return True

    else:
        return False


if __name__ == "__main__":
    main()
