from card import Card
import deck
import unittest

class CardTests(unittest.TestCase):
    cards = [
        ([], "пик", TypeError),
        (9.1, "пик", TypeError),
        ("5", 5, TypeError),
        (5, "треф", ValueError),
        (6, "масть", ValueError),
        ("девятка", "пик", ValueError),
        (6, "бубен", "6 бубен"),
        (7, "пик", "7 пик"),
        (8, "червей", "8 червей"),
        (9, "пик", "9 пик"),
        (10, "ТРЕФ", "10 треф"),
        ("Валет", "червей", "Валет червей"),
        ("Дама", "треф", "Дама треф"),
        ("король", "бубен", "Король бубен"),
        ("туз", "пик", "Туз пик")
    ]

    def test_card_creation(self):
        "Card() should correctly create objects with error processing"
        for value, suit, string in self.cards:
            try:
                Card(value, suit)
            except (ValueError, TypeError) as e:
                self.assertEqual(string, type(e))
            else:
                self.assertEqual(string, str(Card(value, suit)))


class DeckTests(unittest.TestCase):
    None


if __name__ == '__main__':
    unittest.main()