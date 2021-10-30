"""an example of conditional (if-else) statements."""

SECRET: int = 3

print("I am thinking of a number between one and five what is it?")
guess: int = int(input("What is your guess?"))

if guess == SECRET: 
    print("You guessed correctly!")
