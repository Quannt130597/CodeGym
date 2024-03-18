from tkinter import *
from tkinter import ttk

def onEqual():
    # Lấy giá trị trong ô input
    value = nhapso.get()
    # Xử lý biểu thức
    result = eval(value)
    # Xóa dữ liệu trong ô và đưa vào nội dung mới
    nhapso.delete(0,"end")
    nhapso.insert("end",result)

def onClear():
    nhapso.delete(0,"end")
def onPress(number):
    nhapso.insert("end",number)

root = Tk()
root.geometry("450x350")
root.config (bg="Black")
root.title ("Máy tính Casio")

#====== THÂN CHƯƠNG TRÌNH

# Tạo ô input
nhapso = Entry(root,width=50)
nhapso.grid(row=0,columnspan=4,pady=10,padx=50)

# Tạo các phím bấm
Button(root,width=4,height=2,text="1",command=lambda:onPress("1")).grid(row=1,column=0,pady=2)
Button(root,width=4,height=2,text="2",command=lambda:onPress("2")).grid(row=1,column=1,pady=2)
Button(root,width=4,height=2,text="3",command=lambda:onPress("3")).grid(row=1,column=2)
Button(root,width=4,height=2,text="+",command=lambda:onPress("+")).grid(row=1,column=3)

Button(root,width=4,height=2, text="4",command=lambda:onPress("4")).grid( row=2,column=0 )
Button(root,width=4,height=2, text="5",command=lambda:onPress("5")).grid( row=2,column=1 )
Button(root,width=4,height=2, text="6",command=lambda:onPress("6")).grid( row=2,column=2 )
Button(root,width=4,height=2, text="-",command=lambda:onPress("-")).grid( row=2,column=3 )

Button(root,width=4,height=2, text="7",command=lambda:onPress("7")).grid( row=3,column=0 )
Button(root,width=4,height=2, text="8",command=lambda:onPress("8")).grid( row=3,column=1 )
Button(root,width=4,height=2, text="9",command=lambda:onPress("9")).grid( row=3,column=2 )
Button(root,width=4,height=2, text="*",command=lambda:onPress("*")).grid( row=3,column=3 )

Button(root,width=4,height=2, text="0",command=lambda:onPress("0")).grid( row=4,column=0 )
Button(root,width=4,height=2,text="Clear",command=onClear).grid(row=4,column=1)

# Cập nhật lại sự kiện cho phím Clear
Button(root,width=4,height=2,text="=",command=onEqual).grid(row=4,column=2)
Button(root,width=4,height=2,text="/",command=lambda:onPress("/")).grid( row=4,column=3 )

Button(root,width=4,height=2,text=".",command=lambda:onPress(".")).grid( row=5,column=0 )

#====== KẾT THÚC PHẦN THÂN

root.mainloop ()