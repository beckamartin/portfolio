def productFib(prod):
    a, b, c = 0, 1, 1

    while True:

        if prod == a * b:

            return [a, b, True]

        elif prod > a * b and prod < b * c:

            return [b, c, False]

        a, b, c = b, a + b, b + a + b