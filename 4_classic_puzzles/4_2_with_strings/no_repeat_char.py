"""
Puzzle Wording
==============
Write a function that takes a string and returns the first character that does not appear twice or more.
If there is no non-repeating character, return None.
"""


def non_repeating_character(string):
    count = dict()
    parsed_char = []  # assuming the dictionary is non ordered

    for c in string:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
            parsed_char.append(c)

    for c in parsed_char:
        if count[c] == 1:
            return c


def non_repeating_character_with_counter(string):
    from collections import Counter

    count = Counter(string)
    for c in string:
        if count[c] == 1:
            return c


if __name__ == "__main__":
    pass
