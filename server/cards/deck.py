import random

from .card import Card


class Deck:
    symbols = 'H', 'D', 'C', 'S'
    numbers = range(1, 14)
     
    def __init__(self, autoshuffle=True):
        self.cards = list(self._generate_cards())
        if autoshuffle:
            self.shuffle()

    def _generate_cards(self):
        for symbol in self.symbols:
            for number in self.numbers:
                yield Card(symbol, number)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        return random.shuffle(self.cards)

    def draw_card(self):
        try:
            return self.cards.pop(0)
        except IndexError:
            return None
