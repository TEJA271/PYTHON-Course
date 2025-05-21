#6. Turtle Graphics
#Use Turtle Library and make any fun creation of your choice.



import turtle

turtle.Screen().bgcolor("white")

t = turtle.Turtle()
t.color("violet")
t.pensize(3)


for _ in range(3):
    t.forward(100)
    t.left(120)

turtle.done()
