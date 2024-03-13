# Khai báo module tkinter
from tkinter import *

# Phần mở rộng của thư viện tkinter
from tkinter import ttk

# Tạo cửa sổ chính cho giao diện
root = Tk()

# Thiết lập độ rộng cho giao diện
root.geometry ("400x250")
root.config (bg="blue")

# Đặt tiêu đề cho cửa sổ chính
root.title ("Bố cục với Pack")

# ======== BẮT ĐẦU PHẦN THÂN CHƯƠNG TRÌNH
Button (root, text = "Facebook", fg="red").pack (side = LEFT)
Button (root, text = "Zoom", fg="blue").pack (side = RIGHT)
Button (root, text = "Tiktok", fg="green").pack (side = TOP)
Button (root, text = "Zalo", fg="purple").pack (side = BOTTOM)

root.mainloop()