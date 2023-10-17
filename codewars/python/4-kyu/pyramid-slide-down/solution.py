def longest_slide_down(pyramid):
    pyramid = list(reversed(pyramid))

    for i in range(1, len(pyramid)):
        for j in range(len(pyramid[i])):
            pyramid[i][j] += max(pyramid[i - 1][j], pyramid[i - 1][j + 1])

    return pyramid[-1][0]