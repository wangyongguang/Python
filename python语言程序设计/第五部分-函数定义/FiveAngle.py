from turtle import Turtle
p = Turtle()
p.speed(3)
p.pensize(5)
p.color("blue",'yellow')
p.fillcolor("red")
p.begin_fill()
for i in range(5):
    p.forward(200)
    p.right(144)
p.end_fill()
