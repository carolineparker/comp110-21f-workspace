"""Unit tests for list utility functions."""


__author__ = "730214357"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_multiple_numbers() -> None:
    """Find evens in list of multiple numbers."""
    x: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(x) == [2, 4, 6]


def test_only_evens_negatives() -> None:
    """Find evens in list of negative numbers."""
    x: list[int] = [-1, -2, -3, -4]
    assert only_evens(x) == [-2, -4]


def test_only_evens_empty() -> None:
    """Extract evens from an empty list."""
    x: list[int] = []
    assert only_evens(x) == []


def test_sub_multiple_numbers() -> None:
    """Sub into list of multiple numbers."""
    x: list[int] = [1, 2, 3, 4]
    y: int = 1
    z: int = 3
    assert sub(x, y, z) == [2, 3]


def test_sub_negative_numbers() -> None:
    """Sub into a list of negative numbers."""
    x: list[int] = [-1, -2, -3, -4]
    y: int = 1
    z: int = 3
    assert sub(x, y, z) == [-2, -3]


def test_sub_empty() -> None:
    """Sub into an empty list."""
    x: list[int] = []
    y: int = 1
    z: int = 2
    assert sub(x, y, z) == []


def test_concat_two_lists_equal_numbers() -> None:
    """Concatenate two lists of equal numbers."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]


def test_concat_one_empty() -> None:
    """Concatenate with one empty list."""
    x: list[int] = []
    y: list[int] = [1]
    assert concat(x, y) == [1]


def test_concat_both_empty() -> None:
    """Concatenate two empty lists."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []