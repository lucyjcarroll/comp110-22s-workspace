"""Second Try on Wordle- EX02."""
__author__ = "730320310"

secret_word = str("python")
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

idx = len(secret_word) - 1
emoji_str = ""


i: int = len(guess)  # loop for correct length, wrong guess 

while i != len(secret_word):
    wrong_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
    if len(wrong_guess) == len(secret_word) and wrong_guess != secret_word:
        i = len(secret_word)
    else:
        if wrong_guess == secret_word:
            print("Woo! You got it!")
            exit()
            
# loop for correct length, wrong guess 
while i == len(secret_word) and guess != secret_word:
    print("Not quite. Play again soon!")
    i = i + 1
while i == len(secret_word) and guess == secret_word:
    print(f"{GREEN_BOX}" * len(secret_word))  
    print("Woo! You got it!")
    i = i + 1
