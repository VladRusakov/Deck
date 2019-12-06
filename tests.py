from card import Card
from deck import Deck
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

    def test_len_start(self):
        """amount() should correctly display number of cards 
        in a deck after its creating"""
        deck = Deck()
        self.assertEqual(36, len(deck))

    def test_len_with_draws(self):
        """amount() should correctly display number of cards 
        while it's count changing"""
        deck = Deck()
        deck.draw()
        amount = 35
        self.assertEqual(amount, len(deck))
        for i in range(1, 8):
            amount -= i
            deck.draw(i)
            self.assertEqual(amount, len(deck))

    def test_draw_one(self):
        """draw() should draw one card from deck if it possible,
        in another way returns waste deck"""
        deck = Deck()
        controlCards = deck.get_cards()
        for _ in range(len(deck)+4):
            draw = deck.draw()
            self.assertEqual(draw.get_cards(), controlCards[:1])
            controlCards = controlCards[1:]
            self.assertEqual(deck.get_cards(), controlCards)

    def test_draw_several(self):
        """draw(count) should draw several cards from deck if 
        it possible, in another way returns waste deck"""
        deck = Deck()
        controlCards = deck.get_cards()
        for i in range(1, 10):
            draw = deck.draw(i)
            self.assertEqual(draw.get_cards(), controlCards[:i])
            controlCards = controlCards[i:]
            self.assertEqual(deck.get_cards(), controlCards)

    def test_shuffle_amount(self):
        "shuffle() should save amount of deck cards"
        deck = Deck()
        amount = len(deck)
        deck.shuffle()
        self.assertEquals(amount, len(deck))

    def test_shuffle(self):
        "shuffle() should returns another cards order"
        deck1 = Deck()
        deck2 = deck1.clone()
        deck1.shuffle()
        self.assertNotEquals(deck1, deck2)

    patternSolutions = [
        ("*к", ["6 пик",
                "7 пик",
                "8 пик",
                "9 пик",
                "10 пик",
                "Валет пик",
                "Дама пик",
                "Король пик",
                "Туз пик"]),

        ("Т*", ["Туз пик",
                "Туз червей",
                "Туз бубен",
                "Туз треф"]),

        (r"%% *е%", ["10 червей",
                     "10 бубен",
                     "10 треф"])
    ]

    def test_search_by_pattern(self):
        "search(string) should find all cards that are fit the pattern"
        deck = Deck()
        for pattern, result in self.patternSolutions:
            self.assertEquals(result, deck.search(pattern))


if __name__ == '__main__':
    unittest.main()
