"""
Puzzle Wording
==============
Given two arrays with no duplicates, write a function that returns True if on array is a rotation of the other: same sequence in the same order but starting at a different index.
"""


def is_rotation_with_slices(array_1, array_2):
    if set(array_1) == set(array_2):

        for i, elt in enumerate(array_2):
            if elt == array_1[0]:

                if array_1 == array_2[i:] + array_2[:i]:
                    return True
                else:
                    return False

    return False


def is_rotation_with_modulo(array_1, array_2):
    if set(array_1) == set(array_2):

        for i, elt in enumerate(array_2):
            if elt == array_1[0]:

                for k in range(1, len(array_1)):
                    if array_1[k] != array_2[(i + k) % len(array_1)]:
                        return False

                return True

    return False


if __name__ == "__main__":
    pass
