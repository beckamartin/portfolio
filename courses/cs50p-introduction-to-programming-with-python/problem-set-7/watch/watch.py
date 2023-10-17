# Watch on YouTube


import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = ""

    if matches := re.search(r"^(<iframe\ )(.+)?https?://(www\.)?youtube\.com/embed/(.{11})(\")?(.+)?$", s):
        url = matches.group(4)
        
        return f"https://youtu.be/{url}"
    
    else:
        return f"None"


if __name__ == "__main__":
    main()