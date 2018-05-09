import random

class Baseplayer:
    def __init__(self, game):
        self.game = game
        self.hand = []
        self.reserve = []

    def __repr__(self):
        return f"Player({self.hand})"


    def draw_card(self):
        card = self.game.deck.draw_card()
        if card:
            self.hand.append(card)
        return card

    def pick_card_from_hard(self):
        # WILL ASK FOR PLAYER TO PICK
        try:
            return self.hand.pop()
        except IndexError:
            return None
