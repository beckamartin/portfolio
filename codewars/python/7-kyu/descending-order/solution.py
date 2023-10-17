def descending_order(num):
    array = []
    result = ""

    for i in str(num):
        array.append(i)

    array.sort(reverse=True)

    for i in array:
        result += i

    return int(result)