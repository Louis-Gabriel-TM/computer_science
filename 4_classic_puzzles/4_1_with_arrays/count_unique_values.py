"""
Puzzle Wording
==============
Write a function called 'count_unique_values' which accepts a sorted array and counts the unique values in the array.
There can be negative numbers in the array, but it will always be sorted.
"""


def count_unique_values_with_pointers(arr):
    # Time complexity of 'count_unique_values_with_pointers': O(n)
    # Space compexity of 'count_unique_values_with_pointers': O(1)
    if len(arr) > 1:
        left = 0  # pointer from the beginning
        left_scout = 1  # pointer looking for the next different value

        while left_scout < len(arr):
            if arr[left_scout] == arr[left]:
                left_scout += 1
            else:
                left += 1
                arr[left] = arr[left_scout]
                left_scout += 1

        return left + 1

    return len(arr)


def count_unique_values_with_set(arr):
    return len(set(arr))
