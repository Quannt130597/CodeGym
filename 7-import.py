#turtle
#math

# Tính diện tích hình tròn
import math
r = int(input("Nhập bán kính: "))
S = math.pi * r * r
print("Diện tích hình tròn là: ", S)

# Vẽ hình tròn theo diện tích trên
import turtle
turtle.fillcolor("blue")
turtle.pencolor ("green")
turtle.begin_fill ()
turtle.pensize(5)
turtle.circle(r)
turtle.end_fill ()
turtle.done()