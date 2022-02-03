"""EX03: Structured Wordle"""
__author__ = "730320310"


def contains_char(secret: str, used_char: str) -> bool:
    """Function to search guess for characters that are present in secret word and returns True/False."""
    assert len(used_char) == 1
    idx: int = 0
    while idx < len(secret):
        if secret[idx] == used_char:
            return True
        else:
            idx = idx + 1
    return False 
            