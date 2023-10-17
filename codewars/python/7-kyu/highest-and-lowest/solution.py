def high_and_low(numbers):
    numbers = numbers.split(" ")

    return max(numbers, key=int) + " " + min(numbers, key=int)