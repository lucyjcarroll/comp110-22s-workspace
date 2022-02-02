"""EX03: Structured Wordle"""
__author__ = "730320310"

from asyncio import streams


def contains_char(word_choice: str, char_search: str) -> bool:
    """Function to search word choice for characters that are present in secret word"""
    assert len(char_search) == 1

    