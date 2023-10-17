def is_pangram(s):
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    check = []

    for letter in s.lower():
        if letter in abc:
            check.append(letter)

    check = list(dict.fromkeys(check))
    check.sort()

    if check == abc:
        return True

    else:
        return False