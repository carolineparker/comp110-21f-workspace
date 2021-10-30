"""Drawing forests in a loop."""

__author__ = "730314357"

# The string constant for the pine tree emoji
tree: str = '\U0001F332'
placeholder = str(tree)
depth = int(input("Depth: "))

if depth > 0:
    print(tree)
while depth > 1:
    depth = depth - 1
    tree = tree + placeholder
    print(tree)