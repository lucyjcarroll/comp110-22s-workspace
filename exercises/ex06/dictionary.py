"""Exercise 6: Practicing with Dictionaries."""
__author__ = "730320310"


def invert(a_dictionary):
    resulting_dictionary = {}
    for key, value in a_dictionary:
        if value not in a_dictionary:
            resulting_dictionary[value] = []
        resulting_dictionary[value].append(key)
        return resulting_dictionary