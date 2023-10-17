# Re-requesting a Vanity Plate


def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    elif s.isalnum() == False:
        return False

    elif s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    for i in range(len(s)):
        if i < (len(s)) / 2:
            if s[i].isdigit() == True:
                return False
        else:
            break

    for i in range(len(s)):
        if s[i].isdigit() == True:
            if s[i] == "0":
                return False
            else:
                break

    for i in range(len(s)):
        if s[i].isdigit() == True:
            if s[-1].isalpha() == True:
                return False
            else:
                break

    return True


if __name__ == "__main__":
    main()
