def generate_hashtag(s):
    array = s.split(" ")
    x = "#"

    for word in array:
        x = x + word.capitalize()
    
    if len(x) >= 140 or len(x) == 1:
        return False

    else: return x