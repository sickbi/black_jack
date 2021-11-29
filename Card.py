class Card:
    cards = []
    def __init__(self):
        num_value = [2, 3, 4, 5, 6, 7, 8, 9, 10]  # 0, 1, 2, 3, 4, 5, 6, 7, 8
        str_value = ['J', 'Q', 'K', 'A'] # 9, 10, 11, 12 / 0, 1, 2, 3
        suit = '♥♦♣♠'
        for i in range(4): #suit
            for j in range(13): #cost
                if j > 8:
                    Card.cards.append(f'{suit[i]} {str_value[j - len(num_value)]}')
                else:
                    Card.cards.append(f'{suit[i]} {num_value[j]}')

    def __str__(self):
        return str(Card.cards)

    def score(self, ):
        if self.cost == 12: ## value is A
            return 11
        elif self.cost >= 9 and self.cost <= 11: ## value is J, Q, K
            return 10
        else:
            return self.cost + 2

if __name__ == '__main__':
    card = Card() # for test
    print(card)