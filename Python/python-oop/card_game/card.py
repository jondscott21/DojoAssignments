class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def print_card(self):
        print self.value, 'of', self.suit