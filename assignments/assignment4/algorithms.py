"""
Assignment 4: Algorithms — Sorting and Searching
ITP2 | SE-2057 | Arnur & Marat
"""
from typing import List, TypeVar

T = TypeVar("T")


def bubble_sort(lst: List) -> None:
    """Sort a list in-place using bubble sort (ascending order).

    Time complexity: O(n²) average and worst case.
    """
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break  # already sorted


def merge_sort(lst: List) -> List:
    """Return a new sorted list using merge sort (ascending order).

    Time complexity: O(n log n).
    """
    if len(lst) <= 1:
        return list(lst)

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return _merge(left, right)


def _merge(left: List, right: List) -> List:
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def binary_search(lst: List, target) -> int:
    """Search a sorted list for target using binary search.

    Returns:
        Index of target in lst, or -1 if not found.

    Time complexity: O(log n).
    """
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def linear_search(lst: List, target) -> int:
    """Search a list for target using linear search.

    Returns:
        Index of the first occurrence of target, or -1 if not found.

    Time complexity: O(n).
    """
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1


def main():
    print("=== Bubble Sort ===")
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Before: {data}")
    bubble_sort(data)
    print(f"After : {data}")

    print("\n=== Merge Sort ===")
    data2 = [38, 27, 43, 3, 9, 82, 10]
    print(f"Before: {data2}")
    sorted_data = merge_sort(data2)
    print(f"After : {sorted_data}")

    print("\n=== Binary Search ===")
    sorted_list = [1, 3, 5, 7, 9, 11, 13]
    for target in [7, 6]:
        idx = binary_search(sorted_list, target)
        print(f"  binary_search({sorted_list}, {target}) = {idx}")

    print("\n=== Linear Search ===")
    unsorted_list = [4, 2, 7, 1, 9, 3]
    for target in [9, 5]:
        idx = linear_search(unsorted_list, target)
        print(f"  linear_search({unsorted_list}, {target}) = {idx}")


if __name__ == "__main__":
    main()
