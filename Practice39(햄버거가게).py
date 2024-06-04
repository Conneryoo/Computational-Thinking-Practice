def print_menu():
    print("1.치즈버거 세트\n2.불고기버거 세트\n3.치킨버거 세트\n4.종료")

print_menu()

menu_num=int(input("메뉴 선택 : "))
def check_menu(menu_num):
    if (menu_num>4):
        print("잘못된 메뉴를 선택하셨습니다.")
    elif (menu_num<1):
        print("잘못된 메뉴를 선택하셨습니다.")
    else :
        print(f"{menu_num}번 메뉴가 선택되었습니다.")


check_menu(menu_num)
