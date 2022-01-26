"Second Try on Wordle- EX02"
__author__ = "730320310"

secret_word = str("python")
guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
    
# below is loop for too-long guesses
i: int = len(secret_word)  
while i < len(guess):
    next_guess: str = input(f"That was not {len(secret_word)} letters! Try again: ") 
    i = i + len(secret_word)

# below is loop for too-short guesses 
i: int = len(secret_word)
while i > len(guess):
    next_guess: str = input(f"That was not {len(secret_word)} letters! Try again: ") 
    print(f"That was not {i} letters! Try again: ")
    i = i - len(secret_word)

# below is loop for incorrect guesses with correct length 
i: int = len(secret_word)
while i == len(guess) and guess != secret_word:
    print("Not quite. Play again soon!")
    i = i + 1

# below is loop for correct guesses
i: int = len(secret_word)
while i == len(guess) and guess == secret_word:
    print(f"{GREEN_BOX}" * len(secret_word))  
    print("Woo! You got it!")
    guess = "hello"  # this is a word that would never be chosen as a secret word because it's not 6 letters
    i != len(secret_word)