# Khai báo module tkinter
from tkinter import *

# Phần mở rộng của thư viện tkinter
from tkinter import ttk

# Tạo cửa sổ chính cho giao diện
root = Tk()

# Thiết lập độ rộng cho giao diện
root.geometry ("400x250")

# Đặt tiêu đề cho cửa sổ chính
root.title ("Bố cục với Grid")

Label (root, text = "Welcome to MY SECRETS!").place(x=50,y=20)
Label (root, text = "Fill your information").place(x=50,y=50)
Label (root, text = "Name").place(x=30,y=100)
Entry (root).place(x=80, y=100)
Label (root, text="User").place(x=30,y=140)
Entry (root).place(x=80,y=140)
Label (root, text="Password").place(x=30,y=180)
Entry (root).place(x=100,y=180)
Button (root, text="Log in").place (x=30,y=220)
Button (root, text="Forgot password").place (x=100,y=220)
Button (root, text="Creat account").place (x=220,y=220)

root.mainloop ()