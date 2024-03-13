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
ttk.Label(root,text = "Hello World !").pack()

# Tạo nút nhấn
ttk.Button (root, text = "Cộng").pack()

# Select box
ttk.Combobox (root, values = ["mùa xuân", "mùa hạ", "mùa thu", "mùa đông"]).pack()

# Checkbox
ttk.Checkbutton (root, text ="chọn").pack()

# Ô nhập dữ liệu
ttk.Entry (root).pack()

# Thanh kéo
ttk.Scale (root, from_=0, to=100, orient=HORIZONTAL).pack()

# Ô nhập số
ttk.Spinbox(root, from_=0, to=100).pack()

# Ô nhập nhiều text
Text(root).pack()

# ====== KẾT THÚC PHẦN THÂN CHƯƠNG TRÌNH
# Sử dụng phương thức để cửa sổ chính giao diện hiển thị ra màn hình
root.mainloop()