"""Dictionary related utility functions."""

__author__ = "730320310"

# Define your functions below
from csv import DictReader


def read_csv_rows(file_name: str) -> list[dict[str, str]]: 
    """Read the wrows of  a CSV into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(file_name, "r", encoding="utf8")

    # Prepare to reach the data file as a CSV rather than just strings 
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    # column reps key in the following loop
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produces a column-based table with the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table: 
        first_values: list[str] = []
        i: int = 0
        if N >= len(table[column]):
            first_values = table[column]
        while i < N:
            first_values.append(table[column][i])
            i += 1
        result[column] = first_values
    return result 
      
    
def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only specific columns from the original table."""
    result: dict[str, list[str]] = {}
    for column in names:
        result[column] = table[column]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-vased table that combines two column-based tables."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            i: int = 0
            while i < len(table_2[column]):
                result[column].append(table_2[column][i])
                i = i + 1
        else:
            result[column] = table_2[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Produces a dictionary of with counts (frequency) of each unique item in a list."""
    result: dict[str, int] = {}
    for value in values:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result