import unittest
from Cards import Card

class TestHand(unittest.TestCase):
    def getTestCards(self):
        aos = Card('ace', 'spades')
        koh = Card('king', 'hearts')
        return [aos, koh]

    def testGetCardValues(self):
        self.getTestCards()

        self.assertEqual(

if __name__ == '__main__':
    unittest.main()
