class Card:
    def __init__(self, symbol, number, value=0):
        self.symbol = symbol
        self.number = number
    def __repr__(self):
        return f"Card({self.number} of {self.symbol})"
