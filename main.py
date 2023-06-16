# Card Game (War)
import random
import os
import time


# Player Class


class Player:
    # Initialize Constructor Method (player class)
    def __init__(self, name):
        self.name = name
        self.hand = []

    # Methods (player class)
    def draw_card(self):
        card = self.hand.pop(0)
        return card

    # Used For Testing
    def show_hand(self):
        for c in self.hand:
            c.show_card()


# Card Class


class Card:
    # Initialize Constructor Method (card class)
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # Methods (card class)
    def show_card(self):
        return '{} of {}'.format(self.value, self.suit)


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

    # Used For Testing
    def show_deck(self):
        for c in self.cards:
            c.show_card()


# Game Class


class Game:
    def __init__(self):
        self.p1 = Player(str(input('Player 1 Name: ')))
        self.p2 = Player(str(input('Player 2 Name: ')))
        self.deck = Deck()
        self.cards_drawn = []
        self.play = True

    def play_game(self):
        self.deal_cards()
        os.system('cls')
        print('Starting War!')
        time.sleep(3)
        while len(self.p1.hand) > 0 and len(self.p2.hand) > 0 and self.play == True:
            os.system('cls')
            option = str(input(
                'War! {}({} cards) vs {}({} cards)\n\nType...\n\t"draw" - Players Draw Cards\n\t"quit" - End Game\n\nEnter Option: '.format(self.p1.name, len(self.p1.hand), self.p2.name, len(self.p2.hand))))
            if option.lower() == 'draw':
                self.players_draw()
            elif option.lower() == 'quit':
                self.play = False
            else:
                pass
        game.game_over()

    def deal_cards(self):
        while len(self.deck.cards) > 0:
            self.p1.hand.append(self.deck.cards[0])
            self.deck.cards.pop(0)
            self.p2.hand.append(self.deck.cards[0])
            self.deck.cards.pop(0)

    def show_drawn(self, p1c, p2c):
        print('{} drew {} & {} drew {}'.format(
            self.p1.name, p1c.show_card(), self.p2.name, p2c.show_card()))

    def players_draw(self):
        # Get/Draw Card From Each Players Hand
        p1c = self.p1.draw_card()
        p2c = self.p2.draw_card()
        # Add The Cards To  The Games Drawn List
        self.cards_drawn.append(p1c)
        self.cards_drawn.append(p2c)
        # Show Drawn Cards
        self.show_drawn(p1c, p2c)
        # Determin Winner
        if p1c.value > p2c.value:
            self.declare_winner(self.p1)
        if p2c.value > p1c.value:
            self.declare_winner(self.p2)
        elif p1c.value == p2c.value:
            self.war()

    def war(self):
        if len(self.p1.hand) < 4:
            print('{} Does Not Have Enough Cards For War.'.format(self.p1.name))
            self.play = False
        elif len(self.p2.hand) < 4:
            print('{} Does Not Have Enough Cards For War.'.format(self.p2.name))
            self.play = False
        else:
            print('WAR!')
            time.sleep(3)
            c = 0
            while c < 3:
                self.cards_drawn.append(self.p1.draw_card())
                self.cards_drawn.append(self.p2.draw_card())
                c += 1
            self.players_draw()

    def declare_winner(self, p):
        print(p.name + ' Wins!')
        p.hand.extend(self.cards_drawn)
        self.cards_drawn.clear()
        time.sleep(3)

    def game_over(self):
        if len(self.p1.hand) > len(self.p2.hand):
            print('Game Over, {} Wins!'.format(self.p1.name))
        elif len(self.p2.hand) > len(self.p1.hand):
            print('Game Over, {} Wins!'.format(self.p2.name))
        else:
            print('Game Over, Its A Draw!')


game = Game()
game.play_game()
