"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730320310"

word_choice: str = input("Enter a 5-character word: ")
if len(word_choice) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character_choice: str = input("Enter a single character: ")
if len(character_choice) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character_choice + " in " + word_choice)

if character_choice == word_choice[0]:
    print(character_choice + " found at index 0")
if character_choice == word_choice[1]:
    print(character_choice + " found at index 1")
if character_choice == word_choice[2]:
    print(character_choice + " found at index 2")
if character_choice == word_choice[3]:
    print(character_choice + " found at index 3")
if character_choice == word_choice[4]:
    print(character_choice + " found at index 4") 

char_count = word_choice.count(character_choice)

if char_count == 0:
    print("No instances of " + character_choice + " found in " + word_choice)
else:
    if char_count == 1:
        print("1 instance of " + character_choice + " found in " + word_choice)
    if char_count >= 2:
        print(char_count, "instances of " + character_choice + " found in " + word_choice)
     