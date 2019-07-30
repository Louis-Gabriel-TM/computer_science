"""
Puzzle Wording
==============
Write a function that takes two strings and returns True if they are "one away" from each other, i.e. if a single operation (changing a character, deleting a character or adding a character) will change one to the other.
"""


def is_one_away(s1, s2):
    # case 1: one string too long for the other
    if abs(len(s2) - len(s1)) > 1:
        return False

    # case 2: strings have the same length
    elif len(s2) == len(s1):
        diff = 0

        for i in range(len(s1)):
            if s2[i] != s1[i]:
                diff += 1

        return diff < 2

    # case 3: one string has one more character than the other
    else:
        if len(s2) > len(s1):
            s1, s2 = s2, s1  # s1 is now the longest string

        for i in range(len(s2)):
            if s2[i] != s1[i]:
                # s2 equals s1 without this different char ?
                return s2 == s1[:i] + s1[i+1:]

        return True


if __name__ == "__main__":
    pass
