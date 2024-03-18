from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title ("Chhương trình ghép tên")

def addName():
    ho = name1.get()
    ten = name2.get()
    result = ho +" "+ ten
    ket_qua.config(text="kết quả: " + str(result))

Label(root, text = "Nhập họ").grid(row = 0, column = 0)
name1 = Entry(root)
name1.grid(row=0,column=1)

Label(root, text = "Nhập tên").grid(row = 1, column = 0)
name2 = Entry(root)
name2.grid(row = 1, column = 1)

Button(root, text = "Ghép",command=addName).grid(row = 2, column = 0)
ket_qua = Label(root,text="Kết quả")
ket_qua.grid(row = 2, column = 1)

root.mainloop()