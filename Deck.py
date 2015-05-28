from Cards import suits, ranks, Card
from random import shuffle

def createNewDeck():
    '''() -> a full 52 card deck (minus jokers)'''
    cards = [Card(rank, suit) for rank in ranks for suit in suits]
    return cards

def shuffleDeck(cards):
    shuffle(cards)
    return cards

def deal(numberOfCards, deck):
    '''number of cards -> [Card] -> (dealt cards, cards remaining)'''
    if numberOfCards < len(deck):
        return (deck[:numberOfCards], deck[numberOfCards:])
    else:
        return (deck, [])

