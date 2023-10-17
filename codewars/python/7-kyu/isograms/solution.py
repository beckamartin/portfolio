def is_isogram(string):
    from collections import Counter

    ctn = Counter()

    if string == "":
        return True
    
    else:
        for char in string.lower():
            ctn[char] += 1

            if ctn[char] > 1:
                return False

        if ctn[char] <= 1 or ctn[char] == None:
            return True