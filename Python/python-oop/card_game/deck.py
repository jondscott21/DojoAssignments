from random import randint
import card


class Deck(object):
    def __init__(self):
        self.amount = 52
        self.cards = []
        for i in range(1, 14):
            for j in ['spades', 'hearts', 'diamonds', 'clubs']:
                self.cards.push(Card, (i, j))
        self.shuffle()
        return self

    def shuffle(self):
        while randint(0, self.amount - 1) > 1:
            i = randint(0, self.amount - 1)
            j = randint(0, self.amount - 1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def list_cards(self):
        for card in self.cards:
            card.print_card()