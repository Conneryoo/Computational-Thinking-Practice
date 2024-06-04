count=0
for i in range(1, 7, 1):
    for j in range(1, 7, 1):
        if i+j==6:
            print(f"{i} {j}")
            count=count+1

print(f"2개의 주사위 합이 6이 되는 경우의 수 : {count}")
