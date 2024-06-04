n=int(input("어디까지 더할 것인지 입력하시오: "))
sum_num=0
i=1
while i<=n:
    sum_num=sum_num+i
    i=i+1
print(f"1부터 {n}까지의 정수의 합 = {sum_num}")
