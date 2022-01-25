"Second Try on Wordle- EX02"
__author__ = "730320310"

secret_word = str("python")
guess: str = input("What is your 6-letter guess? ")
i: int = len(secret_word)

while i < len(guess):
    print(f"That was not {i} letters! Try again: ")
    i = i + 1

while i > len(guess):
    print(f"That was not {i} letters! Try again: ")
    
while i == len(guess) and guess == secret_word:
    print("Woo! You got it!")