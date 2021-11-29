import random
from Card import Card

a = Card()

class Deck:
    deck = []
    def __init__(self):
        pass

    def draw(self, iteration):
        for i in range(iteration):
            card = random.choice(Card.cards)
            Card.cards.remove(card)
            Deck.deck.append(card)

    def count(self):
        return len(Card.cards)

if __name__ == '__main__':
    t_deck = Deck()
    print(t_deck.draw(1))
    print(t_deck.count())