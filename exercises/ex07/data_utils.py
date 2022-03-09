"""Dictionary related utility functions."""

__author__ = "730320310"

# Define your functions below
from csv import DictReader
from distutils.command.build_scripts import first_line_re


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
    result: dict[str, str] = {}
    
    for column in table: 
        first_values: list[str] = []
        for column in table[N]:
            first_values.append(column[N])
            
    return result 


    return result 