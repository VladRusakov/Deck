from card import *
from random import random

FULL_DECK = []
for suit in suits:
    for value in values:
        FULL_DECK.append(Card(value, suit))


class Deck:
    """Represents card deck with functions of drawing number of cards,
    shuffling current deck and looking for cards in deck with pattern.
    Constructor gets list<Card>.
    """

    def __init__(self, cards: "list of cards" = None):
        if(cards == None):
            self.cards = FULL_DECK.copy()
        else:
            self._check_cards_correctness(cards)
            self.cards = cards

    def __len__(self):
        return len(self.cards)

    def __eq__(self, other: object):
        return type(other) == Deck and self.get_cards() == other.get_cards()

    def __ne__(self, other: object):
        return not(self == other)

    def _check_cards_correctness(self, cards: "list of cards"):
        """list<Card> is correct if contains only non-repeatable cards"""
        for card in cards:
            if not(isinstance(card, Card)):
                raise ValueError(str(card) + " is not a card")
        cardsSet = set(cards)
        if len(cardsSet) != len(cards):
            raise ValueError("Amount of cards is incorrect")

    def get_cards(self) -> "list of strings":
        """Returns list<str> with text representation of all cards in deck"""
        return [str(card) for card in self.cards]

    def clone(self):
        "Returns copy of current Deck object"
        return Deck(self.cards.copy())

    def draw(self, count: int = 1):
        """Returns new Deck with 'count' first cards from current deck. 
        Removes these cards from original deck"""
        if count < 0:
            raise ValueError("count can't be less than 0")
        otherCards = self.cards[:count]
        otherDeck = Deck(otherCards)
        self.cards = self.cards[count:]
        return otherDeck

    def shuffle(self):
        "Mixes randomly"
        newOrder = self.cards
        while(self.cards == newOrder):
            newOrder = sorted(self.cards, key=lambda _:  random() - 0.5)
        self.cards = newOrder

    def search(self, pattern: str):
        """Returns list<str> with cards that are satisfy the pattern"""
        matches = []
        for card in self.get_cards():
            if self.match(pattern, card):
                matches.append(card)
        return matches

    def match(self, pattern: str, cardname: str, indexC: int = 0, indexP: int = 0):
        """Checks if cardname is satisfy the pattern. 
        indexC is the index in cardname string.
        indexP is the index in pattern string."""
        while(indexC < len(cardname) and indexP < len(pattern)):
            if pattern[indexP] == "%" or pattern[indexP] == cardname[indexC]:
                indexC += 1
                indexP += 1
            elif pattern[indexP] == "*":
                if indexP == len(pattern)-1:
                    return True
                c = indexC + 1
                while c < len(cardname):
                    if self.match(pattern, cardname, c, indexP+1):
                        return True
                    c += 1
                return False
            else:
                return False
        return indexP == len(pattern) and indexC == len(cardname)
