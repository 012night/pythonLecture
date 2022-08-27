# ATM[3단계]
# 1. 로그인
# . 로그인 후 재 로그인 불가
# . 로그아웃 상태에서만 이용 가능
# 2. 로그아웃
# . 로그인 후 이용가능
# 3. 입금
# . 로그인 후 이용가능
# 4. 출금
# . 로그인 후 이용가능
# 5. 이체
# . 로그인 후 이용가능
# 6. 조회
# . 로그인 후 이용가능
# 7. 종료


db_acc1 = 'admin1'
db_pw1 = 1234
db_money1 = 50000

db_acc2 = 'admin2'
db_pw2 = 2345
db_money2 = 70000

log = -1

run = True
while run:
    print("<로그인 상태>")
    if log == 1:
        print(db_acc1, "로그인 중...")
    elif log == 2:
        print(db_acc2, "로그인 중...")
    else:
        print("로그아웃")

    print("1.로그인")
    print("2.로그아웃")
    print("3.입금")
    print("4.출금")
    print("5.이체")
    print("6.조회")
    print("0.종료")

    choice = int(input("메뉴 선택 : "))
    if choice == 1:
        if log == -1:
            acc = int(input("ID 입력 : "))
            pw = int(input("PW 입력 : "))

            if acc == db_acc1 and pw == db_pw1:
                log = 1
                print(db_acc1, "환영합니다.")
            elif acc == db_acc2 and pw == db_pw2:
                log = 2
                print(db_acc2, "환영합니다.")
            else:
                print("계좌번호와 비밀번호를 확인해주세요.")
        else:
            if log == 1:
                print(db_acc1, "로그인 중...")
            elif log == 2:
                print(db_acc2, "로그인 중...")
    elif choice == 2:
        if log != -1:
            log = -1
            print("로그아웃 되었습니다.")
        else:
            print("로그인 후 이용해주세요.")
    elif choice == 3:
        if log != -1:
            money = int(input("입금할 금액 입력 : "))

            if log == 1:
                db_money1 += money
            elif log == 2:
                db_money2 += money
        else:
            print("로그인 후 이용해주세요.")

    elif choice == 4:
        if log != -1:
            money = int(input("출금할 금액 입력 : "))

            if log == 1:
                if money <= db_money1:
                    db_money1 -= money
                else:
                    print("계좌잔액이 부족합니다.")
            elif log == 2:
                if money <= db_money2:
                    db_money2 -= money
                else:
                    print("계좌잔액이 부족합니다.")
        else:
            print("로그인 후 이용해주세요.")
    elif choice == 5:
        if log != -1:
            acc = int(input("이체할 계좌번호 입력 : "))

            if log == 1:
                if acc == db_acc2:
                    money = int(input("이체할 금액 입력 : "))

                    if money <= db_money1:
                        db_money1 -= money
                        db_money2 += money
                    else:
                        print("계좌잔액이 부족합니다.")
                else:
                    print("계좌번호를 확인해주세요.")
            elif log == 2:
                if acc == db_acc1:
                    money = int(input("이체할 금액 입력 입력 : "))

                    if money <= db_money2:
                        db_money2 -= money
                        db_money1 += money
                    else:
                        print("계좌잔액이 부족합니다.")
                else:
                    print("계좌번호를 확인해주세요.")
        else:
            print("로그인 후 이용해주세요.")
    elif choice == 6:
        if log != -1:
            print("db_money1 =", db_money1)
            print("db_money2 =", db_money2)
        else:
            print("로그인 후 이용해주세요.")
    elif choice == 0:
        run = False
        print("프로그램 종료")