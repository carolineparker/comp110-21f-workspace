"""Example of using lists in a simple game"""


from random import randint

rolls: list[int] = list()
print(rolls)

rolls: list[int] = list()
rolls.append(randint(1, 6))
print(rolls)

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))


rolls.pop(len(rolls) - 1)
print(rolls)

i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1
print(f'Total score: {sum}')
