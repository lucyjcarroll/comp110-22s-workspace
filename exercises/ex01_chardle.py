"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730320310"

word_choice: str = input("Enter a 5-character word: ")
character_choice: str = input("Enter a single character: ")
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

count_char = word_choice.count(character_choice)

if count_char == 0:
    print("No instances of " + character_choice + " found in " + word_choice)
if count_char == 1:
    print("1 instance of " + character_choice + " found in " + word_choice)
if count_char == 2:
    print("2 instances of " + character_choice + " found in " + word_choice)
    