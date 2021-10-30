"""An exercise in remainders and boolean logic."""

__author__ = "730314357"


number = int(input("Enter an int: "))
no_remainder_2 = number / 2
remainder_2 = number // 2
no_remainder_7 = number / 7
remainder_7 = number // 7

if no_remainder_2 == remainder_2:
    if no_remainder_7 == remainder_7:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if no_remainder_7 == remainder_7:
        print("HEELS")
    else:
        print("CAROLINA")