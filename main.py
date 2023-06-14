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
        return '{} of {}'.format(self.suit, self.value)

# Deck Class


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
        os.system('cls')
        random.shuffle(self.cards)
        print('Shuffling Cards...')
        time.sleep(2)
        os.system('cls')


# Game Class


class Game:
    # Initialize Constructor Method (game)
    def __init__(self):
        p1_name = str(input("Enter Player 1 Name: "))
        p2_name = str(input("Enter Player 2 Name: "))
        self.deck = []
        self.build_deck()
        self.player1 = Player(p2_name)
        self.player2 = Player(p1_name)

    def build_deck(self):
        for s in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for v in range(1, 14):
                self.deck.append(Card(s, v))

    # Methods (game)
    def deal_cards(self):
        pass

    def start_game(self):
        os.system('cls')
        print('Starting War!\n\n' + self.player1.name +
              " Vs. " + self.player2.name)
        time.sleep(3)
        os.system('cls')
        # while len(self.player1.cards) > 0 or len(self.player2.cards) > 0:


game = Game()
game.start_game()
