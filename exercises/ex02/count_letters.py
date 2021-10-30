"""Counting letters in a string."""

__author__ = "730314357"


letter = str(input("What letter do you want to search for?: "))
word = str(input("Enter a word: "))
search = 0
count = 0

while search < len(word):
    if word[search] == letter:
        count = count + 1
    search = search + 1
print("Count:", count)