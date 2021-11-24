class Card:
    def __init__(self, cost, suit):
        self.cost = cost
        self.num_value = [2, 3, 4, 5, 6, 7, 8, 9, 10]  # 0, 1, 2, 3, 4, 5, 6, 7, 8
        self.str_value = ['J', 'Q', 'K', 'A'] # 9, 10, 11, 12 / 0, 1, 2, 3
        self.suit = '♥♦♣♠'[suit]

    def __str__(self):
        if self.cost > 8:
            return f'{self.suit} {self.str_value[self.cost - len(self.num_value)]}'
        else:
            return f'{self.suit} {self.num_value[self.cost]}'

    def score(self):
        if self.cost == 12: ## value is A
            return 11
        elif self.cost >= 9 and self.cost <= 11: ## value is J, Q, K
            return 10
        else:
            return self.cost + 2

if __name__ == '__main__':
    card = Card(0, 3) # for test
    print(card)
    print(card.score())