import turtle
t = turtle.Turtle ()
t.hideturtle ()
t.pencolor ("green")
def hinh_vuong(q):
    for i in range(4):
        t.forward(q)
        t.right(90)
    turtle.done()
hinh_vuong(100)