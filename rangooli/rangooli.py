import random
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(10)
length = 100
angle = 50
size = 5
for i in range(length):
    color=random.choice(colors)
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.forward(i +size)
    t.pendown()
    t.left(angle)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
turtle.exitonclick()
turtle.done()

#Thanks for reading this snippet. If you have any questions, please feel free to ask.
#Code snippet written by: Devansh Shukla