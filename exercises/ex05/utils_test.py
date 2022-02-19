"""Exercise 05: Practicing testing on list utility functions."""
__author__ = "730320310"
from exercises.ex05.utils import only_evens, concat


def test_only_evens_mix() -> None:
    numbers: list[int] = [3, 1, 2]
    assert only_evens(numbers) == [2]


def test_only_evens_odds() -> None:
    numbers: list[int] = [1, 5, 3]
    assert only_evens(numbers) == []


def test_only_evens_even() -> None:
    numbers: list[int] = [4, 4, 4]
    assert only_evens(numbers) == [4, 4, 4]


def test_concat_2_full_lists() -> None:
    a_list: list[int] = [2, 2, 2]
    another_list: list[int] = [1, 1, 1]
    assert concat(a_list, another_list) == [2, 2, 2, 1, 1, 1]


def test_concat_2_empty_lists() -> None:
    a_list: list[int] = []
    another_list: list[int] = []
    assert concat(a_list, another_list) == []


def test_concat_1_empty_list() -> None:
    a_list: list[int] = []
    another_list: list[int] = [47, 5, 6]
    assert concat(a_list, another_list) == [47, 5, 6]
