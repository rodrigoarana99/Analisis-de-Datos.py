
def main():
    word = input("Escriba su tweet: ")
    shortened_word = shorten(word)
    print(shortened_word)


def shorten(word):
    vowels = ('aeiouAEIOU')
    for vowel in vowels:
        word = word.replace(vowel, "")
    return word


if __name__ == "__main__":
    main()

