"""
Puzzle Wording
==============
Write a function that returns True if a string is a palindrome (string equal to his reversed string) and False in the other case.
If a string contains multiple words, spaces, digits and punctuation must be removed before testing.
"""


def keep_letters(string):
    letters = []

    for c in string:
        if c.isalpha():
            letters.append(c.casefold())

    return "".join(letters)


def is_palindrome_comparing_symmetric_characters(string):
    string = keep_letters(string)

    return all(string[i] == string[-1 - i] for i in range(len(string) // 2 + 1))


def is_palindrome_with_reverse(string):
    string = keep_letters(string)

    letters = list(string)
    letters.reverse()

    return string == "".join(letters)


def is_palindrome_with_slicing(string):
    string = keep_letters(string)

    return string == string[::-1]


if __name__ == "__main__":
    pass
