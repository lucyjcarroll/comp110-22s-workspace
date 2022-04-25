"""Tests for linked list utils."""

from exercises.ex10.linked_list import Node, last, value_at, max, linkify, scale
import pytest

__author__ = "730320310"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a value error."""
    with pytest.raises(ValueError):
        last(None)
    

def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Raises IndexError if list is empty."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_at_non_empty() -> None:
    """Value at of a non-empty list should return the Node value at the given index."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 1) == 20


def test_max_empty() -> None:
    """Max of an empty list should raise a value error."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """Max of a non empty list- should return the value of the Node with the max value."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30
# works because 30 is last value


def test_max_non_empty2() -> None:
    """Max of a non empty list- should return the value of the Node with the max value."""
    linked_list = Node(30, Node(10, Node(20, None)))
    assert max(linked_list) == 30
    # doesn't work because 30 is not the last value


def test_linkify_empty() -> None:
    """Linkify of empty list should return None."""
    list = [1, 2]
    assert linkify(list) == Node(1, Node(2, None))


def test_linkify_non_empty() -> None:
    """Linkify of a list should return Linked list of nodes with the same values."""


def test_scale_empty() -> None:
    """Scale of an empty linked list should return None."""
    list = None


def test_scale_use() -> None:
    """Scale of linked list should return linkedd list with values muliplied by factor."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert scale(linked_list, 2) == Node(2, Node(4, Node(6, None)))