"""EX03: Structured Wordle"""
__author__ = "730320310"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Function to search guess for characters that are 
    present in secret word and returns True/False."""
    assert len(char) == 1
    idx: int = 0
    while idx < len(word):
        if word[idx] == char:
            return True
        else:
            idx = idx + 1
    return False 


def emojified(guess: str, secret: str) -> str: 
    """Function to print emojis(white, yellow, green boxes)to 
    signal if characters match/do not match/are contained in the word."""
    assert len(guess) == len(secret)
    idx: int = 0
    emoji: str = ""
    while idx < len(secret):
        if secret[idx] == guess[idx]:
            emoji = emoji + f"{GREEN_BOX}"
            idx = idx + 1
        elif contains_char(secret, guess[idx]):
            emoji = emoji + f"{YELLOW_BOX}"
            idx = idx + 1
        elif contains_char is not True:
            emoji = emoji + f"{WHITE_BOX}"
            idx = idx + 1
    return emoji 


def input_guess(exp_length: int) -> str:
    """Function for prompting a guess of certain length
     and continues until expected word length is reached."""

    guess: str = input(f"Enter a {exp_length} character word: ")
    if len(guess) == exp_length:
        return guess 
    while len(guess) != exp_length:
        input(f"That wasn't {exp_length} chars! Try again: ")
        if len(guess) == exp_length:
            exp_length = len(guess) 
    return guess
    
