"""List utility functions part 2."""

__author__ = "730314357"


def only_evens(x: list[int]) -> list[int]:
    """Extract even numbers."""
    i = 0
    evens = []
    while i < len(x):
        if x[i] % 2 == 0:
            evens.append(x[i])
        i += 1
    return(evens)


def sub(x: list[int], y: int, z: int) -> list[int]:
    """Sub an integer into a list."""
    i = 0
    a_list = []
    while i < len(x):
        if i >= y and i < z:
            a_list.append(x[i])
        i += 1
    return a_list


def concat(x: list[int], y: list[int]) -> list[int]:
    """Concatenation of two lists."""
    i: int = 0
    j: int = 0
    this_list: list[int] = []
    while i < len(x):
        this_list.append(x[i])
        i += 1
    while j < len(y):
        this_list.append(y[j])
        j += 1
    return this_list





    
