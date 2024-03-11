import turtle

# Cài đặt cửa sổ hiển thị
wn = turtle.Screen ()
wn.bgcolor ("green")
wn.title ("Star")

# Cài đặt màu sắc và tốc độ vẽ hình
myPen = turtle.Turtle ()
myPen.speed (0)
myPen.color ("yellow")

# Sử dụng for..in và hàm range () để quy định tổng số ngôi sao được vẽ
for j in range (1,100):
    for i in range (1,6):
        myPen.left (144)
        myPen.forward (200)
    myPen.left (5)

for i in range (1,6):
    myPen.left (144)
    myPen.forward (200)

turtle.done ()