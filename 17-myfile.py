# Mở file ở chế độ đọc và ghi
file = open ("data.txt","r")
print ("Tên của file là: ", file.name)
print ("File có đóng hoặc không?: ", file.close)
print ("Chế độ mở file: ", file.mode)

# Đọc file...........
# str = file.read()
# print ("Noi dung file la:\n",str)

line1  = file.readline()
line2 = file.readline()
print ("dòng 1: ", line1)
print ("dòng 2: ", line2)

# Đóng sau khi xử lý file
file.close ()