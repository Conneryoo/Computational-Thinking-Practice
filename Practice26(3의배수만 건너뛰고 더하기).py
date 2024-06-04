sum_num=0
for i in range(1, 101, 1):
    if i%3==0:
        continue
    sum_num=sum_num+i

print(f"1~100의 합계(3의 배수 제외): {sum_num}")
