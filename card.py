suits = ["пик", "червей", "бубен", "треф"]
values = ["6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]


class Card:
    def __init__(self, value: "int or str", suit: str):

        if(not(isinstance(value, int) or isinstance(value, str)) or
                not(isinstance(suit, str))):
            raise TypeError("Incorrect type of parameter")

        suit = suit.lower()
        value = str(value).title()

        if(value not in values or suit not in suits):
            raise ValueError("Invalid value of parameter")

        self.value = value
        self.suit = suit

    def __eq__(self, other: object):
        return isinstance(other, Card) and self.value == other.value and self.suit == other.suit

    def __ne__(self, other: object):
        return not(self == other)

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return self.value + " " + self.suit
