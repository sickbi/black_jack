exit_game = False

while exit_game:
    print("=====게임 메뉴=====")
    print("1. 게임 시작")
    print("2. 게임 종료")
    menu = input("메뉴를 선택하세요: ")

    if menu == "1":
        print("게임을 시작합니다.")
    elif menu == "2":
        print("게임을 종료합니다.")
        exit_game = True
    else:
        print("잘못된 메뉴입니다.")