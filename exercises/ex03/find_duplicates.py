"""Finding duplicate letters in a word."""

__author__ = "730314357"

word: str = input("Enter a word: ")
dup: bool = False

i: int = 0
j: int = 0
while i < len(word):
    j = i + 1
    character: str = word[i]
    while j < len(word):
        character_2: str = word[j]
        j = j + 1 
        if character == character_2:
            dup = True
    i = i + 1
print("Found duplicate:", dup)

    
