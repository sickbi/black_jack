class Card:
    def __init__(self, cost, suit):
        self.cost = cost
        self.num_value = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.str_value = ['A', 'J', 'Q', 'K']
        self.suit = '♥♦♣♠'[suit]

    def __str__(self):
        if value > 8:
            return f'{self.suit} {self.str_value[self.cost - len(self.num_value) + 1]}'
        else:
            return f'{self.suit} {self.num_value[self.cost]}'

    def price(self):
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost

C = Card(1, 0)

print(C)