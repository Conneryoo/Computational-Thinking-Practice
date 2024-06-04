price=int(input("주머니 사용료는?"))
mult=int(input("한 번 두드리면 불어나는 돈의 배수는? : "))
hit_num=int(input("방망이를 치려는 횟수는? : "))
money=int(input("필요한 돈은 얼마? : "))

for i in range(1, hit_num+1, 1):
    money=(money+price)/mult
    
    
print(f"처음에 넣어야 할 돈 : {money}")
