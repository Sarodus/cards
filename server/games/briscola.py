from .basegame import Basegame

class Briscola(Basegame):
    value_map = {
        1: 11,
        3: 10,
        11: 2,
        12: 3,
        13: 4
    }

    def __init__(self, *args, **kwargs):
        self.master_card = None
        self.turn_count = 0
        super(Briscola, self).__init__(*args, **kwargs)

    def start(self):
        for card in self.deck.cards:
            setattr(card, 'value', self.value_map.get(card.number, 0))
        self.master_card = self.deck.draw_card()
        for player in self.players:
            for _ in range(3):
                player.draw_card()

    def turn(self):
        if self.turn_count:
            for player in self.players:
                player.draw_card()
        self.turn_count += 1

        table_cards = {}
        for player in self.players:
            card = player.pick_card_from_hard()
            table_cards[card] = player

        winner_card = self.card_win_resolution(table_cards.keys())
        winner_player_turn = table_cards[winner_card]
        winner_player_turn.reserve += list(table_cards)
        
        return bool(self.deck.cards)


    def card_win_resolution(self, cards):
        winner = None
        for card in cards:
            if winner is None:
                winner = card
                continue

            if card.symbol == winner.symbol and card.value > winner.value:
                winner = card
            elif card.symbol == winner.symbol and card.number > winner.number and winner.value == 0:
                winner = card
            elif card.symbol == self.master_card.symbol:
                winner = card
        return winner
