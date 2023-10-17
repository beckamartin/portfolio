# Response Validation


import validators


def main():
    print(valid(input("What's your email address? ")))


def valid(s):
    if not validators.email(s):
        return f"Invalid"
        
    else:
        return f"Valid"


if __name__ == "__main__":
    main()
