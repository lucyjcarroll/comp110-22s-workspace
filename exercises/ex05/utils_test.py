"""Exercise 05: Practicing testing on list utility functions."""
__author__ = "730320310"
from exercises.ex05.utils import only_evens


def test_only_evens_mix() -> None:
    numbers: list[int] = [3, 1, 2]
    assert only_evens(numbers) == [2]


def test_only_evens_odds() -> None:
    numbers: list[int] = [1, 5, 3]
    assert only_evens(numbers) == []


def test_only_evens_even() -> None:
    numbers: list[int] = [4, 4, 4]
    assert only_evens(numbers) == [4, 4, 4]

def test_sub_
