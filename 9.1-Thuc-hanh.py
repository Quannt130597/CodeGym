# Gọi chú rùa lên
import turtle

# Khai báo biến shapeInput bằng giá trị người dùng nhập vào
shapeInput = input('Circle and square, what is your favorite shape?: ')

# Kiểm tra biến shapeInput
if shapeInput == 'circle' or shapeInput == 'square':
    ...
else:
    print ("Sorry, I don't have this shape :(")

# shapeInput thoã điều kiện, tiếp tục khai báo biến colorInput
colorInput = input('what color will it be?: ')

# Kiểm tra biến “colorInput”
if colorInput == 'yellow' or colorInput == 'red' or colorInput == 'blue':
    ...
else:
	print("Sorry, I don't have this color :(")

# Nếu biến “colorInput” thoã điều kiện
wn = turtle.Screen ()
wn.bgcolor("black")
wn.title("Your shape")

# Set up hình dạng
displayShape = turtle.Turtle ()
displayShape.shape (shapeInput)
displayShape.color(colorInput)
turtle.done ()