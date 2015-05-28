from Cards import Card
from Hand import Hand

class Player:
    def __init__(self, name, hand, credits):
        self._hand = hand
        self._credits = credits
        self._name = name

    def __str__(self):
        name, credits = self._name, self._credits
        hand = ', '.join((str(x) for x in self._hand))
        return '{0} [{1}] {2} credits'.format(name, hand, credits)

    def getCredits(self):
        return self._credits

    def getHand(self):
        return self._hand;

    def getName(self):
        return self._name

