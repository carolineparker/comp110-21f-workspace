"""List utility functions."""

__author__ = "730314357"


def all(x: list[int], y: int) -> bool: 
    """Return True if input matches list."""
    i: int = 0
    length = len(x)
    counter: int = 0
    if length == 0:
        return False
    while i < length:
        item: int = x[i]
        i += 1
        if y != item:
            counter += 1
    if counter > 0:
        return False
    else:
        return True
            
    
def is_equal(x: list[int], y: list[int]) -> bool:
    """Match list values."""
    i: int = 0
    if len(x) != len(y):
        return False
    while i < len(x):
        item_x: int = x[i]
        item_y: int = y[i]
        i += 1
        if item_x != item_y:
            return False
    return True


def max(x: list[int]) -> int:
    """Identify largest value."""
    i: int = 0
    item: int = x[0]
    while i < len(x):
        item_2: int = x[i]
        i += 1
        if item_2 > item:
            item = item_2
    return item