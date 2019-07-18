import random


def binary_search(ordered_list, item_to_find):
    min_index = 0
    max_index = len(ordered_list) - 1

    while min_index <= max_index:
        med_index = (min_index + max_index) // 2
        med_value = ordered_list[med_index]

        if med_value == item_to_find:
            return med_index
        elif med_value > item_to_find:
            max_index = med_index - 1
        else:
            min_index = med_index + 1


if __name__ == '__main__':
    # Trying on a sorted list of n random numbers in [0, 20]
    # Searching a random value in [0, 20]

    n = 10
    array = [random.randint(0, 20) for _ in range(n)]
    array.sort()

    print(array)

    to_find = random.randint(0, 20)

    print(f"Number to find: {to_find}")

    print(f"{to_find} has been found at index {binary_search(array, to_find)}")
