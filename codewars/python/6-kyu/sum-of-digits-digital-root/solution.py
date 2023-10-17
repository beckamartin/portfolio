def digital_root(n):

    sum = 0

    while n > 9:
        for i in str(n):
            sum += int(i)
        
        n = sum
        
        sum = 0

    if n < 10:
        return(n)