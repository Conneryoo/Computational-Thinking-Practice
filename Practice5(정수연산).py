num1=int(input("첫 번째 정수를 입력하시오: "))
num2=int(input("두 번째 정수를 입력하시오: "))

print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
if (num2 ==0):
    print(f"{num1} // {num2} = {0}")
else :
    print(f"{num1} // {num2} = {num1//num2}")
