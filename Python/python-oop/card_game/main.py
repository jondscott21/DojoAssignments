from random import randint


class Deck(object):
    def __init__(self, game_name=None):
        self.cards = []
        if game_name == 'euchre':
            self.amount = 16
            for i in range(10, 14):
                # for j in ['red', 'green', 'blue', 'yellow']:
                for j in ['spades', 'hearts', 'diamonds', 'clubs']:
                    self.cards.append(Card(i, j))
        else:
            print "Game name not found - using rules for Poker"
            self.amount = 52
            for i in range(1, 14):
                for j in ['spades', 'hearts', 'diamonds', 'clubs']:
                    self.cards.append(Card(i, j))
        self.shuffle()

    def shuffle(self):
        for k in range(0, 200):
            i = randint(0, self.amount - 1)
            j = randint(0, self.amount - 1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def list_cards(self):
        for card in self.cards:
            card.print_card()

    def deal(self):
        return self.cards.pop()


class Card(object):
    def __init__(self, value, suit):
        if value == 11:
            self.value = 'J'
        elif value == 12:
            self.value = 'Q'
        elif value == 13:
            self.value = 'K'
        elif value == 1:
            self.value = 'A'
        else:
            self.value = value
        self.suit = suit

    def print_card(self):
        print self.value, 'of', self.suit

# class UnoCard(object):
#     def __init__(self, value, suit):
#         if suit == "black" and value == 1:
#             self.number = "Skip"
#         elif suit == "black" and value == 2:
#             self.number = "Draw Two"
#         elif suit == "black" and value == 3:
#             self.number = "Reverse"
#         elif suit == "black" and value == 4:
#             self.number = "Wild Draw Four"
#         elif suit == "black" and value == 5:
#             self.number =


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, number=1):
        for i in range(number):
            self.hand.append(deck.deal())

    def revealHand(self):
        for card in self.hand:
            card.print_card()


my_deck = Deck()
my_deck.list_cards()
# my_euchre_deck = Deck("euchre")
# my_euchre_deck.list_cards()
jon = Player("Jon")
jon.draw(my_deck, 4)
jon.draw(my_deck)
    # jon.draw(my_euchre_deck)
# print "Remaining Euchre deck:"
# my_euchre_deck.list_cards()
print ""
print "{}'s hand:".format(jon.name)
jon.revealHand()

# print 'SHUFFLE'
# my_deck.shuffle()
# my_deck.list_cards()