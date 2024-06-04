num1=int(input("첫 번째 정수를 입력하시오: "))
num2=int(input("두 번째 정수를 입력하시오: "))

def get_max(num1, num2):
    if num1>num2:
        max_num=num1
        print(f"큰 수는 {max_num}")
    elif num1<num2:
        max_num=num2
        print(f"큰 수는 {max_num}")
    else :
        max_num=num1
        print(f"큰 수는 {max_num}")

max_num=get_max(num1, num2)

    
