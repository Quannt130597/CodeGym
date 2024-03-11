#hop_sach = ["Van","Su", "Dia"]
#print (hop_sach)

#hop_sach = ["Văn" , "Sử" , "Địa"]
#print (hop_sach)
#print (hop_sach [0])
#print (hop_sach [1])
#print (hop_sach [2])
#print (hop_sach)

#hop_sach = ["Văn" , "Sử" , "Địa"]
#hop_sach [0] = "Văn học"
#hop_sach [1] = "Sử học"
#hop_sach [2] = "Địa lý"
#print (hop_sach)

#hop_sach = ["Văn" , "Sử" , "Địa"]
#hop_sach [0] = "Văn học"
#hop_sach [1] = "Sử học"
#hop_sach [2] = "Địa lý"
#hop_sach.append ("Hóa")
#hop_sach.append ("Sinh")
#hop_sach.append ("Lý")
#print (hop_sach)

#hop_sach = ["Văn" , "Sử" , "Địa"]
#hop_sach [0] = "Văn học"
#hop_sach [1] = "Sử học"
#hop_sach [2] = "Địa lý"
#hop_sach.append ("Hóa")
#hop_sach.append ("Sinh")
#hop_sach.append ("Lý")
#hop_sach.sort ()
#print (hop_sach)
#hop_sach.sort (reverse=True)
#print (hop_sach)

#hop_sach = ["Văn" , "Sử" , "Địa"]
#hop_sach_khac = ["Hóa" , "Sinh" , "Lý"]
#hop_sach += hop_sach_khac
#hop_sach.sort (reverse=True)
#print (hop_sach)

#tieng_anh = ["hi" , "bye" , "love"]
#tieng_viet = ["chào" , "tạm biệt" , "yêu"]
#txt = input ("nhập 1 trong các giá trị trên: ")
#i = tieng_anh.index (txt)
#print (tieng_viet [i])

# Dùng vòng lặp for để tạo ra một mảng gồm các số chẵn từ 1 đến 10

numbers = []
for i in range (1,11):
    if i % 2 == 0:
        numbers.append (i)
print (numbers)