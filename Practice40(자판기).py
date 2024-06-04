### 문제인식 -> 문제정의 -> 데이터수집 -> 분해,패턴인식,추상화,알고리즘->평가->자동화

def print_menu():
    print("="*24)
    print(" "*2, "음료수 자판기 메뉴")
    print("="*24)
    print(" 1. 제 티 : 500원")
    print(" 2. 코코팜 : 600원")
    print(" 3. 초록매실 : 700원")
    print(" 4. 데자와 : 800원")
    print(" 5. 레쓰비 : 900원")
    print(" 6. 솔의눈 : 1000원")
    print(" 7. 코카콜라 : 1500원")
    print()



def input_money(money):
    print("----돈을 투입하세요----")
    _1000won=int(input("1000원(장) : "))
    _500won=int(input("500원(개) : "))
    _100won=int(input("100원(개) : "))
    money=money+1000*_1000won+500*_500won+100*_100won
    print(f"투입금액 : {money}원")
    return money

def able_menu(money):
    if money>=1500:
        print("1. 제티 2. 코코팜 3. 초록매실 4. 데자와 5. 레쓰비 6. 솔의눈 7. 코카콜라")
    elif money>=1000:
        print("1. 제티 2. 코코팜 3. 초록매실 4. 데자와 5. 레쓰비 6. 솔의눈")
    elif money>=900:
        print("1. 제티 2. 코코팜 3. 초록매실 4. 데자와 5. 레쓰비")
    elif money>=800:
        print("1. 제티 2. 코코팜 3. 초록매실 4. 데자와")
    elif money>=700:
        print("1. 제티 2. 코코팜 3. 초록매실")
    elif money>=600:
        print("1. 제티 2. 코코팜")
    else:
        print("1. 제티")

def sel_menu(select, money):
    if select==1:
        print("제티를 구입하였습니다.")
        return money-500
    elif select==2:
        print("코코팜을 구입하였습니다.")
        return money-600
    elif select==3:
        print("초록매실 구입하였습니다.")
        return money-700
    elif select==4:
        print("데자와를 구입하였습니다.")
        return money-800
    elif select==5:
        print("레쓰비를 구입하였습니다.")
        return money-900
    elif select==6:
        print("솔의눈을 구입하였습니다.")
        return money-1000
    else:
        print("코카콜라를 구입하였습니다.")
        return money-1500

def cheak_flag(cn_flag):
    if cn_flag!='y' and cn_flag!='Y' and cn_flag!='n' and cn_flag!='N':
        return 1
    else:
        return 0

def give_change(money):
    print()
    print("-----거스름돈 반환-----")
    if money>=1000:
        print(f"1000원 : 1장")
        money=money-1000
        print(f"500원 : {money//500}개")
        money=money%500
        print(f"100원 : {money//100}개")
        money=money%100
    else:
        print(f"500원 : {money//500}개")
        money=money%500
        print(f"100원 : {money//100}개")
        money=money%100
        
        

    



print_menu()
money=0






while True:
    money=input_money(money)
    if money<500:
        print("구매할 수 있는 음료가 없습니다.")
        print("돈을 더 투입하시기 바랍니다.")
        continue
    else:
        break


while True:
    able_num=able_menu(money)
    select=int(input("메뉴 선택 : "))
    if(select> able_num or select<1):
        print("구입 가능한 상품을 입력하세요")
        continue
    else:
        money=sel_menu(select, money)
        print(f"잔액 : {money}원")
    if money<500:
        print("잔액이 부족하여 거스름돈을 드립니다.")
        break
    while True:
        cn_flag=input("자판기를 계속 이용하시겠습니까?(Y/N)")
        if cheak_flag(cn_flag):
            print("Y/N으로만 입력하세요")
            continue
        break
    if cn_flag=='Y' or cn_flag=='y':
        continue

give_change(money)
        
    




















        
