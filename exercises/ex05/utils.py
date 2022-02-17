"""Exercise 05: Practicing List Utility Functions."""
__author__ = "730320310"


def only_evens(xs: list[int]) -> int:
    """Function to return only even numbers in a list."""
    for item in xs:
        if item == 0:
            return item
            item += 2


def sub(a_list: list[int], start_idx: int, end_idx: int) -> int:
    """Function to return a list with only numbers between the start and end index."""
    i: int = 0
    while i < end_idx and i > start_idx:
        item: int = a_list[i]
        return item
        i += 1

def concat(a_list: list[int], another_list: list[int]) -> str:
    """Function to combine 2 lists to create a new one."""
    empty_string = ""
    return f"{empty_string} {a_list} {another_list}"

