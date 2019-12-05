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

    "amount() should correctly display number of cards in a deck after its creating"
    def test_amount_start(self):
        deck = Deck()
        self.assertEqual(36, deck.amount())


    "amount() should correctly display number of cards while it's count changing"
    def test_amount_with_draws(self):
        deck = Deck()
        deck.draw()
        amount = 35
        self.assertEqual(amount, deck.amount())
        for i in range(1, 8):
            amount -= i
            deck.draw(i)
            self.assertEqual(amount, deck.amount())


    "draw() should draw one card from deck if it possible, in another way returns waste deck"
    def test_draw_one(self):
        deck = Deck()
        controlCards = deck.getCardsList().copy()
        for i in range(1, 36):
            draw = deck.draw()
            self.assertEqual(draw.getCardsList(), controlList[:1])

            controlCards = controlList[1:]
            self.assertEqual(deck.getCardsList(), controlCards)
        
        emptyDraw = deck.draw()
        self.assertEqual(emptyDraw.getCardsList(), [])
        self.assertEqual(deck.getCardsList(), [])


    "draw(count) should draw several cards from deck if it possible, in another way returns waste deck"
    def test_draw_few(self):
        deck = Deck()
        controlCards = deck.getCardsList().copy()
        for i in range(1, 9):
            draw = deck.draw(i)
            self.assertEqual(draw.getCardsList(), controlList[:i])

            controlCards = controlList[i:]
            self.assertEqual(deck.getCardsList(), controlCards)
        
        emptyDraw = deck.draw(5)
        self.assertEqual(emptyDraw.getCardsList(), [])
        self.assertEqual(deck.getCardsList(), [])


    "shuffle() should save amount of deck cards"
    def test_shuffle_amount(self):
        deck = Deck()
        amount = deck.amount()
        deck.shuffle()
        self.assertEquals(amount, deck.amount())


    "shuffle() should returns another cards order"
    def test_shuffle(self):
        deck1 = Deck()
        deck2 = deck1.clone()
        deck.shuffle()
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

    "search(string) should find all cards that are fit the pattern"
    def test_search_by_pattern(self):
        deck = Deck()
        for pattern, result in self.patternSolutions:
            self.assertEquals(result, deck.search(pattern).getCardsList())

if __name__ == '__main__':
    unittest.main()