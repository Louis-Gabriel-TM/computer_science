"""
Puzzle Wording
==============
Find the common elements (as a sorted array) between two sorted arrays of integers.
"""


def common_elements_with_index_pointers(array_1, array_2):
    # Easy to implement in another langage.
    # The fact that the arrays are sorted is important here.
    common_elts = []

    pointer_1 = pointer_2 = 0

    while pointer_1 < len(array_1) and pointer_2 < len(array_2):

        if array_1[pointer_1] == array_2[pointer_2]:
            common_elts.append(array_1[pointer_1])
            pointer_1 += 1
            pointer_2 += 1
        elif array_1[pointer_1] < array_2[pointer_2]:
            pointer_1 += 1
        else:
            pointer_2 += 1

    return common_elts


def common_elements_with_in(array_1, array_2):
    # Easy to adapt if the arrays are not sorted.
    common_elts = []

    for elt in array_1:
        if elt in array_2:
            common_elts.append(elt)

    return common_elts


def common_elements_with_sets(array_1, array_2):
    # A more "symetric" solution.
    # The fact that the two arrays are sorted is not used.
    if array_1 and array_2:
        elts_of_array_1 = set(array_1)
        elts_of_array_2 = set(array_2)

        common_elts = elts_of_array_1 & elts_of_array_2

        return sorted(list(common_elts))

    return []


if __name__ == "__main__":
    pass
