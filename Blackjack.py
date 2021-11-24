from Deck import Deck
from Player import Player

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)

    def play(self):
        p_status = self.player.deal()
        d_status = self.dealer.deal()

        self.player.show()

        if p_status == 1:
            print("블랙잭! 축하합니다!")
            if d_status == 1:
                print("Dealer와 Player 둘다 블랙잭! 무승부네요")
            return 1

        cmd = ""
        while cmd != "Stay":
            bust = 0
            cmd = input("Hit 또는 Stay?")

            if cmd == "Hit":
                cmd = input("홀 또는 짝")
                if cmd == "홀":
                    bust = self.player.hit()
                    self.player.show()
                elif cmd == "짝":
                    bust = self.player.hit()
                    self.player.show()
                else:
                    print("틀림")
            if bust == 1:
                print("Player 버스트. GG!")
                return 1
        print("\n")
        self.dealer.show()
        if d_status == 1:
            print("Dealer 블랙잭! 다음엔 행운을 빌어!")
            return 1

        while self.dealer.check_score() < 17:
            if self.dealer.hit() == 1:
                self.dealer.show()
                print("Dealer 버스트. 추가합니다!")
                return 1
            self.dealer.show()

        if self.dealer.check_score() == self.player.check_score():
            print("무승부입니다. 다음엔 잘해봐.")
        elif self.dealer.check_score() > self.player.check_score():
            print("Dealer가 이겼습니다. GG")
        elif self.dealer.check_score() < self.player.check_score():
            print("Player가 이겼습니다. 축하합니다.")

b = Blackjack()
b.play()