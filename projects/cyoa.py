"""Create your own adventure."""

__author__ = "730314357"
player: str = ""
points: int = 5
HAPPY_FACE: str = '\U0001F603'
SAD_FACE: str = '\U0001F61E'


def greet() -> None:
    """Greeting."""
    print("Welcome to Flip the Coin. You will be guessing if the flipped coin is heads or tails. If you guess correctly, you get one adventure point. If you guess incorrectly you lose one point. You will start out with 5. If you get to 0 you lose. If you get to 10 you win.")
    global player
    player = input(str("What is your name? "))


def main() -> None:
    """Main Function."""
    greet()
    global points
    correct_guess: str = ""
    while points > 0 and points < 10:
        choice = str(input(f"Hi {player}! If you would like to flip the coin, type 'Flip'. If you would like an extra point for practice, type 'Practice'. If you would like to roll a dice instead, type 'Dice'. If you would like to end your game, type 'Exit' "))
        if choice == "Practice" or choice == "practice":
            practice_point(points)
        if choice == "Flip" or choice == "flip":
            from random import randint
            coin = randint(1, 2)
            guess = str(input(f"Hi {player}, type 'Heads' to guess heads and type 'Tails' to guess tails: "))
            if coin == 1:
                correct_guess = "Heads"
            if coin == 2:
                correct_guess = "Tails"
            if guess == correct_guess:
                points = points + 1
                print("Correct")
                print(f"Adventure points: {points}")
            else:
                points = points - 1
                print("Guess again")
                print(f"Adventure points: {points}")
            if points == 0:
                print(f"Sorry, you lost {SAD_FACE}")
            if points == 10:
                print(f"You won! {HAPPY_FACE}")
        if choice == "Exit":
            points = points - 10
            print(f"You started with 5 points. You ended with {points + 10}")
            print("Thanks for playing!")
        if choice == "Dice": 
            dice()


def dice() -> None:
    """Roll a dice."""
    global points
    while points > 0 and points < 10:
        from random import randint
        die_roll = randint(1, 6)
        guess_2 = int(input(f"Hi {player}, what number do you think the dice rolled? "))
        if die_roll == guess_2:
            points = points + 1
            print("Correct")
            print(f"Adventure points {points}")
        if die_roll != guess_2:
            points = points - 1
            print("Guess again")
            print(f"Adventure points: {points}")
        if points == 0:
            print(f"Sorry, you lost {SAD_FACE}")
        if points == 10: 
            print(f"You won! {HAPPY_FACE}")

                       
def practice_point(x: int) -> None:
    """Add a practice point."""
    global points
    points = points + 1
    global player
    print(f"Here is an extra practice point, {player}. Good luck!")
    print(f"Adventure points: {points}")
    main()


if __name__ == "__main__":
    main()
