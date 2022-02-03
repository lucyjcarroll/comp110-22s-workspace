"""Second Try on Wordle- EX02."""
__author__ = "730320310"

secret = str("python")
guess: str = input(f"What is your {len(secret)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess_len: int = len(guess)
idx = len(secret) - len(guess)
emoji = ""
used_char: bool = False 
alt_idx = 0

while idx < len(secret) and len(secret) == len(guess):    # emoji loop 
    if guess[idx] == secret[idx]:
        emoji = emoji + f"{GREEN_BOX}"
        idx = idx + 1 
    elif guess[idx] != secret[idx]:
        emoji = emoji + f"{WHITE_BOX}" 
        idx = idx + 1 
        while guess[alt_idx] == secret[idx]:
            emoji = emoji + f"{YELLOW_BOX}"
            alt_idx = alt_idx + 1

print(emoji)

while guess_len != len(secret): 
    guess_again = input(f"That was not {len(secret)} letters! Try again: ")
    if len(guess_again) == len(secret) and guess_again != secret:
        guess_len = len(secret)

while guess_len == len(secret) and guess != secret:  # loop for correct length, wrong guess
    print("Not quite. Play again soon!")
    guess_len = guess_len + 1
while guess_len == len(secret) and guess == secret:  # loop for correct guess  
    print("Woo! You got it!")
    guess_len = guess_len + 1
   