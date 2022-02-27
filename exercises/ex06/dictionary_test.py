"""Unit Tests for Dictionaries: Exercise 6."""
__author__ = "730320310"

from exercises.ex06.dictionary import invert


def test_invert_use_1() -> None:
    """Use case 1 for a dictionary function."""
    assert invert({'cat': 'apple'}) == {'apple': 'cat'}
