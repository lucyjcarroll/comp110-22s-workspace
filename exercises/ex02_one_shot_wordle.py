"Second Try on Wordle- EX02"
__author__ = "730320310"

secret_word = str("python")
guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

firstidx: str = secret_word[0]
secondidx: str = secret_word[1]
thirdidx: str = secret_word[2]
fourthidx: str = secret_word[3]
fifthidx: str = secret_word[4]
sixthidx: str = secret_word[5]
idx = str = [secret_word]

i: int = len(secret_word)  
while i < len(guess):
    print(f"That was not {i} letters! Try again: ")
    i = i + 6
i: int = len(secret_word)
while i > len(guess):
    print(f"That was not {i} letters! Try again: ")
    i = i - 6

i: int = len(secret_word)
while i == len(guess) and guess != secret_word:
   
    while idx == [guess]:
        print(GREEN_BOX)
        idx != [guess]
        
    print("Not quite. Play again soon!")
    i = i + 1

i: int = len(secret_word)
while i == len(guess) and guess == secret_word:
    print(f"{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}")  # no need to check indices because if secret_word == guess, it will always be correct to print 6 green boxes. 
    print("Woo! You got it!")
    guess = "hello"  # this is a word that would never be chosen as a secret word because it's not 6 letters
    i != len(secret_word)