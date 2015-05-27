import unittest
from Cards import Card

class TestCard(unittest.TestCase):
    def getTestCards(self):
        aos = Card('ace', 'spades')
        koh = Card('king', 'hearts')
        return [aos, koh]

    def testToString(self):
        aos, koh = self.getTestCards()
        self.assertEqual(aos.toString(), 'ace of spades')
        self.assertEqual(koh.toString(), 'king of hearts')

    def testGetValues(self):
        aos, koh = self.getTestCards()
        self.assertEqual(aos.getValues(), [1, 11])
        self.assertEqual(koh.getValues(), [10])

if __name__ == '__main__':
    unittest.main()
