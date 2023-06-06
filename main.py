# Card Game (War)
import random


# Player Class


class Player:
    # Initialize Constructor Method (player)
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.wins = 0

    # Card Class


class Card:
    # Initialize Constructor Method (card)
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # Methods (card)
    def show_card(self):
        print('{} of {}'.format(self.suit, self.value))

# deck Class


class Deck:
    # Initialize Constructor Method (deck)
    def __init__(self):
        self.cards = []
        self.build_deck()

    # Methods (deck)
    def build_deck(self):
        for s in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def shuffle_deck(self):
        random.shuffle(self.cards)

# Game Class


class Game:
    # Initialize Constructor Method (game)
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


print('check')
