thoi_tiet = str(input("Thời tiết thế nào: "))
if (thoi_tiet == "dep"):
    print ("đi chơi")
print ("ở nhà")

thoi_tiet = input("thoi tiet: ")
if (thoi_tiet == "dep"):
    print ("di du dua")
else:
    print ("di ngu")

a = float(input("a: "))
b = float(input("b: "))

if a == 0:
    if b == 0:
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    print("Phuong trinh co nghiem: ",-b/a)

thu_ngay = input ("Nhập thứ ngày: ")
if thu_ngay == ("thứ hai" or "thứ ba" or "thứ tư" or "thứ năm" or "thứ sáu"):
    print ("Lam viec")
elif thu_ngay == ("thứ bảy"):
    print ("choi the thao")
else:
    print ("nghi ngoi")