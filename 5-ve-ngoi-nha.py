import turtle

# Vẽ tường nhà
turtle.fillcolor ("yellow")
turtle.pencolor ("green")
turtle.pensize (5)
turtle.begin_fill ()
turtle.goto (-100, -100)
turtle.forward (200)
turtle.right (90)
turtle.forward (100)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.end_fill ()
turtle.mainloop ()