import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
turtle.tracer(0, 0) 
tree = turtle.Turtle()
tree.speed(-100)
tree.hideturtle()
tree.left(90)
tree.penup()
tree.goto(0, -300)
tree.pendown()

def draw_branch(length):
    if length < 10:
        tree.color("lime")
        tree.dot(6)
        return

    tree.pensize(length / 10)

    colors = ["brown", "sienna", "peru", "chocolate"]
    tree.color(random.choice(colors))

    tree.forward(length)

    angle = random.randint(15, 35)

    tree.right(angle)
    draw_branch(length * random.uniform(0.65, 0.85))

    tree.left(angle * 2)
    draw_branch(length * random.uniform(0.65, 0.85))

    tree.right(angle)
    tree.backward(length)


draw_branch(60)

screen.mainloop()