def count_bits(n):
    binary = format(n, "b")

    count = 0

    for i in binary:
        if i == "1":
            count += 1
            
    return count