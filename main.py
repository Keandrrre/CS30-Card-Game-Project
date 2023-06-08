# Card Game (War)
import random
import os
import time


# Player Class


class Player:
    # Initialize Constructor Method (player)
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.wins = 0

    # Methods (player)
    def draw_card(self):
        return random.choice(self.cards)

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
        self.shuffle_deck()

    # Methods (deck)
    def build_deck(self):
        for s in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def shuffle_deck(self):
        random.shuffle(self.cards)
        print('Cards Have Been Shuffled.')


# Game Class


class Game:
    # Initialize Constructor Method (game)
    def __init__(self):
        p1_name = str(input("Enter Player 1 Name: "))
        p2_name = str(input("Enter Player 2 Name: "))
        self.deck = Deck()
        self.player1 = Player(p2_name)
        self.player2 = Player(p1_name)

    # Methods (game)
    def start_game(self):
        os.system('cls')
        print('Starting War!')
        while self.player1.cards > 0 or self.player2.cards > 0:
            p1_card = self.player1.draw_card()
            p2_card = self.player2.draw_card()
            p1_name = self.player1.name
            p2_name = self.player2.name
