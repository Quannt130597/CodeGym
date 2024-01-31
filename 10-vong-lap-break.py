#cnt = 1
#while (cnt <= 10):
#    print (cnt)
#    cnt += 1

#cnt = 1
#while (cnt <= 10):
#    print (cnt)
#    if (cnt == 5):
#        break
#    cnt += 1

#cnt = 0
#while (cnt <= 10):
#    cnt += 1
#    if (cnt == 5):
#        continue
#    print (cnt)

#chạy vòng lặp từ 1 đến 10: for
#cnt = 7 => break
#for i in range (1,11,1):
#    if (i == 7):
#        break
#    print (i)

#chạy vòng lặp từ 1 đến 10:for
#dung lenh continue để in ra số chẵn
for i in range (1,11,1):
    if (i%2 != 0):
        continue
    print (i)