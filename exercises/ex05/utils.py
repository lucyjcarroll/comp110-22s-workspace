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


def concat(a_list: list[int], another_list: list[int]):
    """Function to combine 2 lists to create a new one."""
    merged_list: list[int] = []
    i: int = 0
    while i < len(a_list):
        item: int = a_list[i]
        merged_list.append(item)
        i += 1
    i: int = 0
    while i < len(another_list):
        item: int = another_list[i]
        merged_list.append(item)
        i += 1
    return merged_list


def sub(a_list: list[int], start_idx: int, end_idx: int):
    """Function to return a list with only numbers between the start and end index."""
    new_list: list[int] = []
    i: int = 0
    if start_idx < 0:
        start_idx = 0
    if end_idx > len(a_list):
        end_idx = len(a_list) - 1
    if len(a_list) == 0 or start_idx > len(a_list) or end_idx <= 0:
        return new_list
    while i >= start_idx and i < end_idx:
        new_list.append(a_list[i])  
        i += 1
    return new_list