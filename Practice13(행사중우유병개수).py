price_milk=int(input("한 병의 가격을 입력하시오 : "))
money=int(input("현재 소지하고 있는 금액을 입력하시오 : "))
milk_bottle=0
bottle=0
change_sum=0
while True:
    money=money-price_milk
    bottle=bottle+1
    if money<price_milk:
        break

change_bottle1=bottle//3
change_bottle=change_bottle1
while True:
    change_bottle=change_bottle//3
    change_sum=change_sum+change_bottle
    if change_bottle==0:
        break

milk_bottle=change_bottle1+bottle+change_sum

print(f"총 마신 우유병 수 : {milk_bottle}")
