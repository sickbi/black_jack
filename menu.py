from game import game

exit_game = False

while not exit_game:
    print("=====게임 메뉴=====")
    print("1) 게임 시작")
    print("2) 게임 종료")
    print("3) 시계 확인하기")
    menu = input(">> ")

    if menu == "1":
        print("게임을 시작합니다.")
        game()

    elif menu == "2":
        print("게임을 종료합니다.")
        exit_game = True

    elif menu == "3":
        print("시계 따윈 없다")
        print("강원랜드에 온 걸 환영한다 애송아")

    else:
        print("잘못된 메뉴입니다.")