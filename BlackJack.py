from Deck import shuffleDeck, deal, createNewDeck
from Player import Player

def dealCards(players, deck):
    '''given a list of players deal each one two cards'''
    for player in players:
        name, credits = player.getName(), player.getCredits()
        cards, deck = deal(2,deck)
        yield Player(name, cards, credits)

deck = shuffleDeck(createNewDeck())
players = (Player(name, [], 100) for name in ['Joe', 'Billy Bob', 'Bubba'])
dealtPlayers = dealCards(players, deck)
print([str(x) for x in dealtPlayers])
