import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(800,900)
polygon = turtle.Turtle()
num_sides = 6 
side_legth = 70
angle = 360 / num_sides
for i in range (num_sides):
    polygon.forward(side_legth)
    polygon.right(angle)

turtle.done()