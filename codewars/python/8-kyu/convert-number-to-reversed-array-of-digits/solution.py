def digitize(n):
    array = []

    for i in str(n):
        array.append(int(i))

    return array[::-1]