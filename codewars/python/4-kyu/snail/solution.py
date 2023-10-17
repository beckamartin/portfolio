def snail(snail_map):
    arrays = snail_map
    new_array = []

    while arrays:
        for i in range(len(arrays[0])):
            new_array.append(arrays[0][i])
        arrays.remove(arrays[0])

        if not arrays:
            break

        for i in range(len(arrays)):
            new_array.append(arrays[i][-1])
            arrays[i].pop()

        if not arrays:
            break

        for i in range(len(arrays[-1])):
            new_array.append(arrays[-1][-1])
            arrays[-1].pop()
        arrays.remove(arrays[-1])

        if not arrays:
            break

        for i in range(len(arrays)-1, -1, -1):
            new_array.append(arrays[i][0])
            arrays[i].pop(0)
    
    return new_array