n=int(input("배수 입력 : "))
max_num=int(input("최댓값 입력 : "))

def mul(n, max_num):
    if n>max_num:
        print(f"잘못된 입력입니다")
    else :
        for i in range(n, max_num+1, n):
            print(f"{i}")
            

mul(n, max_num)
        
