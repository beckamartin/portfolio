def find_uniq(arr):
    from collections import Counter

    x = Counter(arr)

    for n in x:
        if x[n] == 1:
            return n