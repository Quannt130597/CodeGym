from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title ("Chương trình chuyển đổi nhiệt độ")

def FconvertC():
    nhietdoF = int(do_F.get())
    result = 5/9*(nhietdoF-32)
    ket_qua_do_C.config(text = str(result) + "độ C")

do_F = Entry(root)
do_F.grid(row=0,column=0)

Label(root, text = "độ F").grid(row = 0, column = 1)

Button(root, text=">",command=FconvertC).grid(row=0,column=2)

ket_qua_do_C = Label(root,text = "độ C")
ket_qua_do_C.grid(row=0,column=3)

def CconverF():
    nhietdoC = int(do_C.get())
    result = 9/4*(nhietdoC+32)
    ket_qua_do_F.config(text=str(result) + "độ F")

do_C = Entry(root)
do_C.grid (row = 1, column = 0)
Label (root, text = "độ C").grid (row = 1, column = 1)

Button(root, text=">",command=CconverF).grid(row=1,column=2)

ket_qua_do_F = Label (root,text="độ F")
ket_qua_do_F.grid(row=1,column=3)

root.mainloop()