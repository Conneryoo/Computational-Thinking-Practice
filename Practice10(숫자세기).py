num1=int(input("a를 입력하시오 : "))
num2=int(input("b를 입력하시오 : "))
if num1>num2:
    i=num1
    num1=num2
    num2=i

while num1<=num2:
    print(f"Count {num1}")
    num1=num1+1
