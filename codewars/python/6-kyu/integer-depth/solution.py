def compute_depth(n):
    numbers = []
    count = 0

    while numbers != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        count += 1
        x = n * count

        for char in str(x):
            if int(char) not in numbers:
                numbers.append(int(char))
        
        numbers = sorted(numbers)

    return count