"""
Puzzle Wording
==============
Write a function called 'same' which accept two arrays.
The function should return True if every value in the first array has it's corresponding value squared in the second array, at the same frequency.

Example:
-------
same([1, 2, 3], [4, 1, 9]) --> True
same([1, 2, 3], [1, 9]) --> False
same([1, 2, 1], [4, 4, 1]) --> False (must be same frequency)
"""


def naive_same(array_1, array_2):
    # Time complexity: O(n**2)
    if len(array_1) != len(array_2):
        return False

    for i in range(len(array_1)):
        try:
            correct_index = array_2.index(array_1[i] ** 2)
            # for and index() are like a nested loop
        except ValueError:
            return False

        del(array_2[correct_index])

    return True


def refactored_same(array_1, array_2):
    # Time complexity: O(n)
    if len(array_1) != len(array_2):
        return False

    counter_1 = dict()
    counter_2 = dict()
    for elt in array_1:
        counter_1.setdefault(elt, 0)
        counter_1[elt] += 1
    for elt in array_2:
        counter_2.setdefault(elt, 0)
        counter_2[elt] += 1

    for key in counter_1:
        if key**2 not in counter_2:
            return False
        if counter_2[key**2] != counter_1[key]:
            return False
    # Successive loops are often better than a nested loop

    return True


def same_with_counters(array_1, array_2):
    from collections import Counter

    counter_1 = Counter((n * n for n in array_1))
    counter_2 = Counter(array_2)
    return counter_1 == counter_2


if __name__ == "__main__":
    pass
