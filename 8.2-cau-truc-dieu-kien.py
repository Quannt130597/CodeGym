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
print("Max = {}".format(Max))