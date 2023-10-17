def wave(people):
    array = []
    
    if len(people) == 0:
        return []
    
    else:
        for n, letter in enumerate(people):
            if letter == " ":
                continue
                
            else:
                array.append(people[:n] + people[n].upper() + people[n+1:])

        return array