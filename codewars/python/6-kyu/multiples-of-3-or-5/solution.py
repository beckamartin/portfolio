def solution(number):
    number_list = []

    if number <= 0:
        return 0
    
    else:
        number = number - 1

        while True:
            number_list.append(number)
        
            number = number - 1
        
            if number == 0:
                break
        
        number_list.sort()
        
        sum = 0

        for i in number_list:
            if i % 3 == 0 or i % 5 == 0:

                if i % 3 == 0 and i % 5 == 0:
                    sum = sum + i
        
                elif i % 3 == 0 and i % 5 != 0:
                    sum = sum + i

                elif i % 3 != 0 and i % 5 == 0:
                    sum = sum + i 
                
        return sum