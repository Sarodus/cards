from cards import Deck
from .player import Baseplayer

class Basegame(object):    
    autoshuffle = True
    PlayerClass = Baseplayer

    def __init__(self, num_players):
        self.deck = Deck(self.autoshuffle)
        self.players = [self.PlayerClass(self) for _ in range(num_players)]
        self.start()
    
    def start(self):
        pass
