def array_diff(a, b):
    array = []

    for i in a:
        if i not in b:
            array.append(i)

    return array