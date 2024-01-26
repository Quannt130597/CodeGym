thu_ngay = input ("Nhập thứ ngày: ")
if (thu_ngay == "thứ hai" or thu_ngay == "thứ ba" or thu_ngay == "thứ tư" or thu_ngay == "thứ năm" or thu_ngay == "thứ sáu"):
    print ("Lam viec")
elif thu_ngay == ("thứ bảy"):
    print ("choi the thao")
else:
    print ("nghi ngoi")

# input A, B, C
# Xét điều kiện để
# A lớn nhất
# B lớn nhất
# C lớn nhất
    
A = float (input("nhập A: "))
B = float (input("nhập B: "))
C = float (input("nhập C: "))
Max = A
if A < B:
    Max = B
if B < C:
    Max = C
print("Max = {}".format(MAX))