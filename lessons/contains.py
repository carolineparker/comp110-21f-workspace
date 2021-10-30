"""Example of writing a function to process a list"""


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True iff needle is found in haystack, False otherwise"""
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1

    return False
