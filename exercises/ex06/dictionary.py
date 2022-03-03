"""Exercise 6: Practicing with Dictionaries."""
__author__ = "730320310"


def invert(a_dictionary: dict[str, str]) -> dict[str, str]: 
    """Function to invert a dictionary's keys and values."""
    if a_dictionary == {}:
        return {}
    inverse_dict = {a_dictionary[key]: key for key in a_dictionary}
    return inverse_dict


def favorite_color(a_dict: dict[str, str]) -> str: 
    """Function to find the most common color value in a dictionary."""
    colors: list[str] = []
    for name in a_dict:
        if a_dict[name] == a_dict[name]:
            colors.append(a_dict[name])
            fav_color = "".join(colors)
            return fav_color

    if a_dict == {}:
        return ""


def count(values: list[str]) -> dict[str, int]:
    """Function to return a dictionary of counts of each of the items in input list."""
    result: dict[str, int]
    i: int = 0
    for value in values: