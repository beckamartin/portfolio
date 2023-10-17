def spin_words(sentence):
    words = sentence.split(" ")
    array = []    

    for word in words:
        if len(word) < 5:
            array.append(word)
        
        elif len(word) >= 5:
            word = word[::-1]
            array.append(word)
    
    array = " ".join(array)

    return array