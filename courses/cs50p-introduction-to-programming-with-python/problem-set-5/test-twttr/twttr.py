# Testing my twttr


def main():
    word = input("Input: ")

    ans = shorten(word)

    print("Output: " + ans)


def shorten(word):
    vowels = "aeiouAEIOU"

    short = ""

    for i in word:
        if i not in vowels:
            short = short + i

    return f"{short}"


if __name__ == "__main__":
    main()