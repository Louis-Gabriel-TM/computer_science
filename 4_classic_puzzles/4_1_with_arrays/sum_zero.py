"""
Puzzle Wording
==============
Write a function called 'sumZero' which accepts a sorted array of integers.
It should returns the first pair where sum is 0 and 'undefined' if such a pair does not exist.
"""


def naive_sum_zero(arr):
    # Time complexity of 'naiveSumZero': O(n**2)
    # Space compexity of 'naiveSumZero': O(1)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == 0:
                return [arr[i], arr[j]]


def sum_zero(arr):
    # Time complexity of 'refactoredSumZero': O(n)
    # Space compexity of 'refactoredSumZero': O(1)
    left = 0  # pointer from the beginning
    right = len(arr) - 1  # pointer from the end

    while left < right:
        total = arr[left] + arr[right]

        if total == 0:
            return [arr[left], arr[right]]
        elif total > 0:
            right -= 1
        else:
            left += 1


if __name__ == "__main__":
    pass
