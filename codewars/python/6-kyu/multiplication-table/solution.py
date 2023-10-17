def multiplication_table(size):
    array = []

    for i in range(1, size + 1):
        row = []
        
        for j in range(1, size + 1):
            row.append(i * j)

        array.append(row)

    return array