"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730314357"

from exercises.ex06.dictionaries import invert, favorite_color, count


def test_invert_values() -> None:
    """Invert a dictionary with 1 key and value."""
    my_dictionary: dict[str, str] = {'apple': 'cat'}
    assert invert(my_dictionary) == {'cat': 'apple'}


def test_invert_empty() -> None: 
    """Invert an empty dictionary."""
    my_dictionary: dict[str, str] = {}
    assert invert(my_dictionary) == {}


def test_invert_repeat_keys() -> None:
    """Raise key error from repeated keys."""
    import pytest
    with pytest.raises(KeyError):
        my_dictionary: dict[str, str] = {'hi': 'hello', 'bye': 'hello'}
        invert(my_dictionary)


def test_favorite_colors_dict() -> None: 
    """Return the most popular color."""
    x: dict[str, str] = {'Bob': 'blue', 'Tom': 'Green', 'Billy': 'blue'}
    assert favorite_color(x) == 'blue'


def test_favorite_colors_tie() -> None:
    """Return the first color if there is a tie."""
    x: dict[str, str] = {'Bob': 'blue', 'Tom': 'Green'}
    assert favorite_color(x) == 'blue'


def test_favorite_colors_same() -> None:
    """Return color if everyone has the same."""
    x: dict[str, str] = {'Bob': 'blue', 'Tom': 'blue', 'Jerry': 'blue'}
    assert favorite_color(x) == 'blue'


def test_count_large_list() -> None:
    """Return count of a large list of values."""
    x: list[str] = ['Bob', 'Tom', 'Bob', 'Bob', 'Bob']
    assert count(x) == {'Bob': 4, 'Tom': 1}


def test_count_small_list() -> None: 
    """Return small list count."""
    x: list[str] = ['Bob', 'Tom']
    assert count(x) == {'Bob': 1, 'Tom': 1}


def test_count_empty() -> None:
    """Return an empty dict."""
    x: list[str] = []
    assert count(x) == {}