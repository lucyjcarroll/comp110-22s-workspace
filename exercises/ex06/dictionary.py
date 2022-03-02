"""Exercise 6: Practicing with Dictionaries."""
__author__ = "730320310"


def invert(a_dictionary: dict[str, str]) -> dict[str, str]: 
    inverse_dict = {a_dictionary[key]: key for key in a_dictionary}
    return inverse_dict


def favorite_color(a_dict: dict[str, str]) -> str: 
    colors = []
    for color in a_dict:
        if color in a_dict:
            colors.append(color)
    for favorite in colors:
        if favorite in colors:
            return favorite_color(colors.count(favorite))


def count(a_list: list[str]) -> dict[str, int]: