"""Exercise 05: Practicing List Utility Functions."""
__author__ = "730320310"


def only_evens(xs: list[int]):
    """Function to return only even numbers in a list."""
    i: int = 0
    returned_list = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            returned_list.append(xs[i])
            i += 1
        elif xs[i] % 2 != 0:
            i += 1
    return returned_list
            

def sub(a_list: list[int], start_idx: int, end_idx: int):
    """Function to return a list with only numbers between the start and end index."""
    i: int = 0
    while i < end_idx and i > start_idx:
        return a_list[i]
        i += 1


def concat(a_list: list[int], another_list: list[int]) -> str:
    """Function to combine 2 lists to create a new one."""
    empty_string = ""
    return f"{empty_string} {a_list} {another_list}"
