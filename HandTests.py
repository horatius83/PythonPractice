import unittest
from Cards import Card
from Hand import Hand

class TestHand(unittest.TestCase):
    def getTestCards(self):
        aos = Card('ace', 'spades')
        koh = Card('king', 'hearts')
        return [aos, koh]

    def testGetCardValues(self):
        hand = Hand(self.getTestCards())
        self.assertEqual(hand.getCardValues(), [11, 21])

if __name__ == '__main__':
    unittest.main()
