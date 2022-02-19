"""Exercise 05: Practicing testing on list utility functions."""
__author__ = "730320310"
from exercises.ex05.utils import only_evens


def test_only_evens_mix() -> None:
    xs: list[int] = [3, 1, 2]
    assert only_evens(xs) == [2]


def test_only_evens_odds() -> None:
    xs: list[int] = [1, 5, 3]
    assert only_evens(xs) == []


def test_only_evens_even() -> None:
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]
