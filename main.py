# Card Game (War)
import random
import os
import time


# Player Class


class Player:
    # Initialize Constructor Method (player)
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.cards = []

    # Methods (player)
    def draw_card(self):
        return random.choice(self.hand)

    def show_hand(self):
        for c in self.hand:
            c.show_card()

    # Card Class


class Card:
    # Initialize Constructor Method (card)
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # Methods (card)
    def show_card(self):
        print('{} of {}'.format(self.suit, self.value))

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
                self.cards.append(Card(v, s))

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def show_deck(self):
        for c in self.cards:
            c.show_card()
        time.sleep(3)
        os.system('cls')

# New Game Class


class New_Game:
    def __init__(self):
        self.p1 = Player(str(input("Player 1 Name:")))
        self.p2 = Player(str(input("Player 2 Name:")))
        self.deck = Deck()

    def deal_cards(self):
        while len(self.deck.cards) > 26:
            self.p1.hand.append(self.deck.cards[0])
            self.deck.cards.pop(0)
        while len(self.deck.cards) > 0:
            self.p2.hand.append(self.deck.cards[0])
            self.deck.cards.pop(0)

    def players_draw(self):
        pass


game = New_Game()
game.deal_cards()
