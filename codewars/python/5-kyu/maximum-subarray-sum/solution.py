def max_sequence(arr):
    if len(arr) == 0 or arr[0] == 0:
        return 0

    count_n = 0

    for n in arr:
        count_n += 1
        
        if n <= 0:
            if count_n == len(arr):
                return 0
            
        elif n > 0:
            break

# Kadane's Algorithm

    current_sum = 0
    max = 0
    
    for i in range(0, len(arr)):
        current_sum = current_sum + arr[i]

        if max < current_sum:
            max = current_sum

        elif current_sum < 0:
            current_sum = 0

    return(max)