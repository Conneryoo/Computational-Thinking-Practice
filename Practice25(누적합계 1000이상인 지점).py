sum_num=0
for i in range(1, 101, 1):
    sum_num=sum_num+i
    if sum_num>1000:
        location=i
        print(f"1~100의 합에서 최초로 1000이 넘는 위치: {location}")
        break
