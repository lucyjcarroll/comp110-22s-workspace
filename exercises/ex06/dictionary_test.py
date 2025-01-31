"""Unit Tests for Dictionaries: Exercise 6."""
__author__ = "730320310"

from exercises.ex06.dictionary import invert, favorite_color, count 


def test_invert_use_1() -> None:
    """Use case 1 for invert function."""
    assert invert({'cat': 'apple'}) == {'apple': 'cat'}


def test_invert_use_2() -> None:
    """Use case 2 for invert function."""
    assert invert({'hello': 'world', 'me': 'you'}) == {'world': 'hello', 'you': 'me'}


def test_invert_edge() -> None:
    """Edge case for invert function."""
    assert invert({}) == {}


def test_favorite_color_use_1() -> None:
    """Use case 1 for favorite color function."""
    assert favorite_color({'Lucy': 'blue', 'Lila': 'blue', 'Henry': 'green'}) == "blue"


def test_favorite_color_use_2() -> None:
    """Use case 2 for favorite color function."""
    assert favorite_color({'Lucy': 'green', 'Lila': 'green', 'Henry': 'green', 'Holden': 'blue'}) == 'green'


def test_favorite_color_edge() -> None:
    """Edge case for favorite color function."""
    assert favorite_color({}) == ''


def test_count_use_1() -> None:
    """Use case 1 for count function."""
    assert count(['2', '2', '1']) == {'2': 2, '1': 1}


def test_count_use_2() -> None:
    """Use case 2 for count function."""
    assert count(['3', '3', '2', '1', '3', '2']) == {'3': 3, '2': 2, '1': 1}


def test_count_edge() -> None:
    """Edge case for count function."""
    assert count([]) == {}