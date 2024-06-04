import turtle
t=turtle.Turtle()
t.shape("turtle")

while True:
    move=input("명령 입력 : ")
    if move=='L':
        t.left(90)
        t.forward(100)

    elif move=='R':
        t.right(90)
        t.forward(100)
    elif move=='Q':
        break
    else:
        break
