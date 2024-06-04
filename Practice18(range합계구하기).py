last_num=int(input("어디까지 더할 것인지 입력하시오: "))
sum_num=0
for i in range(1, last_num+1, +1):
    sum_num=sum_num+i

print(f"1부터 {last_num}까지의 정수의 합= {sum_num}")
