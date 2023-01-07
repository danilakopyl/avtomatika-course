import string


def is_palindrome(words):
    words = words.translate(str.maketrans('', '', string.punctuation)).lower()
    return words == words[::-1]


if __name__ == '__main__':
    print(is_palindrome('1спел:;;;:!?,. ЛепС1'))
