import string


def pig_it(text):
    words = text.split()
    new_words = ""

    for word in words:
        if word in string.punctuation:
            new_words += word + " "
        else:
            new_words += word[1:] + word[0] + "ay "

    return new_words.rstrip()