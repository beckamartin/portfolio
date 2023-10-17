def move_zeros(lst):
    array = []
    
    zero_array = []

    for i in lst:
        if i != 0:
            array.append(i)
        
        else:
            zero_array.append(i)
    
    return array + zero_array