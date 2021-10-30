"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730314357"

from random import randint
phrase = (randint(1, 4))
print("Your fortune cookie says...")
if phrase == int(1):
    print("You will have an awesome day")
if phrase == int(2):
    print("You will make new friends today")
if phrase == int(3):
    print("Today, you will discover something new")
if phrase == int(4):
    print("You are going to have a great week")

print("Now, go spread positive vibes!")