def shortcut(s):
    x = ""

    for char in s:
        if char not in "aeiou":
            x = x + char

    return x