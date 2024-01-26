So_tien_mua_hang = int(input("Hóa đơn của bạn bao nhiêu tiền?: "))

if So_tien_mua_hang >= 150:
    print ("Số tiền phải trả = ", So_tien_mua_hang - 50)
elif So_tien_mua_hang >= 100:
    print ("Số tiền phải trả = ", So_tien_mua_hang - 25)
elif So_tien_mua_hang > 75:
    print ("Số tiền phải trả = ", So_tien_mua_hang - 15)
else:
    print ("Số tiền phải trả = ", So_tien_mua_hang)