import turtle
t = turtle.Turtle()
t.shape("turtle")

color_list = []
for s in range(4):
  color = input("색상 입력(영문): ")
  color_list.append(color)

for i in range(4):
  t.fillcolor(color_list[i])
  t.begin_fill()
  t.circle(100)
  t.end_fill()

  t. forward(50)
