while True:
    num1=int(input("첫 번째 정수를 입력하시오: "))
    if num1==0:
        print(f"0을 입력해서 반복문을 탈출했습니다.")
        break
    num2=int(input("두 번째 정수를 입력하시오: "))
    if num2==0:
        print(f"0을 입력해서 반복문을 탈출했습니다.")
        break

    
    print(f"{num1} + {num2} = {num1+num2}")
