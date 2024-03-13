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

Label (root, text = "Chào mừng bạn đến với Bí Mật Của Quân").grid(row=0,column=1)
Label (root, text = "Vui lòng nhập thông tin").grid(row=1,column=1)
Label (root, text = "Tài khoản").grid(row=3,column=0)
Entry (root).grid(row=3, column=1)
Label (root, text="Mật khẩu").grid(row=4,column=0)
Entry (root).grid(row=4,column=1)
Button (root, text="Đăng nhập").grid (row=5,column=0)
Button (root, text="Quên mật khẩu").grid (row=5,column=1)
Button (root, text="Tạo tài khoản").grid (row=5,column=2)

root.mainloop ()