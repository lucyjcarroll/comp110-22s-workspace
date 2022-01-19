"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730320310" 

word: str = input("Enter a 5-character word: ")
character: str = input("Enter a single character: ")
print("Searching for e in hello")

if character == "hello"[1]:
    print("e found at index 1")
else:
    character == "hello"[0]
    character == "hello"[2]
    character == "hello"[3]
    character == "hello"[4]
    print("letter not found at index 1")



word: str = input("Enter a 5 character word: ")
character: str = input("Enter a single character: ")
print("Searching for e in heels")

if character == "heels"[1]:  
    print("e found at index 1")
    if character == "heels"[2]: 
        print("e found at index 2")
else: 
    character != "heels"[1]
    print("letter not found at index 1")
    character != "heels"[2]
    print("letter not found at index 2")
    


word: str = input("Enter a 5-character word: ")
character: str = input("Enter a single character: ")
print("Searching for s in heels")

if  character == "heels"[4]:
    print("s found at index 4")
else: 
    character != "heels"[4]
    print("letter not found at index 4")