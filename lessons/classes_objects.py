"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of Pizza."""

    # Attribute Definitions
    size: str
    toppings: int
    extra_cheese: bool

    def price(self, tax: float) -> float:
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0

        total += self.toppings * .75

        if self.extra_cheese:
            total += 1.0

        total *= tax

        return total


a_pizza: Pizza = Pizza()
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False


print(a_pizza.price())
