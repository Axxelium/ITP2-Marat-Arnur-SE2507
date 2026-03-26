"""
Tests for Assignment 4: Algorithms — Sorting and Searching
"""
import pytest
from algorithms import bubble_sort, merge_sort, binary_search, linear_search


class TestBubbleSort:
    def test_sorts_integers(self):
        lst = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(lst)
        assert lst == sorted([64, 34, 25, 12, 22, 11, 90])

    def test_already_sorted(self):
        lst = [1, 2, 3, 4, 5]
        bubble_sort(lst)
        assert lst == [1, 2, 3, 4, 5]

    def test_single_element(self):
        lst = [42]
        bubble_sort(lst)
        assert lst == [42]

    def test_empty_list(self):
        lst = []
        bubble_sort(lst)
        assert lst == []

    def test_sorts_in_place(self):
        lst = [3, 1, 2]
        ref = lst
        bubble_sort(lst)
        assert lst is ref  # same object


class TestMergeSort:
    def test_sorts_integers(self):
        lst = [38, 27, 43, 3, 9, 82, 10]
        assert merge_sort(lst) == sorted(lst)

    def test_does_not_mutate_input(self):
        lst = [5, 3, 1]
        original = lst[:]
        merge_sort(lst)
        assert lst == original

    def test_empty(self):
        assert merge_sort([]) == []

    def test_single_element(self):
        assert merge_sort([7]) == [7]

    def test_duplicates(self):
        lst = [3, 1, 4, 1, 5, 9, 2, 6]
        assert merge_sort(lst) == sorted(lst)


class TestBinarySearch:
    def test_found(self):
        lst = [1, 3, 5, 7, 9, 11, 13]
        assert binary_search(lst, 7) == 3

    def test_not_found(self):
        lst = [1, 3, 5, 7, 9]
        assert binary_search(lst, 6) == -1

    def test_first_element(self):
        lst = [2, 4, 6, 8]
        assert binary_search(lst, 2) == 0

    def test_last_element(self):
        lst = [2, 4, 6, 8]
        assert binary_search(lst, 8) == 3

    def test_empty_list(self):
        assert binary_search([], 1) == -1


class TestLinearSearch:
    def test_found(self):
        lst = [4, 2, 7, 1, 9, 3]
        assert linear_search(lst, 9) == 4

    def test_not_found(self):
        lst = [4, 2, 7, 1, 9, 3]
        assert linear_search(lst, 5) == -1

    def test_first_occurrence(self):
        lst = [1, 2, 3, 2, 1]
        assert linear_search(lst, 2) == 1

    def test_empty_list(self):
        assert linear_search([], 1) == -1
