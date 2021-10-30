"""Repeating a beat in a loop."""

__author__ = "730314357"


beat = str(input("What beat do you want to repeat? "))
repeat = int(input("How many times do you want to repeat it? "))
placeholder = str(beat)

if repeat <= 0: 
    print("No beat...")
else:
    while repeat > 1:
        repeat = repeat - 1
        beat = beat + " " + placeholder
    print(beat)