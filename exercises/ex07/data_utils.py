"""Utility functions."""

__author__ = "123456789"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform row orientated table to column oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def select(data_dictionary: dict[str, list[str]], data_list: list[str]) -> dict[str, list[str]]:
    """Select a value from a list and add it to a dictionary."""
    result_dict: dict[str, list[str]] = {}
    for value in data_list:
        result_dict[value] = data_dictionary[value]
    
    return result_dict


def head(data_dictionary: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Return a certain number of key value pairs."""
    result_dict: dict[str, list[str]] = {}
    for key in data_dictionary:
        empty_list: list[str] = []
        i: int = 0
        if rows > len(data_dictionary):
            return data_dictionary
        while i < rows: 
            empty_list.append(data_dictionary[key][i])
            i += 1
        result_dict[key] = empty_list
            
    return result_dict


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two dictionaries."""
    result_dict: dict[str, list[str]] = {}
    for key in x:
        result_dict[key] = x[key]
    for key in y:
        if key in result_dict:
            result_dict[key] += y[key]
        else:
            result_dict[key] = y[key]

    return result_dict


def count(data_list: list[str]) -> dict[str, int]:
    """Count occurences of strings in a list."""
    result_dict: dict[str, int] = {}
    for key in data_list:
        if key in result_dict:
            result_dict[key] += 1
        else:
            result_dict[key] = 1

    return result_dict
