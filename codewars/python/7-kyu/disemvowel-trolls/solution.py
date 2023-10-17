def disemvowel(string_):
    
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    string2 = ""

    while True:
        for i in string_:
            if i in vowels:
                string2 = string2 + ""
            else:
                string2 = string2 + i  
        return string2