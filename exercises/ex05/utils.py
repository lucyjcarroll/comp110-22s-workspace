"""Exercise 05: Practicing List Utility Functions."""
__author__ = "730320310"


def only_evens(numbers: list[int]):
    """Function to return only even numbers in a list."""
    i: int = 0
    returned_list = []
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            returned_list.append(numbers[i])
            i += 1
        elif numbers[i] % 2 != 0:
            i += 1
    return returned_list
            

def sub(a_list: list[int], start_idx: int, end_idx: int):
    """Function to return a list with only numbers between the start and end index."""
    i: int = 0
    resulting_list = []
    if len(a_list) == 0 or start_idx > len(a_list) or end_idx <= 0:
        return resulting_list

    return resulting_list


def concat(a_list: list[int], another_list: list[int]) -> str:
    """Function to combine 2 lists to create a new one."""
    empty_string = ""
    return f"{empty_string} {a_list} {another_list}"
