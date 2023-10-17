def hamming(a,b):
    result = 0

    for pos, char in enumerate(a):
        if char not in b[pos]:
            result += 1

    return result
