"""Practice with dictionaries."""

__author__ = "730314357"


def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary."""
    inverted_dict: dict[str, str] = {}
    for key in my_dictionary:
        if my_dictionary[key] in inverted_dict:
            raise KeyError("Key already in dictionary")
        value: str = my_dictionary[key]
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(x: dict[str, str]) -> str:
    """Return most common color."""
    color_dict: dict[str, int] = {}
    most: str = ""
    max: int = 0
    for key in x:
        if x[key] in color_dict:
            color_dict[x[key]] += 1
        else: 
            color_dict[x[key]] = 1
    for key in color_dict:
        count: int = color_dict[key]
        if count > max: 
            max = count
            most = key
    return most


def count(x: list[str]) -> dict[str, int]:
    """Count occurences of each value."""
    empty_dict: dict[str, int] = {}
    i: int = 0
    while i < len(x):
        if x[i] in empty_dict:
            empty_dict[x[i]] += 1
        else: 
            empty_dict[x[i]] = 1
        i += 1
    return empty_dict