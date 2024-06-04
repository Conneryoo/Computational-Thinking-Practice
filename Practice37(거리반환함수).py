x_l=int(input("x좌표 입력 : "))
y_l=int(input("y좌표 입력 : "))

def distance(x_l, y_l):
    x_square=x_l**2
    y_square=y_l**2
    square_sum=x_square+y_square
    dis=square_sum**(1/2)
    print(f"거리 : {dis} ")

dis=distance(x_l, y_l)
