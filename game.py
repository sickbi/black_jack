from Deck import Deck
from Player import Player

def game():
    deck = Deck()
    player = Player(False, deck)
    dealer = Player(True, deck)

    p_status = player.deal()
    d_status = dealer.deal()

    player.show()

    if p_status == 1:
        print("블랙잭! 축하합니다!")
        if d_status == 1:
            print("Dealer와 Player 둘다 블랙잭! 무승부네요")
        return 1

    cmd = ""
    while cmd != "2":
        bust = 0
        print("1) Hit")
        print("2) Stay")
        cmd = input(">> ")

        if cmd == "1":
            bust = player.hit()
            player.show()
        if bust == 1:
            print("Player Bust. GG!")
            return 1

    print("\n")
    dealer.show()
    if d_status == 1:
        print("Dealer 블랙잭! 다음엔 행운을 빌어!")
        return 1

    while dealer.check_score() < 17:
        if dealer.hit() == 1:
            dealer.show()
            print("Dealer 버스트. 추가합니다!")
            return 1
        dealer.show()

    if dealer.check_score() == player.check_score():
        print("무승부입니다. 다음엔 잘해봐.")
    elif dealer.check_score() > player.check_score():
        print("Dealer가 이겼습니다. GG")
    elif dealer.check_score() < player.check_score():
        print("Player가 이겼습니다. 축하합니다.")

if __name__=="__main__":
    game()