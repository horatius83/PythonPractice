from itertools import repeat, product

suits = set(['diamonds', 'hearts', 'clubs', 'spades'])
ranks = [str(i) for i in range(2,10)] + ['jack', 'queen', 'king', 'ace']
ranksSet = set(ranks)
values = dict(zip(ranks,[[x] for x in range(2,9)] + [[x] for x in repeat(10,4)] + [[1,11]]))

class Card:
    def __init__(self, rank, suit):
        if(rank in ranksSet and suit in suits):
            self._rank = rank
            self._suit = suit
        else:
            raise Exception('Invalid rank or suit: {0}, {1}'.format(rank, suit))
            
    def getRank(self):
        return self._rank
    def getSuit(self):
        return self._suit
    def toString(self):
        return '{0} of {1}'.format(self._rank, self._suit)
    def getValues(self):
        return values[self._rank]

class Hand:
    def __init__(self, cards):
        self._cards = [x for x in cards]
    def getCards(self):
        return self._cards
    def getCardValues(self):
        return [sum(x) for x in product(*(x.getValues() for x in self._cards))]

