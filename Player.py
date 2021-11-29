from Deck import Deck

class Player(Deck): #deck 클래스 상속
    def __init__(self, isDealer):
        super().__init__()
        self.isDealer = isDealer
        self.score = 0

    def hit(self):
        super().draw(1)
        self.check_score()
        if self.score > 21:
            return 1
        return 0

    def deal(self):
        super().draw(2)
        self.check_score()
        if self.score == 21:
            return 1
        return 0

    def check_score(self):
        a_counter = 0
        self.score = 0
        for card in Deck.deck:
            if card.score() == 11:
                a_counter += 1
            self.score += card.score()

        while a_counter != 0 and self.score > 21:
            a_counter -= 1
            self.score -= 10
        return self.score

    def show(self):
        if self.isDealer:
            print("Dealer의 카드")
        else:
            print("Player의 카드")

        for i in Deck.deck:
            i.show()

        print("Score: " + str(self.score))