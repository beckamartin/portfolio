def transpose(matrix):
    new_array = list()

    for i in range(len(matrix[0])):
        new_array.append([])

        for x in matrix:
            new_array[i].append(x[i])

    return new_array