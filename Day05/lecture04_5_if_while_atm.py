# ATM[3단계]
# 1. 로그인
# . 로그인 후 재 로그인 불가
# . 로그아웃 상태에서만 이용 가능
# 2. 로그아웃
# . 로그인 후 이용가능
# 3. 입금
# . 로그인 후 이용가능
# 4. 출금money1
# . 로그인 후 이용가능
# 5. 이체
# . 로그인 후 이용가능
# 6. 조회
# . 로그인 후 이용가능
# 7. 종료


# 고객1
id1 = '김메가'
pw1 = 1111
money1 = 50000

# 고객2
id2 = '박메가'
pw2 = 2222
money2 = 70000

# 상태값 -1:로그아웃, 그외 : 로그인
status = -1

# 프로그램 상태
run = True

while run:
    print("<<<로그인 상태>>>")
    if status == 1:
        print(id1, "로그인 중...")
    elif status == 2:
        print(id2, "로그인 중...")
    else:
        print("로그아웃")

    print("1.로그인")
    print("2.로그아웃")
    print("3.입금")
    print("4.출금")
    print("5.이체")
    print("6.조회")
    print("0.종료")

    # 메뉴선택 - 로그인 여부 파악
    choice = int(input("메뉴 선택 : "))
    if choice == 1:
        if status == -1:
            ID = input("ID 입력 : ")
            PW = int(input("PW 입력 : "))

            if ID == id1 and PW == pw1:
                status = 1
                print(id1, "환영합니다.")
            elif ID == id2 and PW == pw2:
                status = 2
                print(id2, "환영합니다.")
            else:
                print("아이디와 비밀번호를 확인해주세요.")
        else:
            if status == 1:
                print(id1, "로그인 중...")
            elif status == 2:
                print(id2, "로그인 중...")
    elif choice == 2:
        if status != -1:
            status = -1
            print("로그아웃 되었습니다.")
        else:
            print("로그인 후 이용해주세요.")
    elif choice == 3:
        if status != -1:
            money = int(input("입금할 금액 입력 : "))

            if status == 1:
                money1 += money
            elif status == 2:
                money2 += money
        else:
            print("로그인 후 이용해주세요.")

    elif choice == 4:
        if status != -1:
            money = int(input("출금할 금액 입력 : "))

            if status == 1:
                if money <= money1:
                    money1 -= money
                else:
                    print("계좌잔액이 부족합니다.")
            elif status == 2:
                if money <= money2:
                    money2 -= money
                else:
                    print("계좌잔액이 부족합니다.")
        else:
            print("로그인 후 이용해주세요.")
    elif choice == 5:
        if status != -1:
            ID = input("이체대상의 고객명(ID) 입력 : ")

            if status == 1:
                if ID == id2:
                    money = int(input("이체할 금액 입력 : "))

                    if money <= money1:
                        money1 -= money
                        money2 += money
                    else:
                        print("계좌잔액이 부족합니다.")
                else:
                    print("고객명(ID)를 확인해주세요.")
            elif status == 2:
                if ID == id1:
                    money = int(input("이체할 금액 입력 입력 : "))

                    if money <= money2:
                        money2 -= money
                        money1 += money
                    else:
                        print("계좌잔액이 부족합니다.")
                else:
                    print("고객명(ID)를 확인해주세요.")
        else:
            print("로그인 후 이용해주세요.")
    elif choice == 6:
        if status != -1:
            if status == 1 :
                print("보유금액 =", money1)
            else :
                print("보유금액 =", money2)
        else:
            print("로그인 후 이용해주세요.")
    elif choice == 0:
        run = False
        print("프로그램 종료")