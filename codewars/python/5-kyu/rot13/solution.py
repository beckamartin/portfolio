def rot13(message):
    rot13 = {"A": "N", "B": "O", "C": "P", "D": "Q", "E": "R", "F": "S", "G": "T", "H": "U", "I": "V", "J": "W", "K": "X", "L": "Y", "M": "Z",
         "a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z"}
    new_message = ""

    for char in message:
        for key, value in rot13.items():
            if char == value:
                new_message += key
                break
            elif char == key:
                new_message += value
                break
        else: new_message += char
    return new_message