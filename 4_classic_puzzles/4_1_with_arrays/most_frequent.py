"""
Puzzle Wording
==============
Find the most frequently occuring item in an item.
If given an empty array, return None.
Else, assume there is a unique value that appears most frequently.
"""


def most_frequent_item_with_counting_dictionary(array):
    max_count = -1
    most_frequent_item = None

    counting_items = dict()
    for item in array:
        if item in counting_items:
            counting_items[item] += 1
        else:
            counting_items[item] = 1

        if counting_items[item] > max_count:
            max_count = counting_items[item]
            most_frequent_item = item

    return most_frequent_item


def most_frequent_item_with_set_and_sorting(array):
    if array:
        items = set(array)
        counting_items = []

        for item in items:
            counting_items.append((item, array.count(item)))

        counting_items.sort(key=lambda x: x[1], reverse=True)

        return (counting_items[0][0])


def most_frequent_item_with_counter(array):
    from collections import Counter

    counting_items = Counter(array)

    max_count = -1
    most_frequent_item = None
    for key, count in counting_items.items():
        if count > max_count:
            max_count = count
            most_frequent_item = key

    return most_frequent_item


if __name__ == "__main__":
    pass
