"Second Try on Wordle- EX02"
__author__ = "730320310"

secret_word = str("python")
guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = len(guess)
while i == len(secret_word) and guess != secret_word:
    print("Not quite. Play again soon!")
    i = i + 1

# below loop is for guesses with incorrect length
i: int = len(guess)
while i != len(secret_word):
    wrong_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
    if len(wrong_guess) == len(secret_word) and wrong_guess != secret_word:
        print("Not quite. Play again soon!")
        i = len(secret_word)

# below is loop for correct guesses
i: int = len(guess)
while i == len(secret_word) and guess == secret_word:
    print(f"{GREEN_BOX}" * len(guess))  
    print("Woo! You got it!")
    guess = "hello"  # this is a word that would never be chosen as a secret word because it's not 6 letters
    i != len(secret_word)