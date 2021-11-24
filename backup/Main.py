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
            print("Blackjack! Congratulation!")
            if d_status == 1:
                print("Dealer와 Player 둘다 Blackjack! The game ended in a tie")
            return 1

        cmd = ""
        while cmd != "Stay":
            bust = 0
            cmd = input("Hit or Stay?")

            if cmd == "Hit":
                bust = self.player.hit()
                self.player.show()
            if bust == 1:
                print("Player Bust. GG!")
                return 1
        print("\n")
        self.dealer.show()
        if d_status == 1:
            print("Dealer Blackjack! Play of the game")
            return 1

        while self.dealer.check_score() < 17:
            if self.dealer.hit() == 1:
                self.dealer.show()
                print("Dealer Bust. GG!")
                return 1
            self.dealer.show()

        if self.dealer.check_score() == self.player.check_score():
            print("The game ended in a tie. It was neck and neck.")
        elif self.dealer.check_score() > self.player.check_score():
            print("Dealer beat me! GG")
        elif self.dealer.check_score() < self.player.check_score():
            print("Player beat Dealer. Congratulation.")

b = Blackjack()
b.play()