
import turtle

s = turtle.getscreen()

pen = turtle.Turtle()
pen.speed(100)
pen.color("black")
def drawBuilding(pen):
    pen.penup()
pen.goto(-160,-20)
pen.pendown()
pen.setheading(90)
pen.fillcolor("white")
pen.begin_fill()
pen.forward(150)
pen.right(90)
pen.forward(300)
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(300)
pen.right(90)
pen.end_fill()
turtle.title("Turtle City")
turtle.bgcolor("turquoise")

i =input()
    



