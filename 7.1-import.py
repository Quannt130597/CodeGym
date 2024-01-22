# Input CD,CR
import math
chieu_dai = float(input("Nhập chiều dài: "))
chieu_rong = float(input("Nhập chiều rộng: "))

# Tính theo công thức Cvi,Dtich
chu_vi = (chieu_dai + chieu_rong) * 2
dien_tich = chieu_dai * chieu_rong

print("Chu vi của hình chữ nhật (dài = {chieu_dai}, rộng = {chieu_rong}) là {chu_vi}".format(chieu_dai = chieu_dai, chieu_rong = chieu_rong , chu_vi = chu_vi))
print("Diện tích của hình chữ nhật (dài = {chieu_dai}, rộng = {chieu_rong}) là {dien_tich}".format(chieu_dai = chieu_dai, chieu_rong = chieu_rong , dien_tich = dien_tich))

# Vẽ hình chữ nhật
import turtle
turtle.fillcolor ("yellow")
turtle.pencolor ("green")
turtle.pensize (5)
turtle.begin_fill ()
turtle.forward (chieu_dai)
turtle.right (90)
turtle.forward (chieu_rong)
turtle.right(90)
turtle.forward(chieu_dai)
turtle.right(90)
turtle.forward(chieu_rong)
turtle.end_fill ()
turtle.done ()