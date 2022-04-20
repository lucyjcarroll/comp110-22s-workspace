"""Tests for linked list utils."""

from exercises.ex10.linked_list import Node, last
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