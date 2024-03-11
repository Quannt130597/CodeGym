# Khai báo module tkinter
from tkinter import *
from tkinter import ttk

# Tạo cửa sổ chính cho giao diện
root = Tk()

# Thiết lập độ rộng cho giao diện
root.geometry ("400x250")
root.config (bg="orange")

# Đặt tiêu đề cho cửa sổ chính
root.title("First_Program")

# ====== BẮT ĐẦU PHẦN THÂN CHƯƠNG TRÌNH
# Tạo Text "Hello World" , đây là kết quả sẽ in ra
Label(root,text = "Hello World !").pack()

# ====== Kết thúc phần thân chương trình

# Sử dụng phương thức để cửa sổ chính giao diện hiển thị ra màn hình
root.mainloop()