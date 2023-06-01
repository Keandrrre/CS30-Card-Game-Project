# Card Game (War)
import random

# Card Class


class card():
    # Initialize Constructor Method (card)
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # Methods (card)
    def show_card(self):
        print('{} of {}'.format(self.suit, self.value))

# Deck Class


class deck():
    # Initialize Constructor Method (deck)
    def __init__(self):
        self.cards = []
        self.build_deck()

    # Methods (deck)
    def build_deck(self):
        for s in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for v in range(1, 14):
                self.cards.append(card(s, v))

# Player Class


class player():
    # Initialize Constructor Method (player)
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.wins = 0

    def draw(self):
        return random.choice(self.cards)


class game():
    deck = deck()
    # Define Constructor Method (game)
    def __init__(self):
