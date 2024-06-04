num1=int(input("정수를 입력하시오 : "))
i=10
sum_num=num1%10
while True:
    num1=num1//10
    rest=num1%i
    sum_num=sum_num+rest
    if rest==num1:
        ㅌ2break

print(f"자리수의 합은 : {sum_num}")
