# Regular, um, Expressions


import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    roaster = re.findall(r"\bum\b", s, flags=re.IGNORECASE)

    return len(roaster)      


if __name__ == "__main__":
    main()
