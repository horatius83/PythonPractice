from itertools import product

from Cards import Card

class Hand:
    def __init__(self, cards):
        self._cards = [x for x in cards]
    def getCards(self):
        return self._cards
    def getCardValues(self):
        return [sum(x) for x in product(*(x.getValues() for x in self._cards))]

