import turtle
t=turtle.Turtle()
t.shape("turtle")

nshape=int(input("그릴 다각헝(3~6): "))
line=int(input("한 변의 길이 입력: "))
inner_angle=(180*(nshape-2))/nshape
for i in range(1, nshape+1, 1):
    t.forward(line)
    t.left(180-inner_angle)
