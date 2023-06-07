# Card Game (War)
import random
import os
import time
import keyboard


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
        self.deck = Deck
        self.player1 = player1
        self.player2 = player2

    # Methods (game)
    def deal_cards(self):
        self.deck.shuffle_deck
        print('Dealing Cards')


while True:
    # Main Menu
    os.system('cls')
    print("WAR\n\nOptions:\n1 -- 'Start New Game'\n2 -- 'Rules'")
    if keyboard.is_pressed('1'):
        os.system('cls')
        # Enter Player Names
        p1_name = str(input("Enter Player 1 Name: "))
        p2_name = str(input("Enter Player 2 Name: "))
        os.system('cls')
        p1 = Player(p1_name)
        p2 = Player(p2_name)
        # Game Starts
        print('Starting War!')
        new_game = Game(p1, p2)
        new_game.deal_cards
